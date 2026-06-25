let currentLang = localStorage.getItem('siteLang') || 'tr';
const OFFICIAL_AUTHORITY_LINKS = [
    { href: 'https://gebze.adalet.gov.tr/', labelKey: 'official-link-gebze-courthouse', defaultLabel: 'Gebze Adliyesi' },
    { href: 'https://www.mevzuat.gov.tr/', labelKey: 'official-link-mevzuat', defaultLabel: 'T.C. Mevzuat Sistemi' },
    { href: 'https://www.gebzeto.org.tr/', labelKey: 'official-link-gebze-chamber', defaultLabel: 'Gebze Ticaret Odasi' },
    { href: 'https://www.kocaelibarosu.org.tr/', labelKey: 'official-link-kocaeli-bar', defaultLabel: 'Kocaeli Barosu' },
    { href: 'https://www.barobirlik.org.tr/', labelKey: 'official-link-tbb', defaultLabel: 'Turkiye Barolar Birligi' },
    { href: 'https://www.yargitay.gov.tr/', labelKey: 'official-link-court-of-appeal', defaultLabel: 'Yargitay' },
    { href: 'https://www.resmigazete.gov.tr/', labelKey: 'official-link-official-gazette', defaultLabel: 'Resmi Gazete' },
    { href: 'https://www.anayasa.gov.tr/', labelKey: 'official-link-constitutional-court', defaultLabel: 'Anayasa Mahkemesi' },
    { href: 'https://www.gebze.bel.tr/', labelKey: 'official-link-gebze-municipality', defaultLabel: 'Gebze Belediyesi' },
    { href: 'https://www.turkiye.gov.tr/', labelKey: 'official-link-e-devlet', defaultLabel: 'E-Devlet Kapisi' }
];
window.OFFICIAL_AUTHORITY_LINKS = OFFICIAL_AUTHORITY_LINKS;
const UI_TRANSLATABLE_LANGS = new Set(['en', 'de', 'fr', 'ru', 'ar']);
let myMemoryRetryAfterMs = 0;
const blogTextNodeOriginals = new WeakMap();
let blogTranslationToken = 0;

function upsertMetaTag(attrName, attrValue, content) {
    if (!attrName || !attrValue) return;
    let selector = '';
    if (attrName === 'name') selector = `meta[name="${attrValue}"]`;
    if (attrName === 'property') selector = `meta[property="${attrValue}"]`;
    if (!selector) return;

    let meta = document.head.querySelector(selector);
    if (!meta) {
        meta = document.createElement('meta');
        meta.setAttribute(attrName, attrValue);
        document.head.appendChild(meta);
    }
    meta.setAttribute('content', content || '');
}

function getCanonicalUrlFromLocation() {
    const url = new URL(window.location.href);
    url.hash = '';

    if (url.pathname.endsWith('/index.html')) {
        url.pathname = url.pathname.replace(/\/index\.html$/i, '/') || '/';
    }

    // Normalize duplicate slashes in path
    url.pathname = url.pathname.replace(/\/{2,}/g, '/');
    return url.toString();
}

function parseTurkishDateToIso(text) {
    if (!text) return null;
    const monthMap = {
        ocak: 1, subat: 2, 'şubat': 2, mart: 3, nisan: 4, mayis: 5, 'mayıs': 5, haziran: 6,
        temmuz: 7, agustos: 8, 'ağustos': 8, eylul: 9, 'eylül': 9, ekim: 10, kasim: 11, 'kasım': 11, aralik: 12, 'aralık': 12
    };
    const cleaned = String(text).toLowerCase().replace(/\s+/g, ' ').trim();
    const match = cleaned.match(/(\d{1,2})\s+([a-zçğıöşü]+)\s+(\d{4})/i);
    if (!match) return null;

    const day = Number(match[1]);
    const month = monthMap[match[2]] || null;
    const year = Number(match[3]);
    if (!day || !month || !year) return null;

    const isoDate = new Date(Date.UTC(year, month - 1, day, 9, 0, 0));
    if (Number.isNaN(isoDate.getTime())) return null;
    return isoDate.toISOString();
}

function ensureSeoMetaTags() {
    const title = (document.title || (typeof siteConfig !== 'undefined' ? siteConfig.brandName : 'AV. AYŞENUR AVCI HUKUK BÜROSU')).trim();
    const descNode = document.querySelector('meta[name="description"]');
    const fallbackDesc = document.querySelector('main p')?.textContent?.trim() || 'Gebze merkezli hukuki danismanlik ve avukatlik hizmetleri.';
    const description = (descNode?.getAttribute('content') || fallbackDesc).replace(/\s+/g, ' ').trim();
    const canonicalUrl = getCanonicalUrlFromLocation();
    const isBlog = window.location.pathname.includes('/blog/');
    const image = `${window.location.origin}/favicon.svg`;

    let canonicalTag = document.querySelector('link[rel="canonical"]');
    if (!canonicalTag) {
        canonicalTag = document.createElement('link');
        canonicalTag.setAttribute('rel', 'canonical');
        document.head.appendChild(canonicalTag);
    }
    canonicalTag.setAttribute('href', canonicalUrl);

    upsertMetaTag('name', 'robots', 'index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1');
    upsertMetaTag('property', 'og:locale', 'tr_TR');
    upsertMetaTag('property', 'og:type', isBlog ? 'article' : 'website');
    upsertMetaTag('property', 'og:site_name', (typeof siteConfig !== 'undefined' ? siteConfig.brandName : 'AV. AYŞENUR AVCI HUKUK BÜROSU'));
    upsertMetaTag('property', 'og:title', title);
    upsertMetaTag('property', 'og:description', description);
    upsertMetaTag('property', 'og:url', canonicalUrl);
    upsertMetaTag('property', 'og:image', image);

    upsertMetaTag('name', 'twitter:card', 'summary_large_image');
    upsertMetaTag('name', 'twitter:title', title);
    upsertMetaTag('name', 'twitter:description', description);
    upsertMetaTag('name', 'twitter:image', image);

    if (isBlog) {
        const dateSource = document.querySelector('.meta-info')?.textContent || '';
        const publishedIso = parseTurkishDateToIso(dateSource);
        if (publishedIso) {
            upsertMetaTag('property', 'article:published_time', publishedIso);
            upsertMetaTag('property', 'article:modified_time', publishedIso);
        }
        const section = document.querySelector('.breadcrumb span')?.textContent?.trim();
        if (section) upsertMetaTag('property', 'article:section', section);
    }
}

