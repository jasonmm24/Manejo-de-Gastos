# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDateEdit, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 760)
        MainWindow.setStyleSheet(u"\n"
"    /* TEMA OSCURO (por defecto) - preparado para alternar con clase .light */\n"
"    QMainWindow, QWidget#centralwidget, QTabWidget::pane {\n"
"        background-color: #121212;\n"
"        color: #e0e0e0;\n"
"    }\n"
"    QLabel { color: #e0e0e0; }\n"
"    \n"
"    QGroupBox {\n"
"        font-weight: bold;\n"
"        border: 1px solid #333333;\n"
"        border-radius: 8px;\n"
"        margin-top: 12px;\n"
"        padding-top: 10px;\n"
"        background-color: #1e1e1e;\n"
"        color: #ffffff;\n"
"    }\n"
"    QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 15px;\n"
"        padding: 0 10px;\n"
"        color: #4dabf7;\n"
"    }\n"
"    \n"
"    QPushButton {\n"
"        background-color: #2b5797;\n"
"        color: white;\n"
"        border: none;\n"
"        border-radius: 5px;\n"
"        padding: 8px 16px;\n"
"        font-weight: bold;\n"
"    }\n"
"    QPushButton:hover { background-color: #366cb9; }\n"
"    QPushButton#btnGuardar { background-color: #1e844"
                        "9; font-size: 14px; }\n"
"    QPushButton#btnGuardar:hover { background-color: #27ae60; }\n"
"    QPushButton#btnEliminar { background-color: #922b21; }\n"
"    QPushButton#btnEliminar:hover { background-color: #c0392b; }\n"
"    QPushButton#btnEditar { background-color: #b9770e; }\n"
"    QPushButton#btnEditar:hover { background-color: #d68910; }\n"
"    QPushButton#btnLimpiar { background-color: #424949; }\n"
"    QPushButton#btnLimpiar:hover { background-color: #515a5a; }\n"
"    QPushButton#btnCopiar { background-color: #2c3e50; }\n"
"    QPushButton#btnCopiar:hover { background-color: #3e5a6c; }\n"
"    QPushButton#btnActualizarDash { background-color: #2c3e50; }\n"
"    QPushButton#btnActualizarDash:hover { background-color: #3e5a6c; }\n"
"    QPushButton#btnToggleTheme { background-color: #5a5a5a; }\n"
"    \n"
"    QLineEdit, QDateEdit, QComboBox, QDoubleSpinBox, QTextEdit {\n"
"        border: 1px solid #444444;\n"
"        border-radius: 5px;\n"
"        padding: 6px;\n"
"        background-color: #2"
                        "b2b2b;\n"
"        color: #ffffff;\n"
"        selection-background-color: #4dabf7;\n"
"    }\n"
"    QLineEdit:focus, QComboBox:focus, QDoubleSpinBox:focus, QTextEdit:focus {\n"
"        border: 1px solid #4dabf7;\n"
"    }\n"
"    \n"
"    QTableWidget {\n"
"        background-color: #1e1e1e;\n"
"        alternate-background-color: #262626;\n"
"        color: #e0e0e0;\n"
"        gridline-color: #333333;\n"
"        selection-background-color: #2c3e50;\n"
"        border: 1px solid #333333;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QHeaderView::section {\n"
"        background-color: #2b2b2b;\n"
"        color: #ffffff;\n"
"        border: 1px solid #333333;\n"
"        padding: 8px;\n"
"        font-weight: bold;\n"
"    }\n"
"    \n"
"    QTabBar::tab {\n"
"        background-color: #2b2b2b;\n"
"        color: #888888;\n"
"        padding: 12px 28px;\n"
"        border: 1px solid #333333;\n"
"        border-bottom: none;\n"
"        border-top-left-radius: 8px;\n"
"        border-top-right-radius: "
                        "8px;\n"
"        font-size: 14px;\n"
"        font-weight: bold;\n"
"    }\n"
"    QTabBar::tab:selected {\n"
"        background-color: #1e1e1e;\n"
"        color: #4dabf7;\n"
"    }\n"
"    \n"
"    QFrame#frameIngresos { background-color: #0b3d1f; border-radius: 12px; border: 1px solid #196f3d; }\n"
"    QFrame#frameGastos { background-color: #4a1515; border-radius: 12px; border: 1px solid #922b21; }\n"
"    QFrame#frameCategoriaTop { background-color: #0f304d; border-radius: 12px; border: 1px solid #1a5276; }\n"
"    QFrame#framePresupuesto { background-color: #1e1e2a; border-radius: 12px; border: 1px solid #4dabf7; }\n"
"    \n"
"    QLabel#lblTotalIngresos { color: #2ecc71; }\n"
"    QLabel#lblTotalGastos { color: #e74c3c; }\n"
"    QLabel#lblCategoriaMayor { color: #5dade2; }\n"
"    QLabel#lblSaldo { font-size: 18px; font-weight: bold; }\n"
"    QLabel#lblSaldo[positive=\"true\"] { color: #2ecc71; }\n"
"    QLabel#lblSaldo[positive=\"false\"] { color: #e74c3c; }\n"
"    \n"
"    QProgressBar {\n"
"    "
                        "    border: 1px solid #444;\n"
"        border-radius: 5px;\n"
"        background-color: #2b2b2b;\n"
"        text-align: center;\n"
"        color: white;\n"
"    }\n"
"    QProgressBar::chunk {\n"
"        background-color: #4dabf7;\n"
"        border-radius: 5px;\n"
"    }\n"
"    \n"
"    QMenuBar {\n"
"        background-color: #1e1e1e;\n"
"        color: #e0e0e0;\n"
"        border-bottom: 1px solid #333;\n"
"    }\n"
"    QMenuBar::item:selected { background-color: #2b2b2b; }\n"
"    QMenu { background-color: #1e1e1e; color: #e0e0e0; border: 1px solid #333; }\n"
"    QMenu::item:selected { background-color: #2b5797; }\n"
"   ")
        self.actionImportar = QAction(MainWindow)
        self.actionImportar.setObjectName(u"actionImportar")
        self.actionExportarTodo = QAction(MainWindow)
        self.actionExportarTodo.setObjectName(u"actionExportarTodo")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionTemaOscuro = QAction(MainWindow)
        self.actionTemaOscuro.setObjectName(u"actionTemaOscuro")
        self.actionTemaClaro = QAction(MainWindow)
        self.actionTemaClaro.setObjectName(u"actionTemaClaro")
        self.actionAcercaDe = QAction(MainWindow)
        self.actionAcercaDe.setObjectName(u"actionAcercaDe")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabMain = QTabWidget(self.centralwidget)
        self.tabMain.setObjectName(u"tabMain")
        self.tabMain.setDocumentMode(False)
        self.tabMain.setTabPosition(QTabWidget.North)
        self.tabDashboard = QWidget()
        self.tabDashboard.setObjectName(u"tabDashboard")
        self.verticalLayoutDash = QVBoxLayout(self.tabDashboard)
        self.verticalLayoutDash.setObjectName(u"verticalLayoutDash")
        self.layoutResumen = QHBoxLayout()
        self.layoutResumen.setObjectName(u"layoutResumen")
        self.frameIngresos = QFrame(self.tabDashboard)
        self.frameIngresos.setObjectName(u"frameIngresos")
        self.vlayoutIn = QVBoxLayout(self.frameIngresos)
        self.vlayoutIn.setObjectName(u"vlayoutIn")
        self.iconIn = QLabel(self.frameIngresos)
        self.iconIn.setObjectName(u"iconIn")
        self.iconIn.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(24)
        self.iconIn.setFont(font)

        self.vlayoutIn.addWidget(self.iconIn)

        self.lblTotalIngresos = QLabel(self.frameIngresos)
        self.lblTotalIngresos.setObjectName(u"lblTotalIngresos")
        self.lblTotalIngresos.setAlignment(Qt.AlignCenter)
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.lblTotalIngresos.setFont(font1)

        self.vlayoutIn.addWidget(self.lblTotalIngresos)


        self.layoutResumen.addWidget(self.frameIngresos)

        self.frameGastos = QFrame(self.tabDashboard)
        self.frameGastos.setObjectName(u"frameGastos")
        self.vlayoutGa = QVBoxLayout(self.frameGastos)
        self.vlayoutGa.setObjectName(u"vlayoutGa")
        self.iconGa = QLabel(self.frameGastos)
        self.iconGa.setObjectName(u"iconGa")
        self.iconGa.setAlignment(Qt.AlignCenter)
        self.iconGa.setFont(font)

        self.vlayoutGa.addWidget(self.iconGa)

        self.lblTotalGastos = QLabel(self.frameGastos)
        self.lblTotalGastos.setObjectName(u"lblTotalGastos")
        self.lblTotalGastos.setAlignment(Qt.AlignCenter)
        self.lblTotalGastos.setFont(font1)

        self.vlayoutGa.addWidget(self.lblTotalGastos)


        self.layoutResumen.addWidget(self.frameGastos)

        self.frameCategoriaTop = QFrame(self.tabDashboard)
        self.frameCategoriaTop.setObjectName(u"frameCategoriaTop")
        self.vlayoutCat = QVBoxLayout(self.frameCategoriaTop)
        self.vlayoutCat.setObjectName(u"vlayoutCat")
        self.iconCat = QLabel(self.frameCategoriaTop)
        self.iconCat.setObjectName(u"iconCat")
        self.iconCat.setAlignment(Qt.AlignCenter)
        self.iconCat.setFont(font)

        self.vlayoutCat.addWidget(self.iconCat)

        self.lblCategoriaMayor = QLabel(self.frameCategoriaTop)
        self.lblCategoriaMayor.setObjectName(u"lblCategoriaMayor")
        self.lblCategoriaMayor.setAlignment(Qt.AlignCenter)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.lblCategoriaMayor.setFont(font2)

        self.vlayoutCat.addWidget(self.lblCategoriaMayor)


        self.layoutResumen.addWidget(self.frameCategoriaTop)


        self.verticalLayoutDash.addLayout(self.layoutResumen)

        self.framePresupuesto = QFrame(self.tabDashboard)
        self.framePresupuesto.setObjectName(u"framePresupuesto")
        self.formPresupuesto = QFormLayout(self.framePresupuesto)
        self.formPresupuesto.setObjectName(u"formPresupuesto")
        self.formPresupuesto.setLabelAlignment(Qt.AlignRight)
        self.labelPresupuestoTotal = QLabel(self.framePresupuesto)
        self.labelPresupuestoTotal.setObjectName(u"labelPresupuestoTotal")

        self.formPresupuesto.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelPresupuestoTotal)

        self.spinPresupuestoTotal = QDoubleSpinBox(self.framePresupuesto)
        self.spinPresupuestoTotal.setObjectName(u"spinPresupuestoTotal")
        self.spinPresupuestoTotal.setMaximum(999999.989999999990687)
        self.spinPresupuestoTotal.setButtonSymbols(QAbstractSpinBox.UpDownArrows)

        self.formPresupuesto.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinPresupuestoTotal)

        self.labelGastadoMes = QLabel(self.framePresupuesto)
        self.labelGastadoMes.setObjectName(u"labelGastadoMes")

        self.formPresupuesto.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelGastadoMes)

        self.progressPresupuesto = QProgressBar(self.framePresupuesto)
        self.progressPresupuesto.setObjectName(u"progressPresupuesto")
        self.progressPresupuesto.setValue(0)

        self.formPresupuesto.setWidget(1, QFormLayout.ItemRole.FieldRole, self.progressPresupuesto)


        self.verticalLayoutDash.addWidget(self.framePresupuesto)

        self.labelPlaceholderGrafico = QLabel(self.tabDashboard)
        self.labelPlaceholderGrafico.setObjectName(u"labelPlaceholderGrafico")
        self.labelPlaceholderGrafico.setAlignment(Qt.AlignCenter)
        self.labelPlaceholderGrafico.setStyleSheet(u"border: 1px dashed #555; background-color: #1a1a1a; margin-top: 10px; border-radius: 10px;")
        self.labelPlaceholderGrafico.setMinimumHeight(260)

        self.verticalLayoutDash.addWidget(self.labelPlaceholderGrafico)

        self.layoutBotonesDash = QHBoxLayout()
        self.layoutBotonesDash.setObjectName(u"layoutBotonesDash")
        self.spacerDashLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutBotonesDash.addItem(self.spacerDashLeft)

        self.btnActualizarDash = QPushButton(self.tabDashboard)
        self.btnActualizarDash.setObjectName(u"btnActualizarDash")

        self.layoutBotonesDash.addWidget(self.btnActualizarDash)

        self.spacerDashRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutBotonesDash.addItem(self.spacerDashRight)


        self.verticalLayoutDash.addLayout(self.layoutBotonesDash)

        self.tabMain.addTab(self.tabDashboard, "")
        self.tabRegistro = QWidget()
        self.tabRegistro.setObjectName(u"tabRegistro")
        self.verticalLayoutReg = QVBoxLayout(self.tabRegistro)
        self.verticalLayoutReg.setObjectName(u"verticalLayoutReg")
        self.spacerRegTop = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutReg.addItem(self.spacerRegTop)

        self.groupNuevo = QGroupBox(self.tabRegistro)
        self.groupNuevo.setObjectName(u"groupNuevo")
        self.groupNuevo.setMaximumWidth(800)
        self.groupNuevo.setAlignment(Qt.AlignCenter)
        self.gridLayoutNuevo = QGridLayout(self.groupNuevo)
        self.gridLayoutNuevo.setObjectName(u"gridLayoutNuevo")
        self.gridLayoutNuevo.setHorizontalSpacing(20)
        self.gridLayoutNuevo.setVerticalSpacing(15)
        self.labelFecha = QLabel(self.groupNuevo)
        self.labelFecha.setObjectName(u"labelFecha")

        self.gridLayoutNuevo.addWidget(self.labelFecha, 0, 0, 1, 1)

        self.dateFecha = QDateEdit(self.groupNuevo)
        self.dateFecha.setObjectName(u"dateFecha")
        self.dateFecha.setCalendarPopup(True)

        self.gridLayoutNuevo.addWidget(self.dateFecha, 0, 1, 1, 1)

        self.labelCat = QLabel(self.groupNuevo)
        self.labelCat.setObjectName(u"labelCat")

        self.gridLayoutNuevo.addWidget(self.labelCat, 0, 2, 1, 1)

        self.comboCategoria = QComboBox(self.groupNuevo)
        self.comboCategoria.addItem("")
        self.comboCategoria.addItem("")
        self.comboCategoria.addItem("")
        self.comboCategoria.addItem("")
        self.comboCategoria.addItem("")
        self.comboCategoria.addItem("")
        self.comboCategoria.addItem("")
        self.comboCategoria.setObjectName(u"comboCategoria")

        self.gridLayoutNuevo.addWidget(self.comboCategoria, 0, 3, 1, 1)

        self.labelDesc = QLabel(self.groupNuevo)
        self.labelDesc.setObjectName(u"labelDesc")

        self.gridLayoutNuevo.addWidget(self.labelDesc, 1, 0, 1, 1)

        self.txtDescripcion = QLineEdit(self.groupNuevo)
        self.txtDescripcion.setObjectName(u"txtDescripcion")

        self.gridLayoutNuevo.addWidget(self.txtDescripcion, 1, 1, 1, 3)

        self.labelMonto = QLabel(self.groupNuevo)
        self.labelMonto.setObjectName(u"labelMonto")

        self.gridLayoutNuevo.addWidget(self.labelMonto, 2, 0, 1, 1)

        self.spinMonto = QDoubleSpinBox(self.groupNuevo)
        self.spinMonto.setObjectName(u"spinMonto")
        self.spinMonto.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinMonto.setMaximum(999999.989999999990687)

        self.gridLayoutNuevo.addWidget(self.spinMonto, 2, 1, 1, 1)

        self.labelTipo = QLabel(self.groupNuevo)
        self.labelTipo.setObjectName(u"labelTipo")

        self.gridLayoutNuevo.addWidget(self.labelTipo, 2, 2, 1, 1)

        self.comboTipo = QComboBox(self.groupNuevo)
        self.comboTipo.addItem("")
        self.comboTipo.addItem("")
        self.comboTipo.setObjectName(u"comboTipo")

        self.gridLayoutNuevo.addWidget(self.comboTipo, 2, 3, 1, 1)

        self.labelMoneda = QLabel(self.groupNuevo)
        self.labelMoneda.setObjectName(u"labelMoneda")

        self.gridLayoutNuevo.addWidget(self.labelMoneda, 3, 0, 1, 1)

        self.comboMoneda = QComboBox(self.groupNuevo)
        self.comboMoneda.addItem("")
        self.comboMoneda.addItem("")
        self.comboMoneda.addItem("")
        self.comboMoneda.setObjectName(u"comboMoneda")

        self.gridLayoutNuevo.addWidget(self.comboMoneda, 3, 1, 1, 1)

        self.labelInfoMoneda = QLabel(self.groupNuevo)
        self.labelInfoMoneda.setObjectName(u"labelInfoMoneda")

        self.gridLayoutNuevo.addWidget(self.labelInfoMoneda, 3, 2, 1, 2)

        self.labelNotas = QLabel(self.groupNuevo)
        self.labelNotas.setObjectName(u"labelNotas")

        self.gridLayoutNuevo.addWidget(self.labelNotas, 4, 0, 1, 1)

        self.txtNotas = QTextEdit(self.groupNuevo)
        self.txtNotas.setObjectName(u"txtNotas")
        self.txtNotas.setMaximumHeight(80)

        self.gridLayoutNuevo.addWidget(self.txtNotas, 4, 1, 1, 3)

        self.layoutBotonesForm = QHBoxLayout()
        self.layoutBotonesForm.setObjectName(u"layoutBotonesForm")
        self.spacerBtn = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutBotonesForm.addItem(self.spacerBtn)

        self.btnLimpiar = QPushButton(self.groupNuevo)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.layoutBotonesForm.addWidget(self.btnLimpiar)

        self.btnGuardar = QPushButton(self.groupNuevo)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setMinimumHeight(42)

        self.layoutBotonesForm.addWidget(self.btnGuardar)


        self.gridLayoutNuevo.addLayout(self.layoutBotonesForm, 5, 1, 1, 3)


        self.verticalLayoutReg.addWidget(self.groupNuevo)

        self.spacerRegBot = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutReg.addItem(self.spacerRegBot)

        self.tabMain.addTab(self.tabRegistro, "")
        self.tabHistorial = QWidget()
        self.tabHistorial.setObjectName(u"tabHistorial")
        self.verticalLayoutHist = QVBoxLayout(self.tabHistorial)
        self.verticalLayoutHist.setObjectName(u"verticalLayoutHist")
        self.groupFiltros = QGroupBox(self.tabHistorial)
        self.groupFiltros.setObjectName(u"groupFiltros")
        self.layoutFiltros = QHBoxLayout(self.groupFiltros)
        self.layoutFiltros.setSpacing(10)
        self.layoutFiltros.setObjectName(u"layoutFiltros")
        self.txtBuscar = QLineEdit(self.groupFiltros)
        self.txtBuscar.setObjectName(u"txtBuscar")

        self.layoutFiltros.addWidget(self.txtBuscar)

        self.labelFiltroCat = QLabel(self.groupFiltros)
        self.labelFiltroCat.setObjectName(u"labelFiltroCat")

        self.layoutFiltros.addWidget(self.labelFiltroCat)

        self.comboFiltro = QComboBox(self.groupFiltros)
        self.comboFiltro.addItem("")
        self.comboFiltro.addItem("")
        self.comboFiltro.addItem("")
        self.comboFiltro.setObjectName(u"comboFiltro")

        self.layoutFiltros.addWidget(self.comboFiltro)

        self.labelFiltroCategoria = QLabel(self.groupFiltros)
        self.labelFiltroCategoria.setObjectName(u"labelFiltroCategoria")

        self.layoutFiltros.addWidget(self.labelFiltroCategoria)

        self.comboFiltroCategoria = QComboBox(self.groupFiltros)
        self.comboFiltroCategoria.addItem("")
        self.comboFiltroCategoria.addItem("")
        self.comboFiltroCategoria.addItem("")
        self.comboFiltroCategoria.addItem("")
        self.comboFiltroCategoria.addItem("")
        self.comboFiltroCategoria.addItem("")
        self.comboFiltroCategoria.addItem("")
        self.comboFiltroCategoria.addItem("")
        self.comboFiltroCategoria.setObjectName(u"comboFiltroCategoria")

        self.layoutFiltros.addWidget(self.comboFiltroCategoria)

        self.labelDesde = QLabel(self.groupFiltros)
        self.labelDesde.setObjectName(u"labelDesde")

        self.layoutFiltros.addWidget(self.labelDesde)

        self.dateDesde = QDateEdit(self.groupFiltros)
        self.dateDesde.setObjectName(u"dateDesde")
        self.dateDesde.setCalendarPopup(True)

        self.layoutFiltros.addWidget(self.dateDesde)

        self.labelHasta = QLabel(self.groupFiltros)
        self.labelHasta.setObjectName(u"labelHasta")

        self.layoutFiltros.addWidget(self.labelHasta)

        self.dateHasta = QDateEdit(self.groupFiltros)
        self.dateHasta.setObjectName(u"dateHasta")
        self.dateHasta.setCalendarPopup(True)

        self.layoutFiltros.addWidget(self.dateHasta)


        self.verticalLayoutHist.addWidget(self.groupFiltros)

        self.tablaMovimientos = QTableWidget(self.tabHistorial)
        if (self.tablaMovimientos.columnCount() < 7):
            self.tablaMovimientos.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaMovimientos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaMovimientos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaMovimientos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaMovimientos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaMovimientos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaMovimientos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaMovimientos.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tablaMovimientos.setObjectName(u"tablaMovimientos")
        self.tablaMovimientos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablaMovimientos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaMovimientos.setAlternatingRowColors(True)
        self.tablaMovimientos.setColumnCount(7)

        self.verticalLayoutHist.addWidget(self.tablaMovimientos)

        self.layoutBotonesTabla = QHBoxLayout()
        self.layoutBotonesTabla.setObjectName(u"layoutBotonesTabla")
        self.btnEliminar = QPushButton(self.tabHistorial)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.layoutBotonesTabla.addWidget(self.btnEliminar)

        self.btnEditar = QPushButton(self.tabHistorial)
        self.btnEditar.setObjectName(u"btnEditar")

        self.layoutBotonesTabla.addWidget(self.btnEditar)

        self.btnCopiar = QPushButton(self.tabHistorial)
        self.btnCopiar.setObjectName(u"btnCopiar")

        self.layoutBotonesTabla.addWidget(self.btnCopiar)

        self.btnExportarCSV = QPushButton(self.tabHistorial)
        self.btnExportarCSV.setObjectName(u"btnExportarCSV")

        self.layoutBotonesTabla.addWidget(self.btnExportarCSV)

        self.spacerBotonesTabla = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutBotonesTabla.addItem(self.spacerBotonesTabla)

        self.lblSaldo = QLabel(self.tabHistorial)
        self.lblSaldo.setObjectName(u"lblSaldo")

        self.layoutBotonesTabla.addWidget(self.lblSaldo)


        self.verticalLayoutHist.addLayout(self.layoutBotonesTabla)

        self.tabMain.addTab(self.tabHistorial, "")

        self.verticalLayout.addWidget(self.tabMain)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setStyleSheet(u"background-color: #1e1e1e; color: #e0e0e0;")
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuConfiguracion = QMenu(self.menubar)
        self.menuConfiguracion.setObjectName(u"menuConfiguracion")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"color: #aaaaaa; font-size: 10pt; background-color: #1e1e1e;")
        self.statusbar.setSizeGripEnabled(False)
        self.btnToggleTheme = QPushButton(self.statusbar)
        self.btnToggleTheme.setObjectName(u"btnToggleTheme")
        self.btnToggleTheme.setFlat(True)
        self.btnToggleTheme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        MainWindow.setStatusBar(self.statusbar)

        self.menuArchivo.addAction(self.actionImportar)
        self.menuArchivo.addAction(self.actionExportarTodo)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuConfiguracion.addAction(self.actionTemaOscuro)
        self.menuConfiguracion.addAction(self.actionTemaClaro)
        self.menuAyuda.addAction(self.actionAcercaDe)

        self.retranslateUi(MainWindow)

        self.tabMain.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestor de Finanzas Personales - Open Source", None))
        self.actionImportar.setText(QCoreApplication.translate("MainWindow", u"Importar desde CSV...", None))
        self.actionExportarTodo.setText(QCoreApplication.translate("MainWindow", u"Exportar todos los movimientos...", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionTemaOscuro.setText(QCoreApplication.translate("MainWindow", u"Modo oscuro", None))
        self.actionTemaClaro.setText(QCoreApplication.translate("MainWindow", u"Modo claro", None))
        self.actionAcercaDe.setText(QCoreApplication.translate("MainWindow", u"Acerca de...", None))
#if QT_CONFIG(tooltip)
        self.frameIngresos.setToolTip(QCoreApplication.translate("MainWindow", u"Total de ingresos registrados", None))
#endif // QT_CONFIG(tooltip)
        self.iconIn.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcb0", None))
        self.lblTotalIngresos.setText(QCoreApplication.translate("MainWindow", u"Ingresos: $0.00", None))
#if QT_CONFIG(tooltip)
        self.frameGastos.setToolTip(QCoreApplication.translate("MainWindow", u"Total de gastos registrados", None))
#endif // QT_CONFIG(tooltip)
        self.iconGa.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcb8", None))
        self.lblTotalGastos.setText(QCoreApplication.translate("MainWindow", u"Gastos: $0.00", None))
#if QT_CONFIG(tooltip)
        self.frameCategoriaTop.setToolTip(QCoreApplication.translate("MainWindow", u"Categor\u00eda con mayor gasto acumulado", None))
#endif // QT_CONFIG(tooltip)
        self.iconCat.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcca", None))
        self.lblCategoriaMayor.setText(QCoreApplication.translate("MainWindow", u"Mayor gasto: --", None))
        self.labelPresupuestoTotal.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcc5 L\u00edmite mensual:", None))
#if QT_CONFIG(tooltip)
        self.labelPresupuestoTotal.setToolTip(QCoreApplication.translate("MainWindow", u"Define un presupuesto m\u00e1ximo para el mes actual", None))
#endif // QT_CONFIG(tooltip)
        self.spinPresupuestoTotal.setPrefix(QCoreApplication.translate("MainWindow", u"$ ", None))
        self.labelGastadoMes.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcb8 Gastado este mes:", None))
        self.progressPresupuesto.setFormat(QCoreApplication.translate("MainWindow", u"%p% ($%v de $%m)", None))
        self.labelPlaceholderGrafico.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcc8 [Gr\u00e1fico de gastos por categor\u00eda]", None))
#if QT_CONFIG(tooltip)
        self.labelPlaceholderGrafico.setToolTip(QCoreApplication.translate("MainWindow", u"Aqu\u00ed se mostrar\u00e1 una gr\u00e1fica circular interactiva", None))
#endif // QT_CONFIG(tooltip)
        self.btnActualizarDash.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd04 Actualizar datos", None))
#if QT_CONFIG(tooltip)
        self.btnActualizarDash.setToolTip(QCoreApplication.translate("MainWindow", u"Refresca los res\u00famenes y el gr\u00e1fico", None))
#endif // QT_CONFIG(tooltip)
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabDashboard), QCoreApplication.translate("MainWindow", u"\ud83c\udfe0 Panel General", None))
        self.groupNuevo.setTitle(QCoreApplication.translate("MainWindow", u"\u270f\ufe0f Complete los detalles", None))
        self.labelFecha.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcc5 Fecha:", None))
