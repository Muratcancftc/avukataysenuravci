/**
 * SEO İç Linkleme Modülü
 * Blog makaleleri ile hesaplama araçları ve faaliyet sayfaları arasında bağlamsal linkleme
 */
(function() {
    'use strict';

    const BASE = document.querySelector('base')?.href || '';
    const isBlog = window.location.pathname.includes('/blog/');

    // Kategori -> Pillar sayfa, hesaplama araçları, ilgili makaleler
    const SEO_CONFIG = {
        'aile-hukuku': {
            pillar: { url: '../faaliyet-alanlari/aile-hukuku/anlasmali-bosanma.html', text: 'Gebze Boşanma Avukatı - Aile Hukuku' },
            calcTools: [
                { url: '../araclar.html#cat-aile', anchor: '2026 Yılı Boşanma Davası Harç ve Masrafları', tab: 'aile' },
                { url: '../araclar.html#cat-aile', anchor: 'Nafaka Tahmini Hesaplama', tab: 'aile' },
                { url: '../araclar.html#cat-aile', anchor: 'Düğün Takıları (Ziynet) Değerlemesi', tab: 'aile' }
            ],
            keywords: ['nafaka', 'boşanma', 'velayet', 'mal paylaşımı', 'tazminat', 'ziynet', 'harç', 'masraf']
        },
        'is-hukuku': {
            pillar: { url: '../faaliyet-alanlari/is-hukuku/kidem-tazminati.html', text: 'Gebze İş Hukuku Uzmanı' },
            calcTools: [
                { url: '../araclar.html#cat-is', anchor: 'Güncel Kıdem Tazminatı Hesaplama Robotu', tab: 'is' },
                { url: '../araclar.html#cat-is', anchor: 'İhbar Tazminatı Hesaplama', tab: 'is' },
                { url: '../araclar.html#cat-is', anchor: 'Fazla Mesai Ücreti Hesaplama', tab: 'is' },
                { url: '../araclar.html#cat-is', anchor: 'Yıllık İzin Ücreti Hesaplama', tab: 'is' },
                { url: '../araclar.html#cat-is', anchor: 'Brütten Nete Maaş Hesaplama', tab: 'is' }
            ],
            keywords: ['kıdem', 'ihbar', 'tazminat', 'hesaplama', 'maaş', 'fazla mesai', 'izin']
        },
        'ceza-hukuku': {
            pillar: { url: '../faaliyet-alanlari/ceza-hukuku/agir-ceza.html', text: 'Gebze Ceza Avukatı' },
            calcTools: [
                { url: '../araclar.html#cat-genel', anchor: 'Dava Harç ve Masraf Hesaplama', tab: 'genel' }
            ],
            keywords: ['dava', 'harç', 'masraf', 'ceza']
        },
        'gayrimenkul': {
            pillar: { url: '../faaliyet-alanlari/gayrimenkul/tahliye.html', text: 'Gebze Gayrimenkul Avukatı' },
            calcTools: [
                { url: '../araclar.html#cat-genel', anchor: 'Dava Harç ve Masraf Hesaplama', tab: 'genel' }
            ],
            keywords: ['kira', 'tahliye', 'harç', 'ecrimisil']
        },
        'icra-iflas': {
            pillar: { url: '../faaliyet-alanlari/icra-iflas/cek-senet.html', text: 'Gebze İcra Avukatı' },
            calcTools: [
                { url: '../araclar.html#cat-genel', anchor: 'Yasal Faiz ve Temerrüt Faizi Hesaplayıcı', tab: 'genel' },
                { url: '../araclar.html#cat-genel', anchor: 'İcra Takip Maliyeti Hesaplama', tab: 'genel' }
            ],
            keywords: ['faiz', 'icra', 'takip', 'maliyet', 'alacak', 'hesaplama']
        },
        'bilisim-e-ticaret': {
            pillar: { url: '../faaliyet-alanlari/bilisim-e-ticaret/kvkk.html', text: 'Gebze Bilişim Hukuku' },
            calcTools: [
                { url: '../araclar.html#cat-genel', anchor: 'Dava Harç Hesaplama', tab: 'genel' }
            ],
            keywords: ['dava', 'harç', 'tazminat']
        }
    };

    // Makale slug -> ilgili makaleler (İlginizi Çekebilir) - slug -> [{slug, title}]
    const RELATED_MAP = {
        'anlasmali-bosanma-davasi-nasil-acilir': [
            { slug: 'velayet-davasinda-uzman-gorusu.html', title: 'Velayet Davasında Uzman Görüşü' },
            { slug: 'mal-rejiminin-tasfiyesinde-deger-artis-payi.html', title: 'Mal Paylaşımı ve Değer Artış Payı' },
            { slug: 'yoksulluk-nafakasi-sartlari.html', title: 'Yoksulluk Nafakası Şartları' }
        ],
        'ise-iade-davasi-acma-sartlari': [
            { slug: 'kidem-tazminati.html', title: 'Kıdem Tazminatı' },
            { slug: 'mobbing-nedeniyle-manevi-tazminat-miktari.html', title: 'Mobbing ve Manevi Tazminat' },
            { slug: 'fazla-mesai-ucreti-ve-ispat-yuku.html', title: 'Fazla Mesai Ücreti' }
        ],
        'icra-takibine-itiraz-ve-itirazin-iptali': [
            { slug: 'maas-haczi-orani-ve-hesaplamasi.html', title: 'Maaş Haczi Oranı' },
            { slug: 'e-haciz-ve-banka-blokesi-kaldirma.html', title: 'E-Haciz ve Banka Blokesi' },
            { slug: 'karsiliksiz-cek-keside-etme-sucu.html', title: 'Karşılıksız Çek Suçu' }
        ],
        'nafaka-artirim-davasi-nasil-acilir': [
            { slug: 'istirak-nafakasi-ve-cocuk-giderleri.html', title: 'İştirak Nafakası' },
            { slug: 'yoksulluk-nafakasi-sartlari.html', title: 'Yoksulluk Nafakası' },
            { slug: 'velayet-davasinda-uzman-gorusu.html', title: 'Velayet Davasında Uzman Görüşü' }
        ],
        'trafik-kazasi-sonrasi-taksirle-yaralama': [
            { slug: 'mobbing-nedeniyle-manevi-tazminat-miktari.html', title: 'Manevi Tazminat Miktarı' },
            { slug: 'kotuniyet-tazminati-sartlari.html', title: 'Kötüniyet Tazminatı' }
        ]
    };

    // Kategoriye göre dış otorite linkleri (yerel + ulusal kaynaklar)
    const DEFAULT_EXTERNAL_AUTHORITY_LINKS = [
        { href: 'https://gebze.adalet.gov.tr/', anchor: 'Gebze Adliyesi' },
        { href: 'https://www.mevzuat.gov.tr/', anchor: 'T.C. Mevzuat Sistemi' },
        { href: 'https://www.gebzeto.org.tr/', anchor: 'Gebze Ticaret Odasi' },
        { href: 'https://www.kocaelibarosu.org.tr/', anchor: 'Kocaeli Barosu' },
        { href: 'https://www.barobirlik.org.tr/', anchor: 'Turkiye Barolar Birligi' },
        { href: 'https://www.yargitay.gov.tr/', anchor: 'Yargitay' },
        { href: 'https://www.resmigazete.gov.tr/', anchor: 'Resmi Gazete' },
        { href: 'https://www.anayasa.gov.tr/', anchor: 'Anayasa Mahkemesi' },
        { href: 'https://www.gebze.bel.tr/', anchor: 'Gebze Belediyesi' },
        { href: 'https://www.turkiye.gov.tr/', anchor: 'E-Devlet Kapisi' }
    ];

    // Güncel hukuki veriler (2026)
    const LIVE_DATA = {
        asgariUcret: '22.002',
        yasalFaiz: '%24',
        kidemTavan: '64.948,77'
    };

    function getCurrentSlug() {
        const path = window.location.pathname;
        const match = path.match(/\/([^/]+)\.html$/);
        return match ? match[1] : null;
    }

    function getCategoryFromPage() {
        const breadcrumb = document.querySelector('.breadcrumb span[data-i18n]');
        if (breadcrumb) {
            const i18n = breadcrumb.getAttribute('data-i18n');
            const map = { 'aile-hukuku': 'aile-hukuku', 'is-hukuku': 'is-hukuku', 'ceza-hukuku': 'ceza-hukuku', 'gayrimenkul': 'gayrimenkul', 'icra-iflas': 'icra-iflas', 'bilisim-e-ticaret': 'bilisim-e-ticaret' };
            return map[i18n] || null;
        }
        const slug = getCurrentSlug();
        if (slug && typeof articles !== 'undefined') {
            const art = articles.find(a => a.slug === slug);
            return art ? art.categorySlug : null;
        }
        const slugToCat = {
            'anlasmali-bosanma-davasi-nasil-acilir': 'aile-hukuku', 'ise-iade-davasi-acma-sartlari': 'is-hukuku',
            'icra-takibine-itiraz-ve-itirazin-iptali': 'icra-iflas', 'nafaka-artirim-davasi-nasil-acilir': 'aile-hukuku'
        };
        return slugToCat[slug] || 'aile-hukuku';
    }

    function createCalcCTA(config, primaryTool) {
        const tool = config.calcTools[0] || primaryTool;
        if (!tool) return '';
        return `
        <div class="seo-cta-card">
            <div class="seo-cta-border"></div>
            <div class="seo-cta-content">
                <h4 class="seo-cta-title">Okuduğunuz konuyla ilgili tazminat miktarınızı merak mı ediyorsunuz?</h4>
                <a href="${tool.url}" class="seo-cta-btn">
                    <i data-lucide="calculator" style="width: 18px; height: 18px;"></i>
                    Hemen Ücretsiz Hesaplayın
                </a>
                <p class="seo-cta-note">Bu rakamlar tahminidir. Kesin sonuç için dosyanızı incelememize izin verin.</p>
            </div>
        </div>`;
    }

    function createExpertGuide(config, slug) {
        const related = RELATED_MAP[slug] || [];
        const pillar = config.pillar;
        let relatedHtml = '';
        if (related.length) {
            const links = related.slice(0, 3).map(r => `<a href="${r.slug}">${r.title}</a>`);
            relatedHtml = `
                <div class="seo-related">
                    <h4>Bu konuyu okuyanlar şunu da inceledi:</h4>
                    <ul>${links.map(l => `<li>${l}</li>`).join('')}</ul>
                </div>`;
        }
        return `
        <div class="seo-expert-guide">
            <h3>Sıradaki Adım</h3>
            <p>Dava açmadan önce hazırlamanız gereken belgeler ve süreç hakkında detaylı bilgi için <a href="${pillar.url}">${pillar.text}</a> sayfamızı inceleyebilirsiniz.</p>
            <a href="../iletisim.html" class="seo-cta-btn fill" style="color:#000;border-bottom:none;">
                <i data-lucide="phone" style="width: 16px; height: 16px;"></i>
                Avukata Danış
            </a>
            <div class="seo-on-inceleme">
                <h4>Ücretsiz Ön İnceleme</h4>
                <p>Dosyanızı ücretsiz ön incelemeye gönderin. 24 saat içinde size dönüş yapacağız.</p>
                <a href="../iletisim.html" class="seo-cta-btn" style="color:#000;border-bottom:none;">Formu Doldurun</a>
            </div>
            ${relatedHtml}
        </div>`;
    }

    function createLiveDataWidget(config) {
        const tools = config.calcTools.slice(0, 2);
        return `
        <div class="seo-live-widget sidebar-widget">
            <h4><i data-lucide="trending-up" style="width: 16px; height: 16px;"></i> Canlı Veri</h4>
            <ul class="seo-live-list">
                <li><span>2026 Asgari Ücret</span><strong>${LIVE_DATA.asgariUcret} ₺</strong></li>
                <li><span>Yasal Faiz Oranı</span><strong>${LIVE_DATA.yasalFaiz}</strong></li>
                <li><span>Kıdem Tavan</span><strong>${LIVE_DATA.kidemTavan} ₺</strong></li>
            </ul>
            <a href="../araclar.html" class="seo-live-btn">Hesaplama Araçları</a>
        </div>`;
    }

    function injectContextualLink(contentBody, config) {
        if (!contentBody || !config.pillar) return;
        const firstP = contentBody.querySelector('p');
        if (!firstP || firstP.querySelector('.seo-contextual-link')) return;
        const pillarText = config.pillar.text;
        const pillarUrl = config.pillar.url;
        const linkHtml = ` <a href="${pillarUrl}" class="seo-contextual-link">${pillarText}</a>`;
        const inline = document.createElement('span');
        inline.className = 'seo-contextual-inline';
        inline.innerHTML = ` Bu konuda detaylı bilgi için${linkHtml} sayfamızı inceleyebilirsiniz.`;
        firstP.appendChild(inline);
    }

    function injectExternalAuthorityLinks(contentBody, category) {
        if (!contentBody) return;
        if (contentBody.querySelector('.seo-external-links, .seo-external-links-auto')) return;

        const globalList = Array.isArray(window.OFFICIAL_AUTHORITY_LINKS) ? window.OFFICIAL_AUTHORITY_LINKS : [];
        const list = globalList.length ? globalList : DEFAULT_EXTERNAL_AUTHORITY_LINKS;
        if (!list.length) return;

        const links = list
            .filter(item => item && item.href)
            .map(item => {
                const text = item.anchor || item.label || item.href;
                return `<a href="${item.href}" target="_blank" rel="noopener noreferrer">${text}</a>`;
            });

        const existingHeading = Array.from(contentBody.querySelectorAll('h2, h3')).find(h => {
            const t = (h.textContent || '').toLowerCase();
            return t.includes('resmi kaynaklar') || t.includes('dış bağlantılar');
        });

        if (existingHeading) {
            const p = document.createElement('p');
            p.className = 'seo-external-links-auto';
            p.innerHTML = `${links.join(', ')} kaynakları bu konudaki hukuki değerlendirmeyi güncel tutmak için düzenli olarak takip edilmelidir.`;
            existingHeading.insertAdjacentElement('afterend', p);
            return;
        }

        const section = document.createElement('section');
        section.className = 'seo-external-links';
        section.innerHTML = `
            <h2>Resmi Kaynaklar ve Dış Bağlantılar</h2>
            <p>${links.join(', ')} kaynakları bu konudaki hukuki değerlendirmeyi güncel tutmak için düzenli olarak takip edilmelidir.</p>
        `;

        // Sonuç başlığından önce ekle; yoksa içeriğin sonuna ekle
        const allH2 = Array.from(contentBody.querySelectorAll('h2'));
        const resultHeading = allH2.find(h => (h.textContent || '').trim().toLowerCase() === 'sonuç');
        if (resultHeading) resultHeading.before(section);
        else contentBody.appendChild(section);
    }

    function injectRequiredInternalLinks(contentBody, slug) {
        if (!contentBody) return;
        if (contentBody.querySelector('.seo-required-internal-links')) return;

        const related = (RELATED_MAP[slug] && RELATED_MAP[slug][0]) ? RELATED_MAP[slug][0] : null;
        const relatedHref = related ? related.slug : '../makaleler.html';
        const relatedText = related ? related.title : 'ilgili blog yazilarimiz';

        const block = document.createElement('section');
        block.className = 'seo-required-internal-links';
        block.innerHTML = `
            <h3>Daha Fazla Hukuki Bilgi</h3>
            <p>
                Bu konuda adim adim destek almak icin
                <a href="../">Gebze hukuk burosu hizmetlerimizi</a>,
                dogrudan randevu icin <a href="../iletisim.html">iletisim sayfamizi</a> ve
                benzer bir konu icin <a href="${relatedHref}">${relatedText}</a> yazisini inceleyebilirsiniz.
            </p>
        `;
        contentBody.appendChild(block);
    }

    function injectAuthorBio(contentBody) {
        if (!contentBody) return;
        if (contentBody.querySelector('.seo-author-bio')) return;

        const bio = document.createElement('section');
        bio.className = 'seo-author-bio';
        bio.innerHTML = `
            <h3>Yazar: Hukuk Editoru</h3>
            <p>
                Ceza hukuku, aile hukuku, is hukuku, gayrimenkul hukuku ve icra-iflas alanlarinda
                Gebze ve Kocaeli bolgesinde hukuki danismanlik sunmaktadir.
                Kocaeli Barosu'na kayitli avukatlik hizmeti vermektedir.
            </p>
            <p class="seo-author-bio-cta">
                Dosyaniza ozel degerlendirme icin <a href="../iletisim.html">randevu olusturun</a>.
            </p>
        `;
        contentBody.appendChild(bio);
    }

    function getContentBodyTarget() {
        const explicit = document.querySelector('.content-body');
        if (explicit) return explicit;

        // Bazı blog şablonlarında .content-body yok; ana içerik konteynerini fallback olarak kullan.
        const scopedContainer = document.querySelector('main .container');
        if (scopedContainer) return scopedContainer;

        const main = document.querySelector('main');
        return main || null;
    }

    function init() {
        if (!isBlog) return;

        const category = getCategoryFromPage();
        const slug = getCurrentSlug();
        const config = category ? SEO_CONFIG[category] : SEO_CONFIG['aile-hukuku'];

        if (!config) return;

        const contentBody = getContentBodyTarget();
        const sidebar = document.querySelector('.sidebar');
        const mainArticle = document.querySelector('.main-article');
        const hasAdvancedArticleLayout = !!document.querySelector('.content-body');

        if (contentBody) {
            if (hasAdvancedArticleLayout) {
                const ctaHtml = createCalcCTA(config);
                const midPoint = Math.floor(contentBody.children.length / 2);
                const insertAfter = contentBody.children[midPoint] || contentBody.firstElementChild;
                if (insertAfter && ctaHtml) {
                    const div = document.createElement('div');
                    div.className = 'seo-cta-wrapper';
                    div.innerHTML = ctaHtml;
                    insertAfter.after(div);
                }

                const guideHtml = createExpertGuide(config, slug);
                if (guideHtml && mainArticle) {
                    const div = document.createElement('div');
                    div.className = 'seo-guide-wrapper';
                    div.innerHTML = guideHtml;
                    contentBody.appendChild(div);
                }
            }

            injectContextualLink(contentBody, config);
            injectExternalAuthorityLinks(contentBody, category);
            injectRequiredInternalLinks(contentBody, slug);
            injectAuthorBio(contentBody);
        }

        if (sidebar) {
            const liveHtml = createLiveDataWidget(config);
            const div = document.createElement('div');
            div.innerHTML = liveHtml;
            sidebar.insertBefore(div.firstElementChild, sidebar.firstChild);
        }

        if (typeof lucide !== 'undefined') lucide.createIcons();
        else document.querySelectorAll('[data-lucide]').forEach(el => {
            if (typeof lucide !== 'undefined') lucide.createIcons();
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
