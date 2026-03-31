import sys
import os
import sqlite3
import csv
from datetime import datetime

from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, 
                               QMessageBox, QFileDialog, QVBoxLayout, QPushButton)
from PySide6.QtCore import QDate, Qt, QFile, QMarginsF
from PySide6.QtGui import QColor, QTextDocument, QPdfWriter, QPageSize, QPageLayout, QPainter, QShortcut, QKeySequence

from PySide6.QtUiTools import QUiLoader

try:
    from PySide6.QtCharts import QChart, QChartView, QPieSeries
    GRAFICOS_OK = True
except ImportError:
    GRAFICOS_OK = False

# Determinar las rutas dependiendo de si es un .exe o el script normal
if getattr(sys, 'frozen', False):
    # Ejecutándose como un .exe empaquetado
    DIRECTORIO_DATOS = sys._MEIPASS # Carpeta temporal oculta donde PyInstaller extrae interfaz.ui
    DIRECTORIO_EXE = os.path.dirname(sys.executable) # Carpeta real donde el usuario puso el .exe
else:
    # Ejecutándose como script .py normal
    DIRECTORIO_DATOS = os.path.dirname(os.path.abspath(__file__))
    DIRECTORIO_EXE = DIRECTORIO_DATOS

# RUTA_BD: Se guarda junto al .exe para que los registros sean persistentes y no se borren
RUTA_BD = os.path.join(DIRECTORIO_EXE, "finanzas_personales.db")

# RUTA_UI: Se lee desde los datos empaquetados temporalmente por PyInstaller
RUTA_UI = os.path.join(DIRECTORIO_DATOS, "interfaz.ui")

