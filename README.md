<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:3b82f6&height=170&section=header&text=PDF%20Page%20Thumbnails&fontColor=ffffff&fontSize=38&animation=fadeIn" width="100%" alt="PDF Page Thumbnails banner"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2800&pause=900&color=3B82F6&center=true&vCenter=true&width=650&lines=Turn+PDF+pages+into+a+contact+sheet;Browse+long+documents+at+a+glance;Render+files+locally" alt="Typing introduction"/>
<p>Build a labeled thumbnail sheet from a local PDF.</p>
<p><img src="https://img.shields.io/github/license/CyberLoop-dev/pdf-page-thumbnails?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/pdf-page-thumbnails?style=for-the-badge" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/pdf-page-thumbnails?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/pdf-page-thumbnails?style=for-the-badge" alt="Last commit"/></p>
<img src="assets/icon.svg" width="112" alt="Project icon"/>
</div>

## ✨ Overview
PDF Page Thumbnails renders selected pages from a PDF and arranges them into a labeled image grid. It is useful for quickly scanning long documents or creating a visual index.

## 🚀 Features
- ✨ Render PDF pages locally with PyMuPDF
- ✨ Arrange thumbnails into a configurable number of columns
- ✨ Label each thumbnail with its page number
- ✨ Limit the number of rendered pages for large documents
- ✨ Keep the source PDF unchanged

## 🎬 Demo
Run `python main.py report.pdf --output pages.png --columns 4 --max-pages 32` to create a PNG contact sheet.

## ⚡ Quick Start
```bash
python -m pip install -r requirements.txt
python main.py report.pdf --output pages.png --columns 4 --max-pages 32
```

## 🧰 Tech Stack
Python 3.10+, PyMuPDF for PDF rendering, and Pillow for thumbnail layout.

## 🗂️ Folder Structure
```text
.
├── main.py
├── requirements.txt
├── tests/test_main.py
├── assets/icon.svg
├── .gitignore
└── LICENSE
```

## 🧭 Roadmap
- [ ] Add selectable page ranges
- [ ] Add a PDF summary page
- [ ] Add optional JPEG output

## 🤝 Contributing
Issues and focused pull requests are welcome. Include tests for layout helpers and preserve source files.

## 📄 License
Released under the [MIT License](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:3b82f6&height=100&section=footer" width="100%" alt="Animated wave footer"/></div>
