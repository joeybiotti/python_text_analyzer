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
    
    fk_grade = round(fk_grade, 2)
    total_words = num_words
    total_sentences = num_sentences
    syllables = syllables

    return {
        'fk_grade': fk_grade,
        'total_words': total_words,
        'total_sentences': total_sentences,
        'syllables': syllables
    }
    