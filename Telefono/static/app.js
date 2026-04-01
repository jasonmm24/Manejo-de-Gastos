// ==========================================
// VARIABLES GLOBALES Y ARRANQUE
// ==========================================
let graficoActual = null; // Guardará la instancia de la gráfica para poder actualizarla

// Cuando la página cargue, inicializamos todo
document.addEventListener('DOMContentLoaded', () => {
    // Poner la fecha de hoy por defecto en el formulario
    document.getElementById('dateFecha').valueAsDate = new Date();
    cargarDatos();
});

// ==========================================
// NAVEGACIÓN (PESTAÑAS)
// ==========================================
function cambiarPestana(idPestana) {
    // Ocultar todas las pestañas
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('activa');
    });
    // Quitar la clase 'activo' de todos los botones de navegación
    document.querySelectorAll('.barra-navegacion button').forEach(btn => {
        btn.classList.remove('activo');
    });

    // Mostrar la pestaña seleccionada y marcar su botón
    document.getElementById(idPestana).classList.add('activa');
    
    // Buscar el botón que corresponde a esa pestaña (basado en el ID)
    const idBoton = idPestana.replace('tab-', 'nav-');
    document.getElementById(idBoton).classList.add('activo');
}

// ==========================================
// LÓGICA DE DATOS (LOCALSTORAGE)
// ==========================================
function obtenerMovimientos() {
    // Leemos la memoria del celular. Si no hay nada, devolvemos un arreglo vacío []
    return JSON.parse(localStorage.getItem('finanzas_movimientos')) || [];
}

function guardarMovimientos(movimientos) {
    // Guardamos el arreglo en formato texto en la memoria del celular
    localStorage.setItem('finanzas_movimientos', JSON.stringify(movimientos));
}

// ==========================================
// REGISTRO Y EDICIÓN
// ==========================================
function registrarMovimiento() {
    const id_edicion = document.getElementById('id_edicion').value;
    const fecha = document.getElementById('dateFecha').value;
    const descripcion = document.getElementById('txtDescripcion').value.trim();
    const tipo = document.getElementById('comboTipo').value;
    const categoria = document.getElementById('comboCategoria').value;
    const monto = parseFloat(document.getElementById('spinMonto').value);
    const moneda = document.getElementById('comboMoneda').value;
    const notas = document.getElementById('txtNotas').value.trim();

    // Validación básica
    if (!descripcion || isNaN(monto) || monto <= 0 || !fecha) {
        alert("Por favor ingresa una fecha, descripción y un monto válido mayor a 0.");
        return;
    }

    let movimientos = obtenerMovimientos();

    if (id_edicion) {
        // Estamos editando un registro existente
        const index = movimientos.findIndex(m => m.id === id_edicion);
        if (index !== -1) {
            movimientos[index] = { id: id_edicion, fecha, descripcion, tipo, categoria, monto, moneda, notas };
        }
    } else {
        // Es un registro nuevo (creamos un ID único basado en la fecha y hora exacta)
        const nuevoMovimiento = {
            id: Date.now().toString(),
            fecha, descripcion, tipo, categoria, monto, moneda, notas
        };
        // Lo agregamos al inicio de la lista
        movimientos.unshift(nuevoMovimiento);
    }

    guardarMovimientos(movimientos);
    limpiarFormulario();
    cargarDatos();
    cambiarPestana('tab-movimientos'); // Regresar a la lista
}

function editarMovimiento(id) {
    const movimientos = obtenerMovimientos();
    const mov = movimientos.find(m => m.id === id);
    if (!mov) return;

    // Llenar el formulario con los datos
    document.getElementById('id_edicion').value = mov.id;
    document.getElementById('dateFecha').value = mov.fecha;
    document.getElementById('txtDescripcion').value = mov.descripcion;
    document.getElementById('comboTipo').value = mov.tipo;
    document.getElementById('comboCategoria').value = mov.categoria;
    document.getElementById('spinMonto').value = mov.monto;
    document.getElementById('comboMoneda').value = mov.moneda;
    document.getElementById('txtNotas').value = mov.notas;

    document.getElementById('titulo-form').innerText = "Editar Movimiento";
    document.getElementById('btnGuardar').innerText = "🔄 Actualizar";
    
    cambiarPestana('tab-registro');
}

function eliminarMovimiento(id) {
    if (confirm("¿Estás seguro de eliminar este registro?")) {
        let movimientos = obtenerMovimientos();
        movimientos = movimientos.filter(m => m.id !== id);
        guardarMovimientos(movimientos);
        cargarDatos();
    }
}

function limpiarFormulario() {
    document.getElementById('id_edicion').value = "";
    document.getElementById('dateFecha').valueAsDate = new Date();
    document.getElementById('txtDescripcion').value = "";
    document.getElementById('spinMonto').value = "";
    document.getElementById('txtNotas').value = "";
    
    document.getElementById('titulo-form').innerText = "Nuevo Movimiento";
    document.getElementById('btnGuardar').innerText = "💾 Guardar";
}