#if QT_CONFIG(tooltip)
        self.dateFecha.setToolTip(QCoreApplication.translate("MainWindow", u"Selecciona la fecha del movimiento", None))
#endif // QT_CONFIG(tooltip)
        self.labelCat.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcc2 Categor\u00eda:", None))
        self.comboCategoria.setItemText(0, QCoreApplication.translate("MainWindow", u"Alimentaci\u00f3n", None))
        self.comboCategoria.setItemText(1, QCoreApplication.translate("MainWindow", u"Transporte", None))
        self.comboCategoria.setItemText(2, QCoreApplication.translate("MainWindow", u"Vivienda / Servicios", None))
        self.comboCategoria.setItemText(3, QCoreApplication.translate("MainWindow", u"Salud", None))
        self.comboCategoria.setItemText(4, QCoreApplication.translate("MainWindow", u"Ocio / Entretenimiento", None))
        self.comboCategoria.setItemText(5, QCoreApplication.translate("MainWindow", u"Salario / Ingresos", None))
        self.comboCategoria.setItemText(6, QCoreApplication.translate("MainWindow", u"Otros", None))

#if QT_CONFIG(tooltip)
        self.comboCategoria.setToolTip(QCoreApplication.translate("MainWindow", u"Selecciona una categor\u00eda predefinida", None))
