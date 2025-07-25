import os
import json
import fitz  
import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for page_num in range(len(doc)):
        text = doc.load_page(page_num).get_text().strip()
        if text: 
            pages.append({
                "page": page_num + 1,
                "text": text,
                "heading": f"Page {page_num + 1}"
            })
    return pages

def find_relevant_sections(pages, query, top_k=3):
    texts = [p['text'] for p in pages]
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([query] + texts)
    query_vec = vectors[0]
    doc_vecs = vectors[1:]

    scores = cosine_similarity(query_vec, doc_vecs).flatten()
    ranked_pages = sorted(zip(scores, pages), key=lambda x: x[0], reverse=True)

   
    return [p for score, p in ranked_pages[:top_k] if score > 0.03]

def process_documents(input_dir, output_dir, persona, task):
    result = {
        "metadata": {
            "persona": persona,
            "task": task,
            "documents": [],
            "timestamp": datetime.datetime.now().isoformat()
        },
        "results": []
    }

    os.makedirs(output_dir, exist_ok=True)
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

    for filename in pdf_files:
        pdf_path = os.path.join(input_dir, filename)
        pages = extract_text_from_pdf(pdf_path)
        relevant = find_relevant_sections(pages, task)

        result["metadata"]["documents"].append(filename)
        result["results"].append({
            "document": filename,
            "relevant_sections": relevant
        })

    output_path = os.path.join(output_dir, "result.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

def main():
    input_dir = "input"
    output_dir = "output"
    persona = "PhD Student"
    task = "Summarize the latest AI methods"

    process_documents(input_dir, output_dir, persona, task)

if __name__ == "__main__":
    main()
