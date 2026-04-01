<h1 align="center">Gestor de Gastos Móvil (PWA)</h1>

<p align="center">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JS">
  <img src="https://img.shields.io/badge/PWA-5A0FC8?style=for-the-badge&logo=pwa&logoColor=white" alt="PWA">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white" alt="ChartJS">
</p>

> **Nota del Proyecto:** Una solución ligera y eficiente para el control financiero personal, diseñada con un enfoque prioritario en la experiencia móvil y la independencia de red.

## Acerca del Proyecto

Esta es una **Progressive Web App (PWA)** enfocada en la gestión de ingresos y egresos. A diferencia de las aplicaciones convencionales, esta herramienta prioriza la privacidad y la disponibilidad, almacenando todo localmente y permitiendo el acceso total sin necesidad de una conexión a internet activa.

**Acceso Directo:** [Probar la App en vivo](https://jasonmm24.github.io/Manejo-de-Gastos/AppGeneral)

---

## Características Principales

* **Privacidad y Almacenamiento Local:** Los datos son tuyos. Todo se guarda directamente en la memoria de tu navegador/dispositivo a través de la caché local.
* **Dashboard Interactivo:** Análisis visual de tus finanzas mediante gráficas dinámicas impulsadas por Chart.js.
* **Reportes Profesionales:** Exportación de movimientos detallados a formato **PDF** (listos para imprimir) y soporte para archivos **CSV**.
* **Experiencia Nativa:** Instalable en la pantalla de inicio de Android e iOS como si fuera una aplicación de la tienda oficial.

---

## Estructura del Repositorio

El proyecto sigue una arquitectura sencilla y modular para facilitar su mantenimiento:

```text
📦 Manejo-de-Gastos
 ├── 📄 index.html          # Interfaz de usuario y estructura principal
 ├── 📄 sw.js               # Service Worker para gestión de caché y offline
 ├── 📄 manifest.json       # Configuración para la instalación de la PWA
 └── 📂 static/
     ├── 📄 app.js          # Lógica central (guardado, renderizado y exportación)
     ├── 📄 style.css       # Diseño visual y adaptabilidad móvil
     └── 📂 icons/          # Recursos gráficos (192x192 y 512x512)
```
---

## Instalación y Uso

### Para Usuarios (Móvil)
1. Abre el [enlace de la aplicación](https://jasonmm24.github.io/Manejo-de-Gastos/AppGeneral) desde Chrome o Safari.
2. En el menú del navegador, selecciona **"Instalar aplicación"** o **"Agregar a la pantalla de inicio"**.
3. Accede directamente desde tu menú de aplicaciones, incluso sin internet.

### Para Desarrolladores (Local)
Si deseas explorar o modificar el código:
1. Clona el repositorio:
   `git clone https://github.com/jasonmm24/Manejo-de-Gastos.git`
2. Navega a la carpeta y levanta un servidor local:
   `python -m http.server 8000`
3. Abre en tu navegador: `http://localhost:8000`

---

## Autor

* **Medina Martinez Jonathan Jason** - Desarrollo y Diseño - [@jasonmm24](https://github.com/jasonmm24)

Este proyecto es de código abierto y fue desarrollado con fines de aprendizaje y utilidad personal. ¡Las contribuciones son bienvenidas!