function injectResponsiveSeoOverrides() {
    const styleId = 'seo-responsive-overrides';
    if (document.getElementById(styleId)) return;

    const style = document.createElement('style');
    style.id = styleId;
    style.textContent = `
@media (max-width: 992px) {
  .article-layout { grid-template-columns: 1fr !important; gap: 24px !important; }
  .sidebar { position: static !important; top: auto !important; }
}
@media (max-width: 768px) {
  .article-content { padding-top: 108px !important; }
  .article-content .container { width: min(100%, 100%) !important; padding-left: 14px !important; padding-right: 14px !important; }
  .breadcrumb { font-size: 11px !important; line-height: 1.5 !important; word-break: break-word !important; }
  .meta-info { display: grid !important; grid-template-columns: 1fr !important; gap: 10px !important; }
  .content-body { font-size: 16px !important; line-height: 1.7 !important; }
  .content-body h2 { font-size: 24px !important; line-height: 1.3 !important; }
  .content-body h3 { font-size: 20px !important; line-height: 1.35 !important; }
  .seo-cta-card { padding: 22px 16px !important; margin: 28px 0 !important; }
  .seo-cta-title { font-size: 16px !important; line-height: 1.45 !important; }
  .seo-cta-btn { width: 100% !important; justify-content: center !important; padding: 13px 14px !important; font-size: 12px !important; letter-spacing: 0.4px !important; }
  .seo-expert-guide { padding: 20px 14px !important; margin-top: 30px !important; }
  .seo-on-inceleme { padding: 14px !important; }
  .seo-live-widget .seo-live-list li { font-size: 13px !important; gap: 12px !important; }
  .seo-live-widget .seo-live-list li span { max-width: 65%; }
  .seo-required-internal-links, .seo-author-bio, .seo-external-links { padding: 14px !important; margin-top: 20px !important; }
  .article-cta-block { padding: 22px 14px !important; margin: 30px 0 !important; }
  .article-cta-block > div { display: grid !important; grid-template-columns: 1fr !important; gap: 10px !important; }
  .article-cta-block a { width: 100% !important; justify-content: center !important; }
}
@media (max-width: 480px) {
  .main-article h1 { font-size: 28px !important; line-height: 1.2 !important; }
  .content-body { font-size: 15.5px !important; }
  .content-body h2 { font-size: 22px !important; }
  .content-body h3 { font-size: 18px !important; }
}
`;
    document.head.appendChild(style);
}

function getTranslatedValue(lang, key, fallback = null) {
    if (typeof translations === 'undefined') return fallback;
    const langPack = translations[lang] || {};
    const enPack = translations.en || {};
    return langPack[key] || enPack[key] || fallback;
}

async function translateUiText(text, lang) {
    if (!text || !lang || lang === 'tr' || !UI_TRANSLATABLE_LANGS.has(lang)) return text;
    const cacheKey = `ui-i18n:${lang}:${text}`;
    const cached = localStorage.getItem(cacheKey);
    if (cached) return cached;
    try {
        // Primary provider: MyMemory
        if (Date.now() >= myMemoryRetryAfterMs) {
            const url = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=tr|${lang}`;
            const response = await fetch(url);
            if (response.ok) {
                const data = await response.json();
                const translated = (data && data.responseData && data.responseData.translatedText) ? data.responseData.translatedText : text;
                localStorage.setItem(cacheKey, translated);
                return translated;
            }
            if (response.status === 429) {
                // Back off to avoid hammering the API
                myMemoryRetryAfterMs = Date.now() + (10 * 60 * 1000);
            }
        }
    } catch (e) {}

    try {
        // Fallback provider: Google public endpoint
        const fallbackUrl = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=tr&tl=${lang}&dt=t&q=${encodeURIComponent(text)}`;
        const fallbackResponse = await fetch(fallbackUrl);
        if (!fallbackResponse.ok) return text;
        const data = await fallbackResponse.json();
        const parts = Array.isArray(data?.[0]) ? data[0] : [];
        const translated = parts.map(part => (Array.isArray(part) ? (part[0] || '') : '')).join('').trim() || text;
        localStorage.setItem(cacheKey, translated);
        return translated;
    } catch (e) {
        return text;
    }
}
window.translateUiText = translateUiText;

function getBlogTranslatableTextNodes(root) {
    const nodes = [];
    if (!root) return nodes;

    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
        acceptNode(node) {
            if (!node || !node.parentElement) return NodeFilter.FILTER_REJECT;
            const parent = node.parentElement;
            const tag = parent.tagName;
            if (tag === 'SCRIPT' || tag === 'STYLE' || tag === 'NOSCRIPT') return NodeFilter.FILTER_REJECT;
            if (parent.closest('[data-i18n], [data-i18n-placeholder], [data-i18n-content]')) return NodeFilter.FILTER_REJECT;
            const raw = node.nodeValue || '';
            const trimmed = raw.trim();
            if (!trimmed || trimmed.length < 2) return NodeFilter.FILTER_REJECT;
            if (/^https?:\/\//i.test(trimmed)) return NodeFilter.FILTER_REJECT;
            return NodeFilter.FILTER_ACCEPT;
        }
    });

    let current = walker.nextNode();
    while (current) {
        nodes.push(current);
        current = walker.nextNode();
    }
    return nodes;
}

async function translateBlogDetailContent(lang) {
    if (!window.location.pathname.includes('/blog/')) return;
    const main = document.querySelector('main');
    if (!main) return;

    const nodes = getBlogTranslatableTextNodes(main);
    const token = ++blogTranslationToken;

    nodes.forEach((node) => {
        if (!blogTextNodeOriginals.has(node)) {
            blogTextNodeOriginals.set(node, node.nodeValue || '');
        }
    });

    if (lang === 'tr' || !UI_TRANSLATABLE_LANGS.has(lang)) {
        nodes.forEach((node) => {
            const original = blogTextNodeOriginals.get(node);
            if (typeof original === 'string') node.nodeValue = original;
        });
        return;
    }

    const grouped = new Map();
    nodes.forEach((node) => {
        const original = blogTextNodeOriginals.get(node) || '';
        const trimmed = original.trim();
        if (!trimmed) return;
        const leading = original.match(/^\s*/)?.[0] || '';
        const trailing = original.match(/\s*$/)?.[0] || '';
        if (!grouped.has(trimmed)) grouped.set(trimmed, []);
        grouped.get(trimmed).push({ node, leading, trailing });
    });

    await Promise.all(Array.from(grouped.keys()).map(async (sourceText) => {
        const translated = await translateUiText(sourceText, lang);
        if (token !== blogTranslationToken) return;
        const targets = grouped.get(sourceText) || [];
        targets.forEach(({ node, leading, trailing }) => {
            node.nodeValue = `${leading}${translated}${trailing}`;
        });
    }));
}

