import json

def main():
    print("Reading scratch_media.txt...")
    # Re-read scratch_media.txt since it is stored in the workspace
    try:
        with open("scratch_media.txt", "r", encoding="utf-8") as f:
            media_js = f.read()
    except FileNotFoundError:
        # If it was cleaned up, we can re-extract it from original HTML or test_base.html
        print("scratch_media.txt not found, re-extracting from test_base.html...")
        import re
        with open("test_base.html", "r", encoding="utf-8") as f:
            html = f.read()
        audio_paths = re.findall(r'<source\s+src="([^"]+)"\s+type="audio/[^"]+"', html)
        seen = set()
        audio_paths = [x for x in audio_paths if not (x in seen or seen.add(x))]
        preload_div_match = re.search(r'<div style="display:\s*none;">(.*?)</div>', html, re.DOTALL)
        if preload_div_match:
            preload_div_content = preload_div_match.group(1)
            image_paths = re.findall(r'<img\s+src="([^"]+)"', preload_div_content)
            seen_img = set()
            image_paths = [x for x in image_paths if not (x in seen_img or seen_img.add(x))]
        else:
            image_paths = re.findall(r'<img\s+src="([^"]+)"', html)
            seen_img = set()
            image_paths = [x for x in image_paths if not (x in seen_img or seen_img.add(x))]
        
        media_js = "const audioPreloads = [\n"
        for path in audio_paths:
            media_js += f"  \"{path}\",\n"
        media_js += "];\n\nconst imagePreloads = [\n"
        for path in image_paths:
            media_js += f"  \"{path}\",\n"
        media_js += "];\n"

    # Define the HTML template pieces
    html_start = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
  <meta name="theme-color" content="#000000">
  <meta name="color-scheme" content="light only">
  <meta name="robots" content="noindex, nofollow, noimageindex">
  <link rel="icon" href="favicon.ico" type="image/x-icon">
  <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
  
  <!-- Dynamic Base Tag Injector for local/production fallback -->
  <script>
    (function() {
      const baseEl = document.createElement('base');
      const isLocal = window.location.hostname === 'localhost' || 
                      window.location.hostname === '127.0.0.1' || 
                      !window.location.hostname;
      if (isLocal) {
        // Local/Offline Mode: Use current folder path as base
        baseEl.href = window.location.origin + window.location.pathname.substring(0, window.location.pathname.lastIndexOf('/')) + '/';
      } else {
        // Production Mode: Use GitHub Pages absolute path
        baseEl.href = "https://erhan3861.github.io/escape_marine/";
      }
      document.head.appendChild(baseEl);
      window.isLocalEnvironment = isLocal;
    })();
  </script>

  <link href="css/gf_SchibstedGrotesk.css" rel="stylesheet">
  <link href="css/view.0.0.87.css" rel="stylesheet">
  <title>Submarine Escape Game</title>
  <link href="css/main.105fc96e.css" rel="stylesheet">
  <link rel="stylesheet" href="css/gf_Viga.css" media="all">
  <link rel="stylesheet" href="css/gf_Barriecito.css" media="all">
  <link rel="stylesheet" href="css/gf_Sora.css" media="all">
  <link rel="stylesheet" href="css/gf_SourceSansPro.css" media="all">
  <link rel="stylesheet" href="css/gf_SchibstedGrotesk.css" media="all">
  <link rel="stylesheet" href="css/gf_OpenSans.css" media="all">
  <link rel="stylesheet" href="css/gf_Inter.css" media="all">
  <link rel="stylesheet" href="css/gf_DMSans.css" media="all">
  <style>
    body,
    html {
      padding: 0 !important;
    }
  </style>
</head>