// ==========================================
// RENDERIZADO, FILTROS Y DASHBOARD
// ==========================================
function cargarDatos() {
    let movimientos = obtenerMovimientos();
    
    // Obtener valores de los filtros
    const textoBusqueda = document.getElementById('txtBuscar').value.toLowerCase();
    const filtroTipo = document.getElementById('comboFiltro').value;

    // Variables para los totales del Dashboard
    let totalIngresos = 0;
    let totalGastos = 0;
    let gastosPorCategoria = {};

    const listaHTML = document.getElementById('listaMovimientos');
    listaHTML.innerHTML = "";

    movimientos.forEach(mov => {
        // Acumular para el dashboard (se calcula con todos, sin importar el filtro de búsqueda)
        if (mov.tipo === 'Ingreso') {
            totalIngresos += mov.monto;
        } else {
            totalGastos += mov.monto;
            // Sumar a la categoría correspondiente para la gráfica
            gastosPorCategoria[mov.categoria] = (gastosPorCategoria[mov.categoria] || 0) + mov.monto;
        }

        // Aplicar filtros visuales para la lista
        const coincideTexto = mov.descripcion.toLowerCase().includes(textoBusqueda) || mov.categoria.toLowerCase().includes(textoBusqueda);
        const coincideTipo = filtroTipo === 'Todos' || mov.tipo === filtroTipo;

        if (coincideTexto && coincideTipo) {
            const claseMonto = mov.tipo === 'Ingreso' ? 'monto-ingreso' : 'monto-gasto';
            const signo = mov.tipo === 'Ingreso' ? '+' : '-';
            
            const li = document.createElement('li');
            li.className = 'item-movimiento';
            li.innerHTML = `
                <div class="item-info">
                    <span class="item-desc">${mov.descripcion}</span>
                    <span class="item-meta">📅 ${mov.fecha} | 📁 ${mov.categoria}</span>
                    <div class="item-acciones">
                        <button class="btn-editar" onclick="editarMovimiento('${mov.id}')">✏️ Editar</button>
                        <button class="btn-borrar" onclick="eliminarMovimiento('${mov.id}')">🗑️</button>
                    </div>
                </div>
                <div class="item-monto ${claseMonto}">
                    ${signo}$${mov.monto.toFixed(2)} <small>${mov.moneda}</small>
                </div>
            `;
            listaHTML.appendChild(li);
        }
    });

    // Actualizar Dashboard
    const saldo = totalIngresos - totalGastos;
    const lblSaldo = document.getElementById('lblSaldo');
    lblSaldo.innerText = `$${saldo.toFixed(2)}`;
    
    // Cambiar color del saldo si es negativo o positivo
    if(saldo < 0) { lblSaldo.style.color = "#e74c3c"; } 
    else { lblSaldo.style.color = "white"; } 

    document.getElementById('lblTotalIngresos').innerText = `$${totalIngresos.toFixed(2)}`;
    document.getElementById('lblTotalGastos').innerText = `$${totalGastos.toFixed(2)}`;

    actualizarPresupuesto(totalGastos);
    actualizarGrafico(gastosPorCategoria);
}

function resetearFiltros() {
    document.getElementById('txtBuscar').value = "";
    document.getElementById('comboFiltro').value = "Todos";
    cargarDatos();
}

function actualizarPresupuesto(gastosTotales = null) {
    if (gastosTotales === null) {
        // Si no se pasó el argumento, recalcular rápido
        let movs = obtenerMovimientos();
        gastosTotales = movs.filter(m => m.tipo === 'Gasto').reduce((sum, m) => sum + m.monto, 0);
    }
    
    const limite = parseFloat(document.getElementById('spinPresupuestoTotal').value) || 5000;
    const barra = document.getElementById('progressPresupuesto');
    
    barra.max = limite;
    barra.value = gastosTotales;

    // Si nos pasamos del presupuesto, cambiar el color a rojo
    if (gastosTotales > limite) {
        barra.classList.add('excedido');
    } else {
        barra.classList.remove('excedido');
    }
}

function actualizarGrafico(datosCategoria) {
    // PROTECCIÓN OFFLINE: Si la librería de internet no cargó, aborta en silencio para no romper la app
    if (typeof Chart === 'undefined') {
        console.log("Gráficos no disponibles sin conexión a internet.");
        return; 
    }

    const ctx = document.getElementById('graficoGastos').getContext('2d');
    
    // Si ya existía un gráfico, lo destruimos para que no se superponga
    if (graficoActual) {
        graficoActual.destroy();
    }

    const etiquetas = Object.keys(datosCategoria);
    const valores = Object.values(datosCategoria);

    if (etiquetas.length === 0) {
        // Gráfico vacío si no hay gastos
        graficoActual = new Chart(ctx, {
            type: 'doughnut',
            data: { labels: ['Sin Gastos'], datasets: [{ data: [1], backgroundColor: ['#e0e0e0'] }] }
        });
        return;
    }

    graficoActual = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: etiquetas,
            datasets: [{
                data: valores,
                backgroundColor: ['#e74c3c', '#f39c12', '#3498db', '#9b59b6', '#34495e']
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'bottom' }
            }
        }
    });
}

