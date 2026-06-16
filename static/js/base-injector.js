/**
 * base-injector.js
 * -------------------------------------------------------
 * Sayfanın çalıştığı ortamı (yerel / GitHub Pages) algılar
 * ve <base href> etiketini dinamik olarak <head>'e ekler.
 * Bu sayede tüm göreli URL'ler (fetch, src, href) doğru
 * konumu işaret eder.
 * -------------------------------------------------------
 */
(function () {
  const baseEl = document.createElement('base');
  const isLocal =
    window.location.hostname === 'localhost' ||
    window.location.hostname === '127.0.0.1' ||
    !window.location.hostname;

  if (isLocal) {
    // Yerel / Offline mod: mevcut klasörü baz al
    baseEl.href =
      window.location.origin +
      window.location.pathname.substring(
        0,
        window.location.pathname.lastIndexOf('/')
      ) +
      '/';
  } else {
    // Production: GitHub Pages mutlak yolu
    baseEl.href = 'https://erhan3861.github.io/escape_marine/';
  }

  document.head.appendChild(baseEl);
  window.isLocalEnvironment = isLocal;
})();
