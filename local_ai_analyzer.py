import os
import re
import csv
import json
from collections import defaultdict

try:
    import fitz  # PyMuPDF
    has_pymupdf = True
except ImportError:
    has_pymupdf = False

try:
    import spacy
    has_spacy = True
except ImportError:
    has_spacy = False

try:
    import pytesseract
    from pdf2image import convert_from_path
    has_ocr = True
except ImportError:
    has_ocr = False

# Setup paths
PDF_DIR = r"c:\PDFs"
OUTPUT_DIR = os.path.join(PDF_DIR, "Analysis_Output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Target keywords to track specifically
TARGET_KEYWORDS = ["Tannehill", "Busby", "East", "Beavers", "Driskell", "Crowder", "Osteen", "Sessums", "Pruitt", "Childers", "Little", "Tollison", "MacArthur", "FOIA"]

if has_spacy:
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        import subprocess
        print("Downloading spaCy model...")
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
        nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    text = ""
    # Try PyMuPDF first
    if has_pymupdf:
        try:
            doc = fitz.open(pdf_path)
            for page in doc:
                text += page.get_text() + "\n"
            doc.close()
        except Exception as e:
            print(f"PyMuPDF failed on {pdf_path}: {e}")
            
    # If text is suspiciously short, it might be a scanned image
    if len(text.strip()) < 100 and has_ocr:
        print(f"Very little text found in {pdf_path}. Attempting OCR...")
        try:
            images = convert_from_path(pdf_path, dpi=200)
            ocr_text = ""
            for img in images:
                ocr_text += pytesseract.image_to_string(img) + "\n"
            text = ocr_text
        except Exception as e:
            print(f"OCR failed on {pdf_path}: {e}")
            
    return text

def analyze_text(text, filename):
    entities = defaultdict(set)
    
    if has_spacy:
        # truncate text for spacy if too long
        spacy_text = text[:990000]
        doc = nlp(spacy_text)
        for ent in doc.ents:
            if ent.label_ in ["PERSON", "ORG", "DATE", "GPE"]:
                entities[ent.label_].add(ent.text.strip().replace('\n', ' '))
            
    # Hunt for target keywords
    keyword_mentions = []
    text_lower = text.lower()
    for kw in TARGET_KEYWORDS:
        if kw.lower() in text_lower:
            keyword_mentions.append(kw)
            
    return {
        "filename": filename,
        "keywords_found": keyword_mentions,
        "PERSON": list(entities["PERSON"]),
        "ORG": list(entities["ORG"]),
        "DATE": list(entities["DATE"]),
        "GPE": list(entities["GPE"])
    }

def main():
    print("Starting local extraction and analysis...")
    results = []
    
    # Process files
    files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith('.pdf')]
    print(f"Found {len(files)} PDF files.")
    
    for idx, filename in enumerate(files):
        print(f"[{idx+1}/{len(files)}] Processing {filename}...")
        filepath = os.path.join(PDF_DIR, filename)
        
        text = extract_text_from_pdf(filepath)
        if not text.strip():
            print(f"  -> No text extracted.")
            continue
            
        analysis = analyze_text(text, filename)
        results.append(analysis)
        
    # Save results
    report_path = os.path.join(OUTPUT_DIR, "master_analysis.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
        
    print(f"\nAnalysis complete! Saved JSON report to {report_path}")
    
    # Generate Markdown Summary
    md_path = os.path.join(OUTPUT_DIR, "summary_report.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Master Analysis Report\n\n")
        f.write("## Target Keyword Mentions by File\n")
        for res in results:
            if res['keywords_found']:
                f.write(f"- **{res['filename']}**: {', '.join(res['keywords_found'])}\n")
                
    print(f"Saved Markdown summary to {md_path}")

if __name__ == "__main__":
    main()