// ==========================================
// EXPORTACIÓN E IMPORTACIÓN
// ==========================================
function exportarCSV() {
    const movimientos = obtenerMovimientos();
    if(movimientos.length === 0) { alert("No hay datos para exportar"); return; }

    // Cabeceras idénticas a tu programa de Python para compatibilidad
    let csvContent = "ID,Fecha,Desc,Cat,Tipo,Monto,Moneda,Notas\n";
    
    movimientos.forEach(m => {
        // Limpiamos las comas de los textos para que no rompan el CSV
        const desc = m.descripcion.replace(/,/g, '');
        const notas = m.notas.replace(/,/g, '');
        csvContent += `${m.id},${m.fecha},${desc},${m.categoria},${m.tipo},${m.monto},${m.moneda},${notas}\n`;
    });

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.setAttribute("href", url);
    link.setAttribute("download", `Gastos_${new Date().toISOString().split('T')[0]}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function importarCSV(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {
        const text = e.target.result;
        const lineas = text.split('\n');
        let movimientosActuales = obtenerMovimientos();
        let agregados = 0;

        // Empezamos desde la línea 1 (saltamos la cabecera)
        for(let i = 1; i < lineas.length; i++) {
            const columnas = lineas[i].split(',');
            if(columnas.length >= 8) {
                const nuevoMov = {
                    id: columnas[0] || Date.now().toString() + i, // Usar ID del CSV o crear uno
                    fecha: columnas[1],
                    descripcion: columnas[2],
                    categoria: columnas[3],
                    tipo: columnas[4],
                    monto: parseFloat(columnas[5]),
                    moneda: columnas[6],
                    notas: columnas[7].trim()
                };
                // Evitar duplicados revisando si el ID ya existe
                if(!movimientosActuales.some(m => m.id === nuevoMov.id)) {
                    movimientosActuales.push(nuevoMov);
                    agregados++;
                }
            }
        }
        
        if (agregados > 0) {
            // Ordenar por fecha más reciente primero
            movimientosActuales.sort((a, b) => new Date(b.fecha) - new Date(a.fecha));
            guardarMovimientos(movimientosActuales);
            cargarDatos();
            alert(`Se importaron ${agregados} registros nuevos.`);
        } else {
            alert("No se encontraron registros nuevos o el formato es incorrecto.");
        }
        // Limpiar el input file
        event.target.value = '';
    };
    reader.readAsText(file);
}

function exportarPDF() {
    // PROTECCIÓN OFFLINE: Si jsPDF no cargó, avisa al usuario y no rompe la app
    if (typeof window.jspdf === 'undefined') { 
        alert("La exportación a PDF requiere conexión a internet para cargar las herramientas de diseño."); 
        return; 
    }

    const movimientos = obtenerMovimientos();
    if(movimientos.length === 0) { alert("No hay datos para generar el PDF"); return; }

    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    // Título del PDF
    doc.setFontSize(18);
    doc.text("Reporte Financiero (App Móvil)", 14, 20);
    
    doc.setFontSize(10);
    doc.text(`Generado el: ${new Date().toLocaleString()}`, 14, 28);

    // Preparar datos para la tabla
    const columnas = ["Fecha", "Descripción", "Tipo", "Categoría", "Monto"];
    const filas = movimientos.map(m => {
        const signo = m.tipo === 'Ingreso' ? '+' : '-';
        return [m.fecha, m.descripcion, m.tipo, m.categoria, `${signo}$${m.monto.toFixed(2)} ${m.moneda}`];
    });

    // Usar el plugin autoTable para dibujar la tabla bonita
    doc.autoTable({
        head: [columnas],
        body: filas,
        startY: 35,
        theme: 'grid',
        headStyles: { fillColor: [41, 128, 185] }, // Azul
        didParseCell: function(data) {
            // Colorear montos de rojo o verde en el PDF
            if (data.section === 'body' && data.column.index === 4) {
                if (data.row.raw[2] === 'Ingreso') {
                    data.cell.styles.textColor = [39, 174, 96]; // Verde
                } else {
                    data.cell.styles.textColor = [231, 76, 60]; // Rojo
                }
            }
        }
    });

    // Añadir resumen al final
    const finalY = doc.lastAutoTable.finalY + 15;
    const lblSaldo = document.getElementById('lblSaldo').innerText;
    const lblIng = document.getElementById('lblTotalIngresos').innerText;
    const lblGas = document.getElementById('lblTotalGastos').innerText;

    doc.setFontSize(12);
    doc.text(`Total Ingresos: ${lblIng}`, 14, finalY);
    doc.text(`Total Gastos: ${lblGas}`, 14, finalY + 8);
    doc.setFontSize(14);
    doc.setFont("helvetica", "bold");
    doc.text(`Saldo Final: ${lblSaldo}`, 14, finalY + 18);

    doc.save(`Reporte_Gastos_${new Date().toISOString().split('T')[0]}.pdf`);
}