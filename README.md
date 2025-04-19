#      🟡 WHOISLOOKUP - Domain Lookup CLI Tool

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![Status](https://img.shields.io/badge/Open%20Source-Yes-success)

A lightweight, colorful Python command-line tool to fetch WHOIS information for one or more domain names.

---

## 📦 Features

- ✅ Lookup multiple domains at once
- 🎨 Color-coded output for clean readability
- ⚠️ Graceful handling of unsupported or invalid domains
- 🧠 Handles WHOIS edge cases (like lists, missing fields)
- 💻 Works right in your terminal — no GUI needed

---

## 🛠️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/AyedAA/whoislookup.git
cd whoislookup
pip install -r requirements.txt
```

---

## 💻 Usage

```bash
python whoislookup.py example.com github.com
```

### 🖥️ Example output:

```yaml
📡 WHOIS Information for: github.com

Domain:     github.com
Registrar:  MarkMonitor Inc.
Created on: 2007-03-26
Expired on: 2025-03-25
```

---

## ⚠️ TLD Limitations

Some domain types like `.edu`, `.gov`, or country-specific TLDs may not return WHOIS data due to:
- Registry restrictions
- Specialized WHOIS servers
- Authentication/CAPTCHA blocks

This tool will still handle errors cleanly and let you know what's unsupported.

---

## 🧾 License

Licensed under the [MIT License](LICENSE)

---

## ✨ Author

Made by **Note**  
GitHub: [AyedAA](https://github.com/AyedAA)


