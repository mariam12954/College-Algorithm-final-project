def get_input():
    array = input("Enter elements separated by spaces: ").split()

    return [float(x) for x in array]

def find_the_median_of_sorted_array(array3):

    z = len(array3)
    for i in range(z):
        for j in range(0, z - i - 1):
            if array3[j] > array3[j + 1]:
                array3[j], array3[j + 1] = array3[j + 1], array3[j]


    if z % 2 == 1:
        median = array3[z // 2]
    else:
        median = (array3[z // 2 - 1] + array3[z // 2]) / 2

    return median

while True:
    print("\n-- Calculate the median of two arrays --")
    print("The first array")
    array1 = get_input()

    print("The second array")
    array2 = get_input()


    m = len(array1)
    n = len(array2)


    if not (0 <= m <= 1000) or not (0 <= n <= 1000) or not (1 <= m + n <= 2000):
        print("Error: Length constraints are violated.")
        continue


    if any(x < -10**6 or x > 10**6 for x in array1) or any(x < -10**6 or x > 10**6 for x in array2):
        print("Error: Array elements must be between -10^6 and 10^6.")
        continue


    array3 = array1 + array2


    median = find_the_median_of_sorted_array(array3)
    print(f"The median is: {median}")


    cont = input("Do you want to enter two more arrays? (yes/no): ")
    if cont != "yes":
        print("Program terminated.")
        break