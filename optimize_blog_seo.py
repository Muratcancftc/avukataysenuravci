#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blog makaleleri için SEO optimizasyonu:
1. Title (max 60 karakter) ve Meta Description (max 155 karakter) - Gebze, Darıca, Çayırova
2. FAQ Schema (3 soru) + SSS HTML bölümü
3. İç linkleme (2 link) + CTA (WhatsApp + Tazminat Hesaplama)
4. Görsel alt text (varsa)
5. Sitemap ve robots güncelleme
"""

import os
import re
import json
from pathlib import Path

BLOG_DIR = Path("blog")
BASE_URL = "https://avukataysenuravci.com"
LOCAL_KEYWORDS = ["Gebze", "Darıca", "Çayırova"]

# Kategori bazlı FAQ soruları (sokak ağzıyla)
FAQ_BY_CATEGORY = {
    "aile-hukuku": [
        ("Boşanmada tazminatımı nasıl söke söke alırım?", "Kusur oranına göre manevi tazminat talep edilir. Gebze Aile Mahkemesi'nde dava açarak haklarınızı koruyabilirsiniz. AV. AYŞENUR AVCI HUKUK BÜROSU danışmanlık sunmaktadır."),
        ("Nafaka ne kadar olur, Gebze'de nasıl hesaplanır?", "Gelir, gider ve çocuk sayısına göre belirlenir. Ücretsiz tazminat hesaplama aracımızla tahmini tutarı öğrenebilirsiniz."),
        ("Velayet için ne yapmam lazım, avukat şart mı?", "Çocuğun üstün yararı ispat edilmelidir. Avukat zorunlu değil ancak süreç karmaşıksa Gebze boşanma avukatı desteği önerilir."),
    ],
    "is-hukuku": [
        ("Tazminatımı nasıl söke söke alırım?", "Kıdem ve ihbar tazminatı için arabuluculuk sonrası İş Mahkemesi'ne dava. Gebze GOSB ve Çayırova lojistik bölgesinde yoğun başvuru alıyoruz."),
        ("Patron tazminat vermiyor, ne yapmalıyım?", "Önce arabuluculuk zorunlu. Anlaşmazlıkta 1 ay içinde İş Mahkemesi'ne dava. Delilleri toplayın, avukata başvurun."),
        ("Kıdem tazminatı 2026'da ne kadar, hesaplama var mı?", "Bakanlar Kurulu tavanı güncellenir. Ücretsiz kıdem tazminatı hesaplama aracımızla tahmini tutarı öğrenebilirsiniz."),
    ],
    "ceza-hukuku": [
        ("Gebze Adliyesi'nde dosyam var, avukat tutmalı mıyım?", "Ceza davalarında avukat hakkı vardır. Erken müdahale savunma stratejisi için kritiktir. Gebze ceza avukatı danışmanlığı alın."),
        ("İfadeye çağrıldım, gitmezsem ne olur?", "Celbe uymazsan zorla getirtme uygulanabilir. Avukat eşliğinde ifade vermeniz hak kaybını önler."),
        ("Sabıkam silinecek mi, ne kadar sürer?", "Suç türüne göre 5-15 yıl. Cumhuriyet Başsavcılığına başvuru. Gebze ve Darıca'dan yoğun talep alıyoruz."),
    ],
    "gayrimenkul": [
        ("Ev sahibi beni çıkarıyor, Gebze'de ne yapmalıyım?", "Tahliye için dava gerekir. Zorla çıkarma suç. Kira tespit davası açabilirsiniz. Hukuki danışmanlık alın."),
        ("Kira çok yükseldi, itiraz edebilir miyim?", "5 yıl dolunca kira tespit davası. Emsal rayiç belirlenir. Gebze, Darıca ve Çayırova'da kira davalarında tecrübeliyiz."),
        ("Tahliye taahhütnamesi imzaladım, başım yanar mı?", "Taahhüt geçerli olabilir. İrade sakatlığı ispatı zor. İmzalamadan önce avukata danışın."),
    ],
    "icra-iflas": [
        ("Maaşıma haciz geldi, ne kadar kesilir?", "Asgari ücretin 1/3'ü korunur. Haciz oranı hesaplama aracımızla öğrenebilirsiniz. İtiraz süresi 7 gün."),
        ("Borçtan hapse girer miyim?", "Nafaka ve özel borçlar dışında hapis yok. Mal beyanı, icra takibi. Gebze icra avukatı danışmanlığı."),
        ("Senet benim değil, nasıl kurtulurum?", "7 gün içinde itiraz. İtirazın iptali davası. Grafolog, imza incelemesi. Hemen avukata başvurun."),
    ],
    "bilisim-e-ticaret": [
        ("İnternetten dolandırıldım, paramı alabilir miyim?", "Suç duyurusu + tazminat davası. Banka ve platform bilgisi talep. Gebze ve Çayırova'dan bilişim suçları başvurusu alıyoruz."),
        ("Sosyal medyada hakaret ettiler, dava açabilir miyim?", "Cumhuriyet Başsavcılığına suç duyurusu. Şikayete bağlı. Ekran görüntüsü, noter onayı delil."),
        ("KVKK ihlali var, şikayet nereye?", "Kişisel Verileri Koruma Kurumu. Tazminat davası. Veri sorumlusuna başvuru. Gebze KOBİ'lerine KVKK uyum danışmanlığı."),
    ],
}

# Varsayılan FAQ (kategori eşleşmezse)
DEFAULT_FAQ = [
    ("Gebze ve çevresinde avukata ne zaman başvurmalıyım?", "Hukuki uyuşmazlık çıktığı anda, süre sınırı olan davalarda (işe iade 1 ay vb.) en kısa sürede Gebze avukat ile görüşün."),
    ("Ücretsiz danışmanlık alabilir miyim?", "Birçok Gebze avukat ofisi ilk görüşmede ücretsiz ön danışmanlık sunar. AV. AYŞENUR AVCI HUKUK BÜROSU da ücretsiz ön görüşme imkânı vermektedir."),
    ("Darıca ve Çayırova'dan da hizmet alabilir miyim?", "Evet. AV. AYŞENUR AVCI HUKUK BÜROSU Gebze merkezli olarak Kocaeli, Darıca, Çayırova ve İstanbul Anadolu Yakası'na hizmet vermektedir."),
]

# Slug -> (SEO title, meta description) - 60 ve 155 karakter
def gen_seo_meta(slug, title, excerpt, category_slug):
    """Gebze, Darıca, Çayırova ile SEO meta üret."""
    loc = "Gebze" if "gebze" in slug or "kidem" in slug else ("Darıca" if "trafik" in slug or "kaza" in slug else "Çayırova")
    if "Gebze" not in title and "Darıca" not in title and "Çayırova" not in title:
        title_opt = f"{title} | {loc} Avukat"
    else:
        title_opt = title
    if len(title_opt) > 58:
        title_opt = title_opt[:55] + "..."
    if len(title_opt) > 60:
        title_opt = title_opt[:57] + "..."
    
    desc = excerpt or title
    if loc not in desc:
        desc = f"{loc} avukat: {desc}"
    if len(desc) > 152:
        desc = desc[:149] + "..."
    if len(desc) > 155:
        desc = desc[:152] + "..."
    
    return title_opt, desc

# Slug -> ilgili 2 makale (iç link)
def get_related_links(slug, all_slugs, category_slug):
    """Konuya göre 2 ilgili makale döndür."""
    related = []
    cat_articles = [s for s in all_slugs if s != slug]
    # Aynı kategoriden veya benzer konulardan seç
    priority = {
        "aile-hukuku": ["bosanmada-maddi-ve-manevi-tazminat", "nafaka-artirim-davasi-nasil-acilir", "velayet-davasinda-uzman-gorusu", "anlasmali-bosanma-davasi-nasil-acilir"],
        "is-hukuku": ["gebze-kidem-tazminati-hesaplama-2026", "ise-iade-davasi-acma-sartlari", "fazla-mesai-ucreti-ve-ispat-yuku", "mobbing-nedeniyle-manevi-tazminat-miktari"],
        "ceza-hukuku": ["agir-ceza-mahkemelerinde-savunma-stratejileri", "denetimli-serbestlik-sartlari-2026", "adli-sicil-kaydinin-sabika-silinmesi"],
        "gayrimenkul": ["kira-tespit-davasinda-5-yil-kurali", "kira-tahliye-davalarinda-arabuluculuk", "ortakligin-giderilmesi-izale-i-suyu", "ecrimisil-haksiz-isgal-tazminati-davasi"],
        "icra-iflas": ["maas-haczi-orani-ve-hesaplamasi", "icra-takibine-itiraz-ve-itirazin-iptali", "e-haciz-ve-banka-blokesi-kaldirma"],
        "bilisim-e-ticaret": ["internet-yoluyla-dolandiricilik-sucu", "kvkk-kapsaminda-veri-sorumlusu", "sosyal-medya-hakaret-santaj-suclari"],
    }
    pool = priority.get(category_slug, []) + list(cat_articles)
    seen = {slug}
    for s in pool:
        if s not in seen and (BLOG_DIR / f"{s}.html").exists():
            seen.add(s)
            related.append(s)
            if len(related) >= 2:
                break
    return related[:2]

# İç link anchor metinleri
ANCHOR_MAP = {
    "bosanmada-maddi-ve-manevi-tazminat": "boşanmada tazminat",
    "nafaka-artirim-davasi-nasil-acilir": "nafaka artırım davası",
    "velayet-davasinda-uzman-gorusu": "velayet davası",
    "anlasmali-bosanma-davasi-nasil-acilir": "anlaşmalı boşanma",
    "gebze-kidem-tazminati-hesaplama-2026": "kıdem tazminatı hesaplama",
    "ise-iade-davasi-acma-sartlari": "işe iade davası",
    "fazla-mesai-ucreti-ve-ispat-yuku": "fazla mesai ücreti",
    "mobbing-nedeniyle-manevi-tazminat-miktari": "mobbing tazminatı",
    "agir-ceza-mahkemelerinde-savunma-stratejileri": "ceza savunması",
    "denetimli-serbestlik-sartlari-2026": "denetimli serbestlik",
    "adli-sicil-kaydinin-sabika-silinmesi": "sabıka silme",
    "kira-tespit-davasinda-5-yil-kurali": "kira tespit davası",
    "kira-tahliye-davalarinda-arabuluculuk": "kira tahliye arabuluculuk",
    "ortakligin-giderilmesi-izale-i-suyu": "izale-i şuyu",
    "ecrimisil-haksiz-isgal-tazminati-davasi": "ecrimisil davası",
    "maas-haczi-orani-ve-hesaplamasi": "maaş haczi oranı",
    "icra-takibine-itiraz-ve-itirazin-iptali": "icra itiraz",
    "e-haciz-ve-banka-blokesi-kaldirma": "banka blokesi kaldırma",
    "internet-yoluyla-dolandiricilik-sucu": "internet dolandırıcılığı",
    "kvkk-kapsaminda-veri-sorumlusu": "KVKK veri sorumlusu",
    "sosyal-medya-hakaret-santaj-suclari": "sosyal medya hakaret",
}

def get_anchor(slug):
    return ANCHOR_MAP.get(slug, slug.replace("-", " ").title())

# CTA HTML
CTA_HTML = '''
<div class="article-cta-block" style="background:#111;border:1px solid var(--border-gold);border-radius:8px;padding:40px;margin:40px 0;text-align:center;">
    <h3 style="color:var(--matte-gold);margin-bottom:15px;">Gebze ve çevresinde hukuki destek için AV. AYŞENUR AVCI HUKUK BÜROSU ile iletişime geçin</h3>
    <p style="color:#888;margin-bottom:25px;">Darıca, Çayırova ve Kocaeli genelinde profesyonel avukatlık hizmeti.</p>
    <div style="display:flex;gap:15px;justify-content:center;flex-wrap:wrap;">
        <a href="https://wa.me/905535062125" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:8px;padding:15px 25px;background:#25D366;color:#fff;text-decoration:none;font-weight:600;border-radius:6px;"><i data-lucide="message-circle" style="width:20px;height:20px;"></i> WhatsApp&apos;tan Yazın</a>
        <a href="../araclar.html" style="display:inline-flex;align-items:center;gap:8px;padding:15px 25px;background:transparent;border:1px solid var(--matte-gold);color:var(--matte-gold);text-decoration:none;font-weight:600;border-radius:6px;"><i data-lucide="calculator" style="width:20px;height:20px;"></i> Tazminat Hesaplama Aracı</a>
    </div>
</div>
'''

def extract_from_html(html):
    """HTML'den title, meta description, h1, content-body çıkar."""
    title = re.search(r'<title>([^<]+)</title>', html)
    meta = re.search(r'<meta name="description" content="([^"]*)"', html)
    h1 = re.search(r'<h1[^>]*>([^<]+)</h1>', html)
    return {
        "title": title.group(1).replace(" | AV. AYŞENUR AVCI HUKUK BÜROSU", "").strip() if title else "",
        "meta": meta.group(1) if meta else "",
        "h1": h1.group(1) if h1 else "",
    }

