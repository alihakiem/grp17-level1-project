def remove_special_characters(statement):
    cleaned_statement = ""
    for char in statement:
        if char.isalnum():
            cleaned_statement = cleaned_statement + char
    return cleaned_statement

# Example usage
ini_string = "123abcjw:, .@! eiw"
result = remove_special_characters(ini_string)
print(result)
