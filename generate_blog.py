import os
import re
import subprocess

SITE_URL = "https://avukataysenuravci.com"

INTERNAL_LINKS = [
    {"href": f"{SITE_URL}/", "anchor": "Gebze hukuk burosu hizmetleri"},
    {"href": f"{SITE_URL}/iletisim.html", "anchor": "iletisim ve randevu sayfasi"},
]

EXTERNAL_AUTHORITY_LINKS = [
    {"href": "https://gebze.adalet.gov.tr/", "anchor": "Gebze Adliyesi resmi duyurulari"},
    {"href": "https://www.mevzuat.gov.tr/", "anchor": "Turk hukuk mevzuati"},
    {"href": "https://www.kocaelibarosu.org.tr/", "anchor": "Kocaeli Barosu bilgilendirmeleri"},
]


def pick_related_article(current_article, all_articles):
    for candidate in all_articles:
        if (
            candidate["slug"] != current_article["slug"]
            and candidate["categorySlug"] == current_article["categorySlug"]
        ):
            return candidate
    return None


def word_count_from_html(html):
    plain = re.sub(r"<[^>]+>", " ", html)
    plain = re.sub(r"\s+", " ", plain).strip()
    return len(plain.split(" ")) if plain else 0


def build_seo_content(article, all_articles):
    related = pick_related_article(article, all_articles)
    related_href = f"{SITE_URL}/blog/{related['slug']}.html" if related else f"{SITE_URL}/makaleler.html"
    related_anchor = related["title"] if related else "ilgili blog makaleleri"

    internal_links_html = (
        f'<a href="{INTERNAL_LINKS[0]["href"]}">{INTERNAL_LINKS[0]["anchor"]}</a>, '
        f'<a href="{INTERNAL_LINKS[1]["href"]}">{INTERNAL_LINKS[1]["anchor"]}</a> ve '
        f'<a href="{related_href}">{related_anchor}</a>'
    )
    external_links_html = ", ".join(
        [
            f'<a href="{link["href"]}" target="_blank" rel="noopener noreferrer">{link["anchor"]}</a>'
            for link in EXTERNAL_AUTHORITY_LINKS
        ]
    )

    body = f"""
                        <p>{article["content"]}</p>
                        <h2>Hukuki Cerceve</h2>
                        <p>{article["excerpt"]}</p>
                        <p>Dava acmadan once delil yapisi, sureler ve usul kurallari netlestirilmelidir. Yanlis adimlar sureci uzatabilir ve hak kaybina neden olabilir.</p>
                        <p>Gebze ve Kocaeli uygulamasinda yetkili mahkeme secimi kritik bir basliktir. Dilekce kurgusunun ilk asamada dogru kurulmasi sonucu dogrudan etkiler.</p>
                        <h3>Ilk adimlar</h3>
                        <p>Ilk olarak olay kronolojisini net bir zaman cizelgesine dokun. Yazili belgeleri ve dijital kayitlari ayri dosyalarda toplayin.</p>
                        <p>Ardindan talep konusunu acik ve olculebilir bicimde belirleyin. Mumkunse dava oncesi profesyonel inceleme alin.</p>
                        <h2>Pratik surec notlari</h2>
                        <p>Yerel mahkemelerde dosya yogunlugu ve tebligat hizi sureyi degistirebilir. Bu nedenle evrak takibi duzenli yapilmalidir.</p>
                        <p>Her dosyada ayni strateji etkili olmaz. Olayin niteligine uygun yol haritasi kurmak, itiraz ve istinaf asamasini da guclendirir.</p>
                        <h3>Gerekli belgeler</h3>
                        <ul>
                            <li>Olay kronolojisini tarih sirasiyla tek sayfada ozetleyin.</li>
                            <li>Sozlesme, banka kaydi, mesaj ve ihtarnameleri ayri klasorlerde saklayin.</li>
                            <li>Sureleri takvimleyip son basvuru gununu netlestirin.</li>
                            <li>Eksik evrak listesini once tamamlayip sonra basvuru yapin.</li>
                        </ul>
                        <h3>Kisa kontrol listesi</h3>
                        <ul>
                            <li>Yetkili mahkeme ve yargi yolu dogru mu?</li>
                            <li>Deliller usule uygun elde edildi mi?</li>
                            <li>Tebligat adresi ve iletisim bilgileri guncel mi?</li>
                        </ul>
                        <h2>Zorunlu ic linkler</h2>
                        <p>Daha kapsamli yol haritasi icin {internal_links_html} baglantilarini inceleyebilirsiniz.</p>
                        <h2>Resmi kaynaklar</h2>
                        <p>Guncel mevzuat, kurum duyurulari ve uygulama notlari icin {external_links_html} kaynaklarini duzenli takip edin.</p>
                        <h3>Bilgilendirme notu</h3>
                        <p>Bu makale genel bilgilendirme amaciyla hazirlanmistir.</p>
                        <p>Somut olayinizin kosullarina gore hukuki sonuc degisebilir. Kisisel degerlendirme icin profesyonel destek alinmasi onerilir.</p>
    """

    # Uzunluk hedefi: en az ~700 kelime
    long_block = """
                        <h2>Sik sorulan sorular</h2>
                        <p>Sureler genellikle resmi bildirim, fesih tarihi veya tebligatla baslar. Yanlis hesaplama hak kaybina yol acabilecegi icin bu adim dikkatle yapilmalidir.</p>
                        <p>Dava once zorunlu basvuru varsa (ornegin arabuluculuk), bu asama atlanmamalidir. Aksi durumda dava usulden reddedilebilir.</p>
                        <h3>Delil ve ispat</h3>
                        <p>Hukuka aykiri yolla elde edilen kayitlar bircok dosyada dikkate alinmaz. Delil toplarken usule uygun hareket edilmesi zorunludur.</p>
                        <p>Ozellikle dijital delillerde tarihce, kaynak ve butunluk kontrolu yapin. Gerekli durumlarda noter tespiti veya resmi teyit alin.</p>
                        <h3>Maliyet planlamasi</h3>
                        <ul>
                            <li>Harc ve tebligat giderlerini onceden hesaplayin.</li>
                            <li>Bilirkişi ve vekalet kalemlerini dava basinda planlayin.</li>
                            <li>Uzlasma ihtimalini maliyet-zaman ekseninde degerlendirin.</li>
                        </ul>
                        <p>Mevzuat ve ictihatlar duzenli takip edilmelidir. Guncel kararlar talep miktari ve ispat olcutlerini degistirebilir.</p>
    """
    if word_count_from_html(body) < 700:
        body += long_block
    return body