def get_category_from_breadcrumb(html, slug=""):
    # data-i18n="categorySlug" breadcrumb'ta
    m = re.search(r'breadcrumb.*?data-i18n="([a-z0-9-]+)"', html, re.DOTALL)
    if m:
        val = m.group(1)
        if val in FAQ_BY_CATEGORY:
            return val
    m = re.search(r'breadcrumb[^>]*>.*?<span[^>]*>([^<]+)</span>', html, re.DOTALL)
    if m:
        span = m.group(1).strip()
        cat_map = {"Aile Hukuku": "aile-hukuku", "İş Hukuku": "is-hukuku", "Ceza Hukuku": "ceza-hukuku",
                   "Gayrimenkul": "gayrimenkul", "İcra İflas": "icra-iflas", "Bilişim & E-Ticaret": "bilisim-e-ticaret"}
        return cat_map.get(span, "aile-hukuku")
    # Slug bazlı fallback
    slug_cat = {"kidem": "is-hukuku", "ise-iade": "is-hukuku", "mobbing": "is-hukuku", "bosanma": "aile-hukuku",
                "nafaka": "aile-hukuku", "velayet": "aile-hukuku", "kira": "gayrimenkul", "tahliye": "gayrimenkul",
                "icra": "icra-iflas", "haciz": "icra-iflas", "ceza": "ceza-hukuku", "dolandiricilik": "bilisim-e-ticaret",
                "kvkk": "bilisim-e-ticaret", "internet": "bilisim-e-ticaret", "siber": "bilisim-e-ticaret"}
    for k, v in slug_cat.items():
        if k in slug:
            return v
    return "aile-hukuku"

