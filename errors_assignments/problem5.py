try:
    def fetch_element(dictionary, key):
        a = dictionary[key]
        print(a)
    fetch_element({'a': 1, 'b': 2}, 'c')
except KeyError:
    print("Key 'c' not found in the dictionary!")
