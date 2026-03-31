import sys
import os
import sqlite3
import csv
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, 
                               QMessageBox, QFileDialog, QVBoxLayout, QPushButton)
from PySide6.QtCore import QDate, Qt, QFile, QMarginsF
from PySide6.QtGui import QColor, QTextDocument, QPdfWriter, QPageSize, QPageLayout

# Carga directa del XML
from PySide6.QtUiTools import QUiLoader

try:
    from PySide6.QtCharts import QChart, QChartView, QPieSeries
    GRAFICOS_OK = True
except ImportError:
    GRAFICOS_OK = False

DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_BD = os.path.join(DIRECTORIO_ACTUAL, "finanzas_personales.db")
RUTA_UI = os.path.join(DIRECTORIO_ACTUAL, "interfaz.ui")

class GestorGastosApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        archivo_ui = QFile(RUTA_UI)
        archivo_ui.open(QFile.ReadOnly)
        self.ui = loader.load(archivo_ui, self)
        archivo_ui.close()
        
        self.setCentralWidget(self.ui.centralwidget)
        self.setMenuBar(self.ui.menubar)
        self.setStatusBar(self.ui.statusbar)
        self.resize(950, 760)
        self.setWindowTitle("Gestor de Finanzas Personales - Open Source")
        
        self.ui.tablaMovimientos.setColumnHidden(0, True) 
        self.ui.tablaMovimientos.setColumnWidth(1, 100) 
        self.ui.tablaMovimientos.setColumnWidth(2, 180) 
        self.ui.tablaMovimientos.setColumnWidth(3, 130) 
        self.ui.tablaMovimientos.setColumnWidth(4, 90)  
        self.ui.tablaMovimientos.setColumnWidth(5, 100) 
        self.ui.tablaMovimientos.horizontalHeader().setStretchLastSection(True)
        
        self.tema_oscuro = True
        
        # --- NUEVO: Inyectamos el botón de PDF dinámicamente ---
        self.btnExportarPDF = QPushButton("📄 Exportar PDF")
        self.btnExportarPDF.setStyleSheet("""
            QPushButton { background-color: #8e44ad; color: white; border-radius: 5px; padding: 8px 16px; font-weight: bold; }
            QPushButton:hover { background-color: #9b59b6; }
        """)
        self.ui.layoutBotonesTabla.insertWidget(4, self.btnExportarPDF)
        self.btnExportarPDF.clicked.connect(self.exportar_pdf)
        # --------------------------------------------------------
        
        if GRAFICOS_OK:
            self.chart_view = QChartView()
            indice = self.ui.verticalLayoutDash.indexOf(self.ui.labelPlaceholderGrafico)
            self.ui.verticalLayoutDash.insertWidget(indice, self.chart_view)
            self.ui.labelPlaceholderGrafico.hide()

        fecha_hoy = QDate.currentDate()
        self.ui.dateFecha.setDate(fecha_hoy)
        self.ui.dateDesde.setDate(fecha_hoy.addMonths(-1))
        self.ui.dateHasta.setDate(fecha_hoy)

        self.inicializar_bd()
        
        self.ui.btnGuardar.clicked.connect(self.registrar_movimiento)
        self.ui.btnLimpiar.clicked.connect(self.limpiar_formulario)
        self.ui.btnEliminar.clicked.connect(self.eliminar_movimiento)
        self.ui.btnCopiar.clicked.connect(self.copiar_movimiento)
        self.ui.btnExportarCSV.clicked.connect(self.exportar_csv)
        self.ui.txtBuscar.textChanged.connect(self.cargar_datos)
        self.ui.comboFiltro.currentIndexChanged.connect(self.cargar_datos)
        self.ui.comboFiltroCategoria.currentIndexChanged.connect(self.cargar_datos)
        self.ui.dateDesde.dateChanged.connect(self.cargar_datos)
        self.ui.dateHasta.dateChanged.connect(self.cargar_datos)
        self.ui.btnActualizarDash.clicked.connect(self.cargar_datos)
        self.ui.spinPresupuestoTotal.valueChanged.connect(self.actualizar_presupuesto)
        
        self.ui.actionSalir.triggered.connect(self.close)
        self.ui.btnToggleTheme.clicked.connect(self.alternar_tema)
        
        self.ui.spinPresupuestoTotal.setValue(5000)
        self.aplicar_tema(True)
        self.cargar_datos()

    def inicializar_bd(self):
        conexion = sqlite3.connect(RUTA_BD)
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS movimientos
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           fecha TEXT, descripcion TEXT, categoria TEXT, tipo TEXT, monto REAL, moneda TEXT, notas TEXT)''')
        conexion.commit()
        conexion.close()

    def registrar_movimiento(self):
        fecha = self.ui.dateFecha.date().toString("yyyy-MM-dd")
        descripcion = self.ui.txtDescripcion.text().strip()
        categoria = self.ui.comboCategoria.currentText()
        monto = self.ui.spinMonto.value()
        moneda = self.ui.comboMoneda.currentText()
        notas = self.ui.txtNotas.toPlainText().strip()
        
        if not descripcion or monto == 0:
            QMessageBox.warning(self, "Aviso", "Ingresa una descripción y un monto válido.")
            return

        tipo = "Ingreso" if "Ingreso" in self.ui.comboTipo.currentText() else "Gasto"
        
        try:
            conexion = sqlite3.connect(RUTA_BD)
            cursor = conexion.cursor()
            cursor.execute('''INSERT INTO movimientos 
                              (fecha, descripcion, categoria, tipo, monto, moneda, notas) 
                              VALUES (?, ?, ?, ?, ?, ?, ?)''',
                           (fecha, descripcion, categoria, tipo, monto, moneda, notas))
            conexion.commit()
            conexion.close()
            self.ui.statusbar.showMessage("✅ Movimiento guardado.", 3000)
            
            self.limpiar_formulario()
            self.cargar_datos()
            self.ui.tabMain.setCurrentIndex(2)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Fallo al guardar:\n{str(e)}")

    def limpiar_formulario(self):
        self.ui.dateFecha.setDate(QDate.currentDate())
        self.ui.txtDescripcion.clear()
        self.ui.spinMonto.setValue(0.0)
        self.ui.txtNotas.clear()
        self.ui.comboTipo.setCurrentIndex(0)
        self.ui.txtDescripcion.setFocus()

    def eliminar_movimiento(self):
        fila = self.ui.tablaMovimientos.currentRow()
        if fila == -1: return
            
        id_movimiento = self.ui.tablaMovimientos.item(fila, 0).text()
        if QMessageBox.question(self, "Confirmar", "¿Eliminar este registro?", 
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            conexion = sqlite3.connect(RUTA_BD)
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM movimientos WHERE id = ?", (id_movimiento,))
            conexion.commit()
            conexion.close()
            self.cargar_datos()

    def copiar_movimiento(self):
        fila = self.ui.tablaMovimientos.currentRow()
        if fila == -1: return
            
        self.ui.txtDescripcion.setText(self.ui.tablaMovimientos.item(fila, 2).text())
        self.ui.comboCategoria.setCurrentText(self.ui.tablaMovimientos.item(fila, 3).text())
        monto_str = self.ui.tablaMovimientos.item(fila, 5).text().split(" ")[0].replace(",", "")
        self.ui.spinMonto.setValue(float(monto_str))
        self.ui.comboTipo.setCurrentIndex(1 if "Ingreso" in self.ui.tablaMovimientos.item(fila, 4).text() else 0)
        self.ui.txtNotas.setText(self.ui.tablaMovimientos.item(fila, 6).text())
        self.ui.tabMain.setCurrentIndex(1)

    def exportar_csv(self):
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar CSV", "", "Archivos CSV (*.csv)")
        if ruta:
            with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(['ID', 'Fecha', 'Descripción', 'Categoría', 'Tipo', 'Monto', 'Notas'])
                for fila in range(self.ui.tablaMovimientos.rowCount()):
                    datos_fila = [self.ui.tablaMovimientos.item(fila, col).text() for col in range(7)]
                    escritor.writerow(datos_fila)
            self.ui.statusbar.showMessage(f"📥 Exportado a {ruta}", 4000)

    # --- NUEVO: FUNCIÓN PARA GENERAR PDF ---
    def exportar_pdf(self):
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar PDF", "Reporte_Finanzas.pdf", "Archivos PDF (*.pdf)")
        if not ruta:
            return
            
        # 1. Construir el esqueleto HTML del reporte
        html = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; }}
                h1 {{ color: #2c3e50; text-align: center; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
                th, td {{ border: 1px solid #bdc3c7; padding: 8px; text-align: left; }}
                th {{ background-color: #2980b9; color: white; font-weight: bold; }}
                .ingreso {{ color: #27ae60; font-weight: bold; }}
                .gasto {{ color: #c0392b; font-weight: bold; }}
                .resumen {{ margin-top: 30px; padding: 15px; background-color: #ecf0f1; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <h1>Reporte de Finanzas Personales</h1>
            <p><strong>Fecha de emisión:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
            <table>
                <thead>
                    <tr>
                        <th>Fecha</th>
                        <th>Descripción</th>
                        <th>Categoría</th>
                        <th>Tipo</th>
                        <th>Monto</th>
                    </tr>
                </thead>
                <tbody>
        """
        
        # 2. Llenar la tabla con los datos visuales
        for fila in range(self.ui.tablaMovimientos.rowCount()):
            fecha = self.ui.tablaMovimientos.item(fila, 1).text()
            desc = self.ui.tablaMovimientos.item(fila, 2).text()
            cat = self.ui.tablaMovimientos.item(fila, 3).text()
            tipo = self.ui.tablaMovimientos.item(fila, 4).text()
            monto = self.ui.tablaMovimientos.item(fila, 5).text()
            
            clase_tipo = "ingreso" if "Ingreso" in tipo else "gasto"
            
            html += f"""
                <tr>
                    <td>{fecha}</td>
                    <td>{desc}</td>
                    <td>{cat}</td>
                    <td class="{clase_tipo}">{tipo}</td>
                    <td>{monto}</td>
                </tr>
            """
            
        # 3. Agregar los saldos finales
        html += f"""
                </tbody>
            </table>
            <div class="resumen">
                <h3>Resumen Financiero</h3>
                <p>{self.ui.lblTotalIngresos.text()}</p>
                <p>{self.ui.lblTotalGastos.text()}</p>
                <h2 style="color: #2c3e50;">{self.ui.lblSaldo.text()}</h2>
            </div>
        </body>
        </html>
        """

        # 4. Crear un documento de texto y renderizarlo como PDF
        documento = QTextDocument()
        documento.setHtml(html)
        
        impresora_pdf = QPdfWriter(ruta)
        impresora_pdf.setPageSize(QPageSize.A4)
        impresora_pdf.setPageMargins(QMarginsF(15, 15, 15, 15), QPageLayout.Millimeter)
        
        documento.print_(impresora_pdf)
        
        self.ui.statusbar.showMessage(f"📄 Reporte PDF guardado en: {ruta}", 5000)
        
        # Abrir automáticamente el PDF (Opcional)
        try:
            os.startfile(ruta) # Solo funciona en Windows
        except:
            pass
    # ----------------------------------------

    def actualizar_presupuesto(self):
        limite = self.ui.spinPresupuestoTotal.value()
        if limite <= 0: return

        self.ui.progressPresupuesto.setMaximum(int(limite))
        mes_actual = datetime.now().strftime("%Y-%m")
        
        conexion = sqlite3.connect(RUTA_BD)
        cursor = conexion.cursor()
        cursor.execute("SELECT SUM(monto) FROM movimientos WHERE tipo='Gasto' AND fecha LIKE ?", (f"{mes_actual}%",))
        gasto_mes = cursor.fetchone()[0] or 0.0
        conexion.close()

        self.ui.progressPresupuesto.setValue(int(gasto_mes))
        if gasto_mes > limite:
            self.ui.progressPresupuesto.setStyleSheet("QProgressBar::chunk { background-color: #e74c3c; }")
        else:
            self.ui.progressPresupuesto.setStyleSheet("QProgressBar::chunk { background-color: #4dabf7; }")

    def actualizar_grafico(self, gastos_por_categoria):
        if not GRAFICOS_OK: return
        
        series = QPieSeries()
        series.setHoleSize(0.35) 
        
        for cat, monto in gastos_por_categoria.items():
            if monto > 0:
                slice_pie = series.append(cat, monto)
                slice_pie.setLabelVisible(True)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Gastos por Categoría")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        
        if self.tema_oscuro:
            chart.setTheme(QChart.ChartThemeDark)
            chart.setBackgroundBrush(QColor("#1a1a1a"))
            chart.setTitleBrush(QColor("#ffffff"))
        else:
            chart.setTheme(QChart.ChartThemeLight)
            chart.setBackgroundBrush(QColor("#ffffff"))
            chart.setTitleBrush(QColor("#000000"))

        self.chart_view.setChart(chart)

    def cargar_datos(self):
        conexion = sqlite3.connect(RUTA_BD)
        cursor = conexion.cursor()
        
        query = "SELECT id, fecha, descripcion, categoria, tipo, monto, moneda, notas FROM movimientos WHERE 1=1"
        params = []
        
        texto_busqueda = self.ui.txtBuscar.text().strip()
        if texto_busqueda:
            query += " AND descripcion LIKE ?"
            params.append(f"%{texto_busqueda}%")
            
        tipo_filtro = self.ui.comboFiltro.currentText()
        if tipo_filtro == "Solo Ingresos":
            query += " AND tipo = 'Ingreso'"
        elif tipo_filtro == "Solo Gastos":
            query += " AND tipo = 'Gasto'"
            
        cat_filtro = self.ui.comboFiltroCategoria.currentText()
        if cat_filtro != "Todas":
            query += " AND categoria = ?"
            params.append(cat_filtro)
            
        fecha_ini = self.ui.dateDesde.date().toString("yyyy-MM-dd")
        fecha_fin = self.ui.dateHasta.date().toString("yyyy-MM-dd")
        query += " AND fecha BETWEEN ? AND ?"
        params.extend([fecha_ini, fecha_fin])
        
        query += " ORDER BY fecha DESC, id DESC"
        
        cursor.execute(query, params)
        registros = cursor.fetchall()
        conexion.close()

        self.ui.tablaMovimientos.setSortingEnabled(False)
        self.ui.tablaMovimientos.setRowCount(0)
        
        total_ingresos = 0.0
        total_gastos = 0.0
        gastos_categoria = {}
        categoria_mayor = ("--", 0)

        for fila_datos in registros:
            id_db, fecha, desc, cat, tipo, monto, moneda, notas = fila_datos
            
            if tipo == "Ingreso": 
                total_ingresos += monto
            else: 
                total_gastos += monto
                gastos_categoria[cat] = gastos_categoria.get(cat, 0) + monto
                if gastos_categoria[cat] > categoria_mayor[1]:
                    categoria_mayor = (cat, gastos_categoria[cat])
            
            row = self.ui.tablaMovimientos.rowCount()
            self.ui.tablaMovimientos.insertRow(row)
            self.ui.tablaMovimientos.setItem(row, 0, QTableWidgetItem(str(id_db)))
            self.ui.tablaMovimientos.setItem(row, 1, QTableWidgetItem(fecha))
            self.ui.tablaMovimientos.setItem(row, 2, QTableWidgetItem(desc))
            self.ui.tablaMovimientos.setItem(row, 3, QTableWidgetItem(cat))
            self.ui.tablaMovimientos.setItem(row, 4, QTableWidgetItem(tipo))
            
            item_monto = QTableWidgetItem()
            item_monto.setData(Qt.EditRole, float(monto))
            item_monto.setText(f"{monto:,.2f} {moneda}")
            self.ui.tablaMovimientos.setItem(row, 5, item_monto)
            self.ui.tablaMovimientos.setItem(row, 6, QTableWidgetItem(notas))

        self.ui.tablaMovimientos.setSortingEnabled(True)

        saldo_total = total_ingresos - total_gastos
        self.ui.lblTotalIngresos.setText(f"Ingresos: ${total_ingresos:,.2f}")
        self.ui.lblTotalGastos.setText(f"Gastos: ${total_gastos:,.2f}")
        self.ui.lblSaldo.setText(f"💰 Saldo Total: ${saldo_total:,.2f}")
        
        if saldo_total >= 0:
            self.ui.lblSaldo.setStyleSheet("color: #2ecc71; font-size: 18px; font-weight: bold;")
        else:
            self.ui.lblSaldo.setStyleSheet("color: #e74c3c; font-size: 18px; font-weight: bold;")

        self.ui.lblCategoriaMayor.setText(f"Mayor gasto:\n{categoria_mayor[0]}")
        
        self.actualizar_presupuesto()
        self.actualizar_grafico(gastos_categoria)

    def alternar_tema(self):
        self.aplicar_tema(not self.tema_oscuro)
        
    def aplicar_tema(self, oscuro):
        self.tema_oscuro = oscuro
        if oscuro:
            self.setStyleSheet("""
                QMainWindow, QWidget#centralwidget, QTabWidget::pane { background-color: #121212; color: #e0e0e0; }
                QLabel { color: #e0e0e0; }
                QGroupBox { border: 1px solid #333; background-color: #1e1e1e; color: #fff; border-radius: 8px; margin-top: 12px; padding-top: 10px; font-weight: bold;}
                QGroupBox::title { color: #4dabf7; subcontrol-origin: margin; left: 15px; padding: 0 10px;}
                QPushButton { background-color: #2b5797; color: white; border-radius: 5px; padding: 8px 16px; font-weight: bold; }
                QPushButton:hover { background-color: #366cb9; }
                QLineEdit, QDateEdit, QComboBox, QDoubleSpinBox, QTextEdit { background-color: #2b2b2b; color: #fff; border: 1px solid #444; border-radius: 5px; padding: 6px;}
                QTableWidget { background-color: #1e1e1e; alternate-background-color: #262626; color: #e0e0e0; gridline-color: #333; selection-background-color: #2c3e50; }
                QHeaderView::section { background-color: #2b2b2b; color: #fff; border: 1px solid #333; padding: 8px; }
                QTabBar::tab { background-color: #2b2b2b; color: #888; padding: 12px 28px; border-top-left-radius: 8px; border-top-right-radius: 8px; font-weight: bold;}
                QTabBar::tab:selected { background-color: #1e1e1e; color: #4dabf7; }
            """)
            self.ui.btnToggleTheme.setText("🌙 Tema")
        else:
            self.setStyleSheet("""
                QMainWindow, QWidget#centralwidget, QTabWidget::pane { background-color: #f5f6fa; color: #2f3640; }
                QLabel { color: #2f3640; }
                QGroupBox { border: 1px solid #dcdde1; background-color: #ffffff; color: #2f3640; border-radius: 8px; margin-top: 12px; padding-top: 10px; font-weight: bold;}
                QGroupBox::title { color: #0097e6; subcontrol-origin: margin; left: 15px; padding: 0 10px;}
                QPushButton { background-color: #0097e6; color: white; border-radius: 5px; padding: 8px 16px; font-weight: bold; }
                QPushButton:hover { background-color: #00a8ff; }
                QLineEdit, QDateEdit, QComboBox, QDoubleSpinBox, QTextEdit { background-color: #f5f6fa; color: #2f3640; border: 1px solid #dcdde1; border-radius: 5px; padding: 6px;}
                QTableWidget { background-color: #ffffff; alternate-background-color: #f5f6fa; color: #2f3640; gridline-color: #dcdde1; selection-background-color: #dcdde1; }
                QHeaderView::section { background-color: #e1e2e6; color: #2f3640; border: 1px solid #dcdde1; padding: 8px; }
                QTabBar::tab { background-color: #e1e2e6; color: #7f8fa6; padding: 12px 28px; border-top-left-radius: 8px; border-top-right-radius: 8px; font-weight: bold;}
                QTabBar::tab:selected { background-color: #ffffff; color: #0097e6; }
            """)
            self.ui.btnToggleTheme.setText("☀️ Tema")
            
        self.cargar_datos() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GestorGastosApp()
    ventana.show()
    sys.exit(app.exec())