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
    if word.endswith("e") and count > 1:
        count -= 1
    return max(count,1)

def analyze_reading_level(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    words = re.findall(r'\b\w+\b', text)
    syllables = sum(count_syllables(word) for word in words)
    num_sentences = len(sentences)
    num_words = len(words)

    if num_sentences == 0 or num_words == 0:
        return {
            'flesch_kincaid': 0.0,
            'total_words': num_words,
            'total_sentences': num_sentences,
            'syllables': syllables
        }

    # Flesch-Kincaid Grade Level formula
    fk_grade = 0.39 * (num_words / num_sentences) + 11.8 * (syllables / num_words) - 15.59
    # Ensure fk_grade is not negative, as grade levels cannot be negative
    fk_grade = max(round(fk_grade, 2), 0.0)

    return {
        'flesch_kincaid': fk_grade,
        'total_words': num_words,
        'total_sentences': num_sentences,
        'syllables': syllables
    }