<body>
  <noscript>You need to enable JavaScript to run this app.</noscript>
  <script src="static/js/offline.js" type="text/javascript"></script>

  <!-- ========================================== -->
  <!-- AI PLACEHOLDER GAME CONTENT (window.gameObject) -->
  <!-- ========================================== -->
  <script>
    window.gameObject = {
      // --- GİRİŞ / HOŞ GELDİNİZ EKRANI (WELCOME SCREEN) ---
      "WELCOME_HEADER": "{{WELCOME_HEADER}}",
      "WELCOME_TITLE": "{{WELCOME_TITLE}}",
      "WELCOME_START_BTN": "{{WELCOME_START_BTN}}",

      // --- HİKAYE GİRİŞ EKRANI (INTRODUCTION SLIDE) ---
      "INTRO_HEADER": "{{INTRO_HEADER}}",
      "INTRO_TEXT": "{{INTRO_TEXT}}",

      // --- BÖLÜM MENÜLERİ (LEVEL MENU SCREENS) ---
      "LEVEL_1_NAME": "{{LEVEL_1_NAME}}",
      "LEVEL_2_NAME": "{{LEVEL_2_NAME}}",
      "LEVEL_3_NAME": "{{LEVEL_3_NAME}}",
      "LEVEL_4_NAME": "{{LEVEL_4_NAME}}",
      "LEVEL_5_NAME": "{{LEVEL_5_NAME}}",

      // --- BÖLÜM 1: KAYALIK VADİ (STAGE 1: ROCKY VALLEY) ---
      "STAGE_1_TITLE": "{{STAGE_1_TITLE}}",
      "STAGE_1_DESC": "{{STAGE_1_DESC}}",

      // --- AKTİVİTELER (INTERACTIVE QUIZ QUESTIONS & ANSWERS) ---
      // Soru 1 (True/False - Whales)
      "QUESTION_1": {
        "text": "{{QUESTION_1_TEXT}}",
        "answers": [
          { "text": "{{QUESTION_1_A}}", "isCorrect": true },
          { "text": "{{QUESTION_1_B}}", "isCorrect": false }
        ]
      },

      // Soru 2 (Quiz - Which animal has a shell)
      "QUESTION_2": {
        "text": "{{QUESTION_2_TEXT}}",
        "answers": [
          { "text": "{{QUESTION_2_A}}", "isCorrect": true },
          { "text": "{{QUESTION_2_B}}", "isCorrect": false },
          { "text": "{{QUESTION_2_C}}", "isCorrect": false }
        ]
      },

      // Soru 3 (Quiz - Which of these are fish)
      "QUESTION_3": {
        "text": "{{QUESTION_3_TEXT}}",
        "answers": [
          { "text": "{{QUESTION_3_A}}", "isCorrect": false },
          { "text": "{{QUESTION_3_B}}", "isCorrect": false },
          { "text": "{{QUESTION_3_C}}", "isCorrect": false },
          { "text": "{{QUESTION_3_D}}", "isCorrect": true }
        ]
      },

      // Soru 4 (Quiz - Which has tentacles)
      "QUESTION_4": {
        "text": "{{QUESTION_4_TEXT}}",
        "answers": [
          { "text": "{{QUESTION_4_A}}", "isCorrect": true },
          { "text": "{{QUESTION_4_B}}", "isCorrect": false }
        ]
      },

      // Soru 5 (Flashlight function in underwater cave)
      "QUESTION_5": {
        "text": "{{QUESTION_5_TEXT}}",
        "answers": [
          { "text": "{{QUESTION_5_A}}", "isCorrect": true },
          { "text": "{{QUESTION_5_B}}", "isCorrect": false },
          { "text": "{{QUESTION_5_C}}", "isCorrect": false }
        ]
      },

      // Soru 6 (Equipment for exploring cave)
      "QUESTION_6": {
        "text": "{{QUESTION_6_TEXT}}",
        "answers": [
          { "text": "{{QUESTION_6_A}}", "isCorrect": true },
          { "text": "{{QUESTION_6_B}}", "isCorrect": false },
          { "text": "{{QUESTION_6_C}}", "isCorrect": false }
        ]
      },

      // Soru 7 (Natural habitat of eels)
      "QUESTION_7": {
        "text": "{{QUESTION_7_TEXT}}",
        "answers": [
          { "text": "{{QUESTION_7_A}}", "isCorrect": true },
          { "text": "{{QUESTION_7_B}}", "isCorrect": false },
          { "text": "{{QUESTION_7_C}}", "isCorrect": false }
        ]
      },

      // Soru 8 (Superpower Classification: Imagining)
      "QUESTION_8": {
        "text": "{{QUESTION_8_TEXT}}",
        "answers": [
          { "text": "{{QUESTION_8_A}}", "isCorrect": true },
          { "text": "{{QUESTION_8_B}}", "isCorrect": false },
          { "text": "{{QUESTION_8_C}}", "isCorrect": false }
        ]
      },

      // Soru 9 (Superpower Classification: Giant Memory)
      "QUESTION_9": {
        "text": "{{QUESTION_9_TEXT}}",
        "answers": [
          { "text": "{{QUESTION_9_A}}", "isCorrect": false },
          { "text": "{{QUESTION_9_B}}", "isCorrect": false },
          { "text": "{{QUESTION_9_C}}", "isCorrect": true }
        ]
      },

      // Soru 10 (Superpower Classification: Co-creation)
      "QUESTION_10": {
        "text": "{{QUESTION_10_TEXT}}",
        "answers": [
          { "text": "{{QUESTION_10_A}}", "isCorrect": false },
          { "text": "{{QUESTION_10_B}}", "isCorrect": true },
          { "text": "{{QUESTION_10_C}}", "isCorrect": false }
        ]
      },

      // Soru 11 (Superpower Classification: Empathy & Love)
      "QUESTION_11": {
        "text": "{{QUESTION_11_TEXT}}",
        "answers": [
          { "text": "{{QUESTION_11_A}}", "isCorrect": true },
          { "text": "{{QUESTION_11_B}}", "isCorrect": false },
          { "text": "{{QUESTION_11_C}}", "isCorrect": false }
        ]
      },

      // Soru 12 (Superpower Classification: Super Processing Speed)
      "QUESTION_12": {
        "text": "{{QUESTION_12_TEXT}}",
        "answers": [
          { "text": "{{QUESTION_12_A}}", "isCorrect": false },
          { "text": "{{QUESTION_12_B}}", "isCorrect": false },
          { "text": "{{QUESTION_12_C}}", "isCorrect": true }
        ]
      },

      // --- OYUN İÇİ DİĞER GÖRSEL METİNLER (IMAGE-BASED QUESTIONS) ---
      // Soru 1 (Yengeç görsel sorusu)
      "IMAGE_Q1_HEADER": "{{IMAGE_Q1_HEADER}}",
      "IMAGE_Q1_BODY": "{{IMAGE_Q1_BODY}}",
      "IMAGE_Q1_CHOICE_A": "{{IMAGE_Q1_CHOICE_A}}",
      "IMAGE_Q1_CHOICE_B": "{{IMAGE_Q1_CHOICE_B}}",
      "IMAGE_Q1_CHOICE_C": "{{IMAGE_Q1_CHOICE_C}}",
      "IMAGE_Q1_CHOICE_D": "{{IMAGE_Q1_CHOICE_D}}",
      "IMAGE_Q1_CHOICE_E": "{{IMAGE_Q1_CHOICE_E}}",
      "IMAGE_Q1_DRAG_TEXT": "{{IMAGE_Q1_DRAG_TEXT}}",

      // Soru 2 (Mavi balina görsel sorusu)
      "IMAGE_Q2_HEADER": "{{IMAGE_Q2_HEADER}}",
      "IMAGE_Q2_BODY": "{{IMAGE_Q2_BODY}}",
      "IMAGE_Q2_CHOICE_A": "{{IMAGE_Q2_CHOICE_A}}",
      "IMAGE_Q2_CHOICE_B": "{{IMAGE_Q2_CHOICE_B}}",
      "IMAGE_Q2_CHOICE_C": "{{IMAGE_Q2_CHOICE_C}}",
      "IMAGE_Q2_CHOICE_D": "{{IMAGE_Q2_CHOICE_D}}",
      "IMAGE_Q2_CHOICE_E": "{{IMAGE_Q2_CHOICE_E}}",

      // Soru 3 (Okyanuslardaki bol madde görsel sorusu)
      "IMAGE_Q3_HEADER": "{{IMAGE_Q3_HEADER}}",
      "IMAGE_Q3_BODY": "{{IMAGE_Q3_BODY}}",
      "IMAGE_Q3_CHOICE_A": "{{IMAGE_Q3_CHOICE_A}}",
      "IMAGE_Q3_CHOICE_B": "{{IMAGE_Q3_CHOICE_B}}",
      "IMAGE_Q3_CHOICE_C": "{{IMAGE_Q3_CHOICE_C}}",
      "IMAGE_Q3_CHOICE_D": "{{IMAGE_Q3_CHOICE_D}}",
      "IMAGE_Q3_CHOICE_E": "{{IMAGE_Q3_CHOICE_E}}",

      // Soru 4 (En büyük okyanus görsel sorusu)
      "IMAGE_Q4_HEADER": "{{IMAGE_Q4_HEADER}}",
      "IMAGE_Q4_BODY": "{{IMAGE_Q4_BODY}}",
      "IMAGE_Q4_CHOICE_A": "{{IMAGE_Q4_CHOICE_A}}",
      "IMAGE_Q4_CHOICE_B": "{{IMAGE_Q4_CHOICE_B}}",
      "IMAGE_Q4_CHOICE_C": "{{IMAGE_Q4_CHOICE_C}}",
      "IMAGE_Q4_CHOICE_D": "{{IMAGE_Q4_CHOICE_D}}",
      "IMAGE_Q4_CHOICE_E": "{{IMAGE_Q4_CHOICE_E}}",

      // --- BÖLÜM 2: YOSUN BARİYERİ (STAGE 2: LUSH BARRIER) ---
      "STAGE_2_TITLE": "{{STAGE_2_TITLE}}",
      "STAGE_2_DESC": "{{STAGE_2_DESC}}",

      // Soru 5 (Resimli palyaço balığı sorusu)
      "IMAGE_Q5_HEADER": "{{IMAGE_Q5_HEADER}}",
      "IMAGE_Q5_BODY": "{{IMAGE_Q5_BODY}}",

      // Soru 6 (Resimli yengeç sorusu)
      "IMAGE_Q6_HEADER": "{{IMAGE_Q6_HEADER}}",
      "IMAGE_Q6_BODY": "{{IMAGE_Q6_BODY}}",

      // Soru 7 (Resimli deniz kabuğu sorusu)
      "IMAGE_Q7_HEADER": "{{IMAGE_Q7_HEADER}}",
      "IMAGE_Q7_BODY": "{{IMAGE_Q7_BODY}}",

      // Soru 8 (Resimli deniz atı sorusu)
      "IMAGE_Q8_HEADER": "{{IMAGE_Q8_HEADER}}",
      "IMAGE_Q8_BODY": "{{IMAGE_Q8_BODY}}",

      // --- BÖLÜM 3: ÇOK YOLLU MAĞARA (STAGE 3: MULTI-PATH CAVE) ---
      "STAGE_3_TITLE": "{{STAGE_3_TITLE}}",
      "STAGE_3_DESC": "{{STAGE_3_DESC}}",

      // --- BÖLÜM 4: KARANLIK UÇURUM (STAGE 4: DARK ABYSS) ---
      "STAGE_4_TITLE": "{{STAGE_4_TITLE}}",
      "STAGE_4_DESC": "{{STAGE_4_DESC}}",

      // Sürükle Eşleştirme 1
      "MATCH_1_HEADER": "{{MATCH_1_HEADER}}",
      "STAGE_5_TITLE": "{{STAGE_5_TITLE}}",
      "STAGE_5_DESC": "{{STAGE_5_DESC}}",
      "MATCH_2_HEADER": "{{MATCH_2_HEADER}}",
      "MATCH_2_ITEM_1": "{{MATCH_2_ITEM_1}}",
      "MATCH_2_ITEM_2": "{{MATCH_2_ITEM_2}}",
      "MATCH_2_ITEM_3": "{{MATCH_2_ITEM_3}}",

      // Sürükle Eşleştirme 2
      "MATCH_3_ITEM_1": "{{MATCH_3_ITEM_1}}",
      "MATCH_3_ITEM_2": "{{MATCH_3_ITEM_2}}",
      "MATCH_3_ITEM_3": "{{MATCH_3_ITEM_3}}",

      // --- SON EKRANLAR (FINALE SCREENS) ---
      "FINALE_STORY_1": "{{FINALE_STORY_1}}",
      "FINALE_CHOOSE_CHEST": "{{FINALE_CHOOSE_CHEST}}",
      
      // Sandık Sonu 1
      "CHEST_1_TEXT": "{{CHEST_1_TEXT}}",
      "CHEST_1_TITLE": "{{CHEST_1_TITLE}}",
      
      // Sandık Sonu 2
      "CHEST_2_TEXT": "{{CHEST_2_TEXT}}",
      
      // Sandık Sonu 3
      "CHEST_3_TEXT": "{{CHEST_3_TEXT}}",
      "CHEST_3_TITLE": "{{CHEST_3_TITLE}}"
    };
  </script>

  <!-- ========================================== -->
  <!-- PRELOADS AND MERGING MAPPER LOGIC          -->
  <!-- ========================================== -->
  <script>