function splitParagraphBySentences(text, maxSentencesPerChunk = 2) {
    const cleaned = (text || '').replace(/\s+/g, ' ').trim();
    if (!cleaned) return [];
    const sentences = cleaned.split(/(?<=[.!?])\s+/).filter(Boolean);
    if (sentences.length <= maxSentencesPerChunk) return [cleaned];

    const chunks = [];
    for (let i = 0; i < sentences.length; i += maxSentencesPerChunk) {
        chunks.push(sentences.slice(i, i + maxSentencesPerChunk).join(' ').trim());
    }
    return chunks;
}

function optimizeMobileArticleReadability() {
    const isMobile = window.matchMedia('(max-width: 768px)').matches;
    const isBlogPage = window.location.pathname.includes('/blog/');
    if (!isMobile || !isBlogPage) return;

    const root = document.querySelector('main');
    if (!root) return;

    const paragraphs = root.querySelectorAll('.content-body p, .main-article p, main .container > p');
    paragraphs.forEach((p) => {
        if (!p || p.dataset.mobileReadable === '1') return;
        if (p.closest('.seo-required-internal-links, .seo-author-bio, .seo-external-links')) return;

        const originalText = (p.textContent || '').trim();
        const chunks = splitParagraphBySentences(originalText, 2);
        if (chunks.length <= 1) {
            p.dataset.mobileReadable = '1';
            return;
        }

        const styleAttr = p.getAttribute('style') || '';
        const cls = p.className || '';
        const fragment = document.createDocumentFragment();

        chunks.forEach((chunk) => {
            const np = document.createElement('p');
            if (cls) np.className = cls;
            if (styleAttr) np.setAttribute('style', styleAttr);
            np.dataset.mobileReadable = '1';
            np.textContent = chunk;
            fragment.appendChild(np);
        });

        p.replaceWith(fragment);
    });
}

function optimizeImageDelivery() {
    const images = Array.from(document.querySelectorAll('img'));
    if (!images.length) return;

    images.forEach((img, index) => {
        if (!img.getAttribute('decoding')) img.setAttribute('decoding', 'async');
        if (!img.getAttribute('loading')) img.setAttribute('loading', index === 0 ? 'eager' : 'lazy');

        if (index === 0) {
            if (!img.getAttribute('fetchpriority')) img.setAttribute('fetchpriority', 'high');
        } else if (!img.getAttribute('fetchpriority')) {
            img.setAttribute('fetchpriority', 'low');
        }
    });
}

