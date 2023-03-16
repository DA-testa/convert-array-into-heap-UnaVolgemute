# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        swaps = sift_down(data, i, n, swaps)
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        swaps.append((0, i))
        swaps = sift_down(data, 0, i, swaps)
    return swaps


def sift_down(data, i, n, swaps):
    while 2 * i + 1 < n:
        j = 2 * i + 1
        if j + 1 < n and data[j + 1] > data[j]:
            j += 1
        if data[i] >= data[j]:
            break
        data[i], data[j] = data[j], data[i]
        swaps.append((i, j))
        i = j
    return swaps


def main():
    data_input = input("Enter 'I' to input from keyboard, 'F' to input from a file: ")
    if data_input == 'I':
        n = int(input("Enter the length of the list: "))
        data = list(map(int, input("Enter the list of integers: ").split()))
    elif data_input == 'F':
        filename = input("Enter the filename: ")
        with open(filename, 'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().strip().split()))
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
    num_swaps = len(swaps)
    max_swaps = 4 * n
    print(f"Number of swaps: {num_swaps}")
    if num_swaps <= max_swaps:
        print("All swaps:")

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
