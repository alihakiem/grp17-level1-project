try:
    def calculate_average(num_list):
        print(sum(num_list)/len(num_list))

    calculate_average([10, 20, '30z', 40])
except TypeError:
    print("Error: Non-numeric value found in the list!")
