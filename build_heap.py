# python3

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        swaps += sift_down(i, data)
    return swaps

def sift_down(i, data):
    swaps = []
    n = len(data)
    while i * 2 + 1 < n:
        j = i * 2 + 1
        if j + 1 < n and data[j + 1] < data[j]:
            j += 1
        if data[i] > data[j]:
            swaps.append((i, j))
            data[i], data[j] = data[j], data[i]
            i = j
        else:
            break
    return swaps

def main():
    data = []
    input_method = input("Enter 'I' to input from keyboard, 'F' to input from a file: ")
    if input_method == 'I':
        n = int(input("Enter the number of elements in the list: "))
        data = list(map(int, input("Enter the elements of the list separated by space: ").split()))
    elif input_method == 'F':
        file_path = input("Enter the path to the file containing the list: ")
        with open(file_path, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        print("Invalid input.")
        return
    
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
   

    # input from keyboard
   


    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= 4 * n

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
