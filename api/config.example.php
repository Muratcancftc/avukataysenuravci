<?php
/**
 * AV. AYŞENUR AVCI Hukuk Asistanı - API Yapılandırması
 * Bu dosyayı config.php olarak kopyalayın ve API anahtarınızı ekleyin.
 * config.php .gitignore'a eklenmelidir (API anahtarı güvenliği için).
 */
return [
    'openai_api_key' => '',  // OpenAI API Key: sk-...
    'gemini_api_key' => '',  // Alternatif: Google Gemini API Key
    'provider' => 'openai',  // 'openai' veya 'gemini'
];
