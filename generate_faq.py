#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SSS sayfası için tüm soru-cevapları ve ilgili linkleri üretir."""

FAQ_DATA = [
    # CEZA HUKUKU
    ("Ceza Hukuku ve İfade Süreçleri", "ceza-hukuku", [
        ("Karakoldan ifadeye çağrıldım, gitmezsem ne olur?", "Gitmemek zorla getirtme (celp) ile sonuçlanabilir. CMK 147 uyarınca şüpheli/sanık çağrıya uymak zorundadır. <a href='faaliyet-alanlari/ceza-hukuku/agir-ceza.html'>Ceza hukuku</a> danışmanlığı için <a href='iletisim.html'>bize ulaşın</a>.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Şüpheli sıfatıyla ifade verirken avukat bulundurmak zorunlu mu?", "Zorunlu değil ancak CMK 150 uyarınca avukat hakkı vardır. Avukat eşliğinde ifade vermek hak kaybını önler. <a href='faaliyet-alanlari/ceza-hukuku/agir-ceza.html'>Gebze ceza avukatı</a> desteği alabilirsiniz.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Savcılıkta ifade verirken nelere dikkat etmeliyim?", "Susma hakkınızı kullanabilir, yalan söylememeli, avukat talep etmelisiniz. <a href='blog/agir-ceza-mahkemelerinde-savunma-stratejileri.html'>Savunma stratejileri</a> makalemizi okuyun.", "blog/agir-ceza-mahkemelerinde-savunma-stratejileri.html"),
        ("Susma hakkı hangi durumlarda kullanılmalı?", "Kendinizi suçlayıcı sorularda, belirsiz durumlarda veya avukat gelene kadar susma hakkınızı kullanabilirsiniz. CMK 147/5.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Adli kontrol şartıyla serbest bırakılmak ne anlama gelir?", "Tutuklama yerine imza, yurt dışına çıkma yasağı gibi şartlarla serbest bırakılma. <a href='faaliyet-alanlari/ceza-hukuku/infaz-hukuku.html'>İnfaz hukuku</a> sayfamız.", "faaliyet-alanlari/ceza-hukuku/infaz-hukuku.html"),
        ("Evimde arama yapıldı, hukuki haklarım nelerdir?", "Arama kararı, arama tutanağı ve el koyulan eşyaların listesini talep edebilirsiniz. Hukuka aykırı aramada itiraz hakkınız vardır.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Gözaltı süresi en fazla ne kadardır?", "Toplu suçlarda 4 gün, terör ve organize suçlarda 4 gün (uzatılabilir). CMK 91.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("İfademde yalan söylersem suç olur mu?", "Evet. TCK 272 yalan beyan suçu 6 aya kadar hapis cezası öngörür.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Avukatım olmadan verdiğim ifade geçersiz sayılır mı?", "Hayır, geçerli sayılır. Ancak avukat hakkı kullanılmadan alınan ifadeler bazı durumlarda delil değeri açısından tartışılabilir.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Denetimli serbestlik ihlal edilirse hapse girilir mi?", "Evet. Denetimli serbestlik şartlarına uymama halinde infaz hakimi kararıyla hapis cezası infaz edilir. <a href='blog/denetimli-serbestlik-sartlari-2026.html'>Detaylar</a>.", "blog/denetimli-serbestlik-sartlari-2026.html"),
    ]),
    # BİLİŞİM
    ("Bilişim ve Sosyal Medya Suçları", "bilisim", [
        ("Sosyal medyadan hakaret davası nasıl açılır?", "Cumhuriyet Başsavcılığına suç duyurusu veya sulh ceza hakimine şikayet. <a href='blog/sosyal-medya-hakaret-santaj-suclari.html'>Sosyal medya hakaret</a> makalemiz.", "blog/sosyal-medya-hakaret-santaj-suclari.html"),
        ("WhatsApp konuşmaları mahkemede delil sayılır mı?", "Evet, HMK 193 uyarınca dijital delil olarak kabul edilir. Ekran görüntüsü ve noter onayı güçlendirir.", "faaliyet-alanlari/bilisim-e-ticaret/kvkk.html"),
        ("Instagram hesabım çalındı, savcılığa nasıl şikayet ederim?", "Cumhuriyet Başsavcılığına TCK 243 (bilişim sistemine girme) suç duyurusu yapın. <a href='faaliyet-alanlari/ceza-hukuku/bilisim-suclari.html'>Bilişim suçları</a>.", "faaliyet-alanlari/ceza-hukuku/bilisim-suclari.html"),
        ("Twitter'da (X) bir gönderiyi beğenmek suç sayılır mı?", "İçeriğe göre değişir. Hakaret veya teşvik içeriyorsa sorumluluk doğabilir.", "blog/sosyal-medya-hakaret-santaj-suclari.html"),
        ("İnternet üzerinden dolandırıldım, paramı geri alabilir miyim?", "Suç duyurusu + tazminat davası. Banka ve platformlardan bilgi talep edilebilir. <a href='blog/internet-yoluyla-dolandiricilik-sucu.html'>İnternet dolandırıcılığı</a>.", "blog/internet-yoluyla-dolandiricilik-sucu.html"),
        ("Adıma sahte profil açıldı, ne yapmalıyım?", "Platforma şikayet + savcılığa TCK 136 (kişisel veri) ve 125 (hakaret) suç duyurusu.", "faaliyet-alanlari/ceza-hukuku/bilisim-suclari.html"),
        ("Ekran görüntüsü (screenshot) mahkemede kesin delil midir?", "Kesin değil; HMK 193'te dijital delil olarak değerlendirilir. Noter onayı veya hash değeri güçlendirir.", "faaliyet-alanlari/bilisim-e-ticaret/kvkk.html"),
        ("İzinsiz ses kaydı almak suç mudur?", "Evet. TCK 134 özel hayatın gizliliğini ihlal; bazı durumlarda meşru müdafaa delili kabul edilebilir.", "blog/ozel-hayatin-gizliligini-ihlal.html"),
        ("Kripto para dolandırıcılığı için nereye başvurulur?", "Cumhuriyet Başsavcılığı + Siber Suçlar Dairesi. <a href='blog/kripto-para-dolandiriciligi-ve-hukuki-yollar.html'>Kripto dolandırıcılığı</a> makalemiz.", "blog/kripto-para-dolandiriciligi-ve-hukuki-yollar.html"),
        ("Siber zorbalığa maruz kalanlar hangi hukuki yollara başvurmalı?", "Suç duyurusu (hakaret, tehdit) + manevi tazminat davası. <a href='blog/siber-zorbalik-ve-hukuki-boyutu.html'>Siber zorbalık</a>.", "blog/siber-zorbalik-ve-hukuki-boyutu.html"),
    ]),
    # İŞ HUKUKU
    ("İş Hukuku ve Tazminat", "is-hukuku", [
        ("Maaşım ödenmiyor, işi haklı nedenle bırakabilir miyim?", "Evet. İK 24/II uyarınca ücretin zamanında ödenmemesi haklı fesih sebebidir. Kıdem ve ihbar tazminatı alırsınız.", "faaliyet-alanlari/is-hukuku/kidem-tazminati.html"),
        ("2026 yılı kıdem tazminatı tavanı ne kadar?", "Bakanlar Kurulu kararıyla güncellenir. <a href='blog/gebze-kidem-tazminati-hesaplama-2026.html'>Kıdem tazminatı hesaplama</a> ve <a href='araclar.html'>hesaplama araçlarımız</a>.", "blog/gebze-kidem-tazminati-hesaplama-2026.html"),
        ("Mobbing nedeniyle istifa eden tazminat alabilir mi?", "Evet. Haklı fesih hakkı + manevi tazminat. <a href='faaliyet-alanlari/is-hukuku/mobbing.html'>Mobbing</a> sayfamız.", "faaliyet-alanlari/is-hukuku/mobbing.html"),
        ("İşe iade davası kaç gün içinde açılmalıdır?", "Arabuluculuk sonrası 1 ay içinde İş Mahkemesi'ne dava açılmalıdır. <a href='faaliyet-alanlari/is-hukuku/ise-iade.html'>İşe iade</a>.", "faaliyet-alanlari/is-hukuku/ise-iade.html"),
        ("Fazla mesai ücretleri nasıl hesaplanır?", "Haftalık 45 saati aşan çalışma x 1.5. <a href='blog/fazla-mesai-ucreti-ve-ispat-yuku.html'>Fazla mesai</a> ve <a href='araclar.html'>hesaplama araçları</a>.", "blog/fazla-mesai-ucreti-ve-ispat-yuku.html"),
        ("İş kazası sonrası maddi ve manevi tazminat davası nasıl açılır?", "İşveren ve SGK'ya karşı dava. <a href='faaliyet-alanlari/is-hukuku/is-kazasi.html'>İş kazası</a> sayfamız.", "faaliyet-alanlari/is-hukuku/is-kazasi.html"),
        ("Hamilelik nedeniyle işten çıkarılmak yasal mı?", "Hayır. İK 18/1 doğumdan önceki ve sonraki 1 yıl koruma sağlar. Tazminatsız fesih geçersizdir.", "faaliyet-alanlari/is-hukuku/ise-iade.html"),
        ("Yıllık izin ücreti hangi durumlarda nakit olarak alınır?", "İşten ayrılışta kullanılmayan izinler nakit ödenir. <a href='blog/yillik-izin-hakki-ve-kullanim-sartlari.html'>Yıllık izin</a>.", "blog/yillik-izin-hakki-ve-kullanim-sartlari.html"),
        ("Performans düşüklüğü gerekçesiyle tazminatsız kovulabilir miyim?", "Geçerli sebep ve usul gerekir. Keyfi fesih tazminat gerektirir. <a href='blog/ise-iade-davasi-acma-sartlari.html'>İşe iade şartları</a>.", "blog/ise-iade-davasi-acma-sartlari.html"),
        ("Arabuluculuk görüşmesinde avukat şart mı?", "Zorunlu değil ancak önerilir. Düşük teklifleri değerlendirmek için <a href='blog/ise-iade-arabuluculuk-mahkeme-sureci.html'>avukat danışmanlığı</a>.", "blog/ise-iade-arabuluculuk-mahkeme-sureci.html"),
    ]),
    # KİRA
    ("Kira ve Gayrimenkul Hukuku", "gayrimenkul", [
        ("Ev sahibi kirayı %25'ten fazla artırabilir mi?", "5 yıllık sözleşmelerde TÜFE oranında artış uygulanır. Anlaşmazlıkta kira tespit davası. <a href='faaliyet-alanlari/gayrimenkul/kira-tespit.html'>Kira tespit</a>.", "faaliyet-alanlari/gayrimenkul/kira-tespit.html"),
        ("Kirasını ödemeyen kiracı ne kadar sürede tahliye edilir?", "İhtarname + tahliye davası. Süre mahkeme yoğunluğuna göre 6-18 ay. <a href='faaliyet-alanlari/gayrimenkul/tahliye.html'>Tahliye</a>.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("İhtiyaç nedeniyle tahliye davası ne kadar sürer?", "Ortalama 12-24 ay. Acil durumlarda ihtiyati tahliye talep edilebilir.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("Kira sözleşmesi bitince otomatik olarak yenilenir mi?", "TBK 347: 5 yıllık süre dolunca taraflar anlaşamazsa kira tespit davası açılır.", "blog/kira-tespit-davasinda-5-yil-kurali.html"),
        ("Ev sahibi evi satarsa yeni malik kiracıyı çıkarabilir mi?", "Hayır. Satış kiracıyı etkilemez; sözleşme yeni malike devredilir.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("Depozito geri alınırken nelere dikkat edilmeli?", "Tahliye tutanağı, hasar tespiti. Anlaşmazlıkta tüketici hakem heyeti veya dava.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("İzale-i şuyu (ortaklığın giderilmesi) davası nedir?", "Paylı mülkiyetin satış yoluyla sonlandırılması. <a href='blog/ortakligin-giderilmesi-izale-i-suyu.html'>İzale-i şuyu</a>.", "blog/ortakligin-giderilmesi-izale-i-suyu.html"),
        ("Tapuda aile konutu şerhi ne işe yarar?", "Eşin rızası olmadan satış/ipotek engellenir. TMK 194.", "faaliyet-alanlari/aile-hukuku/mal-paylasimi.html"),
        ("Ecrimisil (haksız işgal tazminatı) davası nasıl açılır?", "Tahliye sonrası haksız işgal süresi için günlük tazminat. <a href='blog/ecrimisil-haksiz-isgal-tazminati-davasi.html'>Ecrimisil</a>.", "blog/ecrimisil-haksiz-isgal-tazminati-davasi.html"),
        ("Kaç yıllık kiracı sebepsiz yere tahliye edilebilir?", "Sözleşme süresi dolana kadar tahliye edilemez. Süre sonunda ihtiyaç veya anlaşmazlık gerekir.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
    ]),
    # AİLE
    ("Aile ve Boşanma Hukuku", "aile-hukuku", [
        ("Anlaşmalı boşanma protokolü nasıl hazırlanır?", "Velayet, nafaka, mal paylaşımı üzerinde anlaşma. <a href='faaliyet-alanlari/aile-hukuku/anlasmali-bosanma.html'>Anlaşmalı boşanma</a>.", "faaliyet-alanlari/aile-hukuku/anlasmali-bosanma.html"),
        ("Aldatılan eş ne kadar manevi tazminat alabilir?", "Yargıtay 50.000-200.000 TL aralığında. <a href='blog/bosanmada-maddi-ve-manevi-tazminat.html'>Boşanmada tazminat</a>.", "blog/bosanmada-maddi-ve-manevi-tazminat.html"),
        ("Boşanmada çocukların velayeti kime verilir?", "Çocuğun üstün yararı. <a href='faaliyet-alanlari/aile-hukuku/velayet.html'>Velayet</a> sayfamız.", "faaliyet-alanlari/aile-hukuku/velayet.html"),
        ("Nafaka ödemeyen eşe hapis cezası verilir mi?", "Evet. Nafaka borcu nedeniyle icra cezası (hapishane) uygulanabilir.", "blog/nafaka-artirim-davasi-nasil-acilir.html"),
        ("Evlilik öncesi alınan mallar boşanmada paylaşılır mı?", "Kişisel mal sayılır; paylaşılmaz. <a href='faaliyet-alanlari/aile-hukuku/mal-paylasimi.html'>Mal paylaşımı</a>.", "faaliyet-alanlari/aile-hukuku/mal-paylasimi.html"),
        ("Boşanma davası sürerken başka biriyle görüşmek suç mu?", "Sadakat ihlali; boşanma nedenidir. Kusur oranını artırır.", "faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html"),
        ("Çocuğumu görmemi engelleyen eski eşime karşı ne yapabilirim?", "Kişisel ilişki (görüşme) ihlali için icra ve ceza yolu. <a href='blog/gecici-velayet-ve-kisisel-iliski-tesisi.html'>Kişisel ilişki</a>.", "blog/gecici-velayet-ve-kisisel-iliski-tesisi.html"),
        ("Şiddet gören kadınlar uzaklaştırma kararı nasıl alır?", "Aile Mahkemesi'ne başvuru veya 6284 sayılı Kanun kapsamında koruma.", "faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html"),
        ("Altınlar (ziynet eşyası) boşanmada kadının mıdır?", "Ziynet eşyası alacağı davası açılabilir. Hediye/ortaklık durumuna göre değişir. <a href='blog/cekismeli-bosanma-ziynet-esyasi-alacak-davasi.html'>Ziynet eşyası</a>.", "blog/cekismeli-bosanma-ziynet-esyasi-alacak-davasi.html"),
        ("Babalık davası (soybağı) nasıl açılır?", "TMK 301-305. DNA testi ile soybağı tespit veya red. <a href='blog/babalik-davasi-ve-soybaginin-reddi.html'>Babalık davası</a>.", "blog/babalik-davasi-ve-soybaginin-reddi.html"),
    ]),
    # İCRA
    ("İcra ve Borçlar Hukuku", "icra-iflas", [
        ("Maaş haczi en fazla ne kadar olabilir?", "Asgari ücretin 1/3'ü haczedilemez. <a href='blog/maas-haczi-orani-ve-hesaplamasi.html'>Maaş haczi</a> ve <a href='araclar.html'>hesaplama</a>.", "blog/maas-haczi-orani-ve-hesaplamasi.html"),
        ("Eve haciz gelmesi durumunda hangi eşyalar alınamaz?", "İİK 82: Zorunlu ev eşyaları, mesleki araçlar, din kitapları haczedilemez.", "faaliyet-alanlari/icra-iflas/cek-senet.html"),
        ("İmzalamadığım bir senet için icra takibi başlatılırsa ne yapmalıyım?", "7 gün içinde itiraz. İtirazın iptali davası. <a href='blog/icra-takibine-itiraz-ve-itirazin-iptali.html'>İcra itiraz</a>.", "blog/icra-takibine-itiraz-ve-itirazin-iptali.html"),
        ("Kredi borcu nedeniyle banka hesabına bloke konulur mu?", "Evet. İhtiyati haciz veya bloke. <a href='blog/e-haciz-ve-banka-blokesi-kaldirma.html'>Bloke kaldırma</a>.", "blog/e-haciz-ve-banka-blokesi-kaldirma.html"),
        ("İcra takibine itiraz süresi kaç gündür?", "7 gün. Tebligattan itibaren. <a href='faaliyet-alanlari/icra-iflas/menfi-tespit.html'>Menfi tespit</a>.", "faaliyet-alanlari/icra-iflas/menfi-tespit.html"),
        ("Borçtan dolayı hapis cezası var mı?", "Hayır. Ancak nafaka ve bazı özel borçlarda icra cezası (hapishane) uygulanır.", "faaliyet-alanlari/icra-iflas/cek-senet.html"),
        ("Kefil olduğum borçtan nasıl kurtulabilirim?", "Asıl borçluya rücu, zamanaşımı, iflas. <a href='faaliyet-alanlari/icra-iflas/iflas-erteleme.html'>İflas erteleme</a>.", "faaliyet-alanlari/icra-iflas/iflas-erteleme.html"),
        ("Zamanaşımına uğramış borç için ödeme yapılır mı?", "Yapılabilir; ödendikten sonra geri alınamaz (BK 147).", "faaliyet-alanlari/icra-iflas/cek-senet.html"),
        ("Karşılıksız çek keşide etmenin cezası nedir?", "2-5 yıl hapis + tazminat. <a href='blog/karsiliksiz-cek-keside-etme-sucu.html'>Karşılıksız çek</a>.", "blog/karsiliksiz-cek-keside-etme-sucu.html"),
        ("Mal beyanında bulunmamanın cezası var mı?", "Evet. 1 yıla kadar hapis (TCK 210).", "faaliyet-alanlari/icra-iflas/cek-senet.html"),
    ]),
]

# Diğer ve Spesifik sorular - ek kategori
FAQ_DATA_EXTRA = [
    ("Diğer Kritik Sorular", "diger", [
        ("Trafik kazası sonrası sigortadan tazminat nasıl alınır?", "Kusur tespiti, sigorta şirketine başvuru. Red halinde dava. <a href='blog/trafik-kazasi-sonrasi-taksirle-yaralama.html'>Trafik kazası</a>.", "blog/trafik-kazasi-sonrasi-taksirle-yaralama.html"),
        ("Doktor hatası (malpraktis) davası nasıl açılır?", "Sulh hukuk veya tüketici mahkemesi. Bilirkişi raporu gerekir.", "makaleler.html"),
        ("İsim ve soyisim değişikliği davası nasıl açılır?", "Nüfus Müdürlüğü veya mahkeme. <a href='blog/soyadi-degistirme-davasi-sartlari.html'>Soyadı değişikliği</a>.", "blog/soyadi-degistirme-davasi-sartlari.html"),
        ("Vergi cezasına itiraz süreci nasıl işler?", "30 gün içinde vergi mahkemesine dava.", "makaleler.html"),
        ("Kamu görevinden haksız ihraç durumunda dava süresi nedir?", "İdari yargıda 60 gün. İşe iade davası 1 ay.", "faaliyet-alanlari/is-hukuku/ise-iade.html"),
        ("Mirasçılık belgesi (veraset ilamı) nereden alınır?", "Noter veya Sulh Hukuk Mahkemesi.", "makaleler.html"),
        ("Mirası reddetmek (reddi miras) ne kadar sürede yapılmalı?", "3 ay. Ölümü öğrenmeden itibaren.", "makaleler.html"),
        ("Sağlık raporuyla vasi tayini nasıl yapılır?", "Sulh Hukuk Mahkemesi. Akıl hastalığı veya akıl zayıflığı.", "makaleler.html"),
        ("Tüketici Hakem Heyeti'ne başvuru sınırı 2026'da ne kadar?", "Bakanlar Kurulu kararıyla güncellenir. Genellikle 30.000 TL civarı.", "makaleler.html"),
        ("Ayıplı mal iadesinde avukat yardımı gerekli mi?", "Zorunlu değil; karmaşık durumlarda önerilir.", "blog/yaniltici-reklam-ve-tuketici-haklari.html"),
        ("Apartman gürültüsü nedeniyle dava açılabilir mi?", "Evet. Komşuluk hukuku, KMK. Manevi tazminat.", "makaleler.html"),
        ("Köpek ısırılması durumunda sahibine dava açılır mı?", "Evet. BK 56 kusursuz sorumluluk. Maddi ve manevi tazminat.", "makaleler.html"),
        ("Estetik ameliyat sonrası mağduriyetlerde tazminat hakkı var mı?", "Evet. Malpraktis, tüketici hukuku.", "makaleler.html"),
        ("Özel okul ücret iadesi davası nasıl açılır?", "Tüketici mahkemesi. Sözleşme ihlali.", "makaleler.html"),
        ("Sosyal yardım kesilirse hukuki olarak ne yapılabilir?", "İdari yargıda itiraz. Danıştay.", "makaleler.html"),
        ("Kredi kartı aidatı geri alınabilir mi?", "Kullanım yoksa iade davası açılabilir.", "makaleler.html"),
        ("Sigorta şirketi ödemeyi reddederse ne yapmalıyım?", "Tazminat davası. Zorunlu trafik sigortası için doğrudan dava.", "blog/trafik-kazasi-sonrasi-taksirle-yaralama.html"),
        ("Adli sicil kaydı (sabıka) nasıl sildirilir?", "Cumhuriyet Başsavcılığına başvuru. <a href='blog/adli-sicil-kaydinin-sabika-silinmesi.html'>Sabıka silme</a>.", "blog/adli-sicil-kaydinin-sabika-silinmesi.html"),
        ("Pasaport tahdidi nasıl kaldırılır?", "Ceza infaz edildikten sonra savcılığa başvuru.", "faaliyet-alanlari/ceza-hukuku/infaz-hukuku.html"),
        ("Belediye cezalarına itiraz nasıl yapılır?", "İdari yargı. 30 gün içinde.", "makaleler.html"),
    ]),
    ("Spesifik Savunmalar", "savunma", [
        ("Tehdit suçlamasıyla karşı karşıyayım, ne yapmalıyım?", "TCK 106. Savunma, delil toplama. <a href='faaliyet-alanlari/ceza-hukuku/agir-ceza.html'>Ceza avukatı</a>.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("İftiraya uğradım, karşı dava nasıl açarım?", "TCK 267. İftira suç duyurusu + tazminat. <a href='blog/iftira-ve-suc-uydurma-suclari.html'>İftira</a>.", "blog/iftira-ve-suc-uydurma-suclari.html"),
        ("Hırsızlık suçuyla itham ediliyorum, delil nasıl sunarım?", "Zan altındaki delilleri çürütme. <a href='faaliyet-alanlari/ceza-hukuku/agir-ceza.html'>Savunma stratejisi</a>.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Uyuşturucu madde bulundurmaktan dava açıldı, savunma nasıl yapılır?", "Delil geçerliliği, miktar, kullanım amacı. <a href='faaliyet-alanlari/ceza-hukuku/uyusturucu-suclari.html'>Uyuşturucu suçları</a>.", "faaliyet-alanlari/ceza-hukuku/uyusturucu-suclari.html"),
        ("Sahte belge düzenlemekle suçlanıyorum, uzman görüşü gerekir mi?", "Evet. Grafolog veya belge inceleme uzmanı.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Cinsel taciz suçlamasında ispat yükü kime aittir?", "Savcılığa aittir. Sanık aleyhine karine yok. <a href='blog/cinsel-taciz-sucu-ve-sikayet-suresi.html'>Cinsel taciz</a>.", "blog/cinsel-taciz-sucu-ve-sikayet-suresi.html"),
        ("Görevi kötüye kullanma suçlamasıyla açılan davada avukatın rolü?", "Delil toplama, kastın ispatı, yetki ihlali savunması. <a href='blog/guveni-kotuye-kullanma-sucu.html'>Güveni kötüye kullanma</a>.", "blog/guveni-kotuye-kullanma-sucu.html"),
        ("Yaralama (darp) davasında meşru müdafaa nasıl kanıtlanır?", "TCK 25. Saldırı, orantılılık. <a href='blog/mesru-mudafaa-ve-sinirin-asilmasi.html'>Meşru müdafaa</a>.", "blog/mesru-mudafaa-ve-sinirin-asilmasi.html"),
        ("Trafik güvenliğini tehlikeye atmaktan ceza alır mıyım?", "TCK 179. 6 aydan 2 yıla kadar hapis.", "blog/trafik-kazasi-sonrasi-taksirle-yaralama.html"),
        ("Hakaret davasında tahrik indirimi nasıl uygulanır?", "TCK 52. Provokasyon, orantılı tepki.", "blog/sosyal-medya-hakaret-santaj-suclari.html"),
        ("Kaçakçılık suçlamasıyla mallarıma el konuldu, ne yapmalıyım?", "İade davası, müsadere itirazı. <a href='faaliyet-alanlari/ceza-hukuku/agir-ceza.html'>Ceza avukatı</a>.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Vergi kaçakçılığı suçlamasında savunma stratejisi?", "Beyan, belge, zamanaşımı.", "makaleler.html"),
        ("Silahla tehdit davasında tutuklama kararı çıkar mı?", "Olası. TCK 106/2. Ağırlaştırıcı nedenler.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Dolandırıcılık davasında zararın karşılanması cezayı düşürür mü?", "TCK 62 etkin pişmanlık. Cezada indirim.", "blog/dolandiricilik-sucunda-hile-unsuru.html"),
        ("Görevi yaptırmamak için direnme suçu nedir?", "TCK 265. Kamu görevlisine karşı direnme.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Yanlışlıkla birinin malına zarar verdim, suç sayılır mı?", "TCK 151 taksirle mala zarar. Kusur oranı.", "makaleler.html"),
        ("Zimmet suçlamasıyla açılan davalarda avukat yardımı?", "Kritik. Delil, kast, yetki. <a href='faaliyet-alanlari/ceza-hukuku/agir-ceza.html'>Gebze ceza avukatı</a>.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Yardım ve yataklık suçlamasından nasıl aklanırım?", "Bilme, kasıt, yardımın niteliği.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Konut dokunulmazlığını ihlal davası ne kadar ceza alır?", "TCK 116. 1-3 yıl hapis.", "blog/konut-dokunulmazliginin-ihlali-sucu.html"),
        ("Adli sicilim temizse cezam ertelenir mi?", "TCK 51. 2 yıl ve altı hapis, belirli şartlarla ertelenebilir. <a href='blog/hukmun-aciklanmasinin-geri-birakilmasi-hagb.html'>HAGB</a>.", "blog/hukmun-aciklanmasinin-geri-birakilmasi-hagb.html"),
    ]),
]

# "Başım Belada" ve diğer pratik sorular
FAQ_DATA_NEW = [
    ("Başım Belada - Ceza & Karakol", "basim-belada", [
        ("Polis çevirmesinde alkol metreyi üflemezsem paket olur muyum?", "Üflemezsen idari para cezası ve ehliyet iptali. Zorla üfletemezler; reddiniz tutanakta belirtilir. <a href='faaliyet-alanlari/ceza-hukuku/agir-ceza.html'>Ceza avukatı</a>.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Karakolda ben yapmadım dedim ama zorla imzalattılar, ne yapacağım?", "İmza altına \"zorla imzalattılar\" yazın veya avukat talep edin. İtiraz ve savunma hakkınız var. <a href='iletisim.html'>Avukat danışmanlığı</a>.", "iletisim.html"),
        ("Kavga ettik, karşı taraf şikayetçi olmuş; hapis yatar mıyım?", "Yaralama derecesine göre. Basit yaralama şikayete bağlı; ağır yaralama kamu davası. <a href='blog/mesru-mudafaa-ve-sinirin-asilmasi.html'>Meşru müdafaa</a>.", "blog/mesru-mudafaa-ve-sinirin-asilmasi.html"),
        ("Üzerimde emanetle (silah/bıçak) yakalandım, adli kontrolle yırtar mıyım?", "TCK 613/2 taşıma ruhsatı olmadan silah. Adli kontrol veya tutuklama mahkeme kararına bağlı.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Ev arkadaşım uyuşturucu satıyormuş, ben de yanar mıyım?", "Bilme ve iştirak ispatı gerekir. Evde bulunma tek başına suç sayılmaz. <a href='faaliyet-alanlari/ceza-hukuku/uyusturucu-suclari.html'>Uyuşturucu suçları</a>.", "faaliyet-alanlari/ceza-hukuku/uyusturucu-suclari.html"),
        ("Bekçiler üstümü arayabilir mi, itiraz etsem suç mu?", "Şüphe halinde arama yapılabilir. Haksız aramada itiraz hakkınız var; itiraz suç değildir.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Denetimli varken kavga ettim, dosyam patlar mı?", "Denetimli serbestlik ihlali; infaz hakimi kararıyla hapis infazı başlayabilir. <a href='blog/denetimli-serbestlik-sartlari-2026.html'>Denetimli serbestlik</a>.", "blog/denetimli-serbestlik-sartlari-2026.html"),
        ("Kumar baskınında yakalandım, sicilime işler mi?", "Evet. Kumar suçu ceza ve adli sicile işlenir.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Polise mukavemetten dava açılmış, memuriyetim yanar mı?", "TCK 265. Mahkumiyet halinde memuriyet sona erebilir. Savunma kritik.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Mahkemeye gitmezsem polis kapıma dayanır mı?", "Celbe uymazsan zorla getirtme (yakalama) uygulanabilir. CMK 147.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
    ]),
    ("Hanımla/Beyle Papaz Olduk - Aile & Boşanma", "hanimla-papaz", [
        ("Karım/Kocam evi terk etti, terk davası açıp tazminat çakabilir miyim?", "TMK 166/2 terk boşanma sebebidir. Kusur oranına göre tazminat. <a href='faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html'>Çekişmeli boşanma</a>.", "faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html"),
        ("Gizlice telefonunu karıştırdım, yakaladığım mesajlar mahkemede geçer mi?", "Hukuka aykırı elde edilen deliller reddedilebilir. TCK 134 özel hayat ihlali.", "blog/ozel-hayatin-gizliligini-ihlal.html"),
        ("Düğün takıları kimin cebinde kalacak?", "Ziynet eşyası alacağı davası. Hediye/ortaklık durumuna göre. <a href='blog/cekismeli-bosanma-ziynet-esyasi-alacak-davasi.html'>Ziynet eşyası</a>.", "blog/cekismeli-bosanma-ziynet-esyasi-alacak-davasi.html"),
        ("Nafaka ödemezsem direkt hapse mi atıyorlar?", "İcra cezası (hapishane) uygulanabilir. Önce ihtarlar ve icra takibi.", "blog/nafaka-artirim-davasi-nasil-acilir.html"),
        ("Boşanma davası açtım ama hâlâ aynı evdeyiz, sıkıntı çıkar mı?", "Geçici önlemler alınabilir. Aynı evde yaşamak davayı etkilemez.", "faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html"),
        ("Anlaşmalı dedik ama son anda vazgeçti, şimdi ne olacak?", "Çekişmeli boşanmaya döner. Yeni protokol veya dava devam eder. <a href='faaliyet-alanlari/aile-hukuku/anlasmali-bosanma.html'>Anlaşmalı boşanma</a>.", "faaliyet-alanlari/aile-hukuku/anlasmali-bosanma.html"),
        ("Velayeti almak için neyi ispatlamam lazım?", "Çocuğun üstün yararı. Bakım, gelir, ortam. <a href='faaliyet-alanlari/aile-hukuku/velayet.html'>Velayet</a>.", "faaliyet-alanlari/aile-hukuku/velayet.html"),
        ("Aldatıldım, öteki kadına/adama da dava açabilir miyim?", "Evet. Manevi tazminat ve kusur oranı. <a href='blog/bosanmada-maddi-ve-manevi-tazminat.html'>Tazminat</a>.", "blog/bosanmada-maddi-ve-manevi-tazminat.html"),
        ("Boşanmadan önce malları başkasının üstüne yapsam anlaşılır mı?", "Mal kaçırma; TMK 197. Mahkeme bilirkişi ve tapu incelemesi yapar.", "faaliyet-alanlari/aile-hukuku/mal-paylasimi.html"),
        ("Şiddet gördüm, uzaklaştırma kararı kaç günde çıkar?", "6284 sayılı Kanun: Acil durumda 24 saat, normalde birkaç gün.", "faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html"),
    ]),
    ("Patronla Takıştık - İş Hukuku & Emek", "patronla-takistik", [
        ("İstifayı bastım, tazminatın üstüne soğuk su mu içeyim?", "Kendi isteğinizle istifa kıdem/ihbar tazminatı almaz. Haklı fesih için geçerli sebep gerekir.", "faaliyet-alanlari/is-hukuku/kidem-tazminati.html"),
        ("Patron maaşın yarısını elden vercem diyor, kabul etsem başım ağrır mı?", "Kayıt dışı ödeme SGK ve vergi sorunu. İspat zorlaşır. Riskli.", "faaliyet-alanlari/is-hukuku/kidem-tazminati.html"),
        ("Mesaiye kalmıyorum diye kapının önüne koyabilirler mi?", "Hayır. Disiplin veya fesih için geçerli sebep gerekir. Keyfi fesih tazminat.", "faaliyet-alanlari/is-hukuku/ise-iade.html"),
        ("Sigortamı eksik yatırmışlar, geriye dönük parayı alır mıyım?", "Evet. SGK borç tespit davası. Eksik prim alacağı.", "faaliyet-alanlari/is-hukuku/is-kazasi.html"),
        ("10 senelik emeğim var, tazminatımı kuruşu kuruşuna nasıl alırım?", "Kıdem + ihbar + fazla mesai. <a href='blog/gebze-kidem-tazminati-hesaplama-2026.html'>Hesaplama</a> ve <a href='araclar.html'>araçlar</a>.", "blog/gebze-kidem-tazminati-hesaplama-2026.html"),
        ("Mobbing yapıyorlar, her gün ağlayarak işe gidiyorum; dava açsam kazanır mıyım?", "Delil toplama kritik. Haklı fesih + manevi tazminat. <a href='faaliyet-alanlari/is-hukuku/mobbing.html'>Mobbing</a>.", "faaliyet-alanlari/is-hukuku/mobbing.html"),
        ("İş kazası geçirdim, şirket hastanede merdivenden düştüm diyor, ne yapayım?", "İşyerinde mi dışarıda mı ispatı. Tanık, kamera, tutanak. <a href='faaliyet-alanlari/is-hukuku/is-kazasi.html'>İş kazası</a>.", "faaliyet-alanlari/is-hukuku/is-kazasi.html"),
        ("Yıllık iznimi kullandırmıyorlar, paraya çevirip alabilir miyim?", "İşten ayrılışta kullanılmayan izinler nakit ödenir. <a href='blog/yillik-izin-hakki-ve-kullanim-sartlari.html'>Yıllık izin</a>.", "blog/yillik-izin-hakki-ve-kullanim-sartlari.html"),
        ("Arabulucuda patronun teklifini beğenmedim, masadan kalksam ne olur?", "Dava açma hakkınız devam eder. 1 ay içinde İş Mahkemesi. <a href='blog/ise-iade-arabuluculuk-mahkeme-sureci.html'>Arabuluculuk</a>.", "blog/ise-iade-arabuluculuk-mahkeme-sureci.html"),
        ("İş yerinde kavga ettim, tazminatsız kovulur muyum?", "Ciddiyetine göre. Ağır disiplin suçu geçerli fesih sebebi olabilir.", "faaliyet-alanlari/is-hukuku/ise-iade.html"),
    ]),
    ("Ev Sahibi Çık Diyor - Kira & Mülk", "ev-sahibi-cik-diyor", [
        ("Ev sahibi Almanya'dan oğlum gelecek diyor, yalan olduğunu biliyorum; ne yapayım?", "İhtiyaç tahliyesinde sahtelik tespit davası. Bilirkişi, tanık.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("Kirayı %100 artırdı, ödemezsem kapıya kilit vurabilir mi?", "Hayır. Zorla tahliye suç. Kira tespit davası açın. <a href='faaliyet-alanlari/gayrimenkul/kira-tespit.html'>Kira tespit</a>.", "faaliyet-alanlari/gayrimenkul/kira-tespit.html"),
        ("Kontratım yok, ev sahibi beni pat diye sokağa atabilir mi?", "Hayır. Sözlü kira da geçerli. Tahliye için dava gerekir.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("Evi satıyorum bahanesiyle kiracı çıkarılır mı?", "Satış kiracıyı etkilemez. Sözleşme yeni malike devredilir.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("Alt kattaki komşu her gece gürültü yapıyor, nereye şikayet edeyim?", "Belediye, polis, CMK 134 özel hayat ihlali, manevi tazminat.", "makaleler.html"),
        ("Depozitomu vermiyorlar, boya badana bahane ediyorlar; ne yapmalıyım?", "Tahliye tutanağı, hasar tespiti. Tüketici veya icra.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("Ortak miras kalan evi kardeşlerim benden habersiz satabilir mi?", "Paylı mülkiyette tüm ortakların rızası gerekir. İzale-i şuyu. <a href='blog/ortakligin-giderilmesi-izale-i-suyu.html'>İzale-i şuyu</a>.", "blog/ortakligin-giderilmesi-izale-i-suyu.html"),
        ("Evin tavanı akıyor, tamir masrafını kiradan düşebilir miyim?", "TBK 315. Onarım borcu malike ait. Kiradan düşülebilir; tutanak şart.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("10 yıldır aynı evdeyim, ev sahibi kira çok düşük kaldı diye dava açabilir mi?", "5 yıl dolunca kira tespit davası. Emsal rayiç belirlenir.", "blog/kira-tespit-davasinda-5-yil-kurali.html"),
        ("Tahliye taahhütnamesini boşken imzaladım, başım yanar mı?", "Taahhüt geçerli olabilir. İrade sakatlığı ispatı zor. <a href='blog/kira-tahliye-davalarinda-arabuluculuk.html'>Tahliye</a>.", "blog/kira-tahliye-davalarinda-arabuluculuk.html"),
    ]),
    ("İnternette Başım Belaya Girdi - Bilişim & Sosyal Medya", "internette-basim-belada", [
        ("Adıma sahte hesap açıp millete yazmışlar, nasıl temizlerim?", "Platforma şikayet + savcılığa TCK 136, 125 suç duyurusu. <a href='faaliyet-alanlari/ceza-hukuku/bilisim-suclari.html'>Bilişim suçları</a>.", "faaliyet-alanlari/ceza-hukuku/bilisim-suclari.html"),
        ("WhatsApp grubunda küfürleşme oldu, mahkemeye versem sonuç çıkar mı?", "Hakaret şikayete bağlı. Suç duyurusu + tazminat. <a href='blog/sosyal-medya-hakaret-santaj-suclari.html'>Sosyal medya hakaret</a>.", "blog/sosyal-medya-hakaret-santaj-suclari.html"),
        ("Sahibinden'de dolandırıldım, IBAN'a para gönderdim; geri gelir mi?", "Suç duyurusu + tazminat. Banka bilgisi talep. <a href='blog/internet-yoluyla-dolandiricilik-sucu.html'>Dolandırıcılık</a>.", "blog/internet-yoluyla-dolandiricilik-sucu.html"),
        ("Eski sevgilim fotoğraflarımla tehdit ediyor (şantaj), ne yapmalıyım?", "TCK 106 şantaj. Suç duyurusu. İçerik yayınlamadan önce savcılık.", "blog/sosyal-medya-hakaret-santaj-suclari.html"),
        ("Bir siteden alışveriş yaptım ürün gelmedi, muhatap bulamıyorum; ne yapayım?", "Tüketici hakem heyeti, tüketici mahkemesi. Şirket bilgisi TİM.", "makaleler.html"),
        ("Şirket iftira atıyor diye yorum yazdım, tazminat davası açarlar mı?", "Hakaret/iftira sınırını aşarsanız sorumluluk doğar. İspat önemli.", "blog/sosyal-medya-hakaret-santaj-suclari.html"),
        ("Kripto borsası battı, paralar çöp mü oldu?", "İflas/konkordato. Alacaklı sıfatıyla başvuru. <a href='blog/kripto-para-dolandiriciligi-ve-hukuki-yollar.html'>Kripto dolandırıcılığı</a>.", "blog/kripto-para-dolandiriciligi-ve-hukuki-yollar.html"),
        ("İzinsiz resmimi paylaşmışlar, telif veya tazminat alabilir miyim?", "TCK 134 özel hayat ihlali. Manevi tazminat. KVKK şikayet.", "blog/ozel-hayatin-gizliligini-ihlal.html"),
        ("Bahis sitesinden ceza geldi, ödemezsem hapse girer miyim?", "İdari para cezası. Ödenmezse icra, haciz. Hapis yok.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Telefonum hacklendi, verilerim çalındı; suç duyurusu nasıl yapılır?", "Cumhuriyet Başsavcılığına TCK 243, 136. Siber Suçlar Dairesi.", "faaliyet-alanlari/ceza-hukuku/bilisim-suclari.html"),
    ]),
    ("Kaza Yaptım, Borcum Var - Trafik & İcra", "kaza-borcum", [
        ("Alkollü kaza yaptım, sigorta parayı benden alır mı?", "Evet. Rücu hakkı. Sigorta öder, sonra sizden talep eder.", "blog/trafik-kazasi-sonrasi-taksirle-yaralama.html"),
        ("Plakaya ceza gelmiş, haberim yoktu; itiraz etsem silinir mi?", "Tebligat usulüne uygun değilse itiraz. 15 gün süre.", "makaleler.html"),
        ("Maaşıma haciz geldi, eve gelip eşyaları götürürler mi?", "İİK 82'deki istisnalar haczedilemez. Diğerleri götürülebilir.", "blog/maas-haczi-orani-ve-hesaplamasi.html"),
        ("Borçtan dolayı banka hesabım bloke oldu, nasıl açtırırım?", "Borç ödenince veya itiraz kabul edilince. <a href='blog/e-haciz-ve-banka-blokesi-kaldirma.html'>Bloke kaldırma</a>.", "blog/e-haciz-ve-banka-blokesi-kaldirma.html"),
        ("Arkadaşıma kefil oldum, şimdi bütün borç bana kaldı; kurtuluş yok mu?", "Asıl borçluya rücu. İflas, zamanaşımı. <a href='faaliyet-alanlari/icra-iflas/iflas-erteleme.html'>İflas erteleme</a>.", "faaliyet-alanlari/icra-iflas/iflas-erteleme.html"),
        ("Senet imzaladım ama malı teslim almadım, icrayı nasıl durdururum?", "7 gün itiraz. İtirazın iptali davası. <a href='blog/icra-takibine-itiraz-ve-itirazin-iptali.html'>İcra itiraz</a>.", "blog/icra-takibine-itiraz-ve-itirazin-iptali.html"),
        ("Hatalı park yüzünden arabam çekildi, hasar var; kim ödeyecek?", "Çekim sırasında hasar belediyenin/çekici firmasının sorumluluğu.", "makaleler.html"),
        ("Yayaya çarptım ama o suçluydu, hapse girer miyim?", "Kusur oranı. Taksirle yaralama. TCK 89. <a href='blog/trafik-kazasi-sonrasi-taksirle-yaralama.html'>Trafik kazası</a>.", "blog/trafik-kazasi-sonrasi-taksirle-yaralama.html"),
        ("E-devlet'te görünmeyen borç yüzünden icralık olur muyum?", "Tebligat yapılmışsa icra devam eder. İtiraz süresi 7 gün.", "faaliyet-alanlari/icra-iflas/menfi-tespit.html"),
        ("Kredi kartı borcunu yapılandırdım ama yine ödeyemiyorum, ne olacak?", "Yeni yapılandırma, konkordato, iflas. Bankayla görüşme.", "faaliyet-alanlari/icra-iflas/iflas-erteleme.html"),
    ]),
    ("Şöyle Bir Durum Var - Karışık Mevzular", "karisik-mevzular", [
        ("Komşunun köpeği ısırdı, sahibi kendi kaşındı diyor; dava açabilir miyim?", "Evet. BK 56 kusursuz sorumluluk. Maddi ve manevi tazminat.", "makaleler.html"),
        ("Estetik ameliyatım kötü geçti, doktoru mahkemeye versem paramı alır mıyım?", "Malpraktis. Tazminat davası. Bilirkişi raporu.", "makaleler.html"),
        ("İsmimi sevmiyorum, değiştirmek için ne kadar para lazım?", "Mahkeme harçları. <a href='blog/soyadi-degistirme-davasi-sartlari.html'>Soyadı değişikliği</a> makalemiz.", "blog/soyadi-degistirme-davasi-sartlari.html"),
        ("Miras payımı amcamlar yemiş, 20 sene sonra geri alabilir miyim?", "Zamanaşımı 10-20 yıl. Miras davası. Duruma göre.", "makaleler.html"),
        ("Tapuda metrekare düşük yazılmış, müteahhidi dava edebilir miyim?", "Evet. Ayıplı iş, tazminat. Tapu düzeltme davası.", "faaliyet-alanlari/gayrimenkul/tapu-iptal.html"),
        ("Marketten aldığım ürün bozuk çıktı, zehirlendim; tazminat davası açılır mı?", "Evet. Tüketici hukuku, BK. <a href='blog/yaniltici-reklam-ve-tuketici-haklari.html'>Tüketici hakları</a>.", "blog/yaniltici-reklam-ve-tuketici-haklari.html"),
        ("Sabıkam var, temiz kağıdı almamın bir yolu yok mu?", "Cumhuriyet Başsavcılığına başvuru. <a href='blog/adli-sicil-kaydinin-sabika-silinmesi.html'>Sabıka silme</a>.", "blog/adli-sicil-kaydinin-sabika-silinmesi.html"),
        ("Yanlışlıkla birinin hesabına para gönderdim, adam vermiyorum diyor; ne yapayım?", "Sebepsiz zenginleşme davası. BK 77.", "makaleler.html"),
        ("Belediye ağacı budamamış, üstüme düştü; zararı kim öder?", "Kusur sorumluluğu. Belediyeye tazminat davası.", "makaleler.html"),
        ("Yurt dışına çıkış yasağım olup olmadığını nasıl anlarım?", "Pasaport birimi, e-devlet, savcılık. İnfaz dairesi.", "faaliyet-alanlari/ceza-hukuku/infaz-hukuku.html"),
    ]),
    ("Avukat Bey Şöyle Suçlandım - Savunma Soruları", "avukat-bey-suclandim", [
        ("Görevi kötüye kullanma dediler, memuriyetim biter mi?", "Mahkumiyet halinde memuriyet sona erebilir. Savunma kritik. <a href='blog/guveni-kotuye-kullanma-sucu.html'>Güveni kötüye kullanma</a>.", "blog/guveni-kotuye-kullanma-sucu.html"),
        ("Tehdit etmedim sadece görüşeceğiz dedim, suç sayılır mı?", "Bağlam önemli. TCK 106 tehdit. Niyet ve ifade bütünü.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Hırsızlıkla suçlanıyorum ama o gün başka şehirdeydim, nasıl kanıtlarım?", "Alibi: otel, bilet, tanık, kredi kartı hareketi.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("İftiraya uğradım, adamı rezil etsem ben mi suçlu olurum?", "Hakaret, iftira karşılığı. Ölçülü tepki. TCK 125, 267.", "blog/iftira-ve-suc-uydurma-suclari.html"),
        ("Cinsel taciz diyorlar ama sadece selam verdim, ne yapmalıyım?", "İspat yükü savcılıkta. Savunma, tanık. <a href='blog/cinsel-taciz-sucu-ve-sikayet-suresi.html'>Cinsel taciz</a>.", "blog/cinsel-taciz-sucu-ve-sikayet-suresi.html"),
        ("Dolandırıcılık şüphelisi olarak aranıyorum, teslim olsam tutuklanır mıyım?", "Olası. Teslim + avukat. Delil durumuna göre adli kontrol.", "blog/dolandiricilik-sucunda-hile-unsuru.html"),
        ("Sahte fatura kullanmışız haberim yoktu, maliye tepeme bindi; ne yapacağım?", "Bilme, kasıt. Vergi cezası + ceza davası. Savunma.", "makaleler.html"),
        ("Birini ittim düştü, kasten yaralama diye dava açmışlar; çok ceza alır mıyım?", "Yaralama derecesi. Basit yaralama 1-3 yıl. Meşru müdafaa savunması. <a href='blog/mesru-mudafaa-ve-sinirin-asilmasi.html'>Meşru müdafaa</a>.", "blog/mesru-mudafaa-ve-sinirin-asilmasi.html"),
        ("Polise rüşvet teklif etmekten dosya açılmış, avukat beni kurtarabilir mi?", "TCK 252. Savunma, delil. Avukat zorunlu.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Zimmet suçlaması var, banka müfettişi gelecek; ne konuşmalıyım?", "Avukat eşliğinde. Susma hakkı. Sorulara cevap verme zorunluluğu sınırlı.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
    ]),
    ("Merak Edilenler", "merak-edilenler", [
        ("Avukatlık ücretleri 2026'da ne kadar oldu?", "Baro tarifesi. Dava değeri, iş niteliğine göre. <a href='iletisim.html'>Ücretsiz ön görüşme</a>.", "iletisim.html"),
        ("Barodan avukat istesem bana iyi bakarlar mı?", "Baro adli yardım. Gelir şartına göre ücretsiz/indirimli avukat.", "iletisim.html"),
        ("Mahkemede hakimle nasıl konuşulur, ne giyilir?", "Saygılı, kısa. Resmi kıyafet (takım, gömlek).", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Şahitlik yapmaya gitmezsem para cezası kesilir mi?", "Evet. CMK 45. Zorla getirtme. Yalan şahitlik suç.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Adli yardım nedir, kimler faydalanabilir?", "Gelir belgesi, dava türü. Baro veya Adli Yardım Bürosu.", "iletisim.html"),
        ("Dilekçeyi kendim yazsam mahkeme kabul eder mi?", "Evet. Usul şartlarına uygun olmalı. Avukatsız dava açılabilir.", "makaleler.html"),
        ("İstinaf ne demek, Yargıtay ne zaman biter?", "İstinaf: BAM. Yargıtay: Son inceleme. Süre 2 hafta.", "faaliyet-alanlari/ceza-hukuku/infaz-hukuku.html"),
        ("Hükmün açıklanmasının geri bırakılması (HAGB) ne demek?", "Denetim süresi. Koşullu ceza. <a href='blog/hukmun-aciklanmasinin-geri-birakilmasi-hagb.html'>HAGB</a>.", "blog/hukmun-aciklanmasinin-geri-birakilmasi-hagb.html"),
        ("Sabıka kaydı kaç senede bir silinir?", "Suç türüne göre 5-15 yıl. <a href='blog/adli-sicil-kaydinin-sabika-silinmesi.html'>Sabıka silme</a>.", "blog/adli-sicil-kaydinin-sabika-silinmesi.html"),
        ("Avukata vekalet vermek için notere ne kadar ödenir?", "Özel vekalet ~500-1500 TL. Genel vekalet daha yüksek.", "iletisim.html"),
        ("Savcı takipsizlik (KYOK) verirse dosya tamamen kapanır mı?", "Evet. İtiraz süresi 15 gün. İtiraz yoksa kesinleşir.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Müdahil (katılan) olmak ne işe yarar?", "Mağdur sıfatı. Dava takibi, itiraz, tazminat.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Bilirkişi raporu yanlış gelirse itiraz edilir mi?", "Evet. Yeniden bilirkişi, itiraz. HMK 279.", "makaleler.html"),
        ("Adli tıp raporu kaç ayda çıkar?", "1-6 ay. Yoğunluğa göre. Acil vakalar öncelikli.", "makaleler.html"),
        ("Duruşma günü e-devletten nasıl bakılır?", "e-Duruşma, UYAP. TC kimlik ile giriş.", "makaleler.html"),
        ("Bir davanın ne kadar süreceğini önceden bilebilir miyiz?", "Tahmini. Mahkeme yoğunluğu, delil. 6 ay - 3 yıl arası sık.", "makaleler.html"),
        ("Hakim kararı açıkladı, itiraz etmek için kaç günüm var?", "İstinaf 2 hafta. Tebligattan itibaren.", "faaliyet-alanlari/ceza-hukuku/infaz-hukuku.html"),
        ("Avukatım dosyaya bakmıyor, azletmek istesem ne yapmalıyım?", "Vekalet feshi. Yeni avukat. Eski avukata bildirim.", "iletisim.html"),
        ("Gıyabımda verilen karardan nasıl haberim olur?", "Tebligat. e-Devlet, PTT. Süre tebligatla başlar.", "makaleler.html"),
        ("AV. AYŞENUR AVCI HUKUK BÜROSU'na nasıl ulaşırım?", "Telefon: 0553 506 21 25, WhatsApp, <a href='iletisim.html'>iletişim formu</a>. Gebze merkez, Kocaeli ve İstanbul.", "iletisim.html"),
    ]),
]

# Yerel SEO: Gebze, Darıca, Çayırova, Dilovası - sokak ağzıyla aranan sorular
FAQ_DATA_LOCAL = [
    ("Ceza, Karakol ve Başına İş Açanlar", "ceza-karakol", [
        ("Gebze Adliyesi'nde dosyam var, duruşmaya gitmezsem yakalama çıkar mı?", "Celbe uymazsan zorla getirtme (yakalama) uygulanabilir. CMK 147. <a href='faaliyet-alanlari/ceza-hukuku/agir-ceza.html'>Gebze ceza avukatı</a> ile görüşün.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Basit yaralama davasında karşı taraf şikayeti geri çekerse dosya düşer mi?", "Evet. TCK 74/2 şikayetten vazgeçme ile kamu davası düşer. <a href='blog/mesru-mudafaa-ve-sinirin-asilmasi.html'>Yaralama</a>.", "blog/mesru-mudafaa-ve-sinirin-asilmasi.html"),
        ("Polise kimlik vermedim diye ceza kestiler, itiraz edebilir miyim?", "Kabahatler Kanunu. İdari yargıda itiraz. 15 gün süre.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Darıca sahilinde alkol alırken ceza yedik, sicile işler mi?", "Kabahat; adli sicile işlenmez. İdari para cezası.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Evde ruhsatsız silah yakalattım, hatıra kaldı desem kurtarır mıyım?", "TCK 613. Ruhsatsız silah bulundurma. Savunma zor; avukat şart.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("18 yaşından küçük kardeşim kavgaya karıştı, ailesi olarak biz mi ceza alırız?", "Çocuk CMK kapsamında. Velilere idari yaptırım olabilir; ceza çocuğa.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Yağma (gasp) suçlamasıyla tutuklandım, ilk celsede tahliye olur muyum?", "TCK 148. Delil durumuna göre. <a href='blog/yagma-gasp-sucu-ve-cezasi.html'>Yağma cezası</a>.", "blog/yagma-gasp-sucu-ve-cezasi.html"),
        ("Uzlaşma teklifi geldi, kabul edersem tazminat davası açabilirler mi?", "Uzlaşma cezayı düşürür; tazminat ayrı. Zarar tazminat davası açılabilir.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Gece yarısı bekçiler eve baskın yapabilir mi?", "Arama kararı veya acil durum. CMK 119. Hukuka uygunluk şart.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Denetimli serbestlikte imza atmayı unuttum, direkt içeri mi alırlar?", "İhlal tutanağı. İnfaz hakimi kararı. <a href='blog/denetimli-serbestlik-sartlari-2026.html'>Denetimli serbestlik</a>.", "blog/denetimli-serbestlik-sartlari-2026.html"),
        ("Hakaret davasında uzlaşma parası ne kadar olur?", "Taraflar anlaşır. Genelde 5.000-50.000 TL. <a href='blog/sosyal-medya-uzerinden-hakaret-sucu.html'>Hakaret</a>.", "blog/sosyal-medya-uzerinden-hakaret-sucu.html"),
        ("Sosyal medyada devlet büyüklerine hakaret suçlamasıyla ifadeye çağrıldım, ne yapmalıyım?", "TCK 125. Avukat eşliğinde ifade. Savunma kritik.", "faaliyet-alanlari/ceza-hukuku/bilisim-suclari.html"),
        ("Başkasının adına hat açılmış, dolandırıcılık davasında adım geçiyor, nasıl aklanırım?", "Bilme, kasıt ispatı. Kimlik çalınması, sahtecilik delili. <a href='blog/dolandiricilik-sucunda-hile-unsuru.html'>Dolandırıcılık</a>.", "blog/dolandiricilik-sucunda-hile-unsuru.html"),
        ("Şantaj yapılıyor, polise gidersem ailem duyar mı?", "Suç duyurusu gizli değil. Aile koruma talep edilebilir. TCK 106.", "blog/sosyal-medya-hakaret-santaj-suclari.html"),
        ("Kumar makinesi yakalattım, işletme mühürlenir mi?", "Kumar suçu. İşletmeye el koyma, mühürleme olabilir.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Gece kulübünde kavga çıktı, bodyguard bizi dövdü; tazminat alır mıyım?", "Evet. İşveren kusursuz sorumluluk. <a href='araclar.html'>Tazminat hesaplama</a>.", "araclar.html"),
        ("Trafikte yol verme kavgası kasten öldürmeye teşebbüs sayılır mı?", "Kast ispatı gerekir. Genelde yaralama veya tehdit. Bağlama göre.", "blog/trafik-kazasi-sonrasi-taksirle-yaralama.html"),
        ("İfademi alan polis beni tehdit etti, nereye şikayet edebilirim?", "Cumhuriyet Başsavcılığı, İç Denetim, İnsan Hakları Kurumu.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Gözaltındayken yemek/su vermediler, bu durum ifadeyi geçersiz kılar mı?", "İşkence, kötü muamele. İtiraz, delil geçersizliği. CMK.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Hırsızlık malı olduğunu bilmeden telefon aldım, suçlu sayılır mıyım?", "Bilme unsuru. Bilmeden alım suç sayılmaz. İspat önemli.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("İzinsiz kenevir ektim, içiciyim desem hapis yatar mıyım?", "Ekim ayrı suç. Kullanım miktarı önemli. <a href='faaliyet-alanlari/ceza-hukuku/uyusturucu-suclari.html'>Uyuşturucu suçları</a>.", "faaliyet-alanlari/ceza-hukuku/uyusturucu-suclari.html"),
        ("Silahla havaya ateş açtım, polis silahı aldı; geri alabilir miyim?", "El koyma. Dava sonrası iade veya müsadere. Ruhsat şart.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Maskeli kavgaya karıştım, ceza artar mı?", "Ağırlaştırıcı neden. TCK 62. Niyet, tanınmama.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Suçu üstlen dediler, para verdiler; yakalanırsam ne olur?", "Suça iştirak, yalan beyan. Ağır ceza. Savunma zor.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Kamu malına zarar verdim, hapis cezası paraya çevrilir mi?", "TCK 52. Adli para cezası veya 2 yıl altı hapis ertelenebilir.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
    ]),
    ("Aile, Boşanma ve Evdeki Hesaplar", "aile-evdeki-hesaplar", [
        ("Kocam kumar oynuyor, evi barkı sattı; boşanmada evi geri alabilir miyim?", "Mal kaçırma. TMK 197. Tenkis, iptal. <a href='faaliyet-alanlari/aile-hukuku/mal-paylasimi.html'>Mal paylaşımı</a>.", "faaliyet-alanlari/aile-hukuku/mal-paylasimi.html"),
        ("Eşim beni dövdü ama rapor almadım, şahitlerle boşanabilir miyim?", "Evet. Şahit, fotoğraf, kayıt delil. <a href='faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html'>Çekişmeli boşanma</a>.", "faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html"),
        ("Boşanma davası açmadan evi terk etsem suçlu sayılır mıyım?", "Hayır. Terk kusur sebebi olabilir; suç değil. TMK 166.", "faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html"),
        ("Karım çocukları göstermiyor, icra yoluyla çocuk görme nasıl olur?", "Kişisel ilişki ihlali. İcra cezası. <a href='blog/gecici-velayet-ve-kisisel-iliski-tesisi.html'>Kişisel ilişki</a>.", "blog/gecici-velayet-ve-kisisel-iliski-tesisi.html"),
        ("Anlaşmalı boşanma dedik, hakim bizi hemen boşar mı?", "Protokol uygunsa tek celsede. <a href='faaliyet-alanlari/aile-hukuku/anlasmali-bosanma.html'>Anlaşmalı boşanma</a>.", "faaliyet-alanlari/aile-hukuku/anlasmali-bosanma.html"),
        ("Mehir senedim var, boşanırken bu parayı söke söke alır mıyım?", "Mehir alacağı. İlamla icra. TMK 166-169.", "faaliyet-alanlari/aile-hukuku/mal-paylasimi.html"),
        ("Eşim benden gizli kredi çekmiş, borç bana kalır mı?", "Ortak borç değilse eşe ait. Aile konutu şerhi. <a href='faaliyet-alanlari/aile-hukuku/mal-paylasimi.html'>Mal paylaşımı</a>.", "faaliyet-alanlari/aile-hukuku/mal-paylasimi.html"),
        ("Boşanma davası 5 senedir bitmiyor, bu işin kısayolu yok mu?", "İstinaf, Yargıtay. Arabuluculuk, protokol. <a href='faaliyet-alanlari/aile-hukuku/anlasmali-bosanma.html'>Anlaşmalı</a>.", "faaliyet-alanlari/aile-hukuku/anlasmali-bosanma.html"),
        ("Sadakatsizlik davasında dedektif tutsam delil sayılır mı?", "Hukuka uygun elde edilirse kabul. Özel hayat ihlali riski.", "faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html"),
        ("Eski eşim nafaka ödememek için sigortasız çalışıyor, ne yapabilirim?", "Borçlu takibi. İş araştırma. Haciz. <a href='blog/nafaka-artirim-davasi-nasil-acilir.html'>Nafaka</a>.", "blog/nafaka-artirim-davasi-nasil-acilir.html"),
        ("Çocuğun soyadını değiştirmek istiyorum, mümkün mü?", "Evet. TMK 321. Velayet sahibi, çocuk yararı. <a href='blog/soyadi-degistirme-davasi-sartlari.html'>Soyadı değişikliği</a>.", "blog/soyadi-degistirme-davasi-sartlari.html"),
        ("Kaynanam yuvamı yıktı, ona da tazminat davası açabilir miyim?", "Kusur ispatı. Manevi tazminat. Zor ama mümkün.", "blog/bosanmada-maddi-ve-manevi-tazminat.html"),
        ("Eşim seni boşatmam diyor, tek taraflı nasıl boşanırım?", "Çekişmeli boşanma davası. TMK 166 sebepler. <a href='faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html'>Çekişmeli</a>.", "faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html"),
        ("Sosyal medya üzerinden flörtleşmek zina sayılır mı?", "Fiili birliktelik gerekir. Sadakat ihlali; boşanma sebebi.", "faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html"),
        ("Boşanırken evdeki eşyaları kim alır?", "Mal rejimi. Edinilmiş mallara katılma. Paylaşım.", "faaliyet-alanlari/aile-hukuku/mal-paylasimi.html"),
        ("Geçici nafaka ne zaman bağlanır?", "Dava açıldığında talep. Geçici önlem. TMK 169.", "blog/nafaka-artirim-davasi-nasil-acilir.html"),
        ("Eşimin maaşına nafaka için haciz koydurabilir miyim?", "Evet. İlam sonrası icra. Maaş haczi. <a href='blog/maas-haczi-orani-ve-hesaplamasi.html'>Maaş haczi</a>.", "blog/maas-haczi-orani-ve-hesaplamasi.html"),
        ("Ayrıyken başka biriyle hamile kalan kadın tazminat alabilir mi?", "Kusur oranı. Genelde erkek kusurlu. Tazminat alır.", "blog/bosanmada-maddi-ve-manevi-tazminat.html"),
        ("Yurtdışındaki eşimden Türkiye'de nasıl boşanırım?", "Yetkili mahkeme. İkamet. <a href='blog/yabanci-uyruklu-esten-bosanma-sureci.html'>Yabancı eşten boşanma</a>.", "blog/yabanci-uyruklu-esten-bosanma-sureci.html"),
        ("Boşanma davasında ses kaydı gizlice alınmışsa hakim dinler mi?", "Hukuka aykırı delil. HMK 189. Reddedilebilir.", "blog/ozel-hayatin-gizliligini-ihlal.html"),
    ]),
    ("Gebze Sanayi, İşçi Hakları ve Patronla Kavga", "gebze-sanayi", [
        ("Gebze GOSB'da sendikalı oldum diye kovuldum, hakkımı nasıl alırım?", "İK 18. Sendika üyeliği fesih sebebi değil. <a href='blog/sendikal-tazminat-ve-haklar.html'>Sendikal tazminat</a>.", "blog/sendikal-tazminat-ve-haklar.html"),
        ("Çayırova'daki lojistik firması istifa et yoksa tazminat vermem diyor, ne yapayım?", "Tehdit. Haklı fesih. Yazılı belge. <a href='faaliyet-alanlari/is-hukuku/ise-iade.html'>İşe iade</a>.", "faaliyet-alanlari/is-hukuku/ise-iade.html"),
        ("15 yıl 3600 günle kıdem tazminatı alıp işten çıkabilir miyim?", "Evet. Emeklilik yaşı + 3600 gün. <a href='araclar.html'>Kıdem hesaplama</a>.", "araclar.html"),
        ("Patron askere gidiyorum deyince tazminatımı ödemek zorunda mı?", "İşveren değişimi tazminatı etkilemez. Yeni işveren devralır. <a href='faaliyet-alanlari/is-hukuku/kidem-tazminati.html'>Kıdem tazminatı</a>.", "faaliyet-alanlari/is-hukuku/kidem-tazminati.html"),
        ("Dilovası'ndaki fabrikada mesleki hastalığa yakalandım, emekli olabilir miyim?", "SGK maluliyet. İş kazası/meslek hastalığı. <a href='faaliyet-alanlari/is-hukuku/is-kazasi.html'>İş kazası</a>.", "faaliyet-alanlari/is-hukuku/is-kazasi.html"),
        ("Performansın düşük diyerek tazminatsız attılar, işe iade açsam kazanır mıyım?", "Geçerli sebep ispatı işverende. <a href='blog/ise-iade-davasi-acma-sartlari.html'>İşe iade</a>.", "blog/ise-iade-davasi-acma-sartlari.html"),
        ("Maaşın bir kısmı bankaya bir kısmı elden yatıyor, emekli maaşım düşer mi?", "Evet. Eksik prim. SGK borç tespit. <a href='blog/fazla-mesai-ucreti-ve-ispat-yuku.html'>İspat</a>.", "blog/fazla-mesai-ucreti-ve-ispat-yuku.html"),
        ("Haftalık 45 saati geçiyoruz ama mesai yazmıyorlar, nasıl ispatlarım?", "Puantaj, tanık, e-posta. <a href='blog/fazla-mesai-ucreti-ve-ispat-yuku.html'>Fazla mesai</a> ve <a href='araclar.html'>hesaplama</a>.", "araclar.html"),
        ("İş yerinde kamera şifresini biliyorum, görüntüleri alsam suç olur mu?", "Gizlilik ihlali. KVKK, TCK 136. Riskli.", "faaliyet-alanlari/bilisim-e-ticaret/kvkk.html"),
        ("Patron küfretti, ceketimi alıp çıksam tazminat alır mıyım?", "Haklı fesih. İK 24/II. Kıdem + ihbar. <a href='faaliyet-alanlari/is-hukuku/mobbing.html'>Mobbing</a>.", "faaliyet-alanlari/is-hukuku/mobbing.html"),
        ("Yıllık izindeyken işten çıkarıldım, ihbar süresi sayılır mı?", "Evet. İzin süresi iş sözleşmesi devam eder. Fesih geçersiz.", "blog/yillik-izin-hakki-ve-kullanim-sartlari.html"),
        ("Fabrikada yemekten zehirlendik, toplu dava açabilir miyiz?", "Evet. İşveren sorumluluğu. Tazminat. <a href='faaliyet-alanlari/is-hukuku/is-kazasi.html'>İş kazası</a>.", "faaliyet-alanlari/is-hukuku/is-kazasi.html"),
        ("Taşeron işçiyim, asıl kadrodakilerle aynı hakları nasıl alırım?", "Eşit işlem. İK 6. Taşeron farkı yasak. <a href='blog/isyeri-devri-ve-isci-haklari.html'>İşçi hakları</a>.", "blog/isyeri-devri-ve-isci-haklari.html"),
        ("İş kazası tutanağını kendi hatam diye imzaladım, haklarım yandı mı?", "Kısmen. Kusur oranı. Yine de tazminat. <a href='faaliyet-alanlari/is-hukuku/is-kazasi.html'>İş kazası</a>.", "faaliyet-alanlari/is-hukuku/is-kazasi.html"),
        ("EYT ile emekli oldum, patron tazminatı taksitle ödemek istiyor; yasal mı?", "Anlaşma ile olur. Zorunlu değil. Peşin talep hakkı.", "faaliyet-alanlari/is-hukuku/kidem-tazminati.html"),
    ]),
    ("Ev Sahibi, Kiracı ve Mahalle Savaşları", "ev-sahibi-kiracı", [
        ("Gebze'de kiralar uçtu, ev sahibi çık kendim oturacağım diyor; yalanını nasıl bozarım?", "İhtiyaç tahliyesi. Sahtelik tespit. Bilirkişi. <a href='faaliyet-alanlari/gayrimenkul/tahliye.html'>Tahliye</a>.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("Kontratım bitti, ev sahibi yeni kontrat yapmıyor; beni çıkarabilir mi?", "5 yıl dolunca kira tespit. Tahliye için dava. <a href='blog/kira-tespit-davasinda-5-yil-kurali.html'>5 yıl kuralı</a>.", "blog/kira-tespit-davasinda-5-yil-kurali.html"),
        ("Aidat ödemeyen komşu yüzünden asansörü kapattılar, ne yapmalıyım?", "KMK. Ortak karar. Aidat alacağı davası. <a href='blog/kat-mulkiyeti-kanunu-ve-aidat-borclari.html'>Aidat</a>.", "blog/kat-mulkiyeti-kanunu-ve-aidat-borclari.html"),
        ("Tahliye taahhütnamesi imzalamadan ev vermiyorlar, imzalasam ne olur?", "Taahhüt geçerli. İrade sakatlığı zor. <a href='blog/kira-tahliye-davalarinda-arabuluculuk.html'>Tahliye</a>.", "blog/kira-tahliye-davalarinda-arabuluculuk.html"),
        ("Kirayı bankadan değil elden veriyordum, ev sahibi ödemedi diye icra yollamış!", "Ödeme ispatı. Banka, tanık. İtiraz. <a href='faaliyet-alanlari/icra-iflas/menfi-tespit.html'>Menfi tespit</a>.", "faaliyet-alanlari/icra-iflas/menfi-tespit.html"),
        ("Üst kattaki su sızdırıyor, tavan sarardı; tamir parasını nasıl alırım?", "TBK 315. Üst kat sorumlu. Tazminat. <a href='faaliyet-alanlari/gayrimenkul/tahliye.html'>Kira hukuku</a>.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("Evde köpek beslemek yasak mı?", "Sözleşme ve iç yönetmelik. Genelde yasak değil; gürültü yasak.", "blog/kat-mulkiyeti-kanunu-ve-aidat-borclari.html"),
        ("Dükkan sahibi stopajı sen ödeyeceksin diyor, kontratta yazmıyor; ne yapayım?", "Sözleşme hükmü. Yazılı değilse geçersiz. <a href='faaliyet-alanlari/gayrimenkul/kira-tespit.html'>Kira tespit</a>.", "faaliyet-alanlari/gayrimenkul/kira-tespit.html"),
        ("Hava parası vererek dükkan devraldım, mal sahibi beni çıkarıyor!", "Hava parası sözleşme dışı. Tahliye davası. Hak kaybı riski.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("Komşum balkonumun önünü kapattı, belediyeye mi şikayet edeyim?", "Easement, KMK. Mahkeme. <a href='blog/gecit-hakki-davalari.html'>Geçit hakkı</a>.", "blog/gecit-hakki-davalari.html"),
        ("5 yılı dolan kiracıya kira tespit davası nasıl açılır?", "Sulh Hukuk. Rayiç tespit. <a href='faaliyet-alanlari/gayrimenkul/kira-tespit.html'>Kira tespit</a>.", "faaliyet-alanlari/gayrimenkul/kira-tespit.html"),
        ("Evi boyasız aldım, çıkarken boya parası istiyorlar; vermeli miyim?", "Normal aşınma kiracıya ait değil. TBK 347. Anlaşmazlıkta dava.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("Ortak bahçeye çardak yaptım, komşular yıkabilir mi?", "Ortak karar. İzinsiz yapı. KMK.", "blog/ortakligin-giderilmesi-izale-i-suyu.html"),
        ("Elektrik/su faturasını ev sahibi kendi üstüne almıyor, kapansa kim suçlu?", "Sözleşme. Genelde kiracı. Malikin müdahalesi.", "faaliyet-alanlari/gayrimenkul/tahliye.html"),
        ("Fuzuli işgal davası ne kadar sürer?", "6-18 ay. Tahliye + ecrimisil. <a href='blog/ecrimisil-haksiz-isgal-tazminati-davasi.html'>Ecrimisil</a>.", "blog/ecrimisil-haksiz-isgal-tazminati-davasi.html"),
    ]),
    ("İnternet, Dolandırıcılık ve Klavye Delikanlıları", "internet-dolandiricilik", [
        ("Letgo'da bozuk ürün sattılar, adamı bulamıyorum; ne yapmalıyım?", "Suç duyurusu. Platform bilgisi. <a href='blog/internet-yoluyla-dolandiricilik-sucu.html'>Dolandırıcılık</a>.", "blog/internet-yoluyla-dolandiricilik-sucu.html"),
        ("Birinin fotoğrafını izinsiz alıp şerefsize bak diye paylaştım, başım yanar mı?", "TCK 125 hakaret, 134 özel hayat. Evet. <a href='blog/ozel-hayatin-gizliligini-ihlal.html'>Özel hayat</a>.", "blog/ozel-hayatin-gizliligini-ihlal.html"),
        ("E-ticaret sitemden paramı çekemiyorum, firma battı mı?", "Şirket bilgisi. Konkordato, iflas. Alacaklı başvurusu.", "faaliyet-alanlari/bilisim-e-ticaret/e-ticaret-sozlesmeleri.html"),
        ("Çocuk oyun oynarken kredi kartından 50 bin TL çekmiş, geri iade olur mu?", "Banka ile görüşme. 14 yaş altı ehliyetsiz. İade mümkün.", "blog/internet-bankaciligi-dolandiriciligi.html"),
        ("Telegram gruplarında bahis tüyosu verenlere para kaptırdım, suç duyurusu yapılır mı?", "Evet. Dolandırıcılık. Siber Suçlar. <a href='blog/internet-yoluyla-dolandiricilik-sucu.html'>Dolandırıcılık</a>.", "blog/internet-yoluyla-dolandiricilik-sucu.html"),
        ("Gizli kamerayla birini çektim, şantaj yapmıyorum ama telefonumda duruyor; suç mu?", "TCK 134. Veriyi silmek, yaymamak. Yayarsan suç.", "blog/ozel-hayatin-gizliligini-ihlal.html"),
        ("Sahte avukat bizi dolandırdı, dosyan var para yatır dedi; ne yapmalıyım?", "Suç duyurusu. Dolandırıcılık + sahtecilik. Baro şikayet.", "blog/dolandiricilik-sucunda-hile-unsuru.html"),
        ("Şirket bilgisayarından oyun indirdim, virüs girdi; tazminatsız kovulur muyum?", "Ciddiyetine göre. İş güvenliği ihlali. Geçerli sebep olabilir.", "faaliyet-alanlari/is-hukuku/ise-iade.html"),
        ("Hackerlar banka hesabımdan para çekmiş, banka güvenlik hatası senin diyor!", "Banka sorumluluğu. Şikayet, BDDK. Dava. <a href='blog/internet-bankaciligi-dolandiriciligi.html'>Banka dolandırıcılığı</a>.", "blog/internet-bankaciligi-dolandiriciligi.html"),
        ("İnternetten hakaret davasında IP adresi bulunamaz mı?", "Bulunur. Siber Suçlar. ISP kayıtları. <a href='blog/sosyal-medya-uzerinden-hakaret-sucu.html'>Hakaret</a>.", "blog/sosyal-medya-uzerinden-hakaret-sucu.html"),
    ]),
    ("Borç, İcra ve Alacak Savaşları", "borc-icra", [
        ("Arkadaşıma elden borç verdim, şahidim var; senetsiz alabilir miyim?", "Evet. Şahit, banka havalesi. Alacak davası. BK.", "faaliyet-alanlari/icra-iflas/cek-senet.html"),
        ("Üstüme hiçbir mal varlığı yok, borcumdan dolayı hapse girer miyim?", "Hayır. Mal beyanı. İcra cezası sadece nafaka vb.", "faaliyet-alanlari/icra-iflas/cek-senet.html"),
        ("Maaşımın tamamına haciz koymuşlar, bu yasal mı?", "Hayır. 1/3 haczedilemez. <a href='blog/maas-haczi-orani-ve-hesaplamasi.html'>Maaş haczi</a>.", "blog/maas-haczi-orani-ve-hesaplamasi.html"),
        ("Emekli maaşıma borçtan dolayı bloke konulur mu?", "Evet. Haciz oranı. Asgari ücret 1/3 korunur.", "blog/e-haciz-ve-banka-blokesi-kaldirma.html"),
        ("Ödeme şartını ihlal (taahhüdü ihlal) hapis cezası kesin mi?", "TCK 206. Evet. Ödeme ile düşer.", "faaliyet-alanlari/icra-iflas/cek-senet.html"),
        ("İcradan satılık ev alırken nelere dikkat etmeli?", "Tapu, ipotek, kira, ecrimisil. <a href='blog/ecrimisil-haksiz-isgal-tazminati-davasi.html'>Ecrimisil</a>.", "blog/ecrimisil-haksiz-isgal-tazminati-davasi.html"),
        ("Borçlu öldü, mirasçıları bu borcu ödemek zorunda mı?", "Mirası kabul ederse evet. Reddi miras 3 ay.", "makaleler.html"),
        ("Banka borcu nedeniyle telefonuma sürekli mesaj geliyor, taciz sayılır mı?", "Aşırı ise KVKK, taciz. Şikayet. Ölçülü arama yasal.", "faaliyet-alanlari/bilisim-e-ticaret/kvkk.html"),
        ("Senetteki imza benim değil, imza itirazı nasıl yapılır?", "7 gün itiraz. İtirazın iptali davası. Grafolog. <a href='blog/icra-takibine-itiraz-ve-itirazin-iptali.html'>İcra itiraz</a>.", "blog/icra-takibine-itiraz-ve-itirazin-iptali.html"),
        ("İcra müdürü eve girmek için kapıyı kırabilir mi?", "İlamlı icrada, zorunlu hallerde. İİK. Zabıta eşliğinde.", "faaliyet-alanlari/icra-iflas/cek-senet.html"),
    ]),
    ("Kaza, Sağlık ve Başıma Gelenler", "kaza-saglik", [
        ("Darıca Farabi Hastanesi'nde yanlış ameliyat ettiler, tazminat davası açılır mı?", "Evet. Malpraktis. <a href='araclar.html'>Tazminat hesaplama</a>.", "araclar.html"),
        ("Yolda yürürken çukura düştüm, bacağım kırıldı; belediyeyi mahkemeye verebilir miyim?", "Evet. Kusur. Belediye sorumluluğu. <a href='blog/trafik-kazasi-sonrasi-taksirle-yaralama.html'>Tazminat</a>.", "araclar.html"),
        ("Trafik kazasında asli kusurlu benim ama karşı taraf çok para istiyor!", "Kusur oranı. Bilirkişi. Sigorta. <a href='blog/trafik-kazasi-sonrasi-taksirle-yaralama.html'>Trafik kazası</a>.", "blog/trafik-kazasi-sonrasi-taksirle-yaralama.html"),
        ("Sigortasız araçla kaza yaptım, bütün masraf bana mı kalacak?", "Evet. Rücu yok. Siz ödersiniz. MTR.", "blog/trafik-kazasi-sonrasi-taksirle-yaralama.html"),
        ("Doktor riski var dedi, imza attım; yine de dava açabilir miyim?", "Aydınlatılmış onam. Hata varsa evet. Malpraktis.", "makaleler.html"),
        ("Özel hastane yoğun bakım ücreti istedi, bu yasal mı?", "Sözleşme. Acil durumda sınırlı. Tüketici şikayet.", "makaleler.html"),
        ("Dişçide dişim kırıldı, implant parasını doktordan alabilir miyim?", "Evet. Malpraktis. Tazminat.", "makaleler.html"),
        ("Ambulans geç geldiği için hastamız öldü, dava açsak sonuç çıkar mı?", "Evet. Kusur. Sağlık Bakanlığı, 112. Tazminat.", "makaleler.html"),
        ("Okul servisinden düşen çocuğun tazminatı kime ödenir?", "Taşıyıcı, okul. Kusursuz sorumluluk. <a href='araclar.html'>Tazminat</a>.", "araclar.html"),
        ("Marketin önünde kayıp düştüm, kamera görüntülerini vermiyorlar; ne yapayım?", "Mahkeme delil talebi. Tüketici. İşyeri sorumluluğu.", "blog/yaniltici-reklam-ve-tuketici-haklari.html"),
    ]),
    ("Miras ve Kardeş Kavgaları", "miras-kardes", [
        ("Babam ölmeden bütün malı abime devretmiş, dava açıp payımı alabilir miyim?", "Tenkis davası. Saklı pay. TMK 560. <a href='blog/on-alim-hakkindan-feragat-ve-vazgecme.html'>Miras</a>.", "blog/on-alim-hakkindan-feragat-ve-vazgecme.html"),
        ("Tenkis davası nedir, ne zaman açılır?", "Ölüme bağlı tasarrufun saklı paya tecavüzünün kaldırılması. 10 yıl.", "blog/on-alim-hakkindan-feragat-ve-vazgecme.html"),
        ("Veraset ilamı çıkarmak ne kadar sürer?", "Noter 1-2 hafta. Mahkeme 2-6 ay.", "makaleler.html"),
        ("Kardeşlerim miras kalan evi paylaşmıyor, mahkemeyle nasıl sattırırım?", "İzale-i şuyu. <a href='blog/ortakligin-giderilmesi-izale-i-suyu.html'>Ortaklığın giderilmesi</a>.", "blog/ortakligin-giderilmesi-izale-i-suyu.html"),
        ("Üvey anne mirastan pay alır mı?", "Evet. Sağ kalan eş. TMK 499.", "makaleler.html"),
        ("Babamın borçları mirastan fazla, reddi miras nasıl yapılır?", "3 ay. Sulh Hukuk. Yazılı beyan.", "makaleler.html"),
        ("Vasiyetname noterden mi yapılmalı, evde yazsam geçer mi?", "Resmi vasiyetname noter. El yazısı geçerli; 2 şahit.", "makaleler.html"),
        ("Torunlar mirastan pay alabilir mi?", "Evet. Zümre sistemi. TMK 495.", "makaleler.html"),
        ("Ortak mirasta saklı pay (mahfuz hisse) ne demek?", "Kanuni mirasçının alacağı asgari pay. Tenkis koruması.", "blog/onalim-sufa-hakki-ve-kullanimi.html"),
        ("Amcamın çocuğu yok, mirası kime kalır?", "Zümre. Kardeşler, yeğenler. TMK 495.", "makaleler.html"),
    ]),
    ("Avukat Bey Şöyle Bir Durum Var", "avukat-bey-durum", [
        ("Sabıkalıyım, ehliyet alabilir miyim?", "Suç türüne göre. Trafik, hüküm. Genelde engel. <a href='blog/adli-sicil-kaydinin-sabika-silinmesi.html'>Sabıka silme</a>.", "blog/adli-sicil-kaydinin-sabika-silinmesi.html"),
        ("Yalan şahitlik yaptım, vicdan azabı çekiyorum; mahkemeye gidip düzeltsem hapse girer miyim?", "TCK 272. Etkin pişmanlık. İndirim. Risk var.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("GBT'de aranıyor görünüyorum, karakola teslim olmalı mıyım?", "Avukatla teslim. Yakalanmaktan iyi. Adli kontrol.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Yanlışlıkla birinin bahçesindeki meyveyi yedim, hırsızlık sayılır mı?", "Değer düşükse, niyet. Genelde kabahat veya cezasız.", "faaliyet-alanlari/ceza-hukuku/agir-ceza.html"),
        ("Birine borç verdim ama adam kayboldu, dolandırıcılık mı alacak mı?", "Alacak. Kayıp şahıs. İlam, icra. Dolandırıcılık kast gerekir.", "faaliyet-alanlari/icra-iflas/cek-senet.html"),
        ("Adli tıp raporu alkollüydü diyor ama ben içmemiştim, itiraz edilir mi?", "Evet. Yeniden inceleme. Kan örneği, prosedür.", "makaleler.html"),
        ("Tutuklu yargılanan eşim ne zaman tahliye olur?", "Delil, süre. CMK 108. Duruşma, temyiz.", "faaliyet-alanlari/ceza-hukuku/infaz-hukuku.html"),
        ("Savcı beraat istedi ama hakim ceza verdi, şimdi ne olacak?", "İstinaf. 2 hafta. BAM.", "faaliyet-alanlari/ceza-hukuku/infaz-hukuku.html"),
        ("Avukat tutacak param yok, devlet bana avukat verir mi?", "Adli yardım. Gelir şartı. Baro. <a href='iletisim.html'>Danışın</a>.", "iletisim.html"),
        ("Dilekçem reddedildi, ikinci kez dava açabilir miyim?", "Evet. Yeni sebep, dava türü. Res judicata.", "makaleler.html"),
    ]),
]

def generate_faq_html():
    """FAQ HTML içeriğini üretir."""
    all_data = FAQ_DATA + FAQ_DATA_EXTRA + FAQ_DATA_NEW + FAQ_DATA_LOCAL
    html_parts = []
    
    for cat_title, cat_slug, items in all_data:
        html_parts.append(f'''
            <section class="faq-category" id="{cat_slug}">
                <h2 class="faq-category-title">{cat_title}</h2>
                <div class="faq-list">
''')
        CTA_HTML = '''                            <p class="faq-cta"><a href="https://wa.me/905535062125" class="btn-whatsapp-mini" target="_blank" rel="noopener">Gebze ve çevresinde hukuki danışmanlık için WhatsApp&apos;tan Yazın</a> · <a href="araclar.html">Ücretsiz Tazminat Hesapla</a></p>'''
        for q, a, _ in items:
            html_parts.append(f'''                    <div class="faq-item">
                        <button class="faq-question" onclick="toggleFaq(this)">
                            <span>{q}</span>
                            <i data-lucide="plus" class="faq-icon"></i>
                        </button>
                        <div class="faq-answer">
                            <p>{a}</p>
{CTA_HTML}
                        </div>
                    </div>
''')
        html_parts.append('''                </div>
            </section>
''')
    
    return '\n'.join(html_parts)

def generate_full_sss():
    """Tam sss.html sayfasını oluşturur."""
    faq_content = generate_faq_html()
    return f'''<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sık Sorulan Sorular | Gebze Avukat | AV. AYŞENUR AVCI HUKUK BÜROSU</title>
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <meta name="description" content="Ceza, iş, aile, kira, icra ve bilişim hukuku hakkında sık sorulan sorular. Gebze avukat, Tuzla avukat, İstanbul avukat danışmanlığı.">
    <meta name="keywords" content="Gebze avukat, Gebze ceza avukatı, Gebze boşanma avukatı, Gebze iş avukatı, Tuzla avukat, İstanbul avukat, Kocaeli avukat, SSS, sık sorulan sorular">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest" defer></script>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .page-header {{ padding: 150px 0 60px; background: #1a1a1a; text-align: center; border-bottom: 1px solid var(--border-white); }}
        .faq-page {{ padding: 60px 0 100px; }}
        .faq-category {{ margin-bottom: 80px; }}
        .faq-category-title {{ color: var(--matte-gold); font-size: 24px; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 1px solid var(--border-gold); }}
        .faq-nav {{ display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; margin-bottom: 50px; }}
        .faq-nav a {{ padding: 10px 20px; background: #111; border: 1px solid var(--border-white); color: #ccc; font-size: 13px; text-decoration: none; transition: 0.3s; }}
        .faq-nav a:hover {{ border-color: var(--matte-gold); color: var(--matte-gold); }}
        .cta-section {{ background: #111; padding: 50px; text-align: center; margin-top: 60px; border: 1px solid var(--border-gold); border-radius: 8px; }}
        .cta-section h3 {{ color: var(--matte-gold); margin-bottom: 20px; }}
        .cta-btns {{ display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; margin-top: 25px; }}
        .cta-btns a {{ padding: 15px 30px; text-decoration: none; font-weight: 600; transition: 0.3s; }}
        .cta-btns .btn-whatsapp {{ background: #25D366; color: #fff; }}
        .cta-btns .btn-calc {{ background: transparent; border: 1px solid var(--matte-gold); color: var(--matte-gold); }}
        .faq-cta {{ margin-top: 15px; font-size: 13px; }}
        .faq-cta a {{ color: var(--matte-gold); text-decoration: none; }}
        .btn-whatsapp-mini {{ color: #25D366 !important; }}
        @media (max-width: 768px) {{ .page-header {{ padding: 120px 20px 40px; }} .faq-category-title {{ font-size: 20px; }} }}
    </style>
</head>
<body>
    <header id="site-header"></header>
    <main>
        <div class="page-header">
            <div class="container">
                <h1>Sık Sorulan Sorular</h1>
                <p style="margin-top: 15px; color: var(--text-gray); max-width: 600px; margin-left: auto; margin-right: auto;">Ceza, iş, aile, kira, icra ve bilişim hukuku hakkında <strong>Gebze avukat</strong> perspektifiyle en çok sorulan soruların yanıtları.</p>
                <nav class="faq-nav" aria-label="Kategori navigasyonu">
                    <a href="#ceza-hukuku">Ceza</a>
                    <a href="#basim-belada">Başım Belada</a>
                    <a href="#bilisim">Bilişim</a>
                    <a href="#is-hukuku">İş Hukuku</a>
                    <a href="#patronla-takistik">Patronla Takıştık</a>
                    <a href="#gayrimenkul">Kira</a>
                    <a href="#ev-sahibi-cik-diyor">Ev Sahibi Çık Diyor</a>
                    <a href="#aile-hukuku">Aile</a>
                    <a href="#hanimla-papaz">Hanımla Papaz</a>
                    <a href="#internette-basim-belada">İnternette Bela</a>
                    <a href="#icra-iflas">İcra</a>
                    <a href="#kaza-borcum">Kaza & Borç</a>
                    <a href="#diger">Diğer</a>
                    <a href="#karisik-mevzular">Karışık</a>
                    <a href="#savunma">Savunma</a>
                    <a href="#avukat-bey-suclandim">Suçlandım</a>
                    <a href="#merak-edilenler">Merak Edilenler</a>
                    <a href="#ceza-karakol">Ceza & Karakol</a>
                    <a href="#aile-evdeki-hesaplar">Aile & Ev</a>
                    <a href="#gebze-sanayi">Gebze Sanayi</a>
                    <a href="#ev-sahibi-kiracı">Kira & Mahalle</a>
                    <a href="#internet-dolandiricilik">İnternet</a>
                    <a href="#borc-icra">Borç & İcra</a>
                    <a href="#kaza-saglik">Kaza & Sağlık</a>
                    <a href="#miras-kardes">Miras</a>
                    <a href="#avukat-bey-durum">Avukat Bey</a>
                </nav>
            </div>
        </div>
        <div class="faq-page container" style="max-width: 900px;">
            {faq_content}
            <div class="cta-section">
                <h3>Hâlâ sorunuz mu var?</h3>
                <p style="color: #888;">Ücretsiz ön görüşme için hemen iletişime geçin. <strong>Gebze avukat</strong> ofisimiz Kocaeli ve İstanbul bölgesinde hizmet vermektedir.</p>
                <div class="cta-btns">
                    <a href="https://wa.me/905535062125" class="btn-whatsapp" target="_blank" rel="noopener"><i data-lucide="message-circle" style="width: 18px; vertical-align: middle;"></i> WhatsApp'tan Danışın</a>
                    <a href="araclar.html" class="btn-calc"><i data-lucide="calculator" style="width: 18px; vertical-align: middle;"></i> Ücretsiz Tazminat Hesaplayın</a>
                    <a href="iletisim.html" class="btn-calc">İletişim Formu</a>
                </div>
            </div>
        </div>
    </main>
    <footer id="site-footer"></footer>
    <script src="js/translations.js"></script>
    <script src="js/site-config.js"></script>
    <script src="js/main.js"></script>
    <script src="js/schema.js"></script>
    <script>lucide.createIcons();</script>
</body>
</html>'''

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--full":
        with open("sss.html", "w", encoding="utf-8") as f:
            f.write(generate_full_sss())
        print("sss.html oluşturuldu.")
    else:
        print(generate_faq_html())
