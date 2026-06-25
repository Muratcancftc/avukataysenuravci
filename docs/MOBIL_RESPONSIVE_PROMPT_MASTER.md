# Mobil Okunabilirlik ve Responsive Prompt Paketi

Bu dokuman, makale iceriklerinin mobil cihazlarda maksimum okunabilirlikte olmasi ve responsive tasarim hatalarinin sistematik olarak giderilmesi icin kullanilir.

## 1) Makale Mobil Okunabilirlik Promptu

```text
"avukataysenuravci.com.tr sitesindeki [KONU ADI] makalesini, mobil cihazlarda (responsive) en yüksek okunabilirlik seviyesine getirmek için şu kurallara göre düzenle:

Kısa Paragraflar: Her paragrafı mobil ekranda en fazla 4-5 satır kaplayacak şekilde (yaklaşık 2-3 cümle) parçala.

H Etiketleri Ölçeklendirme: H1, H2 ve H3 başlıklarını kısa ve öz tut. Uzun başlıklar mobilde 4-5 satıra yayılıp ekranı kapatmasın.

Liste Odaklı Yapı: Teknik bilgileri ve süreçleri (Örn: Boşanma aşamaları, gerekli belgeler) mutlaka madde işaretleri (bullet points) ile sun.

Görsel Altı Metinler: Resim açıklamalarını ve tablo verilerini, dar ekranlarda taşma yapmayacak şekilde kısa tut.

Okunabilirlik Kontrolü: Cümleleri sadeleştir, karmaşık ve çok uzun birleşik cümlelerden kaçın."
```

## 2) Teknik Hata Tespiti ve CSS Duzeltme Promptu

```text
"Sitemin responsive tasarımında metinlerin alt alta binmesi ve yerleşim bozuklukları (layout shifts) yaşıyorum. Aşağıdaki kod bloğunu şu kriterlere göre optimize et:

Line-Height (Satır Aralığı): Mobil görünümde satır aralıklarını (line-height) 1.6rem yaparak metinlerin nefes almasını sağla.

Fluid Typography: Yazı boyutlarını (font-size) sabit px yerine, ekran genişliğine göre ölçeklenen rem veya vw birimlerine dönüştür.

Padding & Margin: Elemanlar arasındaki boşlukların (margin) mobilde çok daralıp metinleri sıkıştırmasını engelle; yan boşlukları (padding) dengeli ayarla.

Word-Wrap: Uzun hukuki terimlerin veya URL'lerin ekran dışına taşmaması için overflow-wrap: break-word; kuralını ekle.

Touch Targets: Buton ve linklerin (CTA) mobil kullanıcıların kolayca tıklayabileceği boyutta (en az 44x44px) ve aralıklı olmasını sağla.

Mevcut Kod (HTML/CSS): [BURAYA KODU YAPIŞTIR]"
```

## 3) Responsive Kontrol Listesi

- Yatay kaydirma var mi? (Horizontal scroll olmamali)
- CTA butonlari ve menu ogeleri birbirine cok yakin mi?
- Mobil font boyutu en az 16px mi?
- Uzun URL/terimler satir disina tasiyor mu?
- Tablo ve gorseller dar ekranda kaydirilabilir veya olcekli mi?