function upgradeImagesToPictureWebp() {
    const images = Array.from(document.querySelectorAll('img[src]'));
    images.forEach((img) => {
        if (!img || img.closest('picture')) return;
        if (img.classList.contains('logo-emblem') || img.classList.contains('site-logo')) return;
        const src = img.getAttribute('src') || '';
        if (!src) return;
        if (/^https?:\/\//i.test(src)) return;
        if (!/\.(jpe?g|png)(\?.*)?$/i.test(src)) return;

        const webpSrc = src.replace(/\.(jpe?g|png)(\?.*)?$/i, '.webp$2');
        const picture = document.createElement('picture');
        const source = document.createElement('source');
        source.setAttribute('type', 'image/webp');
        source.setAttribute('srcset', webpSrc);
        picture.appendChild(source);
        img.parentNode.insertBefore(picture, img);
        picture.appendChild(img);
    });
}

function ensureIconActionLabels() {
    const actionable = document.querySelectorAll('a, button');
    actionable.forEach((el) => {
        if (el.getAttribute('aria-label')) return;
        const text = (el.textContent || '').replace(/\s+/g, ' ').trim();
        if (text) return;
        if (!el.querySelector('i, svg, img')) return;

        const href = el.getAttribute('href') || '';
        if (href.startsWith('tel:')) {
            el.setAttribute('aria-label', 'Telefon ile ara');
            return;
        }
        if (href.includes('wa.me') || href.includes('whatsapp')) {
            el.setAttribute('aria-label', 'WhatsApp ile iletisime gec');
            return;
        }
        if (el.classList.contains('mobile-menu-btn')) {
            el.setAttribute('aria-label', 'Menuyu ac veya kapat');
            return;
        }
        el.setAttribute('aria-label', 'Eylem dugmesi');
    });
}

function normalizeHeadingHierarchy() {
    const main = document.querySelector('main');
    if (!main) return;

    const headings = Array.from(main.querySelectorAll('h1, h2, h3, h4, h5, h6'));
    if (!headings.length) return;

    let prevLevel = 0;
    headings.forEach((heading, index) => {
        const currentLevel = Number(heading.tagName.slice(1));
        if (Number.isNaN(currentLevel)) return;

        let targetLevel = currentLevel;
        if (index === 0) {
            targetLevel = 1;
        } else if (currentLevel > prevLevel + 1) {
            // Prevent skipped levels: h2 -> h4 becomes h3, h1 -> h4 becomes h2.
            targetLevel = prevLevel + 1;
        }

        if (targetLevel !== currentLevel) {
            const replacement = document.createElement(`h${targetLevel}`);
            Array.from(heading.attributes).forEach((attr) => replacement.setAttribute(attr.name, attr.value));
            replacement.innerHTML = heading.innerHTML;
            heading.replaceWith(replacement);
            prevLevel = targetLevel;
            return;
        }

        prevLevel = currentLevel;
    });
}

async function localizeHardcodedUi(lang) {
    const isSupported = lang && lang !== 'tr' && UI_TRANSLATABLE_LANGS.has(lang);
    const selector = [
        'main h1',
        'main h2',
        'main h3',
        'main p',
        'main li',
        'main a.btn-primary',
        'main button.btn-primary'
    ].join(', ');

    const nodes = Array.from(document.querySelectorAll(selector))
        .filter((el) => !el.hasAttribute('data-i18n') && !el.closest('[data-i18n]'))
        .filter((el) => el.children.length === 0);

    if (!nodes.length) return;

    if (!isSupported) {
        nodes.forEach((el) => {
            if (el.dataset.originalText) {
                el.textContent = el.dataset.originalText;
            }
        });
        return;
    }

    await Promise.all(nodes.map(async (el) => {
        const raw = (el.dataset.originalText || el.textContent || '').trim();
        if (!raw) return;
        if (!el.dataset.originalText) el.dataset.originalText = raw;
        const translated = await translateUiText(el.dataset.originalText, lang);
        if (translated) el.textContent = translated;
    }));
}

async function localizeDynamicAttributes(lang) {
    const targets = Array.from(
        document.querySelectorAll('input[placeholder], textarea[placeholder], img[alt], [aria-label], button, a')
    );
    const shouldTranslate = lang && lang !== 'tr' && UI_TRANSLATABLE_LANGS.has(lang);

    for (const el of targets) {
        const attrs = ['placeholder', 'alt', 'aria-label', 'title'];
        for (const attr of attrs) {
            const value = (el.getAttribute(attr) || '').trim();
            if (!value) continue;
            const originalAttrKey = `data-orig-${attr}`;
            if (!el.getAttribute(originalAttrKey)) el.setAttribute(originalAttrKey, value);
            const originalAttrValue = el.getAttribute(originalAttrKey) || value;
            if (!shouldTranslate) {
                el.setAttribute(attr, originalAttrValue);
                continue;
            }
            const translatedAttr = await translateUiText(originalAttrValue, lang);
            if (translatedAttr) el.setAttribute(attr, translatedAttr);
        }

        if (el.matches('button, a') && !el.hasAttribute('data-i18n') && el.children.length === 0) {
            const rawText = (el.dataset.originalText || el.textContent || '').trim();
            if (!rawText) continue;
            if (!el.dataset.originalText) el.dataset.originalText = rawText;
            if (!shouldTranslate) {
                el.textContent = el.dataset.originalText;
                continue;
            }
            const translatedText = await translateUiText(el.dataset.originalText, lang);
            if (translatedText) el.textContent = translatedText;
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    initPageLoader();
    document.body.classList.remove('accessibility-mode');
    localStorage.removeItem('accessibilityMode');
    renderHeader();
    renderFooter();
    renderFeaturedArticles();
    handleHeaderScroll();
    initStaggerAnimations();
    initScrollReveal();
    applyLanguage(currentLang);
    upgradeImagesToPictureWebp();
    optimizeImageDelivery();
    ensureIconActionLabels();
    normalizeHeadingHierarchy();
    window.setTimeout(normalizeHeadingHierarchy, 900);
    localizeHardcodedUi(currentLang);
    localizeDynamicAttributes(currentLang);
    translateBlogDetailContent(currentLang);
    window.setTimeout(() => translateBlogDetailContent(currentLang), 700);
    optimizeMobileArticleReadability();
    window.setTimeout(optimizeMobileArticleReadability, 900);
    scrubPublicContactData();
    window.setTimeout(scrubPublicContactData, 500);
    initContinuousContactScrub();
    initDelayedLegalAssistant(); /* LCP iyileştirmesi: Etkileşime kadar geciktir */
    initHeroSlider();
    initPageHeaderSlider();
    initQuickCompensationCalculator();
    ensureSeoMetaTags();
    injectResponsiveSeoOverrides();

    document.addEventListener('click', closeLangDropdownOutside);
    document.addEventListener('touchend', closeLangDropdownOutside);
});

function initPageLoader() {
    const loader = document.getElementById('page-loader');
    if (!loader) return;

    let hidden = false;
    const hideLoader = () => {
        if (hidden) return;
        hidden = true;
        loader.classList.add('is-hidden');
        window.setTimeout(() => {
            if (loader && loader.parentNode) loader.parentNode.removeChild(loader);
        }, 420);
    };

    // Hide shortly after first paint for fast pages
    requestAnimationFrame(() => {
        window.setTimeout(hideLoader, 120);
    });

    // Also hide on full load and with hard fallback
    window.addEventListener('load', hideLoader, { once: true });
    window.setTimeout(hideLoader, 3000);
}

function initHeroSlider() {
    const slides = document.querySelectorAll('.hero-slide');
    if (!slides.length) return;
    let idx = 0;
    slides[0].classList.add('active');
    setInterval(() => {
        slides[idx].classList.remove('active');
        idx = (idx + 1) % slides.length;
        slides[idx].classList.add('active');
    }, 5000);
}

function initPageHeaderSlider() {
    const slides = document.querySelectorAll('.page-header-slide');
    if (!slides.length) return;
    let idx = 0;
    slides[0].classList.add('active');
    setInterval(() => {
        slides[idx].classList.remove('active');
        idx = (idx + 1) % slides.length;
        slides[idx].classList.add('active');
    }, 5000);
}

function loadLegalAssistant() {
    const base = getBasePath();
    if (!document.querySelector('#legal-assistant-css')) {
        const link = document.createElement('link');
        link.id = 'legal-assistant-css';
        link.rel = 'stylesheet';
        link.href = base + 'css/legal-assistant.css';
        document.head.appendChild(link);
    }
    if (!document.querySelector('#legal-assistant-js')) {
        const script = document.createElement('script');
        script.id = 'legal-assistant-js';
        script.src = base + 'js/legal-assistant.js';
        script.defer = true;
        document.body.appendChild(script);
    }
}

/**
 * Hukuk Asistanı: Kullanıcı etkileşimine (scroll, click, touch) kadar yükleme.
 * LCP süresini 2 sn altına indirmek için ağır JS/CSS'i geciktirir.
 */
function initDelayedLegalAssistant() {
    let loaded = false;
    function loadOnInteraction() {
        if (loaded) return;
        loaded = true;
        loadLegalAssistant();
        document.removeEventListener('scroll', loadOnInteraction, { passive: true });
        document.removeEventListener('click', loadOnInteraction);
        document.removeEventListener('touchstart', loadOnInteraction, { passive: true });
        document.removeEventListener('keydown', loadOnInteraction);
    }
    document.addEventListener('scroll', loadOnInteraction, { passive: true });
    document.addEventListener('click', loadOnInteraction);
    document.addEventListener('touchstart', loadOnInteraction, { passive: true });
    document.addEventListener('keydown', loadOnInteraction);
}

// Helper to get base path
function getBasePath() {
    const path = window.location.pathname;
    if (path.includes('/blog/')) {
        return '../';
    } else if (path.includes('/faaliyet-alanlari/')) {
        const afterFaaliyet = path.split('faaliyet-alanlari/')[1];
        if (afterFaaliyet) {
            const parts = afterFaaliyet.split('/').filter(p => p.length > 0);
            if (parts.length >= 2) {
                return '../../';
            }
        }
        return '../';
    }
    return '';
}

function getLogoEmblemSrc() {
    const iconFile = (typeof siteConfig !== 'undefined' && siteConfig.logoIcon) ? siteConfig.logoIcon : '/images/logo-emblem.png';
    const version = '20260626';
    const file = iconFile.replace(/^\/+/, '');

    if (window.location.protocol === 'file:') {
        return `${getBasePath()}${file}?v=${version}`;
    }
    return `/${file}?v=${version}`;
}

function getLogoSrc() {
    const configured = (typeof siteConfig !== 'undefined' && siteConfig.logo) ? siteConfig.logo : '/images/logo-aysenur-avci.png';
    const file = configured.replace(/^\/+/, '');
    const version = '20260626';

    if (window.location.protocol === 'file:') {
        return `${getBasePath()}${file}?v=${version}`;
    }

    return `/${file}?v=${version}`;
}

// Language Switching Logic
function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('siteLang', lang);
    applyLanguage(lang);
    
    // Re-render components that have dynamic text to ensure they get new translations
    renderHeader();
    renderFooter();
    renderFeaturedArticles();
    ensureIconActionLabels();
    localizeHardcodedUi(lang);
    localizeDynamicAttributes(lang);
    translateBlogDetailContent(lang);
    optimizeMobileArticleReadability();
    scrubPublicContactData();
    ensureSeoMetaTags();
    window.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang } }));
}