def build_faq_schema(faq_list):
    main = []
    for q, a in faq_list:
        main.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": main
    }, ensure_ascii=False)

def build_faq_html(faq_list):
    items = []
    for q, a in faq_list:
        items.append(f'<div class="faq-article-item" style="margin-bottom:25px;"><h4 style="color:var(--matte-gold);font-size:16px;margin-bottom:8px;">{q}</h4><p style="color:#ccc;line-height:1.6;">{a}</p></div>')
    return f'''
<h2 style="color:var(--matte-gold);margin:40px 0 20px;">Sıkça Sorulan Sorular</h2>
<div class="article-faq-list">
{chr(10).join(items)}
</div>
'''

def add_internal_links(content_body, links, slug):
    """İlk paragrafa veya uygun yere 2 iç link ekle."""
    if not links:
        return content_body
    anchor1 = get_anchor(links[0])
    anchor2 = get_anchor(links[1]) if len(links) > 1 else get_anchor(links[0])
    link1 = f'<a href="{links[0]}.html">{anchor1}</a>'
    link2 = f'<a href="{links[1]}.html">{anchor2}</a>' if len(links) > 1 else link1
    
    # İlk <p> içine doğal bir cümle ekle
    insert = f' Bu konuda <strong>{link1}</strong> ve <strong>{link2}</strong> makalelerimizi de inceleyebilirsiniz.'
    
    # İlk p etiketinin kapanışından hemen önce ekle (içerik varsa)
    first_p = re.search(r'(<p[^>]*>)(.*?)(</p>)', content_body, re.DOTALL)
    if first_p and len(first_p.group(2)) > 50:
        old = first_p.group(0)
        new = first_p.group(1) + first_p.group(2).rstrip() + insert + first_p.group(3)
        content_body = content_body.replace(old, new, 1)
    return content_body

