/**
 * JSON-LD Schema Markup - Attorney, FAQ, Service, Breadcrumb
 * Google YMYL uyumlu yapısal veri
 */
(function() {
    'use strict';

    const SITE_URL = (typeof siteConfig !== 'undefined' && siteConfig.siteUrl) ? siteConfig.siteUrl : (window.location.origin || 'https://avukataysenuravci.com.tr');
    const BRAND_NAME = (typeof siteConfig !== 'undefined' && siteConfig.brandName) ? siteConfig.brandName : 'AV. AYŞENUR AVCI HUKUK BÜROSU';
    const LOGO_URL = SITE_URL + '/images/logo-aysenur-avci.png';

    function getPostalAddressSchema() {
        return {
            '@type': 'PostalAddress',
            streetAddress: 'Hacıhalil Mah. 1207 Sk. No:1 Match Office Kat:4',
            addressLocality: 'Gebze',
            addressRegion: 'Kocaeli',
            addressCountry: 'TR'
        };
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

        const iso = new Date(Date.UTC(year, month - 1, day, 9, 0, 0));
        if (Number.isNaN(iso.getTime())) return null;
        return iso.toISOString();
    }

    function hasSchemaType(typeName) {
        const scripts = Array.from(document.querySelectorAll('script[type="application/ld+json"]'));
        return scripts.some((script) => {
            try {
                const payload = JSON.parse(script.textContent || '{}');
                if (!payload) return false;
                if (payload['@type'] === typeName) return true;
                if (Array.isArray(payload['@graph'])) {
                    return payload['@graph'].some((node) => node && node['@type'] === typeName);
                }
                return false;
            } catch (e) {
                return false;
            }
        });
    }

    function getWebsiteSchema() {
        return {
            '@context': 'https://schema.org',
            '@type': 'WebSite',
            '@id': SITE_URL + '/#website',
            url: SITE_URL,
            name: BRAND_NAME,
            alternateName: 'Ayşenur Avcı Hukuk Bürosu',
            inLanguage: 'tr-TR',
            publisher: {
                '@id': SITE_URL + '/#organization'
            }
        };
    }

    function getOrganizationSchema() {
        return {
            '@context': 'https://schema.org',
            '@type': 'Organization',
            '@id': SITE_URL + '/#organization',
            name: BRAND_NAME,
            legalName: BRAND_NAME,
            url: SITE_URL,
            logo: {
                '@type': 'ImageObject',
                url: LOGO_URL
            },
            address: getPostalAddressSchema(),
            sameAs: [
                'https://www.kocaelibarosu.org.tr',
                'https://www.barobirlik.org.tr'
            ]
        };
    }

    function getHomeLegalGraph() {
        return {
            '@context': 'https://schema.org',
            '@graph': [
                {
                    '@type': 'Attorney',
                    '@id': SITE_URL + '/#attorney',
                    name: BRAND_NAME,
                    legalName: BRAND_NAME,
                    description: 'Gebze merkezli ceza, aile, iş ve gayrimenkul hukuku alanlarında profesyonel avukatlık ve danışmanlık hizmeti.',
                    image: LOGO_URL,
                    url: SITE_URL,
                    address: getPostalAddressSchema(),
                    memberOf: {
                        '@type': 'Organization',
                        name: 'Kocaeli Barosu',
                        url: 'https://www.kocaelibarosu.org.tr'
                    },
                    openingHoursSpecification: [
                        {
                            '@type': 'OpeningHoursSpecification',
                            dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                            opens: '09:00',
                            closes: '18:00'
                        },
                        {
                            '@type': 'OpeningHoursSpecification',
                            dayOfWeek: 'Saturday',
                            opens: '10:00',
                            closes: '14:00'
                        }
                    ],
                    sameAs: [
                        'https://www.turkiye.gov.tr',
                        'https://www.barobirlik.org.tr'
                    ]
                },
                {
                    '@type': 'LegalService',
                    '@id': SITE_URL + '/#legalservice',
                    name: BRAND_NAME,
                    legalName: BRAND_NAME,
                    serviceType: 'Law Firm',
                    additionalType: 'https://schema.org/LawFirm',
                    description: 'Gebze ve Tuzla bölgelerinde profesyonel hukuk danışmanlığı sunan yerel hukuk ofisi.',
                    url: SITE_URL,
                    address: getPostalAddressSchema(),
                    knowsAbout: ['Ceza Hukuku', 'Aile Hukuku', 'Is Hukuku', 'Gayrimenkul Hukuku', 'Icra Iflas Hukuku'],
                    openingHoursSpecification: [
                        {
                            '@type': 'OpeningHoursSpecification',
                            dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                            opens: '09:00',
                            closes: '18:00'
                        },
                        {
                            '@type': 'OpeningHoursSpecification',
                            dayOfWeek: 'Saturday',
                            opens: '10:00',
                            closes: '14:00'
                        }
                    ],
                    provider: {
                        '@type': 'LegalService',
                        name: BRAND_NAME
                    }
                }
            ]
        };
    }

    function getFAQSchema() {
        const faqItems = document.querySelectorAll('.faq-item');
        if (!faqItems.length) return null;
        const mainEntity = Array.from(faqItems).map(item => {
            const q = item.querySelector('.faq-question span');
            const a = item.querySelector('.faq-answer p');
            if (!q || !a) return null;
            return {
                '@type': 'Question',
                name: q.textContent.trim(),
                acceptedAnswer: {
                    '@type': 'Answer',
                    text: a.textContent.trim()
                }
            };
        }).filter(Boolean);
        if (!mainEntity.length) return null;
        return {
            '@context': 'https://schema.org',
            '@type': 'FAQPage',
            mainEntity
        };
    }

    function getBreadcrumbSchema(items) {
        if (!items || !items.length) return null;
        return {
            '@context': 'https://schema.org',
            '@type': 'BreadcrumbList',
            itemListElement: items.map((item, i) => {
                const el = { '@type': 'ListItem', position: i + 1, name: item.name };
                if (item.url) el.item = { '@id': SITE_URL + item.url };
                return el;
            })
        };
    }

    function getArticleSchema(article) {
        if (!article) return null;
        return {
            '@context': 'https://schema.org',
            '@type': 'BlogPosting',
            headline: article.title,
            description: article.excerpt || article.description,
            author: {
                '@type': 'Person',
                name: 'Hukuk Editoru',
                jobTitle: 'Avukat',
                affiliation: {
                    '@type': 'Organization',
                    name: 'Kocaeli Barosu',
                    url: 'https://www.kocaelibarosu.org.tr'
                }
            },
            publisher: {
                '@type': 'Organization',
                name: BRAND_NAME,
                logo: {
                    '@type': 'ImageObject',
                    url: LOGO_URL
                }
            },
            datePublished: article.datePublished || article.date,
            dateModified: article.dateModified || article.date,
            mainEntityOfPage: SITE_URL + window.location.pathname
        };
    }

    function getBlogPostingSchemaFromDom() {
        if (!window.location.pathname.includes('/blog/')) return null;
        const h1 = document.querySelector('main h1');
        if (!h1) return null;

        const descTag = document.querySelector('meta[name="description"]');
        const firstParagraph = document.querySelector('.content-body p, main p');
        const dateInfo = document.querySelector('.meta-info');
        const dateText = dateInfo ? dateInfo.textContent.trim() : '';
        const image = document.querySelector('main img');

        return {
            '@context': 'https://schema.org',
            '@type': 'BlogPosting',
            headline: h1.textContent.trim(),
            description: descTag ? descTag.content : (firstParagraph ? firstParagraph.textContent.trim() : ''),
            datePublished: parseTurkishDateToIso(dateText) || undefined,
            dateModified: parseTurkishDateToIso(dateText) || undefined,
            inLanguage: document.documentElement.lang || 'tr',
            mainEntityOfPage: SITE_URL + window.location.pathname,
            image: image ? image.src : LOGO_URL,
            author: {
                '@type': 'Person',
                name: 'Hukuk Editoru'
            },
            publisher: {
                '@type': 'Organization',
                name: BRAND_NAME,
                logo: {
                    '@type': 'ImageObject',
                    url: LOGO_URL
                }
            }
        };
    }

    function buildPathBreadcrumbItems() {
        const path = window.location.pathname || '/';
        if (path === '/' || path.endsWith('/index.html')) return null;

        const parts = path.replace(/\/+$/, '').split('/').filter(Boolean);
        if (!parts.length) return null;

        const items = [{ name: 'Anasayfa', url: '/' }];
        let cumulative = '';
        for (let i = 0; i < parts.length; i++) {
            cumulative += '/' + parts[i];
            const isLast = i === parts.length - 1;
            let name = parts[i].replace(/\.html$/i, '').replace(/[-_]/g, ' ').trim();
            name = name ? name.charAt(0).toUpperCase() + name.slice(1) : 'Sayfa';
            if (isLast) {
                const h1 = document.querySelector('main h1');
                items.push({ name: h1 ? h1.textContent.trim() : name, url: null });
            } else {
                items.push({ name, url: cumulative });
            }
        }
        return items;
    }

    function getServiceSchema(service) {
        if (!service) return null;
        return {
            '@context': 'https://schema.org',
            '@type': 'Service',
            serviceType: service.name,
            provider: {
                '@type': 'LegalService',
                name: BRAND_NAME
            },
            areaServed: 'TR',
            description: service.description
        };
    }

    function injectSchema(schema) {
        if (!schema) return;
        const script = document.createElement('script');
        script.type = 'application/ld+json';
        script.textContent = JSON.stringify(schema);
        document.head.appendChild(script);
    }

    function init() {
        const path = window.location.pathname;

        if (!hasSchemaType('Organization')) injectSchema(getOrganizationSchema());
        if (!hasSchemaType('WebSite')) injectSchema(getWebsiteSchema());

        if (path === '/' || path.endsWith('index.html')) {
            injectSchema(getHomeLegalGraph());
        }

        if (path === '/' || path.endsWith('index.html') || path.endsWith('sss.html')) {
            const faqSchema = getFAQSchema();
            if (faqSchema) injectSchema(faqSchema);
        }

        const breadcrumbFromPath = buildPathBreadcrumbItems();
        if (breadcrumbFromPath) {
            injectSchema(getBreadcrumbSchema(breadcrumbFromPath));
        }

        const domBlogPosting = getBlogPostingSchemaFromDom();
        if (domBlogPosting && !hasSchemaType('BlogPosting') && !hasSchemaType('Article')) {
            injectSchema(domBlogPosting);
        }

    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
