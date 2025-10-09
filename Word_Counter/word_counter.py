def word_counter(text):
    text = text.lower()
    for ch in ['.', ',', '?', '!', ':', ';']:
        text = text.replace(ch, '')
    words = text.split()

    total_words = len(words)
    total_chars = len(text)

    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    print("🔹 Total Words:", total_words)
    print("🔹 Total Characters:", total_chars)
    print("\n🔹 Word Frequency:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

user_input = input("Enter your text:\n")
word_counter(user_input)
