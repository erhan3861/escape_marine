/**
 * game-init.js
 * -------------------------------------------------------
 * Oyun motorunun başlatılmasından ve Genially data.json
 * ile window.gameObject arasındaki eşlemenin uygulanmasından
 * sorumludur.
 * -------------------------------------------------------
 */

// Statik / Fallback Çeviriler
const FALLBACK_TRANSLATIONS = {
  "try again!": "Tekrar Dene",
  "try again": "Tekrar Dene",
  "you will lose all your progress": "Tüm puanınız sıfırlanacak!",
  "are you sure you want to go back to the start?": "Başlangıç noktasına dönmek istediğinizden emin misiniz?",
  "are you sure you want to return to the start?": "Başlangıç noktasına dönmek istediğinizden emin misiniz?",
  "start over": "Tekrar Başla",
  "congratulations!": "Tebrikler!",
  "introduction": "Giriş",
  "level 1:rocky valley": "Bölüm 1: Zorlu Yollar",
  "level 2:dark abyss": "Bölüm 2: Su ve Hava Direnci",
  "level 3:lush barrier": "Bölüm 3: Akışkanlar Direnci",
  "level 4:multi-path cave": "Bölüm 4: Karanlık Uçurum",
  "level 5:marine opera": "Bölüm 5: Sürtünme Laboratuvarı",
  "continue": "İleri",
  "drag the words to their corresponding sound": "Kelimeleri ilgili alanlara sürükleyin",
  "drag the focus!": "Hedefi sürükleyin!",
  "observe the images and answer": "Görselleri inceleyin ve cevaplayın",
  "observe the images and respond": "Görselleri inceleyin ve cevaplayın",
  "find the correct answer": "Doğru cevabı bulun",
  "wow!": "Harika!"
};

/**
 * Özelleştirilmiş soruları ve metinleri temel Genially veri yapısına eşler.
 */
