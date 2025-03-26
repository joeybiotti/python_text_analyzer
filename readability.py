import re 

def count_syllables(word):
    vowels = "aeiouy"
    word=word.lower() 
    count=0
    if word[0] in vowels:
        count += 1
    for i in range(1, len(word)):
        if word[i] in vowels and word[i-1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    return max(count,1)

def analyze_reading_level(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    words = re.findall(r'\b\w+\b', text)
    syllables=sum(count_syllables(word) for word in words)
    num_sentences=len(sentences)
    num_words=len(words)
    
    # Fleisch-Kincaid Grade Level formula
    fk_grade=0.39 * (num_words / num_sentences) + 11.8 * (syllables / num_words) - 15.59
    
    print(f"Total words: {num_words}")
    print(f"Total sentences: {num_sentences}")
    print(f"Total syllables: {syllables}")
    print(f"Flesch-Kincaid Grade Level: {fk_grade:.2f}")
    
# sample_text = """
# The quick brown fox jumps over the lazy dog. This is a simple sentence to demonstrate readability scoring. Python makes it easy to calculate metrics like this.
# """
# analyze_reading_level(sample_text)