#endif // QT_CONFIG(tooltip)
        self.labelDesc.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcdd Descripci\u00f3n:", None))
        self.txtDescripcion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej. Supermercado, Internet, Salario...", None))
#if QT_CONFIG(tooltip)
        self.txtDescripcion.setToolTip(QCoreApplication.translate("MainWindow", u"Escribe una breve descripci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.labelMonto.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcb0 Monto:", None))
        self.spinMonto.setPrefix("")
#if QT_CONFIG(tooltip)
        self.spinMonto.setToolTip(QCoreApplication.translate("MainWindow", u"Ingresa el valor num\u00e9rico (punto decimal)", None))
#endif // QT_CONFIG(tooltip)
        self.labelTipo.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd04 Tipo:", None))
        self.comboTipo.setItemText(0, QCoreApplication.translate("MainWindow", u"Gasto (-)", None))
        self.comboTipo.setItemText(1, QCoreApplication.translate("MainWindow", u"Ingreso (+)", None))

#if QT_CONFIG(tooltip)
        self.comboTipo.setToolTip(QCoreApplication.translate("MainWindow", u"\u00bfEs un ingreso o un gasto?", None))
#endif // QT_CONFIG(tooltip)
        self.labelMoneda.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcb1 Moneda:", None))
        self.comboMoneda.setItemText(0, QCoreApplication.translate("MainWindow", u"$ (MXN)", None))
        self.comboMoneda.setItemText(1, QCoreApplication.translate("MainWindow", u"$ (USD)", None))
        self.comboMoneda.setItemText(2, QCoreApplication.translate("MainWindow", u"\u20ac (EUR)", None))