function applyGameObjectMapping(data, gameObject) {
  const textMapping = {
    "b7ad9e4e-fb1f-42b1-a4e2-d8c0d98ba2c9": gameObject.WELCOME_HEADER,
    "f40d8d7e-9a60-4a88-8ada-9b2bbf9a2021": gameObject.WELCOME_TITLE,
    "01b16593-8c1d-45fe-8f87-6e6d1bec1e26": gameObject.WELCOME_START_BTN,
    "6df3a1b4-aebf-4b07-86f2-b2bcf5138fe0": gameObject.INTRO_HEADER,
    "ffa142d0-e7df-4b86-86a2-d6b0df877c63": gameObject.INTRO_TEXT,
    
    "43728f55-715f-46b5-99f0-2c634b439bbd": gameObject.LEVEL_1_NAME,
    "8c39c649-a75c-484e-a9b0-e74f4450ed0d": gameObject.LEVEL_2_NAME,
    "d5899a02-f9df-41ff-9ca7-12b13e89effa": gameObject.LEVEL_3_NAME,
    "2f0baa85-c254-4f82-a011-3af059ca40f2": gameObject.LEVEL_4_NAME,
    "0da3ebe7-0f34-4ac0-a640-720646189348": gameObject.LEVEL_5_NAME,
    
    "ac4b357d-1d4b-4ab9-9de9-b08ddd0b6aac": gameObject.STAGE_1_TITLE,
    "516a5a8d-0649-49f9-a1f1-b3b29e0a284a": gameObject.STAGE_1_DESC,
    "e8cb38bd-4028-4aab-99e9-17a06d2564db": gameObject.STAGE_2_TITLE,
    "2e27682d-44f1-4e4f-8b42-5c2a03ea17cc": gameObject.STAGE_2_DESC,
    "f4a3f0ab-e39e-4847-a6e4-2e33b9cb8dd9": gameObject.STAGE_3_TITLE,
    "656f0502-1578-4a0e-8c52-150acfd1ab04": gameObject.STAGE_3_DESC,
    "97206baa-b7ba-4f50-b1b3-37a5848d0f2e": gameObject.STAGE_4_TITLE,
    "1a004fde-4d78-4943-985c-912c6c7cb109": gameObject.STAGE_4_DESC,
    "5ff30151-e845-40a7-bdad-9eea68d28826": gameObject.STAGE_5_TITLE,
    "87c9187f-9ab2-4a3d-a183-a29a5b380f98": gameObject.STAGE_5_DESC,
    
    "3d53491f-0cc8-4583-95ed-e97822327467": gameObject.MATCH_1_HEADER,
    "3966595a-d8e3-42e7-b41c-33469b266638": gameObject.MATCH_2_HEADER,
    "53c05557-2f5d-44c7-8e34-e0b97a98398f": gameObject.MATCH_2_ITEM_1,
    "9565d512-ebfd-4984-940e-1d157d5e0595": gameObject.MATCH_2_ITEM_2,
    "415f8fdc-da14-4448-ab6d-3e82025347bd": gameObject.MATCH_2_ITEM_3,
    
    "2626d3bb-f1c5-49c3-a490-e300c8c10b18": gameObject.MATCH_3_ITEM_1,
    "6573a1bb-a0f3-4775-8409-37ecbdfc8e86": gameObject.MATCH_3_ITEM_2,
    "00eeb14c-0218-48be-b832-44d8fd5bf828": gameObject.MATCH_3_ITEM_3,
    
    "9808db92-d50f-4acb-851a-c25e30aac333": gameObject.FINALE_STORY_1,
    "6eb6dc28-bb8b-4137-8aa3-a6bce436079e": gameObject.FINALE_CHOOSE_CHEST,
    
    "de7857c2-66cc-4b0b-b88e-41abf4a8216f": gameObject.CHEST_1_TEXT,
    "2fbcff4a-5e78-4b76-bb1a-4f2da7533eed": gameObject.CHEST_1_TITLE,
    "4dbc56c9-2639-44d2-ace7-a07bbe758e1e": gameObject.CHEST_2_TEXT,
    "75a463df-ed03-4e5e-a5cb-11b328f0fe8f": gameObject.CHEST_3_TEXT,
    "3556c037-0d93-4647-ae77-4b51cea6118d": gameObject.CHEST_3_TITLE,

    // Image Q1
    "5f6dcd2a-8ba0-4227-9d2c-0144124680db": { "header": gameObject.IMAGE_Q1_HEADER, "body": gameObject.IMAGE_Q1_BODY },
    "c0371aa6-2c6b-409d-9469-d5c80d8e5e4c": gameObject.IMAGE_Q1_CHOICE_A,
    "a8a2ff09-f5bd-402d-b51a-c79ba5f14b5c": gameObject.IMAGE_Q1_CHOICE_B,
    "89101794-44f9-45ff-8f32-c3b06de3f321": gameObject.IMAGE_Q1_CHOICE_C,
    "a4a812f1-f27d-48fa-9bdb-a6732fabbc98": gameObject.IMAGE_Q1_CHOICE_D,
    "4b9db5c6-f0f4-4af4-9471-e1aa34047cca": gameObject.IMAGE_Q1_CHOICE_E,
    "89b28133-a96a-41b5-b514-f0ba07b2d404": gameObject.IMAGE_Q1_DRAG_TEXT,

    // Image Q2
    "ac6019e8-d7ce-4be8-9eb1-e3d9d7fe202a": { "header": gameObject.IMAGE_Q2_HEADER, "body": gameObject.IMAGE_Q2_BODY },
    "3ee6849b-a4f3-43f4-9239-87357eb3a5be": gameObject.IMAGE_Q2_CHOICE_A,
    "ca696c61-e596-4c66-b7e5-8e8bc6700e74": gameObject.IMAGE_Q2_CHOICE_B,
    "33460070-9900-4cca-be5c-088aad682470": gameObject.IMAGE_Q2_CHOICE_C,
    "8bc3d844-529a-41a6-8619-4abd473af7ac": gameObject.IMAGE_Q2_CHOICE_D,
    "303ee3ea-6358-4712-9a04-91f0dac51ae2": gameObject.IMAGE_Q2_CHOICE_E,

    // Image Q3
    "899fe4fa-1437-4561-b635-3b7a57954f3a": { "header": gameObject.IMAGE_Q3_HEADER, "body": gameObject.IMAGE_Q3_BODY },
    "f2e14711-0ddf-4b85-9ded-ac323ee60498": gameObject.IMAGE_Q3_CHOICE_A,
    "e1261b3e-89c8-4b70-b470-c9bfe3ef3c3a": gameObject.IMAGE_Q3_CHOICE_B,
    "8455cd12-f5df-4264-8b26-cf882219ec42": gameObject.IMAGE_Q3_CHOICE_C,
    "239d6977-9850-4cf7-81e4-6e04d8e2c806": gameObject.IMAGE_Q3_CHOICE_D,
    "ab0c9313-dace-48e6-8867-a27a4c27020d": gameObject.IMAGE_Q3_CHOICE_E,

    // Image Q4
    "a16eb8bf-a8ce-416c-b7c9-2fbf147d5098": { "header": gameObject.IMAGE_Q4_HEADER, "body": gameObject.IMAGE_Q4_BODY },
    "8078fa1c-f806-4aef-bf95-5db6724736cd": gameObject.IMAGE_Q4_CHOICE_A,
    "8756c762-3981-4494-a4d1-fe76524e2928": gameObject.IMAGE_Q4_CHOICE_B,
    "0daa4438-747f-4cf7-bad3-cb51b7cf8fc5": gameObject.IMAGE_Q4_CHOICE_C,
    "bdcdba24-6a0a-42eb-989b-3bda50f3288e": gameObject.IMAGE_Q4_CHOICE_D,
    "3ef05600-2e32-4600-b996-643d6d10818f": gameObject.IMAGE_Q4_CHOICE_E,

    // Stage 2 visual Qs
    "0a0d1662-dce3-4e62-b57d-b1ca21796b2f": { "header": gameObject.IMAGE_Q5_HEADER, "body": gameObject.IMAGE_Q5_BODY },
    "4ef86d11-cdf2-424e-860d-4b87c139983e": { "header": gameObject.IMAGE_Q6_HEADER, "body": gameObject.IMAGE_Q6_BODY },
    "f0848bfd-680d-431c-bd42-c83a9b90217b": { "header": gameObject.IMAGE_Q7_HEADER, "body": gameObject.IMAGE_Q7_BODY },
    "b0e80159-9966-4c64-863b-023a91c4a4b7": { "header": gameObject.IMAGE_Q8_HEADER, "body": gameObject.IMAGE_Q8_BODY }
  };

  // Metin bloklarına çevirileri uygula
  if (data.Texts) {
    data.Texts.forEach(item => {
      const translation = textMapping[item.Id];
      if (translation) {
        item.TextMessage = updateTextMessage(item.TextMessage, translation);
      }
    });
  }

  // Quiz Soruları Eşlemesi
  const quizMapping = {
    "793811da-c826-4045-a9b7-abcb5fb5f121": gameObject.QUESTION_1,
    "3d86c82f-c672-44fb-b989-191434ad4d05": gameObject.QUESTION_2,
    "b36b0027-4c47-40d6-865b-eb8f8c781734": gameObject.QUESTION_3,
    "0adf7f1d-a34a-46b5-88f8-97b0809d1f87": gameObject.QUESTION_4,
    "a4928b74-e17b-46d3-9b13-f7de5397aacb": gameObject.QUESTION_5,
    "de548e47-5f11-4468-ab0e-2bd807ff09d2": gameObject.QUESTION_6,
    "74d16d54-10bb-4f18-b0ad-e09992c0ad8f": gameObject.QUESTION_7,
    "8a1b84a5-4382-465d-9504-289eb75e4d63": gameObject.QUESTION_8,
    "99e6afce-c97e-442b-8d33-780df41fb686": gameObject.QUESTION_9,
    "cee5eb4b-370d-4e08-9d95-980cd779e1a7": gameObject.QUESTION_10,
    "11c46ad2-8a47-447f-8060-0d3f14ac8bc5": gameObject.QUESTION_11,
    "2a1c22be-cdd7-4939-9a1b-7984e228e81a": gameObject.QUESTION_12
  };

  if (data.Activities) {
    data.Activities.forEach(act => {
      const qConfig = quizMapping[act.Id];
      if (qConfig) {
        act.Question = qConfig.text;
        if (act.Answers && qConfig.answers) {
          act.Answers.forEach((ans, aIdx) => {
            const mappedAns = qConfig.answers[aIdx];
            if (mappedAns) {
              ans.Text = mappedAns.text;
              ans.IsCorrect = mappedAns.isCorrect;
            }
          });
        }
      }
    });
  }

  // Statik / Fallback Çeviriler
  if (data.Texts) {
    data.Texts.forEach(item => {
      if (!textMapping[item.Id] && item.TextMessage) {
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = item.TextMessage;
        const plainText = tempDiv.textContent.trim().toLowerCase().replace(/\s+/g, ' ');
        if (FALLBACK_TRANSLATIONS[plainText]) {
          item.TextMessage = updateTextMessage(item.TextMessage, FALLBACK_TRANSLATIONS[plainText]);
        }
      }
    });
  }
}