def process_article(filepath, all_slugs):
    slug = filepath.stem
    html = filepath.read_text(encoding="utf-8")
    info = extract_from_html(html)
    category = get_category_from_breadcrumb(html, slug)
    
    title_seo, meta_seo = gen_seo_meta(slug, info["h1"] or info["title"], info["meta"], category)
    faq_list = FAQ_BY_CATEGORY.get(category, DEFAULT_FAQ)
    related = get_related_links(slug, all_slugs, category)
    
    # 1. Title ve meta güncelle
    html = re.sub(r'<title>[^<]+</title>', f'<title>{title_seo} | AV. AYŞENUR AVCI HUKUK BÜROSU</title>', html)
    html = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{meta_seo}"', html, count=1)
    
    # 2. FAQ Schema head'e ekle (</head> öncesi)
    faq_schema = f'<script type="application/ld+json">{build_faq_schema(faq_list)}</script>'
    if 'FAQPage' not in html and 'application/ld+json' in html:
        html = html.replace('</head>', faq_schema + '\n</head>')
    elif 'FAQPage' not in html:
        html = html.replace('</head>', faq_schema + '\n</head>')
    
    # 3. Content-body içine: iç linkler + FAQ + CTA
    content_body_match = re.search(r'(<div class="content-body">)(.*?)(</div>\s*</article>)', html, re.DOTALL)
    if content_body_match:
        content_body = content_body_match.group(2)
        
        # İç link ekle (ilk paragrafa)
        content_body = add_internal_links(content_body, related, slug)
        
        # FAQ ve CTA ekle - content-body sonuna
        if "article-faq-list" not in content_body and "Sıkça Sorulan" not in content_body:
            content_body = content_body + build_faq_html(faq_list)
        if "article-cta-block" not in content_body:
            content_body = content_body + CTA_HTML
        
        html = html[:content_body_match.start(2)] + content_body + html[content_body_match.end(2):]
    
    # 4. Görsel alt text - alt yoksa ekle
    def add_alt(m):
        tag = m.group(0)
        if 'alt=' not in tag.lower():
            return tag.replace('<img', '<img alt="Gebze Avukat AV. AYŞENUR AVCI HUKUK BÜROSU - Hukuki Danışmanlık"')
        return tag
    html = re.sub(r'<img[^>]*>', add_alt, html)
    
    filepath.write_text(html, encoding="utf-8")
    return slug