# Define the template for blog articles with i18n support
template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | AV. AYŞENUR AVCI HUKUK BÜROSU</title>
    <meta name="description" content="{excerpt}" data-i18n-content="blog-desc-full">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
    <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet"></noscript>
    <script src="https://unpkg.com/lucide@latest" defer></script>
    <link rel="stylesheet" href="../css/style.css">
    <style>
        .article-content {{ padding-top: 150px; }}
        .breadcrumb {{ margin-bottom: 30px; font-size: 12px; color: var(--text-gray); text-transform: uppercase; letter-spacing: 1px; }}
        .breadcrumb a:hover {{ color: var(--matte-gold); }}
        .article-layout {{ display: grid; grid-template-columns: 1fr 300px; gap: 60px; }}
        .main-article h1 {{ font-size: clamp(32px, 4vw, 42px); color: var(--matte-gold); margin-bottom: 20px; line-height: 1.25; word-break: break-word; }}
        .meta-info {{ display: flex; gap: 20px; margin-bottom: 40px; padding-bottom: 20px; border-bottom: 1px solid var(--border-white); font-size: 13px; color: #666; }}
        .content-body {{ font-size: 18px; line-height: 1.8; color: #ccc; overflow-wrap: break-word; word-break: break-word; }}
        .content-body p {{ margin-bottom: 16px; }}
        .content-body h2 {{ color: var(--matte-gold); margin: 32px 0 14px; line-height: 1.35; }}
        .content-body h3 {{ color: #fff; margin: 24px 0 12px; line-height: 1.35; }}
        .content-body ul {{ margin: 10px 0 18px 22px; }}
        .sidebar {{ position: sticky; top: 120px; height: fit-content; }}
        .sidebar-widget {{ background: #121212; border: 1px solid var(--border-white); padding: 25px; margin-bottom: 30px; border-radius: 8px; }}
        .sidebar-widget h4 {{ color: var(--matte-gold); margin-bottom: 20px; font-size: 16px; border-bottom: 1px solid var(--border-gold); padding-bottom: 10px; }}
        @media (max-width: 992px) {{ .article-layout {{ grid-template-columns: 1fr; }} .sidebar {{ position: static; }} }}
        @media (max-width: 768px) {{
            .article-content .container, .main-article, .content-body {{ padding-left: 18px; padding-right: 18px; }}
            .main-article h1 {{ font-size: clamp(26px, 8vw, 34px); }}
            .content-body h2 {{ font-size: clamp(22px, 6vw, 28px); }}
            .content-body h3 {{ font-size: clamp(18px, 5vw, 22px); }}
        }}
    </style>
</head>
<body>
    <header id="site-header"></header>
    <main class="article-content section-padding">
        <div class="container">
            <div class="breadcrumb">
                <a href="../" data-i18n="nav-home">Anasayfa</a> / <a href="../makaleler.html" data-i18n="nav-blog">Makaleler</a> / <span data-i18n="{categorySlug}">{category}</span>
            </div>
            <div class="article-layout">
                <article class="main-article">
                    <h1>{title}</h1>
                    <div class="meta-info">
                        <span><i data-lucide="calendar" style="width: 14px; vertical-align: middle;"></i> {date}</span>
                        <span><i data-lucide="user" style="width: 14px; vertical-align: middle;"></i> <span data-i18n="nav-corporate-brand">AV. AYŞENUR AVCI HUKUK BÜROSU</span></span>
                        <span><i data-lucide="tag" style="width: 14px; vertical-align: middle;"></i> <span data-i18n="{categorySlug}">{category}</span></span>
                    </div>
                    <div class="content-body">
{content_html}
                    </div>
                </article>
                <aside class="sidebar">
                    <div class="sidebar-widget">
                        <h4 data-i18n="contact-get-in-touch">Hemen İletişime Geçin</h4>
                        <p style="font-size: 13px; margin-bottom: 20px; color: #888;" data-i18n="contact-desc-short">Hukuki süreçleriniz için profesyonel danışmanlık alın.</p>
                        <a href="tel:+905535062125" class="btn-primary fill" style="display: block; text-align: center; padding: 15px;" data-i18n="contact-btn">TIKLA ARA</a>
                    </div>
                </aside>
            </div>
        </div>
    </main>
    <footer id="site-footer"></footer>
    <script src="../js/translations.js" defer></script>
    <script src="../js/site-config.js" defer></script>
    <script src="../js/main.js" defer></script>
    <script src="../js/schema.js" defer></script>
    <script src="../js/seo-links.js" defer></script>
</body>
</html>"""

# Data from site-config.js
articles = [
    {"title": "Anlaşmalı Boşanma Davası Nasıl Açılır? 2026 Rehberi", "category": "Aile Hukuku", "categorySlug": "aile-hukuku", "slug": "anlasmali-bosanma-davasi-nasil-acilir", "date": "27 Ocak 2026", "excerpt": "Anlaşmalı boşanma süreci, şartları ve gerekli belgeler hakkında Gebze boşanma avukatı perspektifiyle kapsamlı rehber.", "content": "Anlaşmalı boşanma, eşlerin boşanmanın tüm sonuçları üzerinde uzlaşarak evlilik birliğini sonlandırmasıdır..."},
    {"title": "Ağır Ceza Mahkemelerinde Savunma Stratejileri", "category": "Ceza Hukuku", "categorySlug": "ceza-hukuku", "slug": "agir-ceza-mahkemelerinde-savunma-stratejileri", "date": "25 Ocak 2026", "excerpt": "Kocaeli ağır ceza davalarında sanık hakları ve etkili savunma yöntemleri üzerine hukuki inceleme.", "content": "Ağır ceza yargılaması, telafisi güç sonuçlar doğurabilen ciddi bir süreçtir..."},
    {"title": "İşe İade Davası Açma Şartları ve Süreleri", "category": "İş Hukuku", "categorySlug": "is-hukuku", "slug": "ise-iade-davasi-acma-sartlari", "date": "20 Ocak 2026", "excerpt": "İş sözleşmesi haksız feshedilen işçinin işe iade davası açma süreci ve arabuluculuk aşaması.", "content": "7036 sayılı İş Mahkemeleri Kanunu uyarınca, işe iade talebiyle öncelikle arabulucuya başvurulmalıdır..."},
    {"title": "Kira Tahliye Davalarinda Yeni Dönem: Arabuluculuk", "category": "Gayrimenkul", "categorySlug": "gayrimenkul", "slug": "kira-tahliye-davalarinda-arabuluculuk", "date": "15 Ocak 2026", "excerpt": "Kira uyuşmazlıklarında zorunlu arabuluculuk süreci ve tahliye taahhütnamesinin geçerlilik şartları.", "content": "Gayrimenkul hukukunda kira tespit ve tahliye davaları Gebze bölgesinde oldukça yaygındır..."},
    {"title": "Siber Zorbalık ve Hukuki Boyutu", "category": "Bilişim & E-Ticaret", "categorySlug": "bilisim-e-ticaret", "slug": "siber-zorbalik-ve-hukuki-boyutu", "date": "28 Ocak 2026", "excerpt": "İnternet ortamında gerçekleştirilen taciz ve zorbalık eylemlerine karşı yasal haklarınız.", "content": "Siber zorbalık, dijital teknolojiler kullanılarak gerçekleştirilen saldırgan davranışlardır..."},
    {"title": "Sosyal Medya Üzerinden Hakaret Suçu", "category": "Bilişim & E-Ticaret", "categorySlug": "bilisim-e-ticaret", "slug": "sosyal-medya-uzerinden-hakaret-sucu", "date": "27 Ocak 2026", "excerpt": "Instagram, Twitter veya Facebook üzerinden edilen hakaretlerin cezai yaptırımları ve tazminat süreci.", "content": "Sosyal medya üzerinden hakaret, TCK 125. madde kapsamında düzenlenen bir suçtur..."},
    {"title": "Kripto Varlıkların Miras Hukukundaki Yeri", "category": "Bilişim & E-Ticaret", "categorySlug": "bilisim-e-ticaret", "slug": "kripto-varliklarin-miras-hukukundaki-yeri", "date": "26 Ocak 2026", "excerpt": "Bitcoin ve diğer kripto paraların mirasçılara intikali ve dijital tereke kavramı.", "content": "Dijital varlıkların miras yoluyla devri, güncel hukukun en çok tartışılan konularından biridir..."},
    {"title": "Meşru Müdafaa ve Sınırın Aşılması", "category": "Ceza Hukuku", "categorySlug": "ceza-hukuku", "slug": "mesru-mudafaa-ve-sinirin-asilmasi", "date": "25 Ocak 2026", "excerpt": "Nefsi müdafaa hangi şartlarda cezasızlık sağlar? Sınırın aşılması durumunda mahkeme kararları.", "content": "Meşru müdafaa, kendisine veya başkasına yönelen haksız bir saldırıyı defetmek amacıyla yapılan savunmadır..."},
    {"title": "Denetimli Serbestlik Şartları 2026", "category": "Ceza Hukuku", "categorySlug": "ceza-hukuku", "slug": "denetimli-serbestlik-sartlari-2026", "date": "24 Ocak 2026", "excerpt": "Yeni infaz düzenlemeleri sonrası denetimli serbestlik süreleri ve imza yükümlülükleri.", "content": "Denetimli serbestlik, hükümlünün cezasının bir kısmını toplum içinde denetim altında infaz etmesidir..."},
    {"title": "Trafik Kazası Sonrası Taksirle Yaralama", "category": "Ceza Hukuku", "categorySlug": "ceza-hukuku", "slug": "trafik-kazasi-sonrasi-taksirle-yaralama", "date": "23 Ocak 2026", "excerpt": "Ölümlü veya yaralamalı trafik kazalarında kusur durumu ve ceza davası süreci.", "content": "Trafik kazaları neticesinde meydana gelen yaralanmalar TCK 89 kapsamında değerlendirilir..."},
    {"title": "Nafaka Artırım Davası Nasıl Açılır?", "category": "Aile Hukuku", "categorySlug": "aile-hukuku", "slug": "nafaka-artirim-davasi-nasil-acilir", "date": "22 Ocak 2026", "excerpt": "Enflasyon ve değişen yaşam koşulları nedeniyle nafaka miktarının yeniden belirlenmesi.", "content": "Nafaka artırım davası, hükmedilen nafakanın yetersiz kalması durumunda açılır..."},
    {"title": "Yabancı Uyruklu Eşten Boşanma Süreci", "category": "Aile Hukuku", "categorySlug": "aile-hukuku", "slug": "yabanci-uyruklu-esten-bosanma-sureci", "date": "21 Ocak 2026", "excerpt": "Milletlerarası özel hukuk kapsamında yabancı eşle boşanma ve tebligat süreçleri.", "content": "Yabancı uyruklu kişilerle evli olan Türk vatandaşlarının boşanma davaları özel usullere tabidir..."},
    {"title": "Babalık Davası ve Soybağının Reddi", "category": "Aile Hukuku", "categorySlug": "aile-hukuku", "slug": "babalik-davasi-ve-soybaginin-reddi", "date": "20 Ocak 2026", "excerpt": "DNA testi ve hukuki karineler ışığında babalık ilişkisinin kurulması veya reddi.", "content": "Soybağının reddi davası, çocuk ile baba arasındaki hukuki bağın ortadan kaldırılmasını amaçlar..."},
    {"title": "Fazla Mesai Ücreti ve İspat Yükü", "category": "İş Hukuku", "categorySlug": "is-hukuku", "slug": "fazla-mesai-ucreti-ve-ispat-yuku", "date": "19 Ocak 2026", "excerpt": "Haftalık 45 saati aşan çalışmaların ücretlendirilmesi ve tanıkla ispat şartları.", "content": "Fazla çalışma ücreti, normal çalışma ücretinin %50 zamlı halidir..."},
    {"title": "Yıllık İzin Hakkı ve Kullanım Şartları", "category": "İş Hukuku", "categorySlug": "is-hukuku", "slug": "yillik-izin-hakki-ve-kullanim-sartlari", "date": "18 Ocak 2026", "excerpt": "İşçinin kıdemine göre yıllık ücretli izin süreleri ve bölünme kuralları.", "content": "İşçinin yıllık ücretli izin hakkı, işyerindeki kıdemine göre belirlenir ve vazgeçilemez bir haktır..."},
    {"title": "Kötüniyet Tazminatı Şartları", "category": "İş Hukuku", "categorySlug": "is-hukuku", "slug": "kotuniyet-tazminati-sartlari", "date": "17 Ocak 2026", "excerpt": "İş güvencesi kapsamında olmayan işçilerin fesih hakkının kötüye kullanılması durumu.", "content": "Kötüniyet tazminatı, belirsiz süreli iş sözleşmesinin dürüstlük kuralına aykırı feshinde ödenir..."},
    {"title": "Ecrimisil (Haksız İşgal Tazminatı) Davası", "category": "Gayrimenkul", "categorySlug": "gayrimenkul", "slug": "ecrimisil-haksiz-isgal-tazminati-davasi", "date": "16 Ocak 2026", "excerpt": "Bir taşınmazı izinsiz kullanan kişiye karşı açılan geçmişe dönük kullanım bedeli davası.", "content": "Ecrimisil, taşınmazın zilyetliğini haksız olarak elinde bulunduran kişiden talep edilen tazminattır..."},
    {"title": "Ortaklığın Giderilmesi (İzale-i Şuyu)", "category": "Gayrimenkul", "categorySlug": "gayrimenkul", "slug": "ortakligin-giderilmesi-izale-i-suyu", "date": "15 Ocak 2026", "excerpt": "Miras kalan veya paylı mülkiyete konu taşınmazların satış yoluyla paylaştırılması.", "content": "İzale-i şuyu davası, paylı veya elbirliği mülkiyetindeki ortaklığın sonlandırılmasıdır..."},
    {"title": "Maaş Haczi Oranı ve Hesaplaması", "category": "İcra İflas", "categorySlug": "icra-iflas", "slug": "maas-haczi-orani-ve-hesaplamasi", "date": "14 Ocak 2026", "excerpt": "Borçlunun maaşından yapılabilecek kesinti miktarı ve nafaka borçlarının önceliği.", "content": "İcra ve İflas Kanunu uyarınca, borçlunun maaşının en fazla 1/4'ü haczedilebilir..."},
    {"title": "İhtiyati Haciz Kararı Nasıl Alınır?", "category": "İcra İflas", "categorySlug": "icra-iflas", "slug": "ihtiyati-haciz-karari-nasil-alinir", "date": "13 Ocak 2026", "excerpt": "Alacağın tahsilini güvence altına almak için mahkemeden alınan geçici koruma kararı.", "content": "İhtiyati haciz, para alacaklarına ilişkin borçlunun mallarına geçici olarak el konulmasıdır..."},
    {"title": "Karşılıksız Çek Keşide Etme Suçu", "category": "İcra İflas", "categorySlug": "icra-iflas", "slug": "karsiliksiz-cek-keside-etme-sucu", "date": "12 Ocak 2026", "excerpt": "Çek kanunu uyarınca adli para cezası ve çek düzenleme yasağı süreçleri.", "content": "Karşılıksız çek düzenlemek, süresinde ibraz edilen çekin karşılığının bulunmaması durumunda oluşur..."},
    {"title": "KVKK Kapsamında Veri Sorumlusu", "category": "Bilişim & E-Ticaret", "categorySlug": "bilisim-e-ticaret", "slug": "kvkk-kapsaminda-veri-sorumlusu", "date": "11 Ocak 2026", "excerpt": "Kişisel verilerin işlenmesinde veri sorumlusunun idari ve teknik yükümlülükleri.", "content": "KVKK uyarınca veri sorumlusu, kişisel verilerin işleme amaçlarını ve vasıtalarını belirleyen kişidir..."},
    {"title": "İnternet Yoluyla Dolandırıcılık Suçu", "category": "Bilişim & E-Ticaret", "categorySlug": "bilisim-e-ticaret", "slug": "internet-yoluyla-dolandiricilik-sucu", "date": "10 Ocak 2026", "excerpt": "Oltalama (phishing) ve diğer digital yöntemlerle yapılan dolandırıcılık eylemleri.", "content": "Bilişim sistemlerinin araç olarak kullanılması suretiyle dolandırıcılık, nitelikli bir suçtur..."},
    {"title": "Velayet Davasında Uzman Görüşü", "category": "Aile Hukuku", "categorySlug": "aile-hukuku", "slug": "velayet-davasinda-uzman-gorusu", "date": "09 Ocak 2026", "excerpt": "Pedagog ve psikolog raporlarının velayet kararı üzerindeki belirleyici etkisi.", "content": "Mahkeme, velayet kararını vermeden önce sosyal inceleme raporu (SİR) alınmasına karar verir..."},
    {"title": "Kira Tespit Davasında 5 Yıl Kuralı", "category": "Gayrimenkul", "categorySlug": "gayrimenkul", "slug": "kira-testit-davasinda-5-yil-kurali", "date": "08 Ocak 2026", "excerpt": "Kira bedelinin emsal rayiçlere göre yeniden belirlenmesi için gereken yasal süre.", "content": "Kira sözleşmesinin üzerinden 5 yıl geçtikten sonra taraflar kira tespit davası açabilir..."},
    {"title": "Marka Tecavüzü ve Durdurulması", "category": "Bilişim & E-Ticaret", "categorySlug": "bilisim-e-ticaret", "slug": "marka-tecavuzu-ve-durdurulmasi", "date": "07 Ocak 2026", "excerpt": "Tescilli markanızın izinsiz kullanımı durumunda açılacak davalar ve tazminat hakları.", "content": "Marka hakkına tecavüz, tescilli bir markanın mal veya hizmetlerde izinsiz kullanılmasıdır..."},
    {"title": "Haksız Rekabet ve Men Davaları", "category": "Bilişim & E-Ticaret", "categorySlug": "bilisim-e-ticaret", "slug": "haksiz-reket-ve-men-davalari", "date": "06 Ocak 2026", "excerpt": "Ticari dürüstlük kurallarına aykırı davranışlara karşı hukuki koruma yolları.", "content": "Haksız rekabet, ekonomik rekabetin her türlü kötüye kullanılmasıdır..."},
    {"title": "Yanıltıcı Reklam ve Tüketici Hakları", "category": "Bilişim & E-Ticaret", "categorySlug": "bilisim-e-ticaret", "slug": "yaniltici-reklam-ve-tuketici-haklari", "date": "05 Ocak 2026", "excerpt": "Gerçeğe aykırı reklamlarla aldatılan tüketicilerin başvuru yolları ve şikayet süreci.", "content": "Tüketicileri aldatıcı, tecrübe ve bilgi noksanlıklarını istismar edici reklamlar yasaktır..."},
    {"title": "İnternet Servis Sağlayıcılarının Sorumluluğu", "category": "Bilişim & E-Ticaret", "categorySlug": "bilisim-e-ticaret", "slug": "internet-servis-saglayicilarinin-sorumlulugu", "date": "04 Ocak 2026", "excerpt": "Hukuka aykırı içeriklerin yayılmasında yer sağlayıcı ve erişim sağlayıcıların yükümlülükleri.", "content": "5651 sayılı Kanun uyarınca yer sağlayıcılar, içerikleri kontrol etmekle yükümlü değildir ancak..."},
    {"title": "Domain (Alan Adı) Uyuşmazlıkları", "category": "Bilişim & E-Ticaret", "categorySlug": "bilisim-e-ticaret", "slug": "domain-uyusmazliklari", "date": "03 Ocak 2026", "excerpt": "Marka ile çakışan alan adlarının iptali ve devri süreçlerinde WIPO ve TRABİS kuralları.", "content": "Alan adı uyuşmazlıkları, genellikle marka hakkı sahipleri ile alan adı tescil edenler arasında çıkar..."},
    {"title": "Yağma (Gasp) Suçu ve Cezası", "category": "Ceza Hukuku", "categorySlug": "ceza-hukuku", "slug": "yagma-gasp-sucu-ve-cezasi", "date": "02 Ocak 2026", "excerpt": "Cebir veya tehdit kullanılarak gerçekleştirilen mal varlığı suçlarında ağır ceza yargılaması.", "content": "Yağma suçu, bir başkasını kendisinin veya yakınının hayatına yönelik bir saldırı gerçekleştireceğinden bahisle..."},
    {"title": "Dolandırıcılık Suçunda Hile Unsuru", "category": "Ceza Hukuku", "categorySlug": "ceza-hukuku", "slug": "dolandiricilik-sucunda-hile-unsuru", "date": "01 Ocak 2026", "excerpt": "Basit ve nitelikli dolandırıcılık ayrımı ile mağdurun hatasından yararlanma durumları.", "content": "Dolandırıcılık suçu, hileli davranışlarla bir kimseyi aldatıp onun veya başkasının zararına olarak..."},
    {"title": "Güveni Kötüye Kullanma Suçu", "category": "Ceza Hukuku", "categorySlug": "ceza-hukuku", "slug": "guveni-kotuye-kullanma-sucu", "date": "31 Aralık 2025", "excerpt": "Zilyetliğin devredilmesi sonrası malın teslim amacı dışında kullanılması veya inkarı.", "content": "Muhafaza edilmek veya belirli bir şekilde kullanılmak üzere zilyetliği kendisine devredilmiş olan..."},
    {"title": "Özel Hayatın Gizliliğini İhlal", "category": "Ceza Hukuku", "categorySlug": "ceza-hukuku", "slug": "ozel-hayatin-gizliligini-ihlal", "date": "30 Aralık 2025", "excerpt": "Kişilerin gizli yaşam alanına müdahale, görüntü ve seslerin kayda alınması suçları.", "content": "Kişilerin özel hayatının gizliliğini ihlal eden kimse, bir yıldan üç yıla kadar hapis cezası ile..."},
    {"title": "İftira ve Suç Uydurma Suçları", "category": "Ceza Hukuku", "categorySlug": "ceza-hukuku", "slug": "iftira-ve-suc-uydurma-suclari", "date": "29 Aralık 2025", "excerpt": "Yetkili makamlara asılsız ihbar ve şikayetlerde bulunmanın cezai sonuçları.", "content": "İşlenmediğini bildiği bir suçu, yetkili makamlara işlenmiş gibi ihbar eden veya..."},
    {"title": "Boşanmada Maddi ve Manevi Tazminat", "category": "Aile Hukuku", "categorySlug": "aile-hukuku", "slug": "bosanmada-maddi-ve-manevi-tazminat", "date": "28 Aralık 2025", "excerpt": "Kusursuz veya daha az kusurlu eşin, boşanma nedeniyle uğradığı zararların tazmini.", "content": "Mevcut veya beklenen menfaatleri boşanma yüzünden haleldar olan kusursuz veya daha az kusurlu taraf..."},
    {"title": "Yoksulluk Nafakası Şartları", "category": "Aile Hukuku", "categorySlug": "aile-hukuku", "slug": "yoksulluk-nafakasi-sartlari", "date": "27 Aralık 2025", "excerpt": "Boşanma yüzünden yoksulluğa düşecek tarafın, diğer taraftan talep edebileceği süresiz nafaka.", "content": "Boşanma yüzünden yoksulluğa düşecek taraf, kusuru daha ağır olmamak koşuluyla geçimi için..."},
    {"title": "İştirak Nafakası ve Çocuk Giderleri", "category": "Aile Hukuku", "categorySlug": "aile-hukuku", "slug": "istirak-nafakasi-ve-cocuk-giderleri", "date": "26 Aralık 2025", "excerpt": "Velayeti kendisine verilmeyen eşin, çocuğun bakım ve eğitim giderlerine katılımı.", "content": "Velayetin kullanılması kendisine verilmeyen eş, çocuğun bakım ve eğitim giderlerine gücü oranında..."},
    {"title": "Evlat Edinme Şartları ve Usulü", "category": "Aile Hukuku", "categorySlug": "aile-hukuku", "slug": "evlat-edinme-sartlari-ve-usulu", "date": "25 Aralık 2025", "excerpt": "Küçüklerin ve erginlerin evlat edinilmesinde aranan yaş ve süre şartları.", "content": "Bir küçüğün evlat edinilmesi, evlat edinen tarafından bir yıl süreyle bakılmış ve eğitilmiş olması..."},
    {"title": "Tanıma ve Tenfiz Davaları", "category": "Aile Hukuku", "categorySlug": "aile-hukuku", "slug": "tanima-ve-tenfiz-davalari", "date": "24 Aralık 2025", "excerpt": "Yurt dışında verilen boşanma kararlarının Türkiye'de geçerli hale getirilmesi.", "content": "Yabancı bir mahkeme tarafından verilen ve o devlet kanunlarına göre kesinleşmiş olan ilamların..."},
    {"title": "Sendikal Tazminat ve Haklar", "category": "İş Hukuku", "categorySlug": "is-hukuku", "slug": "sendikal-tazminat-ve-haklar", "date": "23 Aralık 2025", "excerpt": "İşçinin sendikaya üye olması veya sendikal faaliyetlere katılması nedeniyle fesihte ödenecek tazminat.", "content": "İşçilerin sendikaya üye olmaları, işten çıkarılmaları için bir sebep oluşturamaz..."},
    {"title": "İşyeri Devri ve İşçi Hakları", "category": "İş Hukuku", "categorySlug": "is-hukuku", "slug": "isyeri-devri-ve-isci-haklari", "date": "22 Aralık 2025", "excerpt": "İşyerinin bir başka işverene devredilmesi durumunda kıdem tazminatı ve sözleşmelerin durumu.", "content": "İşyeri veya işyerinin bir bölümu hukuki bir işlemle başka birine devredildiğinde..."},
    {"title": "Engelli İşçi Çalıştırma Zorunluluğu", "category": "İş Hukuku", "categorySlug": "is-hukuku", "slug": "engelli-isci-calistirma-zorunlulugu", "date": "21 Aralık 2025", "excerpt": "50 ve üzeri işçi çalıştıran işyerlerinde engelli kontenjanı ve idari para cezaları.", "content": "İşverenler, elli veya daha fazla işçi çalıştırdıkları özel sektör işyerlerinde yüzde üç..."},
    {"title": "İş Sağlığı ve Güvenliği Yükümlülükleri", "category": "İş Hukuku", "categorySlug": "is-hukuku", "slug": "is-sagligi-ve-guvenligi-yukumlulukleri", "date": "20 Aralık 2025", "excerpt": "İşverenin iş kazalarını önlemek amacıyla alması gereken teknik ve idari tedbirler.", "content": "İşveren, çalışanların işle ilgili sağlık ve güvenliğini sağlamakla yükümlü olup bu çerçevede..."},
    {"title": "Arabuluculuk Anlaşma Belgesinin İptali", "category": "İş Hukuku", "categorySlug": "is-hukuku", "slug": "arabuluculuk-anlasma-belgesinin-iptali", "date": "19 Aralık 2025", "excerpt": "İrade fesadı (hata, hile, korkutma) durumunda arabuluculuk tutanaklarına karşı açılacak davalar.", "content": "Arabuluculuk faaliyeti sonunda düzenlenen anlaşma belgesi, ilam niteliğinde belge sayılır ancak..."},
    {"title": "Kat Karşılığı İnşaat Sözleşmeleri", "category": "Gayrimenkul", "categorySlug": "gayrimenkul", "slug": "kat-karsiligi-insaat-sozlesmeleri", "date": "18 Aralık 2025", "excerpt": "Arsa payı karşılığı inşaat sözleşmelerinde müteahhit ve arsa sahibinin hak ve borçları.", "content": "Arsa payı karşılığı inşaat sözleşmesi, arsa sahibinin arsasındaki belirli payların mülkiyetini..."},
    {"title": "Önalım (Şufa) Hakkı ve Kullanımı", "category": "Gayrimenkul", "categorySlug": "gayrimenkul", "slug": "onalim-sufa-hakki-ve-kullanimi", "date": "17 Aralık 2025", "excerpt": "Paylı mülkiyette bir paydaşın payını satması durumunda diğer paydaşların öncelikli satın alma hakkı.", "content": "Önalım hakkı, paylı mülkiyet hükümlerine tabi taşınmazlarda bir paydaşın taşınmaz üzerindeki payını..."},
    {"title": "Elatmanın Önlenmesi (Müdahalenin Men-i)", "category": "Gayrimenkul", "categorySlug": "gayrimenkul", "slug": "elatmanin-onlenmesi-mudahalenin-men-i", "date": "16 Aralık 2025", "excerpt": "Mülkiyet hakkına yönelik haksız saldırıların durdurulması için açılan dava türü.", "content": "Mülkiyet hakkı sahibi, hakkını haksız olarak elinden alan veya müdahale eden herkese karşı..."},
    {"title": "Geçit Hakkı Davaları", "category": "Gayrimenkul", "categorySlug": "gayrimenkul", "slug": "gecit-hakki-davalari", "date": "15 Aralık 2025", "excerpt": "Genel yola çıkışı bulunmayan taşınmazlar için komşu parsellerden yol hakkı talep edilmesi.", "content": "Taşınmazından genel yola çıkmak için yeterli geçidi bulunmayan malik, tam bir bedel karşılığında..."},
    {"title": "Tapu Kaydındaki Yanlışlıkların Düzeltilmesi", "category": "Gayrimenkul", "categorySlug": "gayrimenkul", "slug": "tapu-kaydindaki-yanlisliklarin-duzeltilmesi", "date": "14 Aralık 2025", "excerpt": "İsim, soyisim veya baba adı gibi kimlik bilgilerindeki hataların mahkeme yoluyla düzeltilmesi.", "content": "Tapu sicilindeki bilgilerin nüfus kayıtlarına uygun hale getirilmesi amacıyla açılan davalardır..."}
]

# Create blog directory if it doesn't exist
if not os.path.exists('blog'):
    os.makedirs('blog')

# Generate each article file
for article in articles:
    file_path = os.path.join('blog', f"{article['slug']}.html")
    content_html = build_seo_content(article, articles)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(template.format(**article, content_html=content_html))

print(f"Successfully generated {len(articles)} blog articles.")
subprocess.run(["python3", "generate_seo_assets.py"], check=False)
