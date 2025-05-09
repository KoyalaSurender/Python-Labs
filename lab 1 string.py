#1. Write a Python program to count the occurrences of each word in a given sentence
 #string = “To change the overall look of your document. To change the look available in the gallery”


string = "To change the overall look of your document. To change the look available in the gallery"
word_list = string.lower().replace('.', '').split()
word_count = {}
for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1
print("1. Word occurrences:\n", word_count)

#2. Write a Python program to remove a newline in Python. String = "\nBest \nDeeptech \nPython \nTraining\n"

string = "\nBest \nDeeptech \nPython \nTraining\n"
clean_string = string.replace('\n', '')
print("\n2. String without newlines:\n", clean_string)

#3. Write a Python program to reverse words in a string.  String = “Deeptech Python Training”

string = "Deeptech Python Training"
reversed_words = ' '.join(reversed(string.split()))
print("\n3. Reversed words:\n", reversed_words)


#4. Write a Python program to count and display the vowels of a given text . String=”Welcome to python Training

string = "Welcome to python Training"
vowels = "aeiou"
vowel_count = {v: string.count(v) for v in vowels if v in string}
print("\n4. Vowel occurrences:\n",vowel_count)

