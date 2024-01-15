def reverse_string(statement):
    words_reversing= statement.split()
    reversed_statement = ' '.join(reversed(words_reversing))
    return reversed_statement
str = "i like this program very much"
answer = reverse_string(str)
print(answer)