"""

    html_end = """
  // Dynamic media preloader
  function preloadMedia() {
    console.log("Starting media preloading...");
    if (typeof audioPreloads !== "undefined") {
      audioPreloads.forEach(src => {
        const a = new Audio();
        a.src = src;
      });
    }
    if (typeof imagePreloads !== "undefined") {
      imagePreloads.forEach(src => {
        const img = new Image();
        img.src = src;
      });
    }
  }

  // Safe text translation replacement
  function updateTextMessage(originalHtml, translation) {
    if (typeof translation === 'string') {
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = originalHtml;
      let textReplaced = false;
      function walk(node) {
        if (node.nodeType === Node.TEXT_NODE) {
          if (node.nodeValue.trim() !== "") {
            if (!textReplaced) {
              node.nodeValue = translation;
              textReplaced = true;
            } else {
              node.nodeValue = "";
            }
          }
        } else {
          for (let child of node.childNodes) {
            walk(child);
          }
        }
      }
      walk(tempDiv);
      return tempDiv.innerHTML;
    } else if (typeof translation === 'object' && translation !== null) {
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = originalHtml;
      let textNodes = [];
      function collectTextNodes(node) {
        if (node.nodeType === Node.TEXT_NODE) {
          if (node.nodeValue.trim() !== "") {
            textNodes.push(node);
          }
        } else {
          for (let child of node.childNodes) {
            collectTextNodes(child);
          }
        }
      }
      collectTextNodes(tempDiv);
      if (textNodes.length >= 1 && translation.header) {
        textNodes[0].nodeValue = translation.header;
      }
      if (textNodes.length >= 2 && translation.body) {
        textNodes[1].nodeValue = translation.body;
        for (let i = 2; i < textNodes.length; i++) {
          textNodes[i].nodeValue = "";
        }
      } else if (textNodes.length === 1 && translation.body) {
        textNodes[0].nodeValue = translation.header + " - " + translation.body;
      }
      return tempDiv.innerHTML;
    }
    return originalHtml;
  }

  // Applies clean template mappings to base Genially JSON structures
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

    // Apply translations on simple Text blocks
    if (data.Texts) {
      data.Texts.forEach(item => {
        const translation = textMapping[item.Id];
        if (translation) {
          item.TextMessage = updateTextMessage(item.TextMessage, translation);
        }
      });
    }

    // Apply quiz configurations (Questions, Choices, and Correctness)
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

    // Apply fallback static label translations
    const fallbackTranslations = {
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

    if (data.Texts) {
      data.Texts.forEach(item => {
        if (!textMapping[item.Id] && item.TextMessage) {
          const tempDiv = document.createElement('div');
          tempDiv.innerHTML = item.TextMessage;
          const plainText = tempDiv.textContent.trim().toLowerCase().replace(/\\s+/g, ' ');
          if (fallbackTranslations[plainText]) {
            item.TextMessage = updateTextMessage(item.TextMessage, fallbackTranslations[plainText]);
          }
        }
      });
    }
  }

  // Helper function to dynamically load webpack runtime scripts in sequence
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

  // Load game data externally and initialize the player engine
  async function init() {
    console.log("Loading base game data...");
    try {
      let data;
      // Determine the path to load data.json.
      // If we are on localhost, load directly from the local folder, bypassing the <base> tag domain.
      let dataUrl = 'data.json';
      if (window.isLocalEnvironment) {
        dataUrl = window.location.origin + window.location.pathname.substring(0, window.location.pathname.lastIndexOf('/')) + '/data.json';
        console.log("Local environment detected. Fetching game data from:", dataUrl);
      } else {
        dataUrl = 'https://erhan3861.github.io/escape_marine/data.json';
        console.log("Production environment detected. Fetching game data from:", dataUrl);
      }

      try {
        const res = await fetch(dataUrl);
        data = await res.json();
      } catch (fetchErr) {
        console.warn("Primary fetch failed, trying fallback local fetch...", fetchErr);
        // Direct local fetch fallback
        const fallbackUrl = window.location.origin + window.location.pathname.substring(0, window.location.pathname.lastIndexOf('/')) + '/data.json';
        const res = await fetch(fallbackUrl);
        data = await res.json();
      }

      // Map customized questions
      applyGameObjectMapping(data, window.gameObject);
      window.dataGeniallyOffline = data;

      // Start preloading media
      preloadMedia();

      // Load runtime engines in sequence
      console.log("Initializing player engine...");
      await loadScript('static/js/offline-runtime.5c6b7cc8.js');
      await loadScript('static/js/main.7e2d9301.js');
      console.log("Initialization complete. Submarine Escape Game Ready!");
    } catch (err) {
      console.error("Critical error during game initialization:", err);
    }
  }

  // Run on load
  window.addEventListener('DOMContentLoaded', init);
</script>

<input type="hidden" id="offline-6a1d323253aa85d97924e633" value="true">
<div class="iframe-container">
  <div class="container-wrapper-genially" style="position: relative; min-height: 400px; width: 100%;"><video
      class="loader-genially" autoplay="" loop="" playsinline="playsInline" muted=""
      style="position: absolute;top: 45%;left: 50%;transform: translate(-50%, -50%);width: 120px;height: 120px;margin-bottom: 10%">
      <source src="videos/loader-edu.mp4" type="video/mp4">Your browser does not support the video tag.
    </video>
    <div id="6a1d323253aa85d97924e633" class="genially-embed"
      style="margin: 0px auto; position: relative; height: auto; width: 100%;"></div>
  </div>
</div>

</body>
</html>
"""

    print("Assembling final HTML file...")
    # Assemble it
    html_content = html_start + media_js + html_end

    print("Writing to test_base copy.html...")
    with open("test_base copy.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Successfully compiled and saved test_base copy.html")

if __name__ == "__main__":
    main()