def update_sitemap(blog_files):
    """sitemap.xml'deki blog URL'lerini güncelle."""
    sitemap_path = Path("sitemap.xml")
    if not sitemap_path.exists():
        return
    content = sitemap_path.read_text(encoding="utf-8")
    
    # Mevcut blog url'leri kaldır (tek satırda olan)
    content = re.sub(r'\s*<url><loc>https://[^/]+/blog/[^<]+</loc><changefreq>[^<]+</changefreq><priority>[^<]+</priority></url>', '', content)
    
    # </urlset> hemen öncesine blog url'leri ekle
    blog_urls = [f'  <url><loc>{BASE_URL}/blog/{f.stem}.html</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>' for f in sorted(blog_files)]
    insert = '\n' + '\n'.join(blog_urls) + '\n'
    content = content.replace('</urlset>', insert + '</urlset>')
    sitemap_path.write_text(content, encoding="utf-8")

def update_robots():
    """robots.txt güncelle."""
    robots = Path("robots.txt")
    if not robots.exists():
        robots.write_text(f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
""", encoding="utf-8")
    else:
        content = robots.read_text(encoding="utf-8")
        if "Sitemap:" not in content:
            content = content.strip() + f"\n\nSitemap: {BASE_URL}/sitemap.xml\n"
            robots.write_text(content, encoding="utf-8")

def main():
    blog_files = list(BLOG_DIR.glob("*.html"))
    all_slugs = [f.stem for f in blog_files]
    
    print(f"Toplam {len(blog_files)} makale işleniyor...")
    for f in blog_files:
        try:
            process_article(f, all_slugs)
            print(f"  OK: {f.stem}")
        except Exception as e:
            print(f"  HATA {f.stem}: {e}")
    
    update_sitemap(blog_files)
    update_robots()
    print("\nSitemap ve robots.txt güncellendi.")
    print("SEO optimizasyonu tamamlandı.")

if __name__ == "__main__":
    main()