/**
 * Ana başlatma fonksiyonu.
 * data.json'u yükler -> eşlemeleri uygular -> oyun motorlarını sırayla başlatır.
 */
async function init() {
  console.log('Loading base game data...');
  try {
    let data;
    const dataUrl = 'data.json';
    let cachedData = null;

    // Try reading from parent window cache (same-origin check)
    try {
      if (window.parent && window.parent !== window && window.parent.dataGeniallyOfflineCache) {
        cachedData = window.parent.dataGeniallyOfflineCache;
      }
    } catch (e) {
      // Cross-origin iframe parent access blocked, fallback to local window cache
    }

    // Try reading from local window cache
    if (!cachedData && window.dataGeniallyOfflineCache) {
      cachedData = window.dataGeniallyOfflineCache;
    }

    if (cachedData) {
      console.log('Using cached game data from memory...');
      data = cachedData;
    } else {
      const res = await fetch(dataUrl);
      data = await res.json();
      
      // Try saving to parent window cache
      try {
        if (window.parent && window.parent !== window) {
          window.parent.dataGeniallyOfflineCache = data;
        }
      } catch (e) {
        // Cross-origin access blocked, ignore
      }
      window.dataGeniallyOfflineCache = data;
    }

    applyGameObjectMapping(data, window.gameObject);
    window.dataGeniallyOffline = data;

    console.log('Initializing player engine...');
    // Scriptler relative yüklenir (base tag'e göre çözümlenir)
    await loadScript('static/js/offline-runtime.5c6b7cc8.js');
    await loadScript('static/js/main.7e2d9301.js');

    preloadMedia();

    console.log('Initialization complete. Submarine Escape Game Ready!');
  } catch (err) {
    console.error('Critical error during game initialization:', err);
  }
}

window.addEventListener('DOMContentLoaded', init);