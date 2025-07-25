# 🔍 Intelligent PDF Section Relevance Analyzer


## 🌟 Overview
A Dockerized solution that automatically identifies and extracts the most relevant sections from PDF documents based on semantic similarity 
to user-defined tasks and personas. Developed for Adobe GenAI Hackathon 2025.

## ✨ Key Features
- **Semantic Analysis** - TF-IDF + Cosine Similarity scoring
- **Persona Adaptation** - Tailors results for researchers, students, etc.
- **Offline Operation** - No internet connection required
- **Fast Processing** - Under 60s for 50-page documents
- **Structured Output** - Clean JSON with page references

##  Project Structure
```text
.
├── app/
│   ├── input/          # PDF input directory (mount point)
│   ├── output/         # JSON results directory
│   └── round2.py         # Core extraction engine
├── Dockerfile          # Production-grade container setup
├── requirements.txt    # Pinned dependencies
└── README.md           # This documentation