function applyLanguage(lang) {
    // Set HTML dir attribute for Arabic
    document.documentElement.dir = (lang === 'ar') ? 'rtl' : 'ltr';
    document.documentElement.lang = lang;

    // Translate all elements with data-i18n attribute
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        const translated = getTranslatedValue(lang, key);
        if (translated) {
            // Special handling for elements with icons or specific structures
            if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                el.placeholder = translated;
            } else {
                // If it has icons, we might need to be careful, but here we usually just replace text
                // For safety in this project, we'll just set textContent or innerHTML if needed
                el.innerHTML = translated;
            }
        }
    });

    // Update placeholders separately if needed
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        const translated = getTranslatedValue(lang, key);
        if (translated) {
            el.placeholder = translated;
        }
    });

    // Update meta descriptions if they have data-i18n-content
    document.querySelectorAll('[data-i18n-content]').forEach(el => {
        const key = el.getAttribute('data-i18n-content');
        const translated = getTranslatedValue(lang, key);
        if (translated) {
            el.setAttribute('content', translated.replace(/<br>/g, ' '));
        }
    });
    
    // Re-run Lucide icons because innerHTML might have cleared them
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
}

// Render Header
function renderHeader() {
    const header = document.getElementById('site-header');
    if (!header) return;

    const basePath = getBasePath();
    const lang = currentLang;
    const langFlagMap = {
        tr: 'tr',
        en: 'gb',
        de: 'de',
        ar: 'sa',
        ru: 'ru',
        fr: 'fr'
    };
    const currentFlagCode = langFlagMap[lang] || 'tr';
    const currentFlagAlt = (lang || 'tr').toUpperCase();

    const langDropdownHtml = `
        <div class="lang-grid">
            <button onclick="setLanguage('tr')" class="lang-option ${lang === 'tr' ? 'active' : ''}">
                <img src="https://flagcdn.com/w40/tr.png" alt="TR" width="40" height="27"> Türkçe
            </button>
            <button onclick="setLanguage('en')" class="lang-option ${lang === 'en' ? 'active' : ''}">
                <img src="https://flagcdn.com/w40/gb.png" alt="EN" width="40" height="27"> English
            </button>
            <button onclick="setLanguage('de')" class="lang-option ${lang === 'de' ? 'active' : ''}">
                <img src="https://flagcdn.com/w40/de.png" alt="DE" width="40" height="27"> Deutsch
            </button>
            <button onclick="setLanguage('ar')" class="lang-option ${lang === 'ar' ? 'active' : ''}">
                <img src="https://flagcdn.com/w40/sa.png" alt="AR" width="40" height="27"> العربية
            </button>
            <button onclick="setLanguage('ru')" class="lang-option ${lang === 'ru' ? 'active' : ''}">
                <img src="https://flagcdn.com/w40/ru.png" alt="RU" width="40" height="27"> Русский
            </button>
            <button onclick="setLanguage('fr')" class="lang-option ${lang === 'fr' ? 'active' : ''}">
                <img src="https://flagcdn.com/w40/fr.png" alt="FR" width="40" height="27"> Français
            </button>
        </div>
    `;

    const brandName = (typeof siteConfig !== 'undefined' && siteConfig.brandName) ? siteConfig.brandName : 'AV. AYŞENUR AVCI HUKUK BÜROSU';
    const brandLabel = translations[lang]['nav-corporate-brand'] || brandName;

    header.innerHTML = `
        <div class="header-inner">
            <a href="/" class="logo-wrapper" aria-label="${brandName} - Anasayfaya git">
                <span class="logo-title" data-i18n="nav-corporate-brand">${brandLabel}</span>
            </a>
            
            <nav id="main-navigation" class="header-nav">
                <ul class="nav-list">
                    ${renderNavigationHtml(basePath)}
                </ul>
            </nav>

            <div class="header-actions">
                <!-- Language (Desktop) - icon + text aligned -->
                <div class="header-lang-desktop nav-item" id="header-lang-desktop-trigger" role="button" tabindex="0" aria-label="Dil seçimi" aria-expanded="false">
                    <button type="button" class="header-lang-btn" aria-label="Dil seçimi - Türkçe, İngilizce ve diğer diller">
                        <img src="https://flagcdn.com/w40/${currentFlagCode}.png" alt="${currentFlagAlt}" class="lang-icon" width="20" height="15">
                        <span class="lang-text" data-i18n="nav-language">${translations[lang]['nav-language']}</span>
                    </button>
                    <div class="dropdown-menu lang-dropdown">${langDropdownHtml}</div>
                </div>
                <!-- Language (Mobile) -->
                <div class="header-lang-mobile nav-item" id="header-lang-trigger" role="button" tabindex="0" aria-label="Dil seçimi" aria-expanded="false">
                    <button type="button" class="header-lang-btn" aria-label="Dil seçimi - Türkçe, İngilizce ve diğer diller">
                        <img src="https://flagcdn.com/w40/${currentFlagCode}.png" alt="${currentFlagAlt}" class="lang-icon" width="20" height="15">
                    </button>
                    <div class="dropdown-menu lang-dropdown">${langDropdownHtml}</div>
                </div>
                <button class="mobile-menu-btn" onclick="toggleMobileMenu()" aria-label="Ana menüyü aç veya kapat">
                    <i data-lucide="menu"></i>
                </button>
            </div>
        </div>
        
        <!-- Mobile Drawer -->
        <div id="mobile-drawer" class="mobile-drawer">
            <button onclick="toggleMobileMenu()" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; color: white;">
                <i data-lucide="x"></i>
            </button>
            <div class="mobile-nav-list">
                ${renderMobileNavigationHtml(basePath)}
                
                <!-- Mobile Language Select -->
                <div class="mobile-nav-item">
                    <div class="mobile-nav-link" onclick="this.nextElementSibling.classList.toggle('active')">
                        <span data-i18n="nav-language">${translations[lang]['nav-language']}</span>
                        <i data-lucide="chevron-down" style="width: 16px; float: right;"></i>
                    </div>
                    <div class="mobile-sub-menu">
                        <button onclick="setLanguage('tr')" class="mobile-lang-opt">
                            <img src="https://flagcdn.com/w40/tr.png" alt="TR" width="40" height="27"> Türkçe
                        </button>
                        <button onclick="setLanguage('en')" class="mobile-lang-opt">
                            <img src="https://flagcdn.com/w40/gb.png" alt="EN" width="40" height="27"> English
                        </button>
                        <button onclick="setLanguage('de')" class="mobile-lang-opt">
                            <img src="https://flagcdn.com/w40/de.png" alt="DE" width="40" height="27"> Deutsch
                        </button>
                        <button onclick="setLanguage('ar')" class="mobile-lang-opt">
                            <img src="https://flagcdn.com/w40/sa.png" alt="AR" width="40" height="27"> العربية
                        </button>
                        <button onclick="setLanguage('ru')" class="mobile-lang-opt">
                            <img src="https://flagcdn.com/w40/ru.png" alt="RU" width="40" height="27"> Русский
                        </button>
                        <button onclick="setLanguage('fr')" class="mobile-lang-opt">
                            <img src="https://flagcdn.com/w40/fr.png" alt="FR" width="40" height="27"> Français
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `;
    lucide.createIcons();

    const langTrigger = header.querySelector('#header-lang-trigger');
    if (langTrigger) {
        langTrigger.addEventListener('click', (e) => {
            if (e.target.closest('.lang-option')) return;
            e.stopPropagation();
            e.preventDefault();
            const isOpen = langTrigger.classList.toggle('open');
            langTrigger.setAttribute('aria-expanded', isOpen);
        });
    }
    const langTriggerDesktop = header.querySelector('#header-lang-desktop-trigger');
    if (langTriggerDesktop) {
        langTriggerDesktop.addEventListener('click', (e) => {
            if (e.target.closest('.lang-option')) return;
            e.stopPropagation();
            e.preventDefault();
            const isOpen = langTriggerDesktop.classList.toggle('open');
            langTriggerDesktop.setAttribute('aria-expanded', isOpen);
        });
    }
}

