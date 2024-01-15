def is_palindrome(word):
    cleaned_word = word.lower()
    return cleaned_word == cleaned_word[::-1]

test_word = "level"
result = is_palindrome(test_word)
print(result)