#if QT_CONFIG(tooltip)
        self.comboMoneda.setToolTip(QCoreApplication.translate("MainWindow", u"Selecciona la moneda del movimiento", None))
#endif // QT_CONFIG(tooltip)
        self.labelInfoMoneda.setText(QCoreApplication.translate("MainWindow", u"\u26a0\ufe0f Los saldos se mostrar\u00e1n en la moneda seleccionada", None))
        self.labelInfoMoneda.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: #aaaaaa; font-size: 9pt;", None))
        self.labelNotas.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udccc Notas:", None))
        self.txtNotas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Detalles adicionales (opcional)", None))
#if QT_CONFIG(tooltip)
        self.txtNotas.setToolTip(QCoreApplication.translate("MainWindow", u"Campo opcional para informaci\u00f3n extra", None))
#endif // QT_CONFIG(tooltip)
        self.btnLimpiar.setText(QCoreApplication.translate("MainWindow", u"\ud83e\uddf9 Limpiar", None))
#if QT_CONFIG(tooltip)
        self.btnLimpiar.setToolTip(QCoreApplication.translate("MainWindow", u"Vac\u00eda todos los campos del formulario", None))
#endif // QT_CONFIG(tooltip)
        self.btnGuardar.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcbe Guardar Movimiento", None))
