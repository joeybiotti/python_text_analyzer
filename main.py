from text_analyzer import read_text_file, analyze_text
from readability import analyze_reading_level

def main():
    print('Welcome to the Text Analyzer!')
    file_path = input('Please enter the path to the file you want to analyze: ')
    
    try: 
        sample_text = read_text_file(file_path)
    except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
        return
    except ValueError as e:
        print(e)
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    # Text Analysis
    result = analyze_text(sample_text)
    
    print("\nText Analysis Results:")
    print(f"Total Words: {result['word_count']}")
    print(f"Total Sentences: {result['sentence_count']}")
    print(f"Unique Words: {result['unique_words']}")
    print("\nMost Common Words:")
    for word, freq in result['word_frequency'][:10]:  # Limit to top 10 words
        print(f"{word}: {freq}")
    
    # Reading Time Estimation
    average_reading_speed = 200  # Average reading speed in words per minute
    reading_time_minutes = round(result['word_count'] / average_reading_speed, 2)
    print(f"\nEstimated Reading Time: {reading_time_minutes} minutes")
     
    # Readability Analysis   
    try:
        readability_result = analyze_reading_level(sample_text)
        print("\nReadability Analysis Results:")
        print(f"Flesch-Kincaid Grade Level: {readability_result['flesch_kincaid']}")
        print(f"Total Sentences: {readability_result['total_sentences']}")
        print(f"Total Words: {readability_result['total_words']}")
        print(f"Total Syllables: {readability_result['syllables']}")
    except Exception as e: 
        print(f"An error occurred during readability analysis: {e}")
  
if __name__ == "__main__":
    main()