#!/usr/bin/env python3
"""Generate 5 trending 2026 Gebze-focused SEO blog articles."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://avukataysenuravci.com"
DATE = "26 Haziran 2026"

FAVICON_HEAD = """    <link rel="icon" href="/favicon.ico" sizes="48x48">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
    <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
    <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="apple-touch-icon" sizes="180x180" href="/favicon-180.png">
    <link rel="manifest" href="/site.webmanifest">"""

ARTICLE_STYLE = """
        .article-content { padding-top: 150px; }
        .breadcrumb { margin-bottom: 30px; font-size: 12px; color: var(--text-gray); text-transform: uppercase; letter-spacing: 1px; }
        .breadcrumb a:hover { color: var(--matte-gold); }
        .article-layout { display: grid; grid-template-columns: 1fr 300px; gap: 60px; }
        .main-article h1 { font-size: 42px; color: var(--matte-gold); margin-bottom: 20px; line-height: 1.2; }
        .meta-info { display: flex; gap: 20px; margin-bottom: 40px; padding-bottom: 20px; border-bottom: 1px solid var(--border-white); font-size: 13px; color: #666; flex-wrap: wrap; }
        .content-body { font-size: 18px; line-height: 1.8; color: #ccc; }
        .content-body h2 { color: var(--matte-gold); margin: 40px 0 20px; font-size: 28px; }
        .content-body h3 { color: #fff; margin: 30px 0 15px; font-size: 20px; }
        .content-body p { margin-bottom: 20px; }
        .content-body ul { margin: 0 0 20px 20px; color: #ccc; }
        .content-body li { margin-bottom: 8px; }
        .sidebar { position: sticky; top: 120px; height: fit-content; }
        .sidebar-widget { background: #121212; border: 1px solid var(--border-white); padding: 25px; margin-bottom: 30px; border-radius: 8px; }
        .sidebar-widget h4 { color: var(--matte-gold); margin-bottom: 20px; font-size: 16px; border-bottom: 1px solid var(--border-gold); padding-bottom: 10px; }
        @media (max-width: 992px) { .article-layout { grid-template-columns: 1fr; } .sidebar { position: static; } }
"""

ARTICLES = [
    {
        "slug": "gebze-12-yargi-paketi-bosanma-davalari-2026",
        "title": "Gebze'de 12. Yargı Paketi ve Çekişmeli Boşanma Davaları (2026)",
        "meta_title": "Gebze 12. Yargı Paketi Boşanma Davası 2026 | AV. AYŞENUR AVCI",
        "category": "Aile Hukuku",
        "category_slug": "aile-hukuku",
        "description": "Gebze boşanma avukatı rehberi: 12. Yargı Paketi ile çekişmeli boşanmada iki aşamalı yargılama, velayet ve mal paylaşımı süreçleri 2026.",
        "keywords": "Gebze boşanma avukatı, 12. yargı paketi, çekişmeli boşanma 2026, Gebze aile mahkemesi",
        "faq": [
            ("12. Yargı Paketi Gebze'deki boşanma davalarını nasıl etkiler?", "Çekişmeli boşanmada önce boşanma ve velayet kararı verilip kesinleşebilir; nafaka ve mal paylaşımı ayrı dava olarak görülebilir."),
            ("Gebze'de boşanma davası hangi mahkemede açılır?", "Gebze Adliyesi bünyesindeki Kocaeli Aile Mahkemeleri görevli ve yetkilidir."),
            ("Anlaşmalı boşanma bu paketten etkilenir mi?", "Anlaşmalı boşanma protokolü ile tek celsede sonuçlanma imkânı devam eder; paket özellikle çekişmeli dosyaları hedefler."),
        ],
        "body": """
<h2>12. Yargı Paketi Nedir ve Neden Gündemde?</h2>
<p>2026 yılında TBMM Adalet Komisyonu'nda kabul edilen <strong>12. Yargı Paketi</strong>, yargılamaları hızlandırmayı amaçlayan kapsamlı bir reform paketidir. Özellikle <strong>çekişmeli boşanma davalarında</strong> yıllarca süren süreçler, tarafların yeni hayat kurmasını zorlaştırmaktadır. Paket ile <strong>iki aşamalı yargılama modeli</strong> gündeme gelmiştir: ilk aşamada boşanma ve velayet kararı verilir; nafaka ve mal paylaşımı gibi mali konular ayrı davada görülür.</p>
<p><strong>Gebze boşanma avukatı</strong> desteği ile bu değişiklikleri dosyanıza özel değerlendirmek, hak kaybı riskini azaltır. Gebze, Darıca, Çayırova ve Kocaeli genelinde aile hukuku dosyalarında AV. AYŞENUR AVCI HUKUK BÜROSU olarak müvekkillerimize güncel mevzuat takibi sunuyoruz.</p>

<h2>Gebze'de Çekişmeli Boşanma Süreci Nasıl İşler?</h2>
<p>Gebze Adliyesi'nde açılan boşanma davalarında zorunlu <strong>arabuluculuk</strong> aşaması tamamlanmadan dava açılamaz. Çekişmeli dosyalarda kusur tespiti, delil toplama ve SİR (sosyal inceleme raporu) süreçleri kritik öneme sahiptir. Yeni paket ile boşanma kararının mali taleplerden ayrılması planlandığından, <strong>Gebze aile mahkemesi</strong> pratiğinde dosya stratejisi yeniden planlanmalıdır.</p>

<h3>İki Aşamalı Yargılamanın Avantajları</h3>
<ul>
<li>Boşanma kararının daha hızlı kesinleşmesi</li>
<li>Velayet konusunda erken netlik</li>
<li>Mal paylaşımının ayrı ve detaylı incelenmesi</li>
<li>Mahkeme iş yükünün dengelenmesi</li>
</ul>

<h2>Gebze Boşanma Avukatı ile Doğru Strateji</h2>
<p>Reform sürecinde mevzuat henüz tam yürürlüğe girmemiş olsa bile, dava dilekçesi, protokol hazırlığı ve delil planı bugünden yapılmalıdır. <a href="anlasmali-bosanma-davasi-nasil-acilir.html" title="Anlaşmalı Boşanma Davası Rehberi">Anlaşmalı boşanma</a> imkânı varsa süreç haftalar içinde sonuçlanabilir. Çekişmeli dosyalarda ise <a href="velayet-davasinda-uzman-gorusu.html" title="Velayet Davasında Uzman Görüşü">velayet stratejisi</a> ve <a href="nafaka-artirim-azaltim-davalari-2026.html" title="Nafaka Artırım Azaltım Davaları 2026">nafaka talepleri</a> ayrı ayrı ele alınmalıdır.</p>

<h2>Resmi Kaynaklar</h2>
<p><a href="https://gebze.adalet.gov.tr/" target="_blank" rel="noopener" title="Gebze Adliyesi">Gebze Adliyesi</a>, <a href="https://www.mevzuat.gov.tr/" target="_blank" rel="noopener" title="T.C. Mevzuat">Türk Medeni Kanunu</a> ve <a href="https://www.tbmm.gov.tr/" target="_blank" rel="noopener" title="TBMM">TBMM yasa süreçleri</a> düzenli takip edilmelidir.</p>

<h2>Sıkça Sorulan Sorular</h2>
""",
    },
    {
        "slug": "gebze-aym-suresiz-nafaka-karari-2026",
        "title": "AYM Süresiz Nafaka Kararı: Gebze'de Boşanma Sonrası Ne Değişir? (2026)",
        "meta_title": "Gebze Yoksulluk Nafakası AYM Kararı 2026 | Boşanma Avukatı",
        "category": "Aile Hukuku",
        "category_slug": "aile-hukuku",
        "description": "Anayasa Mahkemesi süresiz yoksulluk nafakası iptali sonrası Gebze boşanma davalarında nafaka süresi, miktarı ve yeniden düzenleme rehberi 2026.",
        "keywords": "Gebze nafaka avukatı, süresiz nafaka iptali, AYM kararı 2026, yoksulluk nafakası Gebze",
        "faq": [
            ("AYM kararı süresiz nafakayı tamamen kaldırdı mı?", "Hayır. Yoksulluk nafakası hakkı devam eder; ancak süresiz uygulamaya imkân tanıyan ifade iptal edilmiştir."),
            ("Gebze'de nafaka azaltım davası açılabilir mi?", "Koşullar değiştiğinde nafaka artırım veya azaltım davası açılabilir."),
            ("Karar ne zaman yürürlüğe girer?", "AYM iptal kararları genellikle Resmi Gazete'de yayımlandıktan sonra dokuz ay içinde yürürlüğe girer."),
        ],
        "body": """
<h2>Anayasa Mahkemesi Kararının Özeti</h2>
<p>Haziran 2026'da <strong>Anayasa Mahkemesi (AYM)</strong>, Türk Medeni Kanunu'nun 175. maddesindeki <strong>süresiz yoksulluk nafakası</strong> düzenlemesini iptal etmiştir. Karar, boşanma sonrası nafaka tartışmalarını yeniden gündeme taşımıştır. <strong>Gebze boşanma avukatı</strong> ile süreci takip etmek, özellikle devam eden veya yeni açılacak dosyalarda kritik önem taşır.</p>
<p>İptal kararı, nafaka hakkını tamamen ortadan kaldırmaz; yoksulluğa düşen tarafın talep hakkı korunur. Ancak <strong>belirsiz süreyle sürdürülen nafaka</strong> uygulaması mevzuat değişikliği ile yeniden şekillenecektir.</p>

<h2>Gebze Aile Mahkemesi'nde Nafaka Davaları</h2>
<p>Gebze Adliyesi'nde görülen boşanma dosyalarında yoksulluk nafakası, iştirak nafakası ve tedbir nafakası talepleri ayrı değerlendirilir. AYM kararı sonrası mevcut kesinleşmiş kararların durumu, yeni düzenleme yürürlüğe girene kadar tartışma konusudur. <strong>Gebze nafaka avukatı</strong> desteği ile dosyanızın güncel içtihata uygun yönetilmesi gerekir.</p>

<h3>Nafaka Türleri ve Gebze Pratiği</h3>
<ul>
<li><strong>Yoksulluk nafakası:</strong> Boşanma sonrası ekonomik yoksunluğu giderir</li>
<li><strong>İştirak nafakası:</strong> Çocuğun giderlerine katkı</li>
<li><strong>Tedbir nafakası:</strong> Dava süresince geçici ödeme</li>
</ul>

<h2>Gebze'de Nafaka Artırım ve Azaltım</h2>
<p>Koşulların değişmesi halinde <a href="nafaka-artirim-azaltim-davalari-2026.html" title="Nafaka Artırım Azaltım Davaları">nafaka artırım veya azaltım davası</a> açılabilir. Enflasyon, gelir değişikliği ve yeniden evlenme gibi hususlar değerlendirilir. <a href="yoksulluk-nafakasi-sartlari.html" title="Yoksulluk Nafakası Şartları">Yoksulluk nafakası şartları</a> makalemizi de inceleyebilirsiniz.</p>

<h2>Resmi Kaynaklar</h2>
<p><a href="https://www.anayasa.gov.tr/" target="_blank" rel="noopener" title="Anayasa Mahkemesi">Anayasa Mahkemesi</a>, <a href="https://www.resmigazete.gov.tr/" target="_blank" rel="noopener" title="Resmi Gazete">Resmi Gazete</a> ve <a href="https://www.yargitay.gov.tr/" target="_blank" rel="noopener" title="Yargıtay">Yargıtay aile hukuku kararları</a> takip edilmelidir.</p>

<h2>Sıkça Sorulan Sorular</h2>
""",
    },
    {
        "slug": "gebze-iban-magdurlari-ceza-sorumlulugu-2026",
        "title": "IBAN Mağdurları ve Hesap Kiralama Suçu: Gebze Ceza Avukatı Rehberi (2026)",
        "meta_title": "Gebze IBAN Mağduru Ceza Avukatı 2026 | Hesap Kiralama",
        "category": "Ceza Hukuku",
        "category_slug": "ceza-hukuku",
        "description": "12. Yargı Paketi ile IBAN mağdurları ve hesap kiralama suçlarında Gebze ceza avukatı rehberi: savunma, ceza indirimi ve delil toplama 2026.",
        "keywords": "Gebze ceza avukatı, IBAN mağduru, hesap kiralama suçu, dolandırıcılık savunması Gebze",
        "faq": [
            ("IBAN'ımı paylaştım, suçlu muyum?", "Hesabınızın dolandırıcılıkta kullanılması durumunda iştirak veya yardım suçlamasıyla karşılaşabilirsiniz; savunma stratejisi önemlidir."),
            ("12. Yargı Paketi cezayı düşürür mü?", "Paket, hesap kiralama fiilinin daha hafif çerçevede değerlendirilmesine yönelik düzenleme içerir."),
            ("Gebze'de ifade avukatı ne zaman gerekir?", "Kolluk veya savcılık ifadesinden önce avukat desteği alınması hak kaybını önler."),
        ],
        "body": """
<h2>IBAN Mağdurları Kimlerdir?</h2>
<p>Son yıllarda artan <strong>dolandırıcılık</strong> vakalarında, mağdurların banka hesap bilgilerini (IBAN) üçüncü kişilerle paylaşması sonucu <strong>hesap kiralama</strong> olarak adlandırılan fiiller gündeme gelmiştir. 12. Yargı Paketi ile TCK 158. madde kapsamında bu fiillerin <strong>daha hafif çerçevede değerlendirilmesi</strong> öngörülmektedir. <strong>Gebze ceza avukatı</strong> ile erken aşamada savunma planı yapmak, adli süreçte kritik öneme sahiptir.</p>

<h2>Gebze Adliyesi'nde Ceza Soruşturması Süreci</h2>
<p>Gebze Cumhuriyet Başsavcılığı'na yapılan şikayetler sonrası soruşturma aşamasında ifade, dijital delil incelemesi ve tutuklama talepleri gündeme gelebilir. Nitelikli dolandırıcılık davalarının bir kısmının <strong>asliye ceza mahkemesine</strong> devredilmesi de paket kapsamındadır. Bu değişiklik, yargılama süresini ve mahkeme görevini doğrudan etkiler.</p>

<h3>İlk 24 Saatte Yapılması Gerekenler</h3>
<ul>
<li>Avukat ile iletişime geçmek</li>
<li>Banka hareketlerini ve mesaj kayıtlarını saklamak</li>
<li>İfade öncesi hukuki danışmanlık almak</li>
<li>Mağduriyet iddiasını belgelemek</li>
</ul>

<h2>Gebze Ceza Avukatı Savunma Stratejileri</h2>
<p>Kastın bulunmaması, ikna edilme, ekonomik zorlanma ve fiilin niteliği savunmada öne çıkar. <a href="internet-bankaciligi-dolandiriciligi.html" title="İnternet Bankacılığı Dolandırıcılığı">İnternet bankacılığı dolandırıcılığı</a> ve <a href="gebze-siber-dolandiricilik-dava-sureci.html" title="Gebze Siber Dolandırıcılık">siber dolandırıcılık</a> makalelerimizle birlikte değerlendirilmelidir.</p>

<h2>Resmi Kaynaklar</h2>
<p><a href="https://gebze.adalet.gov.tr/" target="_blank" rel="noopener" title="Gebze Adliyesi">Gebze Adliyesi</a>, <a href="https://www.mevzuat.gov.tr/" target="_blank" rel="noopener" title="TCK Mevzuat">Türk Ceza Kanunu</a> ve <a href="https://www.kocaelibarosu.org.tr/" target="_blank" rel="noopener" title="Kocaeli Barosu">Kocaeli Barosu</a>.</p>

<h2>Sıkça Sorulan Sorular</h2>
""",
    },
    {
        "slug": "gebze-kidem-tazminati-tavani-2026",
        "title": "Gebze Kıdem Tazminatı Tavanı 2026: Güncel Hesaplama Rehberi",
        "meta_title": "Gebze Kıdem Tazminatı Tavanı 2026 (64.948 TL) | İş Avukatı",
        "category": "İş Hukuku",
        "category_slug": "is-hukuku",
        "description": "2026 kıdem tazminatı tavanı 64.948,77 TL. Gebze iş hukuku avukatı ile kıdem, ihbar ve işçi alacakları hesaplama rehberi GOSB ve sanayi bölgesi.",
        "keywords": "Gebze kıdem tazminatı, kıdem tavanı 2026, Gebze iş avukatı, GOSB iş hukuku",
        "faq": [
            ("2026 kıdem tazminatı tavanı ne kadar?", "1 Ocak – 30 Haziran 2026 dönemi için brüt tavan 64.948,77 TL'dir."),
            ("Gebze GOSB'de işten çıkışta nelere dikkat edilmeli?", "İbraname, kıdem-ihbar hesabı ve SGK çıkış kodu mutlaka kontrol edilmelidir."),
            ("Tavan üstü maaşta ne olur?", "Her çalışma yılı için hesaplama tavanı aşamaz; fazla ücret dikkate alınmaz."),
        ],
        "body": """
<h2>2026 Kıdem Tazminatı Tavanı Açıklandı</h2>
<p>Hazine ve Maliye Bakanlığı'nın 6 Ocak 2026 tarihli genelgesi ile <strong>kıdem tazminatı tavanı</strong> belirlenmiştir. 1 Ocak – 30 Haziran 2026 döneminde geçerli <strong>brüt tavan 64.948,77 TL</strong>'dir. Gebze, Darıca, Çayırova ve <strong>GOSB</strong> bölgesindeki işçiler için bu tutar, işten ayrılış maliyetini doğrudan etkiler.</p>
<p><strong>Gebze iş hukuku avukatı</strong> desteği ile kıdem, ihbar, yıllık izin ve fazla mesai alacaklarınızın eksiksiz hesaplanması sağlanır.</p>

<h2>Kıdem Tazminatı Nasıl Hesaplanır?</h2>
<p>1475 sayılı İş Kanunu'na göre, en az bir yıl çalışan işçiye her tam yıl için <strong>30 günlük giydirilmiş brüt ücret</strong> ödenir. Ücret tavanı aşsa bile ödeme tavanı geçemez. Kıdem hakkı; emeklilik, işveren feshi, askerlik, evlilik (kadın işçi) ve ölüm gibi hallerde doğar.</p>

<h3>Gebze'de Sık Yapılan Hatalar</h3>
<ul>
<li>İbranamede feragat ifadesi bulunması</li>
<li>Yıllık izin ve fazla mesai alacağının düşülmesi</li>
<li>Kıdem süresinin eksik hesaplanması</li>
<li>SGK çıkış kodunun hatalı seçilmesi</li>
</ul>

<h2>Gebze İş Davası ve Arabuluculuk</h2>
<p>Kıdem alacağı uyuşmazlıklarında <strong>zorunlu arabuluculuk</strong> şarttır. Anlaşma sağlanamazsa Gebze İş Mahkemesi'nde dava açılır. <a href="gebze-is-hukuku-kidem-tazminati.html" title="Gebze İş Hukuku Kıdem Tazminatı">kıdem tazminatı rehberimizi</a> ve <a href="gebze-kidem-tazminati-hesaplama-2026.html" title="Kıdem Tazminatı Hesaplama 2026">hesaplama makalemizi</a> inceleyebilirsiniz.</p>

<h2>Resmi Kaynaklar</h2>
<p><a href="https://www.resmigazete.gov.tr/" target="_blank" rel="noopener" title="Resmi Gazete">Resmi Gazete</a>, <a href="https://www.mevzuat.gov.tr/" target="_blank" rel="noopener" title="İş Kanunu">İş Kanunu</a> ve <a href="https://www.sgk.gov.tr/" target="_blank" rel="noopener" title="SGK">SGK</a>.</p>

<h2>Sıkça Sorulan Sorular</h2>
""",
    },
    {
        "slug": "gebze-kira-artis-orani-2026",
        "title": "Gebze Kira Artış Oranı 2026: Kiracı ve Ev Sahibi Hakları Rehberi",
        "meta_title": "Gebze Kira Artış Oranı 2026 | Kira Avukatı Rehberi",
        "category": "Gayrimenkul",
        "category_slug": "gayrimenkul",
        "description": "2026 Gebze kira artış oranı, TÜFE sınırı, kira tespit ve tahliye davalarında kiracı-ev sahibi hakları. Gebze gayrimenkul avukatı rehberi.",
        "keywords": "Gebze kira artış oranı 2026, kira tespit davası Gebze, tahliye avukatı Gebze",
        "faq": [
            ("2026'da kira ne kadar artırılabilir?", "Konut kiralarda 12 aylık TÜFE ortalaması yasal üst sınır olarak uygulanır; aşım geçersizdir."),
            ("Gebze'de kira tespit davası ne işe yarar?", "Emsal kira bedelinin mahkemece belirlenmesini sağlar."),
            ("Tahliye davası açılabilir mi?", "Yasal şartlar ve süreler sağlanmadan tahliye talebi risklidir."),
        ],
        "body": """
<h2>2026 Kira Artış Oranı Nasıl Belirlenir?</h2>
<p>Konut kira sözleşmelerinde yıllık artış oranı, <strong>TÜİK'in açıkladığı 12 aylık TÜFE ortalaması</strong> ile sınırlıdır. 2026 yılında kiracı ve ev sahipleri arasındaki uyuşmazlıklar, Gebze'de yoğun nüfus ve sanayi bölgesi konut talebi nedeniyle artmaktadır. <strong>Gebze gayrimenkul avukatı</strong> desteği ile kira bedeli, artış oranı ve tahliye süreçlerini hukuka uygun yönetebilirsiniz.</p>

<h2>Gebze'de Kira Tespit ve Tahliye Davaları</h2>
<p>Kira bedelinin piyasa rayicinin altında veya üstünde olduğu iddialarında <strong>kira tespit davası</strong> açılabilir. Tahliye için ise sözleşme süresi, ihtar ve yasal sebepler bir arada değerlendirilir. <a href="kira-artis-oranlari-tahliye-davalari-2026.html" title="Kira Artış Oranları Tahliye 2026">Kira artış ve tahliye rehberimizi</a> inceleyebilirsiniz.</p>

<h3>Kiracıların Bilmesi Gerekenler</h3>
<ul>
<li>Sözleşmedeki artış oranı TÜFE'yi aşamaz</li>
<li>Ödenen fazla kira geri istenebilir</li>
<li>Keyfi tahliye tehdidine karşı hukuki koruma vardır</li>
<li>Arabuluculuk bazı uyuşmazlıklarda zorunludur</li>
</ul>

<h3>Ev Sahiplerinin Hakları</h3>
<ul>
<li>Yasal sınırdaki artışı talep etme</li>
<li>Süre bitiminde yenileme koşulları</li>
<li>Kira tespit ile emsal rayic belirleme</li>
<li>Usulüne uygun tahliye davası açma</li>
</ul>

<h2>Gebze Gayrimenkul Avukatı Desteği</h2>
<p><a href="gebze-kira-tahliye-dava-sureci-rehberi.html" title="Gebze Kira Tahliye Dava Süreci">Kira tahliye süreci</a> ve <a href="kira-tespit-davasi-emsal-rayic.html" title="Kira Tespit Davası Emsal Rayiç">emsal rayiç</a> konularında Gebze Adliyesi'nde dosya takibi yapıyoruz.</p>

<h2>Resmi Kaynaklar</h2>
<p><a href="https://www.tuik.gov.tr/" target="_blank" rel="noopener" title="TÜİK">TÜİK enflasyon verileri</a>, <a href="https://www.mevzuat.gov.tr/" target="_blank" rel="noopener" title="Borçlar Kanunu">Borçlar Kanunu</a> ve <a href="https://gebze.adalet.gov.tr/" target="_blank" rel="noopener" title="Gebze Adliyesi">Gebze Adliyesi</a>.</p>

<h2>Sıkça Sorulan Sorular</h2>
""",
    },
]


def faq_html(items: list[tuple[str, str]]) -> str:
    blocks = []
    for q, a in items:
        blocks.append(
            f'<div class="faq-article-item" style="margin-bottom:25px;">'
            f'<h4 style="color:var(--matte-gold);font-size:16px;margin-bottom:8px;">{q}</h4>'
            f'<p style="color:#ccc;line-height:1.6;">{a}</p></div>'
        )
    return "\n".join(blocks)


def faq_schema(items: list[tuple[str, str]]) -> str:
    entities = []
    for q, a in items:
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        })
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}, ensure_ascii=False)


def render_article(article: dict) -> str:
    slug = article["slug"]
    canonical = f"{SITE}/blog/{slug}.html"
    faq_block = faq_html(article["faq"])
    body = article["body"].strip() + "\n" + faq_block

    cta = f"""
<div class="article-cta-block" style="background:#111;border:1px solid var(--border-gold);border-radius:8px;padding:40px;margin:40px 0;text-align:center;">
    <h3 style="color:var(--matte-gold);margin-bottom:15px;">Gebze'de Hukuki Danışmanlık</h3>
    <p style="color:#888;margin-bottom:25px;">AV. AYŞENUR AVCI HUKUK BÜROSU — Gebze ve Kocaeli bölgesinde profesyonel avukatlık hizmeti.</p>
    <div style="display:flex;gap:15px;justify-content:center;flex-wrap:wrap;">
        <a href="https://wa.me/905535062125" target="_blank" rel="noopener" title="WhatsApp ile iletişim" style="display:inline-flex;align-items:center;gap:8px;padding:15px 25px;background:#25D366;color:#fff;text-decoration:none;font-weight:600;border-radius:6px;">WhatsApp'tan Yazın</a>
        <a href="../iletisim.html" title="Gebze hukuk bürosu iletişim" style="display:inline-flex;align-items:center;gap:8px;padding:15px 25px;background:transparent;border:1px solid var(--matte-gold);color:var(--matte-gold);text-decoration:none;font-weight:600;border-radius:6px;">İletişime Geçin</a>
    </div>
</div>
<p><em>Bu makale bilgilendirme amaçlıdır. Hukuki danışmanlık için bir avukat ile görüşünüz.</em></p>
"""

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
{FAVICON_HEAD}
    <title>{article['meta_title']}</title>
    <meta name="description" content="{article['description']}">
    <meta name="author" content="AV. AYŞENUR AVCI HUKUK BÜROSU">
    <meta property="og:title" content="{article['meta_title']}">
    <meta property="og:description" content="{article['description']}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="{SITE}/images/logo-icon-512.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="{SITE}/images/logo-icon-512.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest" defer></script>
    <link rel="stylesheet" href="../css/style.min.css">
    <style>{ARTICLE_STYLE}</style>
    <script type="application/ld+json">{faq_schema(article['faq'])}</script>
    <link rel="canonical" href="{canonical}">
</head>
<body>
    <header id="site-header"></header>
    <main class="article-content section-padding">
        <div class="container">
            <div class="breadcrumb">
                <a href="/" title="Anasayfa">Anasayfa</a> / <a href="../makaleler.html" title="Hukuk makaleleri">Makaleler</a> / <span>{article['category']}</span>
            </div>
            <div class="article-layout">
                <article class="main-article">
                    <h1>{article['title']}</h1>
                    <div class="meta-info">
                        <span><i data-lucide="calendar" style="width: 14px; vertical-align: middle;"></i> {DATE}</span>
                        <span><i data-lucide="user" style="width: 14px; vertical-align: middle;"></i> AV. AYŞENUR AVCI HUKUK BÜROSU</span>
                        <span><i data-lucide="tag" style="width: 14px; vertical-align: middle;"></i> {article['keywords']}</span>
                    </div>
                    <div class="content-body">
{body}
{cta}
                    </div>
                </article>
                <aside class="sidebar">
                    <div class="sidebar-widget">
                        <h4>Hemen İletişime Geçin</h4>
                        <p style="font-size: 13px; margin-bottom: 20px; color: #888;">Gebze'de hukuki danışmanlık için bize ulaşın.</p>
                        <a href="tel:+905535062125" class="btn-primary fill" title="Gebze avukat telefon" style="display: block; text-align: center; padding: 15px;">TIKLA ARA</a>
                    </div>
                </aside>
            </div>
        </div>
    </main>
    <footer id="site-footer"></footer>
    <script defer src="../js/translations.js"></script>
    <script defer src="../js/site-config.js"></script>
    <script defer src="../js/main.js"></script>
    <script defer src="../js/schema.js"></script>
    <script defer src="../js/seo-links.js"></script>
</body>
</html>
"""


def update_site_config(articles_meta: list[dict]) -> None:
    path = ROOT / "js/site-config.js"
    text = path.read_text(encoding="utf-8")
    entries = []
    next_id = 128
    for i, a in enumerate(articles_meta):
        entries.append(
            f"""    {{
        id: {next_id - i},
        title: "{a['title']}",
        category: "{a['category']}",
        categorySlug: "{a['category_slug']}",
        slug: "{a['slug']}",
        excerpt: "{a['description'][:120]}",
        date: "{DATE}",
        content: "{a['description'][:80]}"
    }}"""
        )
    block = ",\n".join(entries) + ",\n"
    text, n = re.subn(r"(const articles = \[\n)", r"\1" + block, text, count=1)
    if n != 1:
        raise RuntimeError("Could not insert articles into site-config.js")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    blog_dir = ROOT / "blog"
    meta = []
    for article in ARTICLES:
        out = blog_dir / f"{article['slug']}.html"
        out.write_text(render_article(article), encoding="utf-8")
        meta.append(article)
        print("wrote", out.name)
    update_site_config(meta)
    print("updated site-config.js")


if __name__ == "__main__":
    main()
