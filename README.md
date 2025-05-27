# 📱 AlwaysOnGuard Phone Scanner

A powerful, open-source phone number intelligence & OSINT tool.  
Easily analyze phone numbers, get instant details & quick links for open-source investigations!

---

## ✨ Features

- 🌍 Multi-language support (English & Turkish)
- 📞 Detects country, carrier, formats & validity
- 🔗 Provides instant OSINT/search links (Google, WhatsApp, Facebook, Truecaller, etc.)
- 🗃️ Keeps a local log of all queries (`searched_numbers.json`)
- 🎨 Colorful and animated terminal interface

---

## 🚀 Getting Started

### ⬇️ Installation

1. Download the repository files.
2. Install the dependencies with:

   ```bash
   pip install -r requirements.txt
   ```

### ▶️ Usage

```bash
python phonescanner.py
```

---

## 🧐 Example Output

```
> Phone number: +905XXXXXXXXX

[✓] Valid Number: True
[i] Country: Turkey
[i] Operator: Vodafone
[#] International format: +90 5XX XXX XX XX

OSINT Links:
- Google:      https://www.google.com/search?q=+905XXXXXXXXX
- WhatsApp:    https://wa.me/905XXXXXXXXX
- Facebook:    https://www.facebook.com/search/top/?q=+905XXXXXXXXX
...
```

---

## 📋 Logs

All scanned numbers are securely stored in a local file:  
`searched_numbers.json`

---

## 🤝 Contributing

Pull requests are welcome!  
Feel free to open issues for bugs or ideas.

---

## ⚖️ License

MIT

---

---

# 🇹🇷 AlwaysOnGuard Phone Scanner

Güçlü, açık kaynak telefon numarası analiz ve OSINT aracı.  
Telefon numaralarını kolayca analiz et, anında detaylara ulaş, OSINT araştırmaları için hızlı arama linkleri oluştur!

---

## ✨ Özellikler

- 🌍 Çoklu dil desteği (Türkçe & İngilizce)
- 📞 Ülke, operatör, format ve geçerlilik tespiti
- 🔗 Anında OSINT/arama linkleri (Google, WhatsApp, Facebook, Truecaller vb.)
- 🗃️ Tüm sorgular yerel olarak kaydedilir (`searched_numbers.json`)
- 🎨 Renkli ve animasyonlu terminal arayüzü

---

## 🚀 Kurulum

1. Depo dosyalarını indir.
2. Bağımlılıkları yüklemek için:

   ```bash
   pip install -r requirements.txt
   ```

### ▶️ Kullanım

```bash
python phonescanner.py
```

---

## 🧐 Örnek Çıktı

```
> Telefon numarası: +905XXXXXXXXX

[✓] Geçerli Numara: True
[i] Ülke: Turkey
[i] Operatör: Vodafone
[#] Uluslararası biçim: +90 5XX XXX XX XX

OSINT Linkleri:
- Google:      https://www.google.com/search?q=+905XXXXXXXXX
- WhatsApp:    https://wa.me/905XXXXXXXXX
- Facebook:    https://www.facebook.com/search/top/?q=+905XXXXXXXXX
...
```

---

## 📋 Kayıtlar

Tüm sorgulanan numaralar güvenli şekilde yerel dosyada tutulur:  
`searched_numbers.json`

---

## 🤝 Katkı

Pull request gönderebilir, hata ve önerilerinizi issue açarak iletebilirsiniz.

---

## ⚖️ Lisans

MIT