#if QT_CONFIG(tooltip)
        self.btnGuardar.setToolTip(QCoreApplication.translate("MainWindow", u"Guarda el movimiento (Ctrl+G)", None))
#endif // QT_CONFIG(tooltip)
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabRegistro), QCoreApplication.translate("MainWindow", u"\u2795 Registrar Movimiento", None))
        self.groupFiltros.setTitle(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d Filtros y b\u00fasqueda", None))
        self.txtBuscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0e Buscar por descripci\u00f3n...", None))
#if QT_CONFIG(tooltip)
        self.txtBuscar.setToolTip(QCoreApplication.translate("MainWindow", u"Filtra en tiempo real por texto", None))
#endif // QT_CONFIG(tooltip)
        self.labelFiltroCat.setText(QCoreApplication.translate("MainWindow", u"Mostrar:", None))
        self.comboFiltro.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))
        self.comboFiltro.setItemText(1, QCoreApplication.translate("MainWindow", u"Solo Ingresos", None))
        self.comboFiltro.setItemText(2, QCoreApplication.translate("MainWindow", u"Solo Gastos", None))

        self.labelFiltroCategoria.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda:", None))
        self.comboFiltroCategoria.setItemText(0, QCoreApplication.translate("MainWindow", u"Todas", None))
        self.comboFiltroCategoria.setItemText(1, QCoreApplication.translate("MainWindow", u"Alimentaci\u00f3n", None))
        self.comboFiltroCategoria.setItemText(2, QCoreApplication.translate("MainWindow", u"Transporte", None))
        self.comboFiltroCategoria.setItemText(3, QCoreApplication.translate("MainWindow", u"Vivienda / Servicios", None))
        self.comboFiltroCategoria.setItemText(4, QCoreApplication.translate("MainWindow", u"Salud", None))
        self.comboFiltroCategoria.setItemText(5, QCoreApplication.translate("MainWindow", u"Ocio / Entretenimiento", None))
        self.comboFiltroCategoria.setItemText(6, QCoreApplication.translate("MainWindow", u"Salario / Ingresos", None))
        self.comboFiltroCategoria.setItemText(7, QCoreApplication.translate("MainWindow", u"Otros", None))

        self.labelDesde.setText(QCoreApplication.translate("MainWindow", u"Desde:", None))
