import re 
from collections import Counter 
import os 
from pdminer.high_level import extraxct_text as extract_pdf_text
from docx import Document 
from bs4 import BeautifulSoup

def read_text_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    
    if file_extension == '.txt':
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif file_extension == '.pdf':
        return extract_pdf_text(file_path)
    elif file_extension == '.docx':
        doc = Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    elif file_extension == '.html' or file_extension == '.htm':
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            return soup.get_text()
    else:
        raise ValueError("Unsupported file type. Please provide a .txt, .pdf, .docx, or .html file.")

def analyze_text(text):
    words=re.findall(r'\b\w+\b', text.lower())  
    sentences=re.split(r'[.!?]+', text)  
    
    word_count=len(words)
    sentence_count=len([s for s in sentences if s.strip()])
    unique_words=len(set(words))
    word_frequency=Counter(words).most_common()
    
    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'unique_words': unique_words,
        'word_frequency': word_frequency
    }