class GestorGastosApp(QMainWindow):
    def __init__(self):
        super().__init__()
        

        loader = QUiLoader()
        archivo_ui = QFile(RUTA_UI)
        if not archivo_ui.open(QFile.ReadOnly):
            print(f"Error: No se encontró el archivo {RUTA_UI}")
            sys.exit(1)
        

        self.ui = loader.load(archivo_ui, self)
        archivo_ui.close()

        self.setCentralWidget(self.ui.centralwidget)
        if hasattr(self.ui, 'menubar'): self.setMenuBar(self.ui.menubar)
        if hasattr(self.ui, 'statusbar'): self.setStatusBar(self.ui.statusbar)
        
        self.setWindowTitle("Gestor de Gastos")
        self.resize(800, 650)

        self.id_edicion = None  
        self.tema_oscuro = True
        

        self.btnExportarPDF = QPushButton("📄 Exportar PDF")
        self.btnExportarPDF.setStyleSheet("""
            QPushButton { background-color: #8e44ad; color: white; border-radius: 5px; padding: 8px 16px; font-weight: bold; }
            QPushButton:hover { background-color: #9b59b6; }
        """)
        self.ui.layoutBotonesTabla.insertWidget(4, self.btnExportarPDF)

        if GRAFICOS_OK:
            self.chart_view = QChartView()
            self.chart_view.setRenderHint(QPainter.Antialiasing)
            indice = self.ui.verticalLayoutDash.indexOf(self.ui.labelPlaceholderGrafico)
            self.ui.verticalLayoutDash.insertWidget(indice, self.chart_view)
            self.ui.labelPlaceholderGrafico.hide()

        self.inicializar_bd()
        self.configurar_tablas()
        self.configurar_atajos()
        self.conectar_eventos()
        
        self.ui.dateFecha.setDate(QDate.currentDate())
        self.ui.spinPresupuestoTotal.setValue(5000)
        self.actualizar_prefijo_moneda()
        self.cargar_datos()

    def configurar_tablas(self):
        self.ui.tablaMovimientos.setColumnHidden(0, True) 
        self.ui.tablaMovimientos.setColumnWidth(1, 100) 
        self.ui.tablaMovimientos.setColumnWidth(2, 220) 
        self.ui.tablaMovimientos.horizontalHeader().setStretchLastSection(True)
        self.ui.tablaRecientes.horizontalHeader().setStretchLastSection(True)

    def configurar_atajos(self):
        QShortcut(QKeySequence("Ctrl+G"), self, lambda: (self.ui.tabMain.setCurrentIndex(1), self.ui.txtDescripcion.setFocus()))
        QShortcut(QKeySequence("Ctrl+E"), self, self.preparar_edicion)
        QShortcut(QKeySequence("Ctrl+L"), self, self.limpiar_formulario)
        QShortcut(QKeySequence("Delete"), self.ui.tablaMovimientos, self.eliminar_movimiento)

    def conectar_eventos(self):

        self.ui.btnGuardar.clicked.connect(self.registrar_movimiento)
        self.ui.btnLimpiar.clicked.connect(self.limpiar_formulario)
        self.ui.btnHoy.clicked.connect(lambda: self.ui.dateFecha.setDate(QDate.currentDate()))
        self.ui.comboMoneda.currentTextChanged.connect(self.actualizar_prefijo_moneda)

        self.ui.btnEliminar.clicked.connect(self.eliminar_movimiento)
        self.ui.btnEditar.clicked.connect(self.preparar_edicion)
        self.ui.btnCopiar.clicked.connect(self.copiar_movimiento)
        self.ui.btnExportarCSV.clicked.connect(self.exportar_csv)
        self.btnExportarPDF.clicked.connect(self.exportar_pdf)

        self.ui.txtBuscar.textChanged.connect(self.cargar_datos)
        self.ui.comboFiltro.currentIndexChanged.connect(self.cargar_datos)
        self.ui.comboFiltroMoneda.currentIndexChanged.connect(self.cargar_datos)
        self.ui.btnLimpiarFiltros.clicked.connect(self.resetear_filtros)

        self.ui.btnActualizarDash.clicked.connect(self.cargar_datos)
        self.ui.spinPresupuestoTotal.valueChanged.connect(self.actualizar_presupuesto)
        self.ui.actionImportarCSV.triggered.connect(self.importar_csv)
        self.ui.actionSalir.triggered.connect(self.close)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Cerrar', "¿Deseas salir de la aplicación?", 
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes: event.accept()
        else: event.ignore()

    def inicializar_bd(self):
        conexion = sqlite3.connect(RUTA_BD); cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS movimientos
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, fecha TEXT, descripcion TEXT, 
                           categoria TEXT, tipo TEXT, monto REAL, moneda TEXT, notas TEXT)''')
        conexion.commit(); conexion.close()

    def actualizar_prefijo_moneda(self):
        moneda = self.ui.comboMoneda.currentText()
        self.ui.spinMonto.setPrefix("€ " if "EUR" in moneda else "$ ")

    def registrar_movimiento(self):
        monto = self.ui.spinMonto.value()
        desc = self.ui.txtDescripcion.text().strip()
        if monto <= 0 or not desc:
            QMessageBox.warning(self, "Aviso", "Monto y descripción son obligatorios.")
            return

        fecha = self.ui.dateFecha.date().toString("yyyy-MM-dd")
        cat = self.ui.comboCategoria.currentText()
        moneda = self.ui.comboMoneda.currentText()
        notas = self.ui.txtNotas.toPlainText().strip()
        tipo = "Ingreso" if "Ingreso" in self.ui.comboTipo.currentText() else "Gasto"
        
        try:
            conexion = sqlite3.connect(RUTA_BD); cursor = conexion.cursor()
            if self.id_edicion:
                cursor.execute("""UPDATE movimientos SET fecha=?, descripcion=?, categoria=?, 
                                  tipo=?, monto=?, moneda=?, notas=? WHERE id=?""",
                               (fecha, desc, cat, tipo, monto, moneda, notas, self.id_edicion))
            else:
                cursor.execute("""INSERT INTO movimientos (fecha, descripcion, categoria, tipo, monto, moneda, notas) 
                                  VALUES (?, ?, ?, ?, ?, ?, ?)""", (fecha, desc, cat, tipo, monto, moneda, notas))
            conexion.commit(); conexion.close()
            self.limpiar_formulario()
            self.cargar_datos()
            self.ui.tabMain.setCurrentIndex(0) 
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def preparar_edicion(self):
        fila = self.ui.tablaMovimientos.currentRow()
        if fila == -1:
            QMessageBox.information(self, "Aviso", "Selecciona una fila primero.")
            return
        self.id_edicion = int(self.ui.tablaMovimientos.item(fila, 0).text())
        conexion = sqlite3.connect(RUTA_BD); cursor = conexion.cursor()
        cursor.execute("SELECT * FROM movimientos WHERE id=?", (self.id_edicion,))
        d = cursor.fetchone(); conexion.close()

        self.ui.dateFecha.setDate(QDate.fromString(d[1], "yyyy-MM-dd"))
        self.ui.txtDescripcion.setText(d[2])
        self.ui.comboCategoria.setCurrentText(d[3])
        self.ui.comboTipo.setCurrentIndex(1 if d[4] == "Ingreso" else 0)
        self.ui.spinMonto.setValue(d[5])
        self.ui.comboMoneda.setCurrentText(d[6])
        self.ui.txtNotas.setText(d[7])
        
        self.ui.btnGuardar.setText("🔄 Actualizar")
        self.ui.btnGuardar.setStyleSheet("background-color: #f39c12; color: white; font-weight: bold;")
        self.ui.tabMain.setCurrentIndex(1)

    def copiar_movimiento(self):
        self.preparar_edicion()
        self.id_edicion = None
        self.ui.btnGuardar.setText("💾 Guardar Copia")
        self.ui.btnGuardar.setStyleSheet("background-color: #2b5797; color: white;")

    def limpiar_formulario(self):
        self.id_edicion = None
        self.ui.txtDescripcion.clear(); self.ui.spinMonto.setValue(0.0); self.ui.txtNotas.clear()
        self.ui.btnGuardar.setText("💾 Guardar")
        self.ui.btnGuardar.setStyleSheet("background-color: #1e8449; color: white; font-weight: bold;")

    def eliminar_movimiento(self):
        fila = self.ui.tablaMovimientos.currentRow()
        if fila == -1: return
        if QMessageBox.question(self, "Eliminar", "¿Borrar registro?", QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
            id_db = self.ui.tablaMovimientos.item(fila, 0).text()
            conn = sqlite3.connect(RUTA_BD); cur = conn.cursor()
            cur.execute("DELETE FROM movimientos WHERE id=?", (id_db,))
            conn.commit(); conn.close(); self.cargar_datos()

    def resetear_filtros(self):
        self.ui.txtBuscar.clear(); self.ui.comboFiltro.setCurrentIndex(0); self.ui.comboFiltroMoneda.setCurrentIndex(0); self.cargar_datos()

    def cargar_datos(self):
        conexion = sqlite3.connect(RUTA_BD); cursor = conexion.cursor()
        query = "SELECT id, fecha, descripcion, categoria, tipo, monto, moneda, notas FROM movimientos WHERE 1=1"
        params = []
        if self.ui.txtBuscar.text():
            query += " AND descripcion LIKE ?"; params.append(f"%{self.ui.txtBuscar.text()}%")
        if "Ingresos" in self.ui.comboFiltro.currentText(): query += " AND tipo='Ingreso'"
        elif "Gastos" in self.ui.comboFiltro.currentText(): query += " AND tipo='Gasto'"
        if self.ui.comboFiltroMoneda.currentIndex() > 0:
            query += " AND moneda LIKE ?"; params.append(f"%{self.ui.comboFiltroMoneda.currentText()}%")

        cursor.execute(query + " ORDER BY fecha DESC", params)
        registros = cursor.fetchall(); conexion.close()

        self.ui.tablaMovimientos.setSortingEnabled(False)
        self.ui.tablaMovimientos.setRowCount(0)
        t_in, t_ga, g_cat = 0.0, 0.0, {}

        for data in registros:
            r = self.ui.tablaMovimientos.rowCount(); self.ui.tablaMovimientos.insertRow(r)
            es_in = (data[4] == "Ingreso")
            color = QColor("#2ecc71") if es_in else QColor("#e74c3c")
            if es_in: t_in += data[5]
            else: t_ga += data[5]; g_cat[data[3]] = g_cat.get(data[3], 0) + data[5]
            
            for i, val in enumerate(data):
                item = QTableWidgetItem(str(val))
                item.setToolTip(str(val))
                if i == 5: 
                    item.setData(Qt.EditRole, data[5])
                    item.setForeground(color)
                    item.setText(f"{data[5]:,.2f} {data[6]}")
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.ui.tablaMovimientos.setItem(r, i, item)

        self.ui.tablaMovimientos.setSortingEnabled(True)
        self.ui.lblSaldo.setText(f"Saldo: ${t_in - t_ga:,.2f}")
        self.ui.lblSaldo.setStyleSheet(f"color: {'#2ecc71' if (t_in-t_ga)>=0 else '#e74c3c'};")
        self.ui.lblTotalIngresos.setText(f"Ingresos: ${t_in:,.2f}")
        self.ui.lblTotalGastos.setText(f"Gastos: ${t_ga:,.2f}")
        
        self.actualizar_tabla_recientes(registros[:5])
        self.actualizar_presupuesto()
        if GRAFICOS_OK: self.actualizar_grafico(g_cat)

    def actualizar_tabla_recientes(self, datos):
        self.ui.tablaRecientes.setRowCount(0)
        for d in datos:
            r = self.ui.tablaRecientes.rowCount(); self.ui.tablaRecientes.insertRow(r)
            self.ui.tablaRecientes.setItem(r, 0, QTableWidgetItem(d[1]))
            self.ui.tablaRecientes.setItem(r, 1, QTableWidgetItem(d[2]))
            self.ui.tablaRecientes.setItem(r, 2, QTableWidgetItem(d[4]))
            it = QTableWidgetItem(f"{d[5]:,.2f}"); it.setForeground(QColor("#2ecc71") if d[4] == "Ingreso" else QColor("#e74c3c"))
            self.ui.tablaRecientes.setItem(r, 3, it)

    def actualizar_presupuesto(self):
        limite = self.ui.spinPresupuestoTotal.value()
        if limite <= 0: return
        self.ui.progressPresupuesto.setMaximum(int(limite))
        mes = datetime.now().strftime("%Y-%m")
        conn = sqlite3.connect(RUTA_BD); cur = conn.cursor()
        cur.execute("SELECT SUM(monto) FROM movimientos WHERE tipo='Gasto' AND fecha LIKE ?", (f"{mes}%",))
        g = cur.fetchone()[0] or 0; conn.close()
        self.ui.progressPresupuesto.setValue(int(g))
        color = "#e74c3c" if g > limite else "#4dabf7"
        self.ui.progressPresupuesto.setStyleSheet(f"QProgressBar::chunk {{ background-color: {color}; }}")

    def importar_csv(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Importar", "", "CSV (*.csv)")
        if ruta:
            try:
                with open(ruta, newline='', encoding='utf-8') as f:
                    lector = csv.reader(f); next(lector)
                    conn = sqlite3.connect(RUTA_BD); cur = conn.cursor()
                    for f in lector:
                        cur.execute("INSERT INTO movimientos (fecha, descripcion, categoria, tipo, monto, moneda, notas) VALUES (?,?,?,?,?,?,?)",
                                   (f[1], f[2], f[3], f[4], float(f[5]), f[6], f[7]))
                    conn.commit(); conn.close(); self.cargar_datos()
                QMessageBox.information(self, "Éxito", "CSV importado.")
            except Exception as e: QMessageBox.critical(self, "Error", str(e))

    def exportar_csv(self):
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar CSV", "", "CSV (*.csv)")
        if ruta:
            with open(ruta, 'w', newline='', encoding='utf-8') as f:
                w = csv.writer(f); w.writerow(['ID', 'Fecha', 'Desc', 'Cat', 'Tipo', 'Monto', 'Moneda', 'Notas'])
                for r in range(self.ui.tablaMovimientos.rowCount()):
                    w.writerow([self.ui.tablaMovimientos.item(r, c).text() for c in range(8)])

    def exportar_pdf(self):
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar PDF", "Reporte.pdf", "PDF (*.pdf)")
        if not ruta: return
        html = f"""
        <html><head><style>
            body {{ font-family: sans-serif; margin: 30pt; }}
            h1 {{ color: #2c3e50; text-align: center; font-size: 28pt; border-bottom: 2pt solid #2980b9; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20pt; }}
            th {{ background-color: #2980b9; color: white; padding: 10pt; font-size: 14pt; }}
            td {{ border: 1pt solid #ddd; padding: 10pt; font-size: 12pt; }}
            .ingreso {{ color: #27ae60; font-weight: bold; }} .gasto {{ color: #c0392b; font-weight: bold; }}
            .resumen {{ background: #f1f2f6; padding: 20pt; margin-top: 30pt; border-radius: 10pt; border-left: 10pt solid #2c3e50; }}
        </style></head><body>
            <h1>REPORTE FINANCIERO</h1>
            <p align='right'>Generado el: {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
            <table><tr><th>Fecha</th><th>Descripción</th><th>Tipo</th><th>Monto</th></tr>
        """
        for r in range(self.ui.tablaMovimientos.rowCount()):
            f, d, t, m = [self.ui.tablaMovimientos.item(r, i).text() for i in [1, 2, 4, 5]]
            clase = "ingreso" if "Ingreso" in t else "gasto"
            html += f"<tr><td>{f}</td><td>{d}</td><td class='{clase}'>{t}</td><td align='right'>{m}</td></tr>"
        html += f"""</table><div class='resumen'>
                    <p style='font-size:16pt'>{self.ui.lblTotalIngresos.text()}</p>
                    <p style='font-size:16pt'>{self.ui.lblTotalGastos.text()}</p>
                    <hr><h1>{self.ui.lblSaldo.text()}</h1></div></body></html>"""
        doc = QTextDocument(); doc.setHtml(html)
        writer = QPdfWriter(ruta); writer.setPageSize(QPageSize.A4)
        writer.setPageMargins(QMarginsF(25, 25, 25, 25), QPageLayout.Millimeter)
        doc.print_(writer)
        try: os.startfile(ruta)
        except: pass

    def actualizar_grafico(self, dict_gastos):
        series = QPieSeries(); series.setHoleSize(0.4)
        for cat, monto in dict_gastos.items():
            if monto > 0: series.append(cat, monto).setLabelVisible(True)
        chart = QChart(); chart.addSeries(series); chart.setTitle("Distribución de Gastos")
        chart.setTheme(QChart.ChartThemeDark); chart.setBackgroundBrush(QColor("#1e1e1e")); chart.setTitleBrush(QColor("#ffffff"))
        self.chart_view.setChart(chart)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GestorGastosApp()
    ventana.show()
    sys.exit(app.exec())