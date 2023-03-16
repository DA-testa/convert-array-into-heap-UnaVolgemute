# python3

import os

def sift_down(i, data, swaps):
    min_index = i
    l = 2 * i + 1
    if l < len(data) and data[l] < data[min_index]:
        min_index = l
    r = 2 * i + 2
    if r < len(data) and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(min_index, data, swaps)

def build_heap(data):
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        sift_down(i, data, swaps)
    return swaps


def main():
    input_method = input("Enter 'I' to input from keyboard, 'F' to input from a file: ").strip().lower()

    if input_method == 'i':
        n = int(input("Enter the length of the list: "))
        data = list(map(int, input("Enter the elements of the list separated by space: ").split()))
    elif input_method == 'f':
        file_path = input("Enter the path to the file containing the list: ")
        if not os.path.exists(file_path):
            print("File not found. Please try again.")
            return
        if os.path.getsize(file_path) == 0:
            print("File is empty. Please try again.")
            return
        with open(file_path, 'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().strip().split()))
    else:
        print("Invalid input method. Please try again.")
        return

    
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
   for d in data:
        if not isinstance(d, int):
            print("Invalid input data. Please try again.")
            return

    # input from keyboard
   


    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    num_swaps = len(swaps)
    max_swaps = 4 * n
    if num_swaps > max_swaps:
        print("Too many swaps. Please try again.")
        return
    print("Number of swaps:", num_swaps)

    # output all swaps
    #print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
