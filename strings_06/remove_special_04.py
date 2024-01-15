statement = "123abcjw:, .@! eiw"
new_statement = ''
for letter in statement:
    if letter.isalnum():
        new_statement = new_statement + letter
statement = new_statement
print(statement)
del new_statement

