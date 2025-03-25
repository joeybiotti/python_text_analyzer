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
    word_frequency=Counter(words).most_common(5)
    
    print(f"Total words: {word_count}")
    print(f"Total sentences: {sentence_count}")
    print(f"Unique words: {unique_words}")
    print("Most common words:")
    for word in word_frequency:
        print(f"{word[0]}: {word[1]}")
    
sample_text=read_text_file('./texts/great_gatsby.txt') 
analyze_text(sample_text)  