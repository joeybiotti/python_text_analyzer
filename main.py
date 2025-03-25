from text_analyzer import read_text_file, analyze_text

def main():
    print('Welcome to the Text Analyzer!')
    file_path = input('Please enter the path to the text file you want to analyze: ')
    
    try: 
        sample_text = read_text_file(file_path)
    except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    result = analyze_text(sample_text)
    
    print("\nText Analysis Results:")
    print(f"Total Words: {result['word_count']}")
    print(f"Total Sentences: {result['sentence_count']}")
    print(f"Unique Words: {result['unique_words']}")
    print("\nMost Common Words:")
    for word, freq in result['word_frequency'][:10]:  # Limit to top 10 words
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()