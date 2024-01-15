try:
    def extract_element(list, index):
        print(list.index(index))
    extract_element([1, 2, 3],6)
except ValueError or IndexError:
    print("Index out of range")


