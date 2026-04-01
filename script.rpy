# 1. Karakter Tanımları
define a = Character("Alkız (Ala)", color="#ff4444")
define k = Character("Bilge Kaplumbağa", color="#2ecc71")
define l = Character("Luck", color="#44aaff")
define lu = Character("Lucie", color="#ff44aa")
define r = Character("Kütüphaneci Rıza", color="#ffcc00")
define h = Character("Hamide", color="#33ff33")
define hp = Character("Hayri Pıtır", color="#00eeee")
define g = Character("Gölge Efendi", color="#000000")

# 2. Görsel Tanımları - SADECE ZOOM 3.0 EKLENDİ
image bg gokkubbe:
    "gokkubbe.png"
    zoom 3.0
    xalign 0.5 yalign 0.5

image bg kutuphane:
    "kutuphane.png"
    zoom 3.0
    xalign 0.5 
    yalign 0.0 # Kütüphane yukarıda

image bg oda:
    "luckvelucieninodasi.png"
    zoom 3.0
    xalign 0.5 yalign 0.5

image bg sera:
    "hamideninsakliserasi.png"
    zoom 3.0
    xalign 0.5 yalign 0.5

image alkiz = "Alkiz.png"
image kaplumbaga = "kaplumbaga.png"
image hayri_pitir = "hayripitir.png"
image luck = "luck.png"
image lucie = "lucie.png"
image riza = "riza.png"
image hamide = "hamide.png"

# -------------------------------------------------------------------------
# OYUN BAŞLIYOR (SENARYOYA DOKUNULMADI)
# -------------------------------------------------------------------------
label start:
    scene bg gokkubbe with fade
    "Sistem: MOGWARTS TEHLİKELİ OYUN - Bölüm 2 Başlıyor..."
    
    show kaplumbaga at left
    show alkiz at right
    k "Alkız, Hayri Pıtır'ın gözleri tuhaf bakıyor. Sanki burada değil gibi!"

    menu:
        "Hayri'nin yanına git ve konuş.":
            jump hayri_hipnoz_farkediş
        "Onu uzaktan izle.":
            "Hayri kendi kendine anlaşılmayan kodlar sayıklıyor..."
            jump hayri_hipnoz_farkediş

label hayri_hipnoz_farkediş:
    scene bg oda with dissolve
    show hayri_pitir at center
    hp "Sistem... Silinmeli... Efendim emretti... Her şey kararmalı..."
    
    menu:
        "Onu sarsarak uyandırmaya çalış.":
            a "Hayri! Kendine gel! Kim bu Efendi?"
            jump soru_3
        "Sihirli aynayı ona doğrult.":
            "Aynada Hayri'nin arkasında dev bir gölge göründü!"
            jump soru_3

label soru_3:
    scene bg kutuphane
    show riza at center
    r "Alkız! Hayri aslında iyi biri, ama 'Gölge Efendi' onu hipnotize etmiş!"
    
    menu:
        "Hipnozu bozacak antik kitabı bul.":
            jump soru_5
        "Kütüphanenin ışıklarını yak.":
            "Gölge ışıktan korkar! Hayri biraz kendine geldi."
            jump soru_5

label soru_5:
    scene bg sera with fade
    show hamide at left
    show hayri_pitir at right
    h "Onu seraya getirin! Şifalı otlar zihnini temizleyebilir."
    
    menu:
        "Mor Lavanta tozunu kullan.":
            "Hayri'nin gözlerindeki siyahlık dağılıyor!"
            jump hayri_kurtulus
        "Zehirli mantarı kullan.":
            "HATA! Hayri daha da saldırganlaştı!"
            jump start

label hayri_kurtulus:
    scene bg gokkubbe
    show hayri_pitir at center
    hp "Ah... Başım çok ağrıyor. Alkız? Ben neden kütüphaneyi hackledim? Özür dilerim!"
    
    menu:
        "Onu affet ve ekibe dahil et.":
            a "Sorun değil Hayri, seni hipnotize ettiler. Bize yardım etmelisin!"
            jump soru_7
        "Ona hala şüpheyle bak.":
            a "Sana tam güvenemiyorum ama şimdilik yanımızda kal."
            jump soru_7

label soru_7:
    scene bg oda
    show luck at left
    show lucie at right
    l "Gölge Efendi kaçtı ama arkasında bir dosya bıraktı!"
    
    menu:
        "Dosyayı Hayri'ye incelet.":
            hp "Bu bir virüs! Mogwarts'ın kalbine gidiyor!"
            jump soru_8
        "Dosyayı Kütüphaneci Rıza'ya götür.":
            r "Bu çok eski bir düşman..."
            jump soru_8

label soru_8:
    scene bg kutuphane
    show riza at left
    show hayri_pitir at right
    r "Gölge Efendi, kütüphanenin gizli bölmesine sızmış!"
    
    menu:
        "Gizli bölmenin kapısını kır.":
            jump soru_9
        "Hayri ile kapının şifresini kır.":
            jump soru_9

label soru_9:
    scene bg gokkubbe
    show kaplumbaga at center
    k "Dikkatli olun! Gölge her yerde olabilir!"
    
    menu:
        "Işık kalkanını aktif et.":
            jump soru_10
        "Karanlıkta ilerle.":
            "TUZAK! Gölge sizi yakaladı."
            jump start

label soru_10:
    scene bg sera
    show hamide at center
    h "Gölge Efendi seradaki çiçekleri solduruyor! Bir şey yapmalıyız!"
    
    menu:
        "Çiçeklere can suyu ver.":
            jump soru_11
        "Gölgeye doğrudan saldır.":
            jump soru_11

label soru_11:
    scene bg oda
    show lucie at left
    show luck at right
    lu "Gölge Efendi'nin asıl amacı Luck ve Lucie'yi kaçırmakmış!"
    
    menu:
        "Onları Gökkubbe'ye sakla.":
            jump soru_12
        "Onları Kütüphaneye sakla.":
            jump soru_12

label soru_12:
    scene bg gokkubbe
    show hayri_pitir at left
    show alkiz at right
    hp "Alkız, benim kodlarım Gölge Efendi'nin kalkanını delebilir!"
    
    menu:
        "Hayri'ye enerji ver.":
            jump soru_13
        "Kendi kanatlarınla saldır.":
            jump soru_13

label soru_13:
    scene bg kutuphane
    show riza at center
    r "Son bir hamle kaldı! Gölge'nin kalbi kütüphanedeki eski bir sunucuda!"
    
    menu:
        "Sunucuyu kapat.":
            jump soru_14
        "Sunucuyu yeniden başlat.":
            jump soru_14

label soru_14:
    scene bg sera
    show hamide at left
    show kaplumbaga at right
    k "Mogwarts'ın tüm dostları burada! Hep beraber bağıralım!"
    
    menu:
        "Mogwarts Güvende!":
            jump final_savasi
        "Gölgeye Elveda!":
            jump final_savasi

label final_savasi:
    scene bg gokkubbe with dissolve
    show hayri_pitir at left
    show alkiz at right
    hp "İşte orada! Gölge Efendi zayıfladı!"
    
    menu:
        "Mogwarts'ın Işığını Patlat!":
            jump bitis
        "Hayri ile beraber dev bir kod yazarak onu sil!":
            jump bitis

label bitis:
    "MOGWARTS TEHLİKELİ OYUN - SEZON 1 MUHTEŞEM FİNAL"

    return