#if QT_CONFIG(tooltip)
        self.dateDesde.setToolTip(QCoreApplication.translate("MainWindow", u"Fecha inicial del rango", None))
#endif // QT_CONFIG(tooltip)
        self.labelHasta.setText(QCoreApplication.translate("MainWindow", u"Hasta:", None))
#if QT_CONFIG(tooltip)
        self.dateHasta.setToolTip(QCoreApplication.translate("MainWindow", u"Fecha final del rango", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.tablaMovimientos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tablaMovimientos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem2 = self.tablaMovimientos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None));
        ___qtablewidgetitem3 = self.tablaMovimientos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda", None));
        ___qtablewidgetitem4 = self.tablaMovimientos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem5 = self.tablaMovimientos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Monto", None));
        ___qtablewidgetitem6 = self.tablaMovimientos.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Notas", None));
        self.btnEliminar.setText(QCoreApplication.translate("MainWindow", u"\u274c Eliminar", None))
#if QT_CONFIG(tooltip)
        self.btnEliminar.setToolTip(QCoreApplication.translate("MainWindow", u"Elimina el movimiento seleccionado (con confirmaci\u00f3n)", None))
#endif // QT_CONFIG(tooltip)
        self.btnEditar.setText(QCoreApplication.translate("MainWindow", u"\u270f\ufe0f Editar", None))
