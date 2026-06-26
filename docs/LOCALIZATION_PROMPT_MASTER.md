# Eksiksiz Ceviri ve Yerellestirme Promptu

Bu prompt, `avukataysenuravci.com` icin tam ceviri/localization islemlerinde kullanilir.

## Master Prompt

```text
avukataysenuravci.com sitemin tam yerellestirmesi (localization) icin asagida paylastigim icerigi [HEDEF DIL] diline cevir.

Kesin Kurallar:
1) Sifir Turkce:
- Metin icerisinde Turkce kelime birakma.
- Istisna: ozel isimler (Muratcan Ciftci) ve sehir adlari (Gebze/Kocaeli).

2) Hukuki Terminoloji:
- Hedef dilde resmi hukuk terimlerini kullan.
- Ornek:
  - Avukat -> Attorney at Law
  - Hukuk Burosu -> Law Firm
  - Bosanma -> Divorce

3) Kod Koruma:
- Icerik HTML/PHP/JS/Flutter ise sadece kullaniciya gorunen metinleri cevir.
- Fonksiyon, degisken, class, id, tag ve teknik anahtar kelimelere dokunma.

4) Responsive Dostu:
- Cok uzun ifadelerden kacin.
- Mobilde satir tasmasi ve ust uste binme olmayacak sekilde kisa ve anlamli ceviri yap.

5) SEO Linkleri:
- Ic/dis linklerin yerini koru.
- Anchor textleri hedef dilde SEO uyumlu ve dogal cevir.

6) Cikti Formati:
- Ceviri sonucu orijinal yapiyi bozmadan, satir/sablon duzenini koruyarak ver.

Cevrilecek Icerik:
[BURAYA TURKCE KALAN KODU VEYA METNI YAPISTIR]
```

## Teknik Kontrol Listesi (Neden Hala Turkce Kalabilir?)

1) Dinamik Veriler:
- Veritabanindan gelen icerikler (yorumlar, otomatik basliklar, CMS alanlari) ayri ceviri gerektirebilir.

2) Placeholder Metinleri:
- Form placeholderlari (`Adiniz`, `Mesajiniz`) panel/eklenti ayarlarindan ayri cevriliyor olabilir.

3) Onbellek (Cache):
- Tarayici cache
- Uygulama cache
- CDN cache
- Ceviri sonrasi mutlaka temizlenmeli.

4) Hardcoded Metinler:
- JS dosyalarinda, template stringlerde veya inline HTML'de kalan sabit Turkce metinler olabilir.

5) Dil Dosyasi Kapsami:
- `translations`/i18n dosyasinda ilgili anahtar yoksa fallback Turkce gelebilir.

## Yayin Oncesi Hızlı QA

- Hedef dil sayfasinda Turkce karakter/kok kontrolu yap.
- Header, footer, buton, placeholder, hata mesaji ve CTA metinlerini tek tek kontrol et.
- Mobil gorunumde baslik ve buton satir kirilimlarini kontrol et.
- Anchor textlerin anlamli ve hedef dile uygun oldugunu dogrula.
