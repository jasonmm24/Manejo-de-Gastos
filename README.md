============================================================
GESTOR DE GASTOS
============================================================

DESCRIPCIÓN:
Es una solución de escritorio integral y de código abierto diseñada 
para el control administrativo de ingresos y gastos. Combina una 
interfaz industrial moderna en modo oscuro con potentes herramientas 
de análisis de datos, permitiendo a individuos y pequeños negocios 
gestionar su salud financiera con precisión profesional.

CARACTERÍSTICAS PRINCIPALES:
---------------------------
1. DASHBOARD ANALÍTICO: 
   Visualización instantánea de saldo total, ingresos y gastos 
   acumulados mediante tarjetas de alto contraste.
   
2. CONTROL DE PRESUPUESTO: 
   Configuración de metas mensuales con barra de progreso dinámica 
   que cambia de color según el nivel de consumo.

3. GRÁFICOS DINÁMICOS: 
   Distribución porcentual de gastos por categoría mediante motor 
   de visualización QtCharts.

4. GESTIÓN AVANZADA DE HISTORIAL: 
   - Filtros cruzados por descripción, moneda y tipo de movimiento.
   - Herramientas de Edición, Eliminación y Copiado de registros.
   - Tooltips integrados para lectura de notas extensas.

5. IMPORTACIÓN Y EXPORTACIÓN:
   - Exportación de reportes profesionales en PDF (Formato A4).
   - Exportación e Importación de datos masivos mediante archivos CSV.

6. MULTIMONEDA: 
   Soporte nativo para MXN, USD y EUR con prefijos dinámicos.

REQUISITOS DEL SISTEMA:
----------------------
- Python 3.11 o superior.
- PySide6 (incluyendo los módulos QtUiTools y QtCharts).
- Motor de base de datos SQLite3 (integrado en Python).

INSTALACIÓN Y EJECUCIÓN:
-----------------------
1. Asegúrese de tener Python instalado.
2. Instalar las dependencias necesarias:
   pip install PySide6
3. Colocar los archivos 'main.py' e 'interfaz.ui' en la misma carpeta.
4. Ejecutar la aplicación:
   python main.py

ATAJOS DE TECLADO (HOTKEYS):
---------------------------
Para maximizar la eficiencia técnica, se han implementado:
- [Ctrl + G]: Ir a la pestaña de Registro y enfocar descripción.
- [Ctrl + E]: Editar el movimiento seleccionado en el historial.
- [Ctrl + L]: Limpiar rápidamente los campos del formulario.
- [Suprimir]: Eliminar el registro seleccionado (previa confirmación).

ESTRUCTURA DE ARCHIVOS:
----------------------
- main.py: Lógica de negocio, gestión de base de datos y eventos.
- interfaz.ui: Definición de la interfaz de usuario (XML).
- finanzas_personales.db: Base de datos relacional generada automáticamente.

LICENCIA:
---------
Este es un proyecto Open Source. Eres libre de usar, modificar y 
distribuir este software siempre que mantengas los créditos 
originales del autor.

DESARROLLADO POR: 
Medina Martinez Jonathan
============================================================