function toggleMobileMenu() {
    const drawer = document.getElementById('mobile-drawer');
    if (drawer) drawer.classList.toggle('open');
}

function closeLangDropdownOutside(e) {
    const langMobile = document.querySelector('.header-lang-mobile.open');
    if (langMobile && !langMobile.contains(e.target)) {
        langMobile.classList.remove('open');
        langMobile.setAttribute('aria-expanded', 'false');
    }
    const langDesktop = document.querySelector('.header-lang-desktop.open');
    if (langDesktop && !langDesktop.contains(e.target)) {
        langDesktop.classList.remove('open');
        langDesktop.setAttribute('aria-expanded', 'false');
    }
}

function renderMobileNavigationHtml(basePath) {
    const lang = currentLang;
    return siteConfig.mainNav.map(item => {
        const href = item.href.startsWith('/') ? basePath + item.href.substring(1) : item.href;
        const titleKey = getNavTitleKey(item);
        const title = translations[lang][titleKey] || item.title;

        if (item.items) {
            return `
                <div class="mobile-nav-item">
                    <div class="mobile-nav-link" onclick="this.nextElementSibling.classList.toggle('active')">
                        <span data-i18n="${titleKey}">${title}</span> <i data-lucide="chevron-down" style="width: 16px; float: right;"></i>
                    </div>
                    <div class="mobile-sub-menu">
                        ${item.items.map(sub => {
                            const subTitle = translations[lang][sub.slug] || sub.title;
                            if (sub.services) {
                                return `
                                    <div style="margin-bottom: 10px;">
                                        <div style="color: #666; font-size: 12px; margin-bottom: 5px;" data-i18n="${sub.slug}">${subTitle}</div>
                                        ${sub.services.map(s => {
                                            const sTitle = translations[lang][s.slug] || s.title;
                                            return `<a href="${basePath}faaliyet-alanlari/${sub.slug}/${s.slug}.html" style="display: block; font-size: 14px; margin-bottom: 5px;" data-i18n="${s.slug}">${sTitle}</a>`;
                                        }).join('')}
                                    </div>
                                `;
                            }
                            return `<a href="${basePath}${item.slug || 'blog'}/${sub.slug}.html" style="display: block; margin-bottom: 10px;" data-i18n="${sub.slug}">${subTitle}</a>`;
                        }).join('')}
                    </div>
                </div>
            `;
        }
        return `<div class="mobile-nav-item"><a href="${href}" class="mobile-nav-link" data-i18n="${titleKey}">${title}</a></div>`;
    }).join('');
}

function getNavTitleKey(item) {
    if (item.title === "Anasayfa") return "nav-home";
    if (item.title === "Kurumsal") return "nav-corporate";
    if (item.title === "Faaliyet Alanları") return "nav-practice-areas";
    if (item.title === "Hizmet Bölgelerimiz") return "nav-service-areas";
    if (item.title === "Blog") return "nav-blog";
    if (item.title === "SSS") return "nav-sss";
    if (item.title === "İletişim") return "nav-contact";
    return "";
}

function renderNavigationHtml(basePath) {
    const lang = currentLang;
    let navHtml = '';
    siteConfig.mainNav.forEach(item => {
        const href = item.href.startsWith('/') ? basePath + item.href.substring(1) : item.href;
        const titleKey = getNavTitleKey(item);
        const title = translations[lang][titleKey] || item.title;

        if (item.items) {
            navHtml += `
                <li class="nav-item">
                    <a href="${href}" class="nav-link">
                        <span data-i18n="${titleKey}">${title}</span>
                    </a>
                    <div class="dropdown-menu">
                        ${renderDropdownContent(item, basePath)}
                    </div>
                </li>
            `;
        } else {
            navHtml += `
                <li class="nav-item">
                    <a href="${href}" class="nav-link" data-i18n="${titleKey}">${title}</a>
                </li>
            `;
        }
    });
    return navHtml;
}

