text = input("Enter a sentence: ")

# Replace word
old = input("Enter word to replace: ")
new = input("Enter new word: ")
text = text.replace(old, new)

# Remove extra spaces
text = " ".join(text.split())

# Count substring
sub = input("Enter substring: ")
print("\nProcessed Sentence:", text)
print("Substring Count:", text.count(sub))

# Count palindrome words
words = text.split()
pal = 0
for w in words:
    if w.lower() == w[::-1].lower() and len(w) > 1:
        pal += 1
print("Palindrome Words:", pal)

# Count anagram pairs
ana = 0
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if sorted(words[i].lower()) == sorted(words[j].lower()):
            ana += 1
print("Anagram Pairs:", ana)