#if QT_CONFIG(tooltip)
        self.btnEditar.setToolTip(QCoreApplication.translate("MainWindow", u"Edita el movimiento seleccionado", None))
#endif // QT_CONFIG(tooltip)
        self.btnCopiar.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udccb Copiar", None))
#if QT_CONFIG(tooltip)
        self.btnCopiar.setToolTip(QCoreApplication.translate("MainWindow", u"Crea un nuevo movimiento con los mismos datos", None))
#endif // QT_CONFIG(tooltip)
        self.btnExportarCSV.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udce5 Exportar CSV", None))
#if QT_CONFIG(tooltip)
        self.btnExportarCSV.setToolTip(QCoreApplication.translate("MainWindow", u"Exporta los movimientos filtrados a CSV", None))
#endif // QT_CONFIG(tooltip)
        self.lblSaldo.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcb0 Saldo Total: $0.00", None))
#if QT_CONFIG(tooltip)
        self.lblSaldo.setToolTip(QCoreApplication.translate("MainWindow", u"Saldo calculado: Ingresos - Gastos", None))
#endif // QT_CONFIG(tooltip)
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabHistorial), QCoreApplication.translate("MainWindow", u"\ud83d\udccb Historial de Movimientos", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuConfiguracion.setTitle(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.statusbar.setStatusTips(QCoreApplication.translate("MainWindow", u"Listo", None))
        self.btnToggleTheme.setText(QCoreApplication.translate("MainWindow", u"\ud83c\udf19 Tema", None))
#if QT_CONFIG(tooltip)
        self.btnToggleTheme.setToolTip(QCoreApplication.translate("MainWindow", u"Cambiar entre tema oscuro y claro", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

