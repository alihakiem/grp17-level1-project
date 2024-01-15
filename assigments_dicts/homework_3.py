book_dict = {"pages":"277","name":"Gone girl","year":2007}
book_dict["Author"] = "Well max"
print(book_dict)
print('--------------------------------')
print(book_dict["name"])
print('-----------------------------')
book_dict["year"] = 2010
print(book_dict)
print('--------------------')
for key,value in book_dict.items():
    print(key,value)
print('------------')
del book_dict["name"]
print(book_dict)