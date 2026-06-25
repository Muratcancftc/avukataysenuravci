import os
import subprocess

# Define the template for blog articles
template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | AV. AYŞENUR AVCI HUKUK BÜROSU</title>
    <meta name="description" content="{excerpt}">
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
        .main-article h1 {{ font-size: 42px; color: var(--matte-gold); margin-bottom: 20px; line-height: 1.2; }}
        .meta-info {{ display: flex; gap: 20px; margin-bottom: 40px; padding-bottom: 20px; border-bottom: 1px solid var(--border-white); font-size: 13px; color: #666; }}
        .content-body {{ font-size: 18px; line-height: 1.8; color: #ccc; }}
        .content-body h2 {{ color: var(--matte-gold); margin: 40px 0 20px; }}
        .sidebar {{ position: sticky; top: 120px; height: fit-content; }}
        .sidebar-widget {{ background: #121212; border: 1px solid var(--border-white); padding: 25px; margin-bottom: 30px; border-radius: 8px; }}
        .sidebar-widget h4 {{ color: var(--matte-gold); margin-bottom: 20px; font-size: 16px; border-bottom: 1px solid var(--border-gold); padding-bottom: 10px; }}
        @media (max-width: 992px) {{ .article-layout {{ grid-template-columns: 1fr; }} .sidebar {{ position: static; }} }}
    </style>
</head>
<body>
    <header id="site-header"></header>
    <main class="article-content section-padding">
        <div class="container">
            <div class="breadcrumb">
                <a href="../">Anasayfa</a> / <a href="../makaleler.html">Makaleler</a> / <span>{category}</span>
            </div>
            <div class="article-layout">
                <article class="main-article">
                    <h1>{title}</h1>
                    <div class="meta-info">
                        <span><i data-lucide="calendar" style="width: 14px; vertical-align: middle;"></i> {date}</span>
                        <span><i data-lucide="user" style="width: 14px; vertical-align: middle;"></i> AV. AYŞENUR AVCI HUKUK BÜROSU</span>
                        <span><i data-lucide="tag" style="width: 14px; vertical-align: middle;"></i> {category}</span>
                    </div>
                    <div class="content-body">
                        <p>{content}</p>
                        <h2>Hukuki İnceleme ve Detaylar</h2>
                        <p>{excerpt} Bu konuda daha fazla bilgi ve hukuki danışmanlık için Gebze'deki ofisimizle iletişime geçebilirsiniz. Hukuki süreçlerin takibi uzmanlık gerektirir ve hak kaybına uğramamanız için profesyonel destek almanız önerilir.</p>
                        <p>Türk hukuk sisteminde süreler ve usul kuralları davanın kaderini belirler. Bu nedenle, makalemizde yer alan genel bilgiler somut olayınıza göre farklılık gösterebilir.</p>
                    </div>
                </article>
                <aside class="sidebar">
                    <div class="sidebar-widget">
                        <h4>Hemen İletişime Geçin</h4>
                        <p style="font-size: 13px; margin-bottom: 20px; color: #888;">Hukuki süreçleriniz için profesyonel danışmanlık alın.</p>
                        <a href="tel:+905535062125" class="btn-primary" style="display: block; text-align: center; padding: 15px;">TIKLA ARA</a>
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

# Data from site-config.js (the new 25 articles)
new_articles = [
    {"title": "Kripto Para Dolandırıcılığı ve Hukuki Yollar", "category": "Bilişim & E-Ticaret", "slug": "kripto-para-dolandiriciligi-ve-hukuki-yollar", "date": "13 Aralık 2025", "excerpt": "Borsa vurgunları, soğuk cüzdan hırsızlıkları ve sahte yatırım platformlarına karşı izlenecek yollar.", "content": "Kripto varlık ekosisteminde yaşanan dolandırıcılık vakaları, bilişim hukukunun en karmaşık alanlarından biridir..."},
    {"title": "NFT Eserlerin Telif Hakları", "category": "Bilişim & E-Ticaret", "slug": "nft-eserlerin-telif-haklari", "date": "12 Aralık 2025", "excerpt": "Dijital sanat eserlerinin mülkiyeti ile telif hakkı arasındaki farklar ve akıllı sözleşmelerin hukuki niteliği.", "content": "NFT (Non-Fungible Token), bir varlığın dijital sertifikası niteliğinde olup, telif haklarını otomatik olarak devretmez..."},
    {"title": "Uzaktan Çalışma Yönetmeliği ve Haklar", "category": "İş Hukuku", "slug": "uzaktan-calisma-yonetmeligi-ve-haklar", "date": "11 Aralık 2025", "excerpt": "Home-office çalışan işçilerin yemek, yol ve internet giderleri ile mesai saatlerinin düzenlenmesi.", "content": "Pandemi sonrası kalıcı hale gelen uzaktan çalışma modeli, İş Kanunu'na eklenen yeni yönetmeliklerle düzenlenmiştir..."},
    {"title": "Mobbing Nedeniyle Manevi Tazminat Miktarı", "category": "İş Hukuku", "slug": "mobbing-nedeniyle-manevi-tazminat-miktari", "date": "10 Aralık 2025", "excerpt": "Yargıtay'ın mobbing davalarında hükmettiği tazminat miktarları ve ispatta kullanılan delil türleri.", "content": "Psikolojik taciz (mobbing), işçinin kişilik haklarını ağır şekilde ihlal eden bir eylemdir..."},
    {"title": "Konut Dokunulmazlığının İhlali Suçu", "category": "Ceza Hukuku", "slug": "konut-dokunulmazliginin-ihlali-sucu", "date": "09 Aralık 2025", "excerpt": "Bir kimsenin konutuna rızası dışında girilmesi veya çıkılmaması durumunda öngörülen cezalar.", "content": "Konut dokunulmazlığı, anayasal bir hak olup TCK 116. maddesi ile koruma altına alınmıştır..."},
    {"title": "Cinsel Taciz Suçu ve Şikayet Süresi", "category": "Ceza Hukuku", "slug": "cinsel-taciz-sucu-ve-sikayet-suresi", "date": "08 Aralık 2025", "excerpt": "Bedensel temas olmaksızın gerçekleştirilen cinsel içerikli davranışların cezai boyutu.", "content": "Cinsel taciz suçu, mağdurun cinsel dokunulmazlığının ihlali boyutuna varmayan eylemleri kapsar..."},
    {"title": "Mal Rejiminin Tasfiyesinde Değer Artış Payı", "category": "Aile Hukuku", "slug": "mal-rejiminin-tasfiyesinde-deger-artis-payi", "date": "07 Aralık 2025", "excerpt": "Eşlerden birinin diğerine ait malın edinilmesine veya iyileştirilmesine yaptığı katkının geri alınması.", "content": "Değer artış payı alacağı, katkı payı alacağından farklı olarak malın tasfiye tarihindeki değeri üzerinden hesaplanır..."},
    {"title": "Soyadı Değiştirme Davası Şartları", "category": "Aile Hukuku", "slug": "soyadi-degistirme-davasi-sartlari", "date": "06 Aralık 2025", "excerpt": "Haklı nedenlerin varlığı halinde (komik, çirkin, kötü tanınan) soyadının değiştirilmesi süreci.", "content": "Kişi, haklı bir nedene dayanarak adının veya soyadının değiştirilmesini hakimden isteyebilir..."},
    {"title": "Yabancıların Türkiye'de Taşınmaz Edinimi", "category": "Gayrimenkul", "slug": "yabancilarin-turkiyede-tasinmaz-edinimi", "date": "05 Aralık 2025", "excerpt": "Mütekabiliyet ilkesi ve askeri yasak bölgeler kapsamında yabancı uyrukluların gayrimenkul alım satımı.", "content": "Yabancı uyruklu gerçek kişilerin Türkiye'de taşınmaz edinimi Tapu Kanunu'nun 35. maddesi ile düzenlenmiştir..."},
    {"title": "İpoteğin Fekki (Kaldırılması) Davası", "category": "Gayrimenkul", "slug": "ipotegin-fekki-kaldirilmasi-davasi", "date": "04 Aralık 2025", "excerpt": "Borcu ödenmiş olmasına rağmen kaldırılmayan banka veya şahıs ipoteklerinin mahkemece silinmesi.", "content": "İpotek, bir borcun teminatı olarak taşınmaz üzerinde kurulan bir haktır. Borç sona erdiğinde..."},
    {"title": "E-Haciz ve Banka Blokesi Kaldırma", "category": "İcra İflas", "slug": "e-haciz-ve-banka-blokesi-kaldirma", "date": "03 Aralık 2025", "excerpt": "Vergi dairesi veya icra müdürlüğü tarafından konulan elektronik hacizlere itiraz ve çözüm yolları.", "content": "E-haciz, borçlunun banka hesaplarındaki varlıklara sistem üzerinden anlık olarak el konulmasıdır..."},
    {"title": "İstihkak Davasında İspat Kriterleri", "category": "İcra İflas", "slug": "istihkak-davasinda-ispat-kriterleri", "date": "02 Aralık 2025", "excerpt": "Haczedilen malın borçluya değil, üçüncü bir kişiye ait olduğunun kanıtlanması süreci.", "content": "İstihkak davası, mülkiyet hakkı ihlal edilen üçüncü kişilerin haklarını koruyan bir yoldur..."},
    {"title": "Kişisel Verilerin Yurt Dışına Aktarımı", "category": "Bilişim & E-Ticaret", "slug": "kisisel-verilerin-yurt-disina-aktarimi", "date": "01 Aralık 2025", "excerpt": "KVKK madde 9 uyarınca güvenli ülkeler ve standart sözleşme hükümleri çerçevesinde veri transferi.", "content": "Kişisel verilerin yurt dışına aktarılması, ilgili kişinin açık rızası veya Kurul'un izni ile mümkündür..."},
    {"title": "İnternet Bankacılığı Dolandırıcılığı", "category": "Bilişim & E-Ticaret", "slug": "internet-bankaciligi-dolandiriciligi", "date": "30 Kasım 2025", "excerpt": "Sim kart bloke, oltalama ve zararlı yazılımlarla boşaltılan banka hesaplarında bankanın sorumluluğu.", "content": "Bankalar, müşterilerinin hesap güvenliğini sağlamakla yükümlü olup, hafif kusurlarından dahi sorumludur..."},
    {"title": "Hükmün Açıklanmasının Geri Bırakılması (HAGB)", "category": "Ceza Hukuku", "slug": "hukmun-aciklanmasinin-geri-birakilmasi-hagb", "date": "29 Kasım 2025", "excerpt": "2 yıl ve altındaki hapis cezalarında sanığın 5 yıl süreyle denetime tabi tutulması ve sonuçları.", "content": "HAGB kararı, sanığın suçlu olduğunu tespit etmekle birlikte, belirli şartlarla hükmün sonuç doğurmamasıdır..."},
    {"title": "Adli Sicil Kaydının (Sabıka) Silinmesi", "category": "Ceza Hukuku", "slug": "adli-sicil-kaydinin-sabika-silinmesi", "date": "28 Kasım 2025", "excerpt": "Cezanın infazından sonra arşiv kaydına alınan bilgilerin silinme süreleri ve başvuru usulü.", "content": "Adli sicil kaydı, kişinin mahkumiyet bilgilerinin tutulduğu sistemdir. Belirli sürelerin geçmesiyle..."},
    {"title": "Boşanmada Eşin Kusur Oranının Tespiti", "category": "Aile Hukuku", "slug": "bosanmada-esin-kusur-oraninin-tespiti", "date": "27 Kasım 2025", "excerpt": "Tazminat ve nafaka miktarını belirleyen en önemli unsur olan kusur araştırmasında emsal kararlar.", "content": "Boşanma davalarında hakim, tarafların birbirine karşı olan davranışlarını kusur ölçeğinde değerlendirir..."},
    {"title": "Geçici Velayet ve Kişisel İlişki Tesisi", "category": "Aile Hukuku", "slug": "gecici-velayet-ve-kisisel-iliski-tesisi", "date": "26 Kasım 2025", "excerpt": "Dava süresince çocuğun kimin yanında kalacağına dair verilen ara kararlar ve görüşme günleri.", "content": "Boşanma davası açıldığında hakim, çocuğun barınma ve bakımına ilişkin geçici önlemleri resen alır..."},
    {"title": "İş Sözleşmesinde Rekabet Yasağı Kaydı", "category": "İş Hukuku", "slug": "is-sozlesmesinde-rekabet-yasagi-kaydi", "date": "25 Kasım 2025", "excerpt": "İşten ayrılan personelin rakip firmada çalışmasını engelleyen maddelerin geçerlilik sınırları.", "content": "Rekabet yasağı kaydı, işçinin işverenin müşteri portföyüne veya ticari sırlarına erişimi varsa geçerlidir..."},
    {"title": "Yıpranma Payı ve Fiili Hizmet Süresi", "category": "İş Hukuku", "slug": "yipranma-payi-ve-fiili-hizmet-suresi", "date": "24 Kasım 2025", "excerpt": "Ağır ve tehlikeli işlerde çalışanların erken emeklilik hakları ve SGK prim hesaplamaları.", "content": "Fiili hizmet süresi zammı, belirli iş kollarında çalışan sigortalılara sağlanan ek prim günüdür..."},
    {"title": "Kat Mülkiyeti Kanunu ve Aidat Borçları", "category": "Gayrimenkul", "slug": "kat-mulkiyeti-kanunu-ve-aidat-borclari", "date": "23 Kasım 2025", "excerpt": "Apartman ve site yönetimlerinde ödenmeyen aidatların icra takibi ve gecikme tazminatı.", "content": "Aidat borcunu ödemeyen kat malikine karşı yönetim planı ve KMK uyarınca icra takibi başlatılabilir..."},
    {"title": "Ön Alım Hakkından Feragat ve Vazgeçme", "category": "Gayrimenkul", "slug": "on-alim-hakkindan-feragat-ve-vazgecme", "date": "22 Kasım 2025", "excerpt": "Hisseli tapularda şufa hakkının kullanılmaması için noterden yapılan feragatnamelerin önemi.", "content": "Önalım hakkından feragat, belirli bir satış için veya genel olarak yapılabilir..."},
    {"title": "Yedieminlik Görevi ve Sorumlulukları", "category": "İcra İflas", "slug": "yedieminlik-gorevi-ve-sorumluluklari", "date": "21 Kasım 2025", "excerpt": "Haczedilen malların muhafazası için atanan yedieminlerin hukuki ve cezai yükümlülükleri.", "content": "Yediemin, kendisine teslim edilen malı aynen muhafaza etmek ve istendiğinde iade etmekle yükümlüdür..."},
    {"title": "İcra Takibine İtiraz ve İtirazın İptali", "category": "İcra İflas", "slug": "icra-takibine-itiraz-ve-itirazin-iptali", "date": "20 Kasım 2025", "excerpt": "Borca veya imzaya yapılan itirazların durdurduğu takibin mahkeme yoluyla devam ettirilmesi.", "content": "İlamsız icra takibine yapılan itiraz takibi durdurur. Alacaklı, takibi devam ettirmek için..."},
    {"title": "Dijital Miras ve Sosyal Medya Hesapları", "category": "Bilişim & E-Ticaret", "slug": "dijital-miras-ve-sosyal-medya-hesaplari", "date": "19 Kasım 2025", "excerpt": "Vefat eden kişinin Facebook, Instagram ve e-posta hesaplarının mirasçılara devri.", "content": "Dijital miras, kişinin internet ortamındaki tüm mal varlığı ve anılarını kapsayan yeni bir hukuk alanıdır..."}
]

# Generate each article file
for article in new_articles:
    file_path = os.path.join('blog', f"{article['slug']}.html")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(template.format(**article))

print(f"Successfully generated {len(new_articles)} new blog articles.")
subprocess.run(["python3", "generate_seo_assets.py"], check=False)
