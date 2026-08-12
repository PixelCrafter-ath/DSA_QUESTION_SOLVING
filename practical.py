# 1. String Length
s = input("Enter string: ")
count = 0
for i in s:
    count += 1
print("Length =", count)


# 2. Character Count
s = input("Enter string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0
for ch in s:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special =", special)


# 3. Reverse a String

s = input("Enter string: ")
reverse = ""

for ch in s:
   reverse = ch + reverse

print("Reverse =", reverse)


# 4. Palindrome Check
s = input("Enter string: ")
reverse = ""
for ch in s:
    reverse = ch + reverse
if s == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# 5. Uppercase and Lowercase Count
s = input("Enter string: ")
upper = 0
lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase =", upper)
print("Lowercase =", lower)


# 6. Replace Characters
s = input("Enter string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")
result = ""
for ch in s:
    if ch == old:
        result += new
    else:
        result += ch
print(result)


# 7. Remove Spaces
s = input("Enter string: ")
result = ""
for ch in s:
    if ch != " ":
        result += ch
print(result)


# 8. Frequency of a Character
s = input("Enter string: ")
ch = input("Enter character: ")
count = 0
for x in s:
    if x == ch:
        count += 1
print("Frequency =", count)


# 9. First and Last Character
s = input("Enter string: ")
print("First character =", s[0])
print("Last character =", s[-1])


# 10. ASCII Values
s = input("Enter string: ")
for ch in s:
    print(ch, "=", ord(ch))


# 11. Word Count
s = input("Enter sentence: ")
words = s.split()
print("Number of words =", len(words))


# 12. Longest Word

s = input("Enter sentence: ")
words = s.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word =", longest)


# 13. Shortest Word
s = input("Enter sentence: ")

words = s.split()
shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print("Shortest word =", shortest)


# 14. Title Case

s = input("Enter sentence: ")
words = s.split()
result = ""
for word in words:
    result += word[0].upper() + word[1:] + " "
print(result)


# 15. Duplicate Characters
s = input("Enter string: ")
for ch in s:
    if s.count(ch) > 1:
        print(ch)


# 16. Character Frequency

s = input("Enter string: ")
for ch in s:
    print(ch, "=", s.count(ch))


# 17. Anagram Check

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")


# 18. Remove Duplicate Characters
s = input("Enter string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch

print(result)


# 19. Substring Search

s = input("Enter main string: ")
sub = input("Enter substring: ")
if sub in s:
    print("Substring found")
else:
    print("Substring not found")


# 20. Count Occurrences of a Word

sentence = input("Enter sentence: ")
word = input("Enter word: ")
words = sentence.split()
count = 0
for w in words:
    if w == word:
        count += 1
print("Count =", count)


# 21. Password Validator

password = input("Enter password: ")
upper = False
lower = False
digit = False
special = False
for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True
if len(password) >= 8 and upper and lower and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")


# 22. Run-Length Encoding

s = input("Enter string: ")
result = ""
count = 1
for i in range(len(s)):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1
print(result)


# 23. String Compression

s = input("Enter string: ")
result = ""
count = 1
for i in range(len(s)):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1
if len(result) < len(s):
    print(result)
else:
    print(s)


# 24. Most Frequent Character

s = input("Enter string: ")
max_count = 0
max_char = ""
for ch in s:
    count = s.count(ch)
    if count > max_count:
        max_count = count
        max_char = ch
print("Most frequent character =", max_char)


# 25. Second Most Frequent Character
s = input("Enter string: ")
first = 0
second = 0
first_char = ""
second_char = ""
for ch in s:
    count = s.count(ch)
    if count > first:
        second = first
        second_char = first_char
        first = count
        first_char = ch
    elif count > second and count != first:
        second = count
        second_char = ch
print("Second most frequent =", second_char)


# 26. Caesar Cipher
s = input("Enter message: ")
shift = int(input("Enter shift: "))
result = ""
for ch in s:
    if ch.isalpha():
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    else:
        result += ch
print("Encrypted =", result)


# 27. Email Validator

email = input("Enter email: ")
if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")


# 28. Word Frequency Dictionary

sentence = input("Enter sentence: ")
words = sentence.split()
for word in words:
    print(word, "=", words.count(word))


# 29. Sentence Reversal

sentence = input("Enter sentence: ")
words = sentence.split()
reverse = ""
for word in words:
    reverse = word + " " + reverse
print(reverse)


# 30. String Rotation
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) == len(s2) and s2 in s1 + s1:
    print("Yes")
else:
    print("No")