function renderDropdownContent(item, basePath) {
    const lang = currentLang;
    if (item.title === "Faaliyet Alanları") {
        return item.items.map(category => {
            const catTitle = translations[lang][category.slug] || category.title;
            return `
                <div class="dropdown-category">
                    <h4 data-i18n="${category.slug}">${catTitle}</h4>
                    <ul>
                        ${category.services.map(service => {
                            const sTitle = translations[lang][service.slug] || service.title;
                            return `<li><a href="${basePath}faaliyet-alanlari/${category.slug}/${service.slug}.html" data-i18n="${service.slug}">${sTitle}</a></li>`;
                        }).join('')}
                    </ul>
                </div>
            `;
        }).join('');
    } else {
        const itemHref = item.href.startsWith('/') ? basePath + item.href.substring(1) : item.href;
        return `
            <div class="dropdown-category" style="grid-column: span 3;">
                <ul style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                    ${item.items.map(subItem => {
                        const subTitle = translations[lang][subItem.slug] || subItem.title;
                        return `<li><a href="${basePath}${item.slug || 'blog'}/${subItem.slug}.html" style="font-size: 14px;" data-i18n="${subItem.slug}">${subTitle}</a></li>`;
                    }).join('')}
                </ul>
            </div>
        `;
    }
}

// Render Footer
function renderFooter() {
    const footer = document.getElementById('site-footer');
    if (!footer) return;

    const basePath = getBasePath();
    const lang = currentLang;
    const brandName = (typeof siteConfig !== 'undefined' && siteConfig.brandName) ? siteConfig.brandName : 'AV. AYŞENUR AVCI HUKUK BÜROSU';
    const logoSrc = getLogoSrc();
    const officeAddress = (typeof siteConfig !== 'undefined' && siteConfig.address) ? siteConfig.address : 'Hacıhalil Mah. 1207 Sk. No:1 Match Office Kat:4, Gebze / Kocaeli';
    const mapQuery = encodeURIComponent((typeof siteConfig !== 'undefined' && siteConfig.mapQuery) ? siteConfig.mapQuery : officeAddress);
    const officialResourcesHtml = OFFICIAL_AUTHORITY_LINKS
        .map(link => `<li><a class="legal-resources-link" href="${link.href}" target="_blank" rel="noopener noreferrer">${getTranslatedValue(lang, link.labelKey, link.defaultLabel)}</a></li>`)
        .join('');

    footer.innerHTML = `
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <a href="/" class="footer-logo-link" aria-label="${brandName} - Anasayfaya git">
                        <img src="${logoSrc}" alt="${brandName}" class="site-logo" height="100" loading="lazy" decoding="async">
                    </a>
                    <p style="font-size: 14px; color: var(--text-gray);" data-i18n="hero-subtitle">
                        ${translations[lang]['hero-subtitle']}
                    </p>
                </div>
                <div class="footer-col">
                    <h4 data-i18n="nav-quick-access">${translations[lang]['nav-quick-access']}</h4>
                    <ul>
                        <li><a href="/" data-i18n="nav-home">${translations[lang]['nav-home']}</a></li>
                        <li><a href="${basePath}kurumsal.html" data-i18n="nav-corporate">${translations[lang]['nav-corporate']}</a></li>
                        <li><a href="${basePath}hizmet-bolgelerimiz.html">Gebze, Tuzla, Kocaeli</a></li>
                        <li><a href="${basePath}makaleler.html" data-i18n="nav-blog">${translations[lang]['nav-blog']}</a></li>
                        <li><a href="${basePath}araclar.html" data-i18n="nav-tools">${translations[lang]['nav-tools'] || 'Hesaplama Araçları'}</a></li>
                        <li><a href="${basePath}iletisim.html" data-i18n="nav-contact">${translations[lang]['nav-contact']}</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4 data-i18n="nav-practice-areas">${translations[lang]['nav-practice-areas']}</h4>
                    <ul>
                        ${siteConfig.mainNav.find(n => n.title === "Faaliyet Alanları").items.map(cat => {
                            const catTitle = translations[lang][cat.slug] || cat.title;
                            return `<li><a href="${basePath}faaliyet-alanlari/${cat.slug}/${cat.services[0].slug}.html" data-i18n="${cat.slug}">${catTitle}</a></li>`;
                        }).join('')}
                    </ul>
                </div>
                <div class="footer-col local-seo-links">
                    <h4 data-i18n="footer-local-guide-title">${getTranslatedValue(lang, 'footer-local-guide-title', 'Gebze Uzman Avukat Rehberi')}</h4>
                    <p class="local-seo-text" style="line-height: 1.8;">
                        AV. AYŞENUR AVCI HUKUK BÜROSU olarak; Gebze bölgesinde
                        <a class="legal-resources-link" href="${basePath}faaliyet-alanlari/aile-hukuku/cekismeli-bosanma.html">Gebze Boşanma Avukatı</a>,
                        <a class="legal-resources-link" href="${basePath}faaliyet-alanlari/icra-iflas/cek-senet.html">Gebze İcra Avukatı</a>,
                        <a class="legal-resources-link" href="${basePath}faaliyet-alanlari/is-hukuku/ise-iade.html">Gebze İş Davası Avukatı</a> ve
                        <a class="legal-resources-link" href="${basePath}faaliyet-alanlari/ceza-hukuku/agir-ceza.html">Gebze Ceza Avukatı</a> alanlarında profesyonel destek sağlıyoruz.
                        Kocaeli ve Gebze avukat iletişim bilgilerimiz için
                        <a class="legal-resources-link" href="${basePath}iletisim.html">iletişim sayfamızı</a> ziyaret edebilirsiniz.
                    </p>
                </div>
                <div class="footer-col legal-resources">
                    <h4 data-i18n="footer-official-links-title">${getTranslatedValue(lang, 'footer-official-links-title', 'Resmi Kurum Linkleri')}</h4>
                    <ul class="legal-resources-list">
                        ${officialResourcesHtml}
                    </ul>
                </div>
            </div>

            <div class="footer-map">
                <h4 data-i18n="footer-map-title">${getTranslatedValue(lang, 'footer-map-title', 'Konum')}</h4>
                <p class="footer-map-address">${officeAddress}</p>
                <div class="footer-map-embed">
                    <iframe
                        src="https://www.google.com/maps?q=${mapQuery}&output=embed"
                        loading="lazy"
                        referrerpolicy="no-referrer-when-downgrade"
                        title="${brandName} - Google Maps Konumu">
                    </iframe>
                </div>
                <a class="footer-map-link" href="https://www.google.com/maps?q=${mapQuery}" target="_blank" rel="noopener noreferrer" data-i18n="footer-map-link">
                    ${getTranslatedValue(lang, 'footer-map-link', 'Google Maps\'te Aç')}
                </a>
            </div>

            <div class="footer-bottom" style="padding-top: 20px;">
                <p style="color: var(--text-gray); font-size: 13px; margin: 0;">
                    &copy; ${new Date().getFullYear()} ${brandName}
                </p>
            </div>
        </div>
    `;
    lucide.createIcons();
}

