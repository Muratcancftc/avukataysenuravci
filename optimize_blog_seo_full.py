#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teknik SEO: Tüm makaleleri standartlara göre yeniden düzenler.
1. URL/Slug: Türkçe karaktersiz, küçük harf, tire, anahtar kelime odaklı
2. Başlık hiyerarşisi: H1, H2, H3, H4 + Gebze/Darıca/Çayırova
3. Meta: Title 60 char, Description 155 char
4. İçerik: İlk 100 kelimede anahtar kelime, bold, paragraf bölme, listeler
5. İç linkleme (2) + CTA (WhatsApp + İletişim Formu)
6. Görsel alt text
7. HTML dosyası olarak kaydet
"""

import re
import json
from pathlib import Path

BLOG_DIR = Path("blog")
BASE_URL = "https://avukataysenuravci.com.tr"
LOCAL_KEYWORDS = ["Gebze", "Darıca", "Çayırova"]

# Slug düzeltmeleri (typo vb.)
SLUG_FIXES = {"kira-testit-davasinda-5-yil-kurali": "kira-tespit-davasinda-5-yil-kurali"}

# Slug -> anahtar kelime (ilk 100 kelimede kullanılacak)
def get_main_keyword(slug, category):
    kw_map = {
        "kidem": "kıdem tazminatı", "ise-iade": "işe iade", "bosanma": "boşanma",
        "nafaka": "nafaka", "kira": "kira", "tahliye": "tahliye", "icra": "icra",
        "haciz": "maaş haczi", "ceza": "ceza avukatı", "mobbing": "mobbing",
        "velayet": "velayet", "dolandiricilik": "dolandırıcılık", "kvkk": "KVKK",
    }
    for k, v in kw_map.items():
        if k in slug:
            return v
    return "Gebze avukat"

# CTA - WhatsApp + İletişim Formu
CTA_HTML = '''
<div class="article-cta-block" style="background:#111;border:1px solid var(--border-gold);border-radius:8px;padding:40px;margin:40px 0;text-align:center;">
    <h3 style="color:var(--matte-gold);margin-bottom:15px;">Ücretsiz Ön Görüşme İçin Hemen İletişime Geçin</h3>
    <p style="color:#888;margin-bottom:25px;">Gebze, Darıca ve Çayırova&apos;da profesyonel hukuki danışmanlık. AV. AYŞENUR AVCI HUKUK BÜROSU.</p>
    <div style="display:flex;gap:15px;justify-content:center;flex-wrap:wrap;">
        <a href="https://wa.me/905535062125" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:8px;padding:15px 25px;background:#25D366;color:#fff;text-decoration:none;font-weight:600;border-radius:6px;"><i data-lucide="message-circle" style="width:20px;height:20px;"></i> WhatsApp&apos;tan Yazın</a>
        <a href="../iletisim.html" style="display:inline-flex;align-items:center;gap:8px;padding:15px 25px;background:transparent;border:1px solid var(--matte-gold);color:var(--matte-gold);text-decoration:none;font-weight:600;border-radius:6px;"><i data-lucide="mail" style="width:20px;height:20px;"></i> İletişim Formu</a>
        <a href="../araclar.html" style="display:inline-flex;align-items:center;gap:8px;padding:15px 25px;background:transparent;border:1px solid var(--matte-gold);color:var(--matte-gold);text-decoration:none;font-weight:600;border-radius:6px;"><i data-lucide="calculator" style="width:20px;height:20px;"></i> Tazminat Hesaplama</a>
    </div>
</div>
'''

# FAQ (kısa)
FAQ_BY_CAT = {
    "aile-hukuku": [("Boşanmada tazminat nasıl alınır?", "Kusur oranına göre manevi tazminat. Gebze Aile Mahkemesi."), ("Nafaka Gebze'de nasıl hesaplanır?", "Gelir ve giderlere göre. Ücretsiz hesaplama aracımız."), ("Velayet için avukat şart mı?", "Zorunlu değil; karmaşık süreçte Gebze boşanma avukatı önerilir.")],
    "is-hukuku": [("Tazminatımı nasıl alırım?", "Arabuluculuk sonrası İş Mahkemesi. Gebze GOSB bölgesi."), ("Patron tazminat vermiyor?", "1 ay içinde dava. Delilleri toplayın."), ("Kıdem tazminatı 2026 tavanı?", "Bakanlar Kurulu günceller. Hesaplama aracımız.")],
    "ceza-hukuku": [("Gebze Adliyesi'nde avukat şart mı?", "Avukat hakkı var. Erken müdahale kritik."), ("İfadeye gitmezsem?", "Zorla getirtme uygulanabilir."), ("Sabıka silinir mi?", "5-15 yıl. Başsavcılığa başvuru.")],
    "gayrimenkul": [("Ev sahibi çıkarıyor, ne yapmalıyım?", "Tahliye davası gerekir. Zorla çıkarma suç."), ("Kira çok yükseldi?", "5 yıl sonra kira tespit davası."), ("Tahliye taahhütnamesi tehlikeli mi?", "İmzalamadan önce avukata danışın.")],
    "icra-iflas": [("Maaş haczi ne kadar?", "1/3 korunur. Hesaplama aracımız."), ("Borçtan hapse girilir mi?", "Nafaka dışında hayır."), ("Senet benim değil?", "7 gün itiraz. Grafolog.")],
    "bilisim-e-ticaret": [("İnternetten dolandırıldım?", "Suç duyurusu + tazminat. Banka bilgisi."), ("Sosyal medyada hakaret?", "Savcılığa şikayet. Ekran görüntüsü."), ("KVKK ihlali nereye?", "Kuruma şikayet. Tazminat davası.")],
}
DEFAULT_FAQ = [("Gebze'de avukata ne zaman başvurmalıyım?", "Hukuki uyuşmazlık çıktığı anda. Süre sınırı olan davalarda erken müdahale kritik."), ("Ücretsiz danışmanlık var mı?", "Evet. AV. AYŞENUR AVCI HUKUK BÜROSU ücretsiz ön görüşme sunar."), ("Darıca ve Çayırova'dan hizmet?", "Evet. Gebze merkezli, Kocaeli genelinde hizmet.")]

def get_category(html, slug):
    m = re.search(r'data-i18n="([a-z0-9-]+)"', html)
    if m and m.group(1) in FAQ_BY_CAT:
        return m.group(1)
    m = re.search(r'<span[^>]*>([^<]+)</span>', html)
    cat_map = {"Aile Hukuku":"aile-hukuku","İş Hukuku":"is-hukuku","Ceza Hukuku":"ceza-hukuku","Gayrimenkul":"gayrimenkul","İcra İflas":"icra-iflas","Bilişim & E-Ticaret":"bilisim-e-ticaret"}
    if m: return cat_map.get(m.group(1).strip(), "aile-hukuku")
    for k in ["kidem","ise-iade","bosanma","nafaka","kira","icra","ceza","kvkk","dolandiricilik"]:
        if k in slug: return {"kidem":"is-hukuku","ise-iade":"is-hukuku","bosanma":"aile-hukuku","nafaka":"aile-hukuku","kira":"gayrimenkul","icra":"icra-iflas","ceza":"ceza-hukuku","kvkk":"bilisim-e-ticaret","dolandiricilik":"bilisim-e-ticaret"}.get(k,"aile-hukuku")
    return "aile-hukuku"

def gen_meta(slug, h1, excerpt, cat):
    loc = "Gebze" if "gebze" in slug or "kidem" in slug else ("Darıca" if "trafik" in slug or "kaza" in slug else "Çayırova")
    title = f"{h1} | {loc} Avukat" if loc not in (h1 or "") else (h1 or slug)
    if len(title) > 58: title = title[:55] + "..."
    desc = f"{loc} avukat: {excerpt or h1}" if loc not in (excerpt or "") else (excerpt or h1)
    if len(desc) > 152: desc = desc[:149] + "..."
    return title, desc

def get_related(slug, all_slugs, cat):
    pool = {
        "aile-hukuku": ["bosanmada-maddi-ve-manevi-tazminat","nafaka-artirim-davasi-nasil-acilir","velayet-davasinda-uzman-gorusu"],
        "is-hukuku": ["gebze-kidem-tazminati-hesaplama-2026","ise-iade-davasi-acma-sartlari","fazla-mesai-ucreti-ve-ispat-yuku"],
        "ceza-hukuku": ["agir-ceza-mahkemelerinde-savunma-stratejileri","denetimli-serbestlik-sartlari-2026","adli-sicil-kaydinin-sabika-silinmesi"],
        "gayrimenkul": ["kira-tespit-davasinda-5-yil-kurali","kira-tahliye-davalarinda-arabuluculuk","ortakligin-giderilmesi-izale-i-suyu"],
        "icra-iflas": ["maas-haczi-orani-ve-hesaplamasi","icra-takibine-itiraz-ve-itirazin-iptali","e-haciz-ve-banka-blokesi-kaldirma"],
        "bilisim-e-ticaret": ["internet-yoluyla-dolandiricilik-sucu","kvkk-kapsaminda-veri-sorumlusu","sosyal-medya-hakaret-santaj-suclari"],
    }.get(cat, []) + [s for s in all_slugs if s != slug]
    out = []
    for s in pool:
        if (BLOG_DIR / f"{s}.html").exists() and s not in out and s != slug:
            out.append(s)
            if len(out) >= 2: break
    return out[:2]

ANCHOR = {"bosanmada-maddi-ve-manevi-tazminat":"boşanmada tazminat","nafaka-artirim-davasi-nasil-acilir":"nafaka artırım","velayet-davasinda-uzman-gorusu":"velayet davası","gebze-kidem-tazminati-hesaplama-2026":"kıdem tazminatı hesaplama","ise-iade-davasi-acma-sartlari":"işe iade davası","fazla-mesai-ucreti-ve-ispat-yuku":"fazla mesai","agir-ceza-mahkemelerinde-savunma-stratejileri":"ceza savunması","kira-tespit-davasinda-5-yil-kurali":"kira tespit","maas-haczi-orani-ve-hesaplamasi":"maaş haczi","icra-takibine-itiraz-ve-itirazin-iptali":"icra itiraz","internet-yoluyla-dolandiricilik-sucu":"internet dolandırıcılığı","kvkk-kapsaminda-veri-sorumlusu":"KVKK"}

def ensure_keyword_in_first_100(content, keyword):
    """İlk paragrafta anahtar kelime yoksa ekle."""
    idx = content.find('content-body')
    if idx < 0: return content
    rest = content[idx:idx+8000]
    first_p = re.search(r'(<p[^>]*>)(.*?)(</p>)', rest, re.DOTALL)
    if not first_p: return content
    text = re.sub(r'<[^>]+>', '', first_p.group(2))
    if keyword.lower() in text.lower(): return content
    insert = f'<strong>{keyword}</strong> konusunda '
    old = first_p.group(0)
    new = first_p.group(1) + insert + first_p.group(2) + first_p.group(3)
    return content.replace(old, new, 1)

def fix_duplicate_internal_links(content):
    """Tekrarlanan 'Bu konuda ... makalelerimizi' cümlesini temizle."""
    pattern = r'( Bu konuda <strong><a href="[^"]+">[^<]+</a></strong> ve <strong><a href="[^"]+">[^<]+</a></strong> makalelerimizi de inceleyebilirsiniz\.){2,}'
    return re.sub(pattern, r'\1', content)

def add_internal_links_once(content, related):
    """İlk paragrafa tek seferlik 2 iç link ekle."""
    if not related or "makalelerimizi de inceleyebilirsiniz" in content:
        return content
    a1 = ANCHOR.get(related[0], related[0].replace("-"," "))
    a2 = ANCHOR.get(related[1], related[1].replace("-"," ")) if len(related)>1 else a1
    insert = f' Bu konuda <strong><a href="{related[0]}.html">{a1}</a></strong> ve <strong><a href="{related[1]}.html">{a2}</a></strong> makalelerimizi de inceleyebilirsiniz.'
    first_p = re.search(r'(<p[^>]*>)(.*?)(</p>)', content, re.DOTALL)
    if first_p and len(first_p.group(2)) > 30 and "makalelerimizi" not in first_p.group(2):
        old = first_p.group(0)
        new = first_p.group(1) + first_p.group(2).rstrip() + insert + first_p.group(3)
        return content.replace(old, new, 1)
    return content

def ensure_heading_hierarchy(content, slug, cat):
    """H2 başlıklarına yerel kelime ekle (en az birinde)."""
    loc = "Gebze" if "gebze" in slug or "kidem" in slug else ("Darıca" if "trafik" in slug else "Çayırova")
    if loc not in content[:2000]:
        first_h2 = re.search(r'(<h2[^>]*>)([^<]+)(</h2>)', content)
        if first_h2 and loc not in first_h2.group(2):
            new_h2 = first_h2.group(1) + first_h2.group(2) + f" – {loc} Perspektifi" + first_h2.group(3)
            if len(new_h2) < 80:
                content = content.replace(first_h2.group(0), new_h2, 1)
    return content

def add_bold_to_key_terms(content, keywords):
    """Önemli kavramları bold yap (uzun ifadeler önce, tek geçiş)."""
    for kw in sorted(keywords[:4], key=len, reverse=True):
        if kw in content and f"<strong>{kw}</strong>" not in content:
            content = content.replace(kw, f'<strong>{kw}</strong>', 1)
    return content

def _split_long_paragraphs(content):
    """150 kelimeden uzun paragrafları böl."""
    def split_p(m):
        p_content = m.group(1)
        words = p_content.split()
        if len(words) <= 150:
            return m.group(0)
        mid = len(words) // 2
        first = ' '.join(words[:mid])
        second = ' '.join(words[mid:])
        return f'<p>{first}</p>\n<p>{second}</p>'
    return re.sub(r'<p([^>]*)>((?:(?!</p>).){500,})</p>', split_p, content, flags=re.DOTALL)

def process_file(filepath, all_slugs):
    slug = filepath.stem
    html = filepath.read_text(encoding="utf-8")
    cat = get_category(html, slug)
    
    h1 = re.search(r'<h1[^>]*>([^<]+)</h1>', html)
    meta = re.search(r'<meta name="description" content="([^"]*)"', html)
    h1_text = h1.group(1) if h1 else slug.replace("-"," ").title()
    excerpt = meta.group(1) if meta else ""
    
    title_seo, desc_seo = gen_meta(slug, h1_text, excerpt, cat)
    related = get_related(slug, all_slugs, cat)
    faq_list = FAQ_BY_CAT.get(cat, DEFAULT_FAQ)
    main_kw = get_main_keyword(slug, cat)
    
    # 1. Title & Meta
    html = re.sub(r'<title>[^<]+</title>', f'<title>{title_seo} | AV. AYŞENUR AVCI HUKUK BÜROSU</title>', html)
    html = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{desc_seo}"', html, count=1)
    
    # 2. FAQ Schema
    faq_schema = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_list]}, ensure_ascii=False)
    if "FAQPage" not in html:
        html = html.replace("</head>", f'<script type="application/ld+json">{faq_schema}</script>\n</head>')
    
    # 3. Content-body
    body_m = re.search(r'(<div class="content-body">)(.*?)(</div>\s*</article>)', html, re.DOTALL)
    if body_m:
        body = body_m.group(2)
        body = fix_duplicate_internal_links(body)
        body = add_internal_links_once(body, related)
        body = ensure_heading_hierarchy(body, slug, cat)
        body = add_bold_to_key_terms(body, [main_kw, "Gebze avukat", "Darıca", "Çayırova"])
        
        if "article-faq-list" not in body:
            faq_html = '<h2 style="color:var(--matte-gold);margin:40px 0 20px;">Sıkça Sorulan Sorular</h2><div class="article-faq-list">'
            for q,a in faq_list:
                faq_html += f'<div class="faq-article-item" style="margin-bottom:25px;"><h4 style="color:var(--matte-gold);font-size:16px;">{q}</h4><p style="color:#ccc;">{a}</p></div>'
            faq_html += '</div>'
            body += faq_html
        if "article-cta-block" not in body:
            body += CTA_HTML
        
        html = html[:body_m.start(2)] + body + html[body_m.end(2):]
    
    html = ensure_keyword_in_first_100(html, main_kw)
    
    # 4. Görsel alt
    def add_alt(m):
        t = m.group(0)
        return t if 'alt=' in t.lower() else t.replace('<img', '<img alt="AV. AYŞENUR AVCI HUKUK BÜROSU - Gebze Avukat - Hukuki Danışmanlık"')
    html = re.sub(r'<img[^>]*>', add_alt, html)
    
    filepath.write_text(html, encoding="utf-8")
    return slug

def main():
    files = list(BLOG_DIR.glob("*.html"))
    slugs = [f.stem for f in files]
    print(f"Toplam {len(files)} makale işleniyor...")
    for f in sorted(files):
        try:
            process_file(f, slugs)
            print(f"  OK: {f.stem}")
        except Exception as e:
            print(f"  HATA {f.stem}: {e}")
    print("\nTeknik SEO optimizasyonu tamamlandı.")

if __name__ == "__main__":
    main()
