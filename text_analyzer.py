import re 
from collections import Counter 

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

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

sample_text=read_text_file('./texts/great_gatsby.txt') 
result=analyze_text(sample_text)

print(f"Total words: {result['word_count']}")
print(f"Total sentences: {result['sentence_count']}")
print(f"Unique words: {result['unique_words']}")
print(f"Most common words: {result['word_frequency']}")

