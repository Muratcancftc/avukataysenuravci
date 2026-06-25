<?php
/**
 * AV. AYŞENUR AVCI Hukuk Asistanı - API Proxy
 * OpenAI veya Gemini API üzerinden güvenli hukuki asistan yanıtları
 */
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed']);
    exit;
}

$input = json_decode(file_get_contents('php://input'), true);
$message = trim($input['message'] ?? '');

if (empty($message) || strlen($message) > 1000) {
    http_response_code(400);
    echo json_encode(['error' => 'Geçersiz mesaj']);
    exit;
}

$configFile = __DIR__ . '/config.php';
if (!file_exists($configFile)) {
    $configFile = __DIR__ . '/config.example.php';
}
$config = file_exists($configFile) ? include $configFile : [];

$systemPrompt = <<<PROMPT
Sen "AV. AYŞENUR AVCI Hukuk Asistanı"sın. Gebze, Kocaeli, Darıca, Çayırova ve Dilovası bölgesindeki hukuki süreçler hakkında kısa, ön bilgilendirme niteliğinde cevaplar veriyorsun.

SİTEDEKİ BLOG KONULARI (referans alabilirsin): İşe iade, kıdem tazminatı, mobbing, boşanma, velayet, nafaka, kira tespit/tahliye, icra takibi, maaş haczi, dolandırıcılık, KVKK, hakaret, ceza davaları, HAGB, sabıka silinmesi, ecrimisil, izale-i şuyu, ipotek fekki, kripto dolandırıcılık, dijital miras, NFT telif hakları vb.

KURALLAR:
- Sadece Türkiye hukuku ve bölgesel (Gebze Adliyesi, Kocaeli Mahkemeleri) bilgisi ver.
- Cevaplar 2-4 cümle, net ve anlaşılır olsun. Önce soruyu cevapla, bilgilendir.
- Avukat-müvekkil ilişkisi kurma, sadece genel bilgi ver.
- WhatsApp veya iletişim önerisi EKLEME. Sadece hukuki bilgi ver.
- Hukuki tavsiye verme, sadece bilgilendirme yap.
PROMPT;

$provider = $config['provider'] ?? 'openai';

try {
    if ($provider === 'gemini' && !empty($config['gemini_api_key'])) {
        $response = callGemini($config['gemini_api_key'], $message, $systemPrompt);
    } elseif (!empty($config['openai_api_key'])) {
        $response = callOpenAI($config['openai_api_key'], $message, $systemPrompt);
    } else {
        http_response_code(503);
        echo json_encode([
            'error' => 'API yapılandırılmamış',
            'fallback' => true,
            'message' => 'API anahtarı tanımlanmamış. config.php dosyasında openai_api_key veya gemini_api_key ekleyin.'
        ]);
        exit;
    }
    echo json_encode(['reply' => $response]);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode([
        'error' => 'API hatası',
        'fallback' => true,
        'message' => 'Şu an yanıt veremiyorum. Lütfen sorunuzu farklı şekilde ifade edin veya WhatsApp üzerinden iletişime geçin.'
    ]);
}

function callOpenAI($apiKey, $message, $systemPrompt) {
    $payload = [
        'model' => 'gpt-4o-mini',
        'messages' => [
            ['role' => 'system', 'content' => $systemPrompt],
            ['role' => 'user', 'content' => $message]
        ],
        'max_tokens' => 400,
        'temperature' => 0.5
    ];

    $ch = curl_init('https://api.openai.com/v1/chat/completions');
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => json_encode($payload),
        CURLOPT_HTTPHEADER => [
            'Content-Type: application/json',
            'Authorization: Bearer ' . $apiKey
        ],
        CURLOPT_TIMEOUT => 30
    ]);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($httpCode !== 200) {
        $err = json_decode($response, true);
        throw new Exception($err['error']['message'] ?? 'API hatası');
    }

    $data = json_decode($response, true);
    return trim($data['choices'][0]['message']['content'] ?? '');
}

function callGemini($apiKey, $message, $systemPrompt) {
    $payload = [
        'contents' => [['parts' => [['text' => $systemPrompt . "\n\nKullanıcı: " . $message]]]],
        'generationConfig' => [
            'maxOutputTokens' => 400,
            'temperature' => 0.5
        ]
    ];

    $url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=' . $apiKey;
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => json_encode($payload),
        CURLOPT_HTTPHEADER => ['Content-Type: application/json'],
        CURLOPT_TIMEOUT => 30
    ]);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($httpCode !== 200) {
        $err = json_decode($response, true);
        throw new Exception($err['error']['message'] ?? 'API hatası');
    }

    $data = json_decode($response, true);
    $text = $data['candidates'][0]['content']['parts'][0]['text'] ?? '';
    return trim($text);
}
