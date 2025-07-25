# 📄 PDF Outline Extractor  

## 🌟 Overview
A lightweight Python solution that automatically extracts hierarchical document outlines from PDFs using font-based analysis. Designed for academic/technical documents with 100% offline operation.

## ✨ Key Features
| Feature | Description |
|---------|-------------|
| 🔍 **Heading Detection** | Identifies H1/H2/H3 via font size analysis |
| 🏷 **Metadata Extraction** | Captures document title and page numbers |
| 📦 **Docker Support** | Pre-configured for linux/amd64 environments |
| ⚡ **Fast Processing** | <10s for 50-page documents |
| 🚫 **No Internet Required** | Fully offline operation |

## 📂 Project Structure
```text
.
├── app/
│   ├── input/          # Input PDFs (mount point)
│   ├── output/         # Generated JSON files
│   └── main.py         # Core extraction logic
├── tests/              # Test cases (pytest)
├── Dockerfile          # Container configuration
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
