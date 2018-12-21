var CACHE_STATIC_NAME = 'static-v6';
// var precacheResources = [
//   '/',
//
// ];

self.addEventListener('install', function (event) {
  console.log('[Service Worker] Installing Service Worker ...', event);
  event.waitUntil(
    caches.open(CACHE_STATIC_NAME)
      .then(function (cache) {
        console.log('[Service Worker] Precaching App Shell');
        cache.addAll([
          '/',

        ]);
      })
  )
});

// self.addEventListener('install', event => {
//   console.log('Service worker install event!');
//   event.waitUntil(
//     caches.open(staticCacheName)
//       .then(cache => {
//         return cache.addAll(precacheResources);
//       })
//   );
// });

self.addEventListener('activate', event => {
  console.log('Service worker activate event!');
});

self.addEventListener('fetch', event => {
  console.log('Fetch intercepted for:', event.request.url);
  event.respondWith(caches.match(event.request)
    .then(cachedResponse => {
        if (cachedResponse) {
          return cachedResponse;
        }
        return fetch(event.request);
      })
    );
})
