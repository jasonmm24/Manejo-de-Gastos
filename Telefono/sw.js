const CACHE_NAME = 'gastos-blindado-v5';

// Usamos rutas absolutas desde la raíz para que el celular no se pierda
const archivos = [
  '/index.html',
  '/static/style.css',
  '/static/app.js',
  '/manifest.json'
];

self.addEventListener('install', event => {
  self.skipWaiting(); // TRUCO: Fuerza a la app a usar la nueva versión inmediatamente
  event.waitUntil(
    caches.open(CACHE_NAME).then(async cache => {
      // TRUCO: Guarda archivo por archivo. Si uno falla, no cancela a los demás.
      for (let archivo of archivos) {
        try {
          await cache.add(archivo);
        } catch (e) {
          console.log("No se pudo guardar, pero continuamos: " + archivo);
        }
      }
    })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      // Borra cualquier versión vieja que haya quedado atrapada
      return Promise.all(keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key)));
    })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      // 1. Si está guardado, úsalo.
      if (response) return response;
      
      // 2. Si no, búscalo. Si falla (no hay internet), fuerza el index.html
      return fetch(event.request).catch(() => caches.match('/index.html'));
    })
  );
});