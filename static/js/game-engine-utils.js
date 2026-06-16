/**
 * game-engine-utils.js
 * -------------------------------------------------------
 * Oyun motorunun ihtiyaç duyduğu yardımcı (utility)
 * fonksiyonlarını içerir. Soru içeriğinden tamamen
 * bağımsızdır; farklı oyun şablonlarında yeniden
 * kullanılabilir.
 * -------------------------------------------------------
 */

/**
 * audioPreloads ve imagePreloads dizilerindeki tüm
 * medya dosyalarını tarayıcı önbelleğine yükler.
 * Diziler media-preloads.js tarafından tanımlanmış olmalıdır.
 */
function preloadMedia() {
  console.log('Starting media preloading in background...');
  
  const loadAssets = () => {
    if (typeof audioPreloads !== 'undefined') {
      audioPreloads.forEach((src, index) => {
        setTimeout(() => {
          const a = new Audio();
          a.src = src;
        }, index * 50); // Stagger audio requests by 50ms
      });
    }
    if (typeof imagePreloads !== 'undefined') {
      imagePreloads.forEach((src, index) => {
        setTimeout(() => {
          const img = new Image();
          img.src = src;
        }, index * 20); // Stagger image requests by 20ms
      });
    }
  };

  if (typeof window.requestIdleCallback !== 'undefined') {
    window.requestIdleCallback(loadAssets);
  } else {
    setTimeout(loadAssets, 500);
  }
}

/**
 * Genially motor çıktısındaki TextMessage HTML bloğunu,
 * verilen çeviriyle güvenli biçimde günceller.
 *
 * @param {string} originalHtml  - Orijinal TextMessage HTML içeriği
 * @param {string|{header:string,body?:string}} translation - Yeni metin
 * @returns {string} Güncellenmiş HTML
 */
function updateTextMessage(originalHtml, translation) {
  if (typeof translation === 'string') {
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = originalHtml;
    let textReplaced = false;

    function walk(node) {
      if (node.nodeType === Node.TEXT_NODE) {
        if (node.nodeValue.trim() !== '') {
          if (!textReplaced) {
            node.nodeValue = translation;
            textReplaced = true;
          } else {
            node.nodeValue = '';
          }
        }
      } else {
        for (let child of node.childNodes) walk(child);
      }
    }

    walk(tempDiv);
    return tempDiv.innerHTML;
  }

  if (typeof translation === 'object' && translation !== null) {
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = originalHtml;
    const textNodes = [];

    function collectTextNodes(node) {
      if (node.nodeType === Node.TEXT_NODE) {
        if (node.nodeValue.trim() !== '') textNodes.push(node);
      } else {
        for (let child of node.childNodes) collectTextNodes(child);
      }
    }

    collectTextNodes(tempDiv);

    if (textNodes.length >= 1 && translation.header) {
      textNodes[0].nodeValue = translation.header;
    }
    if (textNodes.length >= 2 && translation.body) {
      textNodes[1].nodeValue = translation.body;
      for (let i = 2; i < textNodes.length; i++) textNodes[i].nodeValue = '';
    } else if (textNodes.length === 1 && translation.body) {
      textNodes[0].nodeValue = translation.header + ' - ' + translation.body;
    }

    return tempDiv.innerHTML;
  }

  return originalHtml;
}

/**
 * Verilen src yolundaki script'i DOM'a ekleyerek
 * yüklenmesini bekler (webpack runtime script'leri için).
 *
 * @param {string} src - Script URL'si
 * @returns {Promise<void>}
 */
function loadScript(src) {
  return new Promise((resolve, reject) => {
    const s = document.createElement('script');
    s.src = src;
    s.type = 'text/javascript';
    s.onload = resolve;
    s.onerror = reject;
    document.body.appendChild(s);
  });
}

// Global erişim için window'a bağla
window.preloadMedia       = preloadMedia;
window.updateTextMessage  = updateTextMessage;
window.loadScript         = loadScript;