function scrubPublicContactData() {
    const selectorsToRemove = [
        'a[href^="tel:"]',
        'a[href^="callto:"]',
        'a[href^="sms:"]',
        'a[href^="mailto:"]',
        'a[href*="wa.me"]',
        'a[href*="whatsapp"]',
        'a[onclick*="tel:"]',
        'button[onclick*="tel:"]',
        '[onclick*="tel:"]',
        '[onclick*="wa.me"]',
        '[onclick*="whatsapp"]',
        '#mobile-sticky-call',
        '#legal-assistant-root',
        '.footer-map-bridge'
    ];
    selectorsToRemove.forEach((selector) => {
        document.querySelectorAll(selector).forEach((el) => el.remove());
    });

    const sensitivePatterns = [
        /0553\s*506\s*21\s*25/i,
        /\+90\s*553\s*506\s*21\s*25/i,
        /905535062125/i,
        /avukat@avukataysenuravci\.com\.tr/i,
        /whatsapp/i,
        /şimdi\s*arayın/i,
        /simdi\s*arayin/i,
        /tıkla\s*ara/i,
        /tikla\s*ara/i,
        /hemen\s*ara/i
    ];

    const candidateSelector = 'p, a, span, li, h3, h4, strong, em, small, button';
    document.querySelectorAll(candidateSelector).forEach((el) => {
        // Avoid removing large structural containers (like FAQ lists/sections)
        // that only include a matching word somewhere in descendant content.
        if (el.children.length > 0) return;
        const text = (el.textContent || '').trim();
        if (!text) return;
        if (sensitivePatterns.some((pattern) => pattern.test(text))) {
            el.remove();
        }
    });

    // Clean risky click handlers from any remaining interactive elements.
    document.querySelectorAll('[onclick]').forEach((el) => {
        const onclickValue = String(el.getAttribute('onclick') || '').toLowerCase();
        if (!onclickValue) return;
        if (onclickValue.includes('tel:') || onclickValue.includes('wa.me') || onclickValue.includes('whatsapp')) {
            el.removeAttribute('onclick');
            if (el.tagName === 'A' || el.tagName === 'BUTTON') {
                el.remove();
            }
        }
    });
}

function initContinuousContactScrub() {
    if (!document.body || window.__contactScrubObserverInitialized) return;
    window.__contactScrubObserverInitialized = true;

    let rafId = 0;
    const runScrub = () => {
        if (rafId) return;
        rafId = window.requestAnimationFrame(() => {
            rafId = 0;
            scrubPublicContactData();
        });
    };

    const observer = new MutationObserver(runScrub);
    observer.observe(document.body, { childList: true, subtree: true });
}

function initQuickCompensationCalculator() {
    const button = document.getElementById('calc-on-hesapla');
    if (!button) return;

    const brutInput = document.getElementById('calc-brut-ucret');
    const yilInput = document.getElementById('calc-calisma-yili');
    const result = document.getElementById('calc-on-sonuc');

    button.addEventListener('click', () => {
        const brut = parseFloat(brutInput.value || '0');
        const yil = parseFloat(yilInput.value || '0');

        if (brut <= 0 || yil <= 0) {
            result.textContent = 'Lutfen brut ucret ve calisma yilini gecerli bir degerle girin.';
            return;
        }

        const kidem = brut * yil;
        const ihbarWeek = yil < 0.5 ? 2 : (yil < 1.5 ? 4 : (yil < 3 ? 6 : 8));
        const ihbar = (brut / 30) * ihbarWeek * 7;
        const fmt = new Intl.NumberFormat('tr-TR', { style: 'currency', currency: 'TRY', maximumFractionDigits: 0 });

        result.innerHTML = `
            Tahmini Kidem Tazminati: <strong>${fmt.format(kidem)}</strong><br>
            Tahmini Ihbar Tazminati: <strong>${fmt.format(ihbar)}</strong>
        `;
    });
}

// Render Featured Articles
async function renderFeaturedArticles() {
    const container = document.getElementById('featured-articles');
    if (!container) return;

    const basePath = getBasePath();
    const lang = currentLang;
    const cards = await Promise.all(articles.slice(0, 3).map(async article => {
        const catTitle = translations[lang][article.categorySlug] || article.category;
        const title = await translateUiText(article.title, lang);
        const excerpt = await translateUiText(article.excerpt, lang);
        return `
            <article class="article-card">
                <span class="category" data-i18n="${article.categorySlug}">${catTitle}</span>
                <h3>${title}</h3>
                <p>${excerpt}</p>
                <a href="${basePath}blog/${article.slug}.html" class="read-more">
                    <span data-i18n="blog-read-more">${translations[lang]['blog-read-more']}</span> <i data-lucide="arrow-right" style="width: 14px;"></i>
                </a>
            </article>
        `;
    }));
    container.innerHTML = cards.join('');
    lucide.createIcons();
}

// Header Scroll Effect
function handleHeaderScroll() {
    const header = document.getElementById('site-header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 10) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }
}

// FAQ Toggle Function
function toggleFaq(button) {
    const item = button.parentElement;
    const isActive = item.classList.contains('active');
    
    // Close all other FAQ items
    document.querySelectorAll('.faq-item').forEach(i => {
        i.classList.remove('active');
    });

    // Toggle current item
    if (!isActive) {
        item.classList.add('active');
    }
}

// Scroll Reveal Observer
function initScrollReveal() {
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal').forEach(el => {
        observer.observe(el);
    });
}

// Stagger Animation for Grids
function initStaggerAnimations() {
    const grids = document.querySelectorAll('.article-grid, .faq-list');
    grids.forEach(grid => {
        const children = grid.children;
        Array.from(children).forEach((child, index) => {
            child.classList.add('reveal');
            child.style.transitionDelay = `${index * 0.1}s`;
        });
    });
}
