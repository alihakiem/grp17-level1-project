def remove_special(statement):
    clean_str = ""
    for character in statement:
        if character.isalnum():
            clean_str = clean_str + character
    return clean_str
ini_string = "123abcjw:, .@! eiw"
ans = remove_special(ini_string)
print(ans)