import re
import json

def main():
    print("Reading template test_base copy.html...")
    with open("test_base copy.html", "r", encoding="utf-8") as f:
        template = f.read()

    # Define all original Turkish translations
    replacements = {
      "{{WELCOME_HEADER}}": "Fizik Laboratuvarına Gir",
      "{{WELCOME_TITLE}}": "Sürtünme Kuvveti Macerası",
      "{{WELCOME_START_BTN}}": "Başla",

      "{{INTRO_HEADER}}": "Giriş",
      "{{INTRO_TEXT}}": "Kayıp hazineleri bulmak için bu heyecan verici su altı macerasına katılın. Kötü Fener Balığı Kralı hazine sandığının anahtarlarını aldı; onları geri almak için onunla yüzleşin! Yol boyunca karşılaşacağınız fizik bilmecelerini ve sürtünme kuvveti zorluklarını çözün, okyanusun derinliklerindeki gizemli ganimeti ele geçirin!",

      "{{LEVEL_1_NAME}}": "BÖLÜM 1: Zorlu Yollar",
      "{{LEVEL_2_NAME}}": "BÖLÜM 2: Su ve Hava Direnci",
      "{{LEVEL_3_NAME}}": "BÖLÜM 3: Akışkanlar Direnci",
      "{{LEVEL_4_NAME}}": "BÖLÜM 4: Karanlık Uçurum",
      "{{LEVEL_5_NAME}}": "BÖLÜM 5: Sürtünme Laboratuvarı",

      "{{STAGE_1_TITLE}}": "Zorlu Yollar",
      "{{STAGE_1_DESC}}": "Soruları doğru cevaplayarak denizaltımızı engellere çarpmadan ilerletin!",

      "{{QUESTION_1_TEXT}}": "Sürtünme kuvveti her zaman hareket yönü ile aynı yönlüdür. Doğru mu, yanlış mı?",
      "{{QUESTION_1_A}}": "Doğru",
      "{{QUESTION_1_B}}": "Yanlış",

      "{{QUESTION_2_TEXT}}": "Aşağıdaki zeminlerden hangisinde sürtünme kuvveti en azdır?",
      "{{QUESTION_2_A}}": "Buz pisti",
      "{{QUESTION_2_B}}": "Halı kaplı zemin",
      "{{QUESTION_2_C}}": "Toprak saha",

      "{{QUESTION_3_TEXT}}": "Aşağıdaki eylemlerden hangisi sürtünme kuvvetini artırmak amacıyla yapılmıştır?",
      "{{QUESTION_3_A}}": "Makinelerin dişli çarklarının yağlanması",
      "{{QUESTION_3_B}}": "Ağır kolilerin altına tekerlek takılması",
      "{{QUESTION_3_C}}": "Kaydırak yüzeylerinin pürüzsüz yapılması",
      "{{QUESTION_3_D}}": "Karlı yollarda araç lastiklerine zincir takılması",

      "{{QUESTION_4_TEXT}}": "Havadaki cisimlerin hareketini zorlaştıran hava direncini azaltmak için hangisi yapılır?",
      "{{QUESTION_4_A}}": "Uçakların burun kısımlarının sivri tasarlanması",
      "{{QUESTION_4_B}}": "Paraşütlerin yüzey alanlarının geniş yapılması",

      "{{QUESTION_5_TEXT}}": "Pürüzlü yüzeylerde sürtünme kuvveti hakkında hangisi doğrudur?",
      "{{QUESTION_5_A}}": "Hareketi daha fazla zorlaştırır",
      "{{QUESTION_5_B}}": "Sürtünmeyi tamamen yok eder",
      "{{QUESTION_5_C}}": "Cismin hızını her zaman artırır",

      "{{QUESTION_6_TEXT}}": "Aşağıdakilerden hangisi pürüzsüz yüzeylere örnek olarak verilebilir?",
      "{{QUESTION_6_A}}": "Cam zemin",
      "{{QUESTION_6_B}}": "Çakıllı taşlı yol",
      "{{QUESTION_6_C}}": "Toprak saha",

      "{{QUESTION_7_TEXT}}": "Paraşütle atlayan bir sporcuya etki eden direnç kuvveti hangi ortamda gerçekleşir?",
      "{{QUESTION_7_A}}": "Hava ortamında (Hava direnci)",
      "{{QUESTION_7_B}}": "Toprakta (Katı sürtünmesi)",
      "{{QUESTION_7_C}}": "Suda (Su direnci)",

      "{{QUESTION_8_TEXT}}": "Sınıflandırma: **Karlı yollarda araç lastiklerine zincir takılması**",
      "{{QUESTION_8_A}}": "Sürtünmeyi Artırır 📈",
      "{{QUESTION_8_B}}": "Sürtünmeyi Azaltır 📉",
      "{{QUESTION_8_C}}": "Sürtünmeyi Etkilemez ⚖️",

      "{{QUESTION_9_TEXT}}": "Sınıflandırma: **Bir cismin renginin kırmızıdan maviye boyanması**",
      "{{QUESTION_9_A}}": "Sürtünmeyi Artırır 📈",
      "{{QUESTION_9_B}}": "Sürtünmeyi Azaltır 📉",
      "{{QUESTION_9_C}}": "Sürtünmeyi Etkilemez ⚖️",

      "{{QUESTION_10_TEXT}}": "Sınıflandırma: **Kapı menteşelerinin veya bisiklet zincirinin yağlanması**",
      "{{QUESTION_10_A}}": "Sürtünmeyi Artırır 📈",
      "{{QUESTION_10_B}}": "Sürtünmeyi Azaltır 📉",
      "{{QUESTION_10_C}}": "Sürtünmeyi Etkilemez ⚖️",

      "{{QUESTION_11_TEXT}}": "Sınıflandırma: **Merdiven basamaklarına kaydırmaz bant yapıştırılması**",
      "{{QUESTION_11_A}}": "Sürtünmeyi Artırır 📈",
      "{{QUESTION_11_B}}": "Sürtünmeyi Azaltır 📉",
      "{{QUESTION_11_C}}": "Sürtünmeyi Etkilemez ⚖️",

      "{{QUESTION_12_TEXT}}": "Sınıflandırma: **Bir kutunun üzerine isminin yazılması**",
      "{{QUESTION_12_A}}": "Sürtünmeyi Artırır 📈",
      "{{QUESTION_12_B}}": "Sürtünmeyi Azaltır 📉",
      "{{QUESTION_12_C}}": "Sürtünmeyi Etkilemez ⚖️",

      "{{IMAGE_Q1_HEADER}}": "Doğru cevabı bulun",
      "{{IMAGE_Q1_BODY}}": "Sert bir kabuğu ve kıskaçları olan deniz canlısı hangisidir?",
      "{{IMAGE_Q1_CHOICE_A}}": "Yengeç",
      "{{IMAGE_Q1_CHOICE_B}}": "Ahtapot",
      "{{IMAGE_Q1_CHOICE_C}}": "Denizanası",
      "{{IMAGE_Q1_CHOICE_D}}": "Istakoz",
      "{{IMAGE_Q1_CHOICE_E}}": "Mürekkep Balığı",
      "{{IMAGE_Q1_DRAG_TEXT}}": "Hedefi sürükleyin!",

      "{{IMAGE_Q2_HEADER}}": "Doğru cevabı bulun",
      "{{IMAGE_Q2_BODY}}": "Dünyadaki en büyük deniz memelisi hangisidir?",
      "{{IMAGE_Q2_CHOICE_A}}": "Mavi balina",
      "{{IMAGE_Q2_CHOICE_B}}": "Ahtapot",
      "{{IMAGE_Q2_CHOICE_C}}": "Deniz kaplumbağası",
      "{{IMAGE_Q2_CHOICE_D}}": "Yunus",
      "{{IMAGE_Q2_CHOICE_E}}": "Palyaço balığı",

      "{{IMAGE_Q3_HEADER}}": "Doğru cevabı bulun",
      "{{IMAGE_Q3_BODY}}": "Okyanuslarda en bol bulunan element/madde hangisidir?",
      "{{IMAGE_Q3_CHOICE_A}}": "Tuzlu su",
      "{{IMAGE_Q3_CHOICE_B}}": "Mercanlar",
      "{{IMAGE_Q3_CHOICE_C}}": "Kum",
      "{{IMAGE_Q3_CHOICE_D}}": "Kayalar",
      "{{IMAGE_Q3_CHOICE_E}}": "Sucul bitkiler",

      "{{IMAGE_Q4_HEADER}}": "Doğru cevabı bulun",
      "{{IMAGE_Q4_BODY}}": "Dünyadaki en büyük okyanus hangisidir?",
      "{{IMAGE_Q4_CHOICE_A}}": "Büyük Okyanus (Pasifik)",
      "{{IMAGE_Q4_CHOICE_B}}": "Hint Okyanusu",
      "{{IMAGE_Q4_CHOICE_C}}": "Güney Okyanusu",
      "{{IMAGE_Q4_CHOICE_D}}": "Atlas Okyanusu (Atlantik)",
      "{{IMAGE_Q4_CHOICE_E}}": "Arktik Okyanusu",

      "{{STAGE_2_TITLE}}": "Su ve Hava Direnci",
      "{{STAGE_2_DESC}}": "Karşımıza çıkan engelleri aşmak için hava ve su direnci sorularını doğru yanıtlayın!",

      "{{IMAGE_Q5_HEADER}}": "Görselleri inceleyin ve cevaplayın",
      "{{IMAGE_Q5_BODY}}": "Suda hareket eden cisimlerin gövdeleri su direncini (sürtünmeyi) azaltacak şekilde tasarlanır. Görsellerdeki balıklardan hangisi su direncini en aza indiren aerodinamik vücut yapısına sahiptir?",

      "{{IMAGE_Q6_HEADER}}": "Görselleri inceleyin ve cevaplayın",
      "{{IMAGE_Q6_BODY}}": "Hangi deniz canlısı deniz tabanında yürürken kaymamak için ayaklarındaki pürüzler sayesinde sürtünme kuvvetini kullanır?",

      "{{IMAGE_Q7_HEADER}}": "Görselleri inceleyin ve cevaplayın",
      "{{IMAGE_Q7_BODY}}": "Görsellerdeki deniz nesnelerinden hangisi pürüzlü ve çıkıntılı yapısıyla sürtünmeyi en fazla artırır?",

      "{{IMAGE_Q8_HEADER}}": "Görselleri inceleyin ve cevaplayın",
      "{{IMAGE_Q8_BODY}}": "Suda dik konumda durarak su direncine karşı farklı bir denge kuran, görsellerdeki bu sevimli canlı hangisidir?",

      "{{STAGE_3_TITLE}}": "Akışkanlar Direnci",
      "{{STAGE_3_DESC}}": "Hava ve su direncini azaltan veya artıran durumları ayırt ederek doğru mağaradan ilerleyin!",
      "{{STAGE_4_TITLE}}": "Karanlık Uçurum Labi",
      "{{STAGE_4_DESC}}": "Feneri sürükleyerek sürtünme kuvveti örneklerini ve kavramları doğru yerlere yerleştirin!",

      "{{MATCH_1_HEADER}}": "Sürtünme durumlarını örneklerle eşleştirin (Sürükle-Bırak)",
      "{{STAGE_5_TITLE}}": "Sürtünme Laboratuvarı",
      "{{STAGE_5_DESC}}": "Uzaktan bir ses dalgası yayılıyor... Sürtünme ve ses laboratuvarı yeni bir çalışma alanı hazırladı! Akışkan direncini ve sürtünmeyi etkileyen durumları doğru eşleştirerek yolunuza devam edin!",
      "{{MATCH_2_HEADER}}": "Sürtünme durumlarını örneklerle eşleştirin (Sürükle-Bırak)",
      "{{MATCH_2_ITEM_1}}": "1. Artırır (Kış Lastiği)",
      "{{MATCH_2_ITEM_2}}": "2. Azaltır (Makine Yağı)",
      "{{MATCH_2_ITEM_3}}": "3. Azaltır (Bavul Tekerleği)",

      "{{MATCH_3_ITEM_1}}": "2. Gemi burnu (Su direnci)",
      "{{MATCH_3_ITEM_2}}": "3. Halı zemin (Katı sürtünmesi)",
      "{{MATCH_3_ITEM_3}}": "1. Paraşüt (Hava direnci)",

      "{{FINALE_STORY_1}}": "Tüm sürtünme kuvveti zorluklarını aştınız ve anahtarı kazandınız! Hadi, anahtarı kullanarak sandığı açın!",
      "{{FINALE_CHOOSE_CHEST}}": "Hazine sandığınızı seçin",
      "{{CHEST_1_TEXT}}": "Fizik bilgileriniz sayesinde servet değerinde kalıntılarla dolu hazine sandığını buldunuz. Yüzeye çıktığınızda harika bir ödül sizi bekliyor olacak!",
      "{{CHEST_1_TITLE}}": "Tebrikler!",
      "{{CHEST_2_TEXT}}": "Kimin aklına gelirdi ki hazinenin içinde başka bir hazine haritasının saklı olduğu... Görünüşe göre bu denizaltının maceraları burada bitmiyor!",
      "{{CHEST_3_TEXT}}": "Görünüşe göre deniz altı sakinleri yeni kaptan olarak sizi seçti. Sürtünme kuvvetinin sırlarını çözerek iyi bir kaptan olmaya hazır mısınız?",
      "{{CHEST_3_TITLE}}": "Ne sürpriz ama!"
    }

    print("Replacing placeholders...")
    for key, value in replacements.items():
        template = template.replace(key, value)

    print("Saving test HTML test_base_test.html...")
    with open("test_base_test.html", "w", encoding="utf-8") as f:
        f.write(template)

    print("Successfully created test_base_test.html")

if __name__ == "__main__":
    main()
