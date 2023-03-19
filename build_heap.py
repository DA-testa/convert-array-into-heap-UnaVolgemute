# python3

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
    input_method = input("'I' to input from keyboard, 'F' to input from a file: ").strip().lower()

    if input_method == 'i':
        n = int(input("length of the list: "))
        data = list(map(int, input("elements of the list separated by space: ").split()))
    elif input_method == 'f':
        file_path = input("path to the file containing the list: ").strip()
        try:
            with open(file_path, 'r') as f:
                n = int(f.readline().strip())
                data = list(map(int, f.readline().strip().split()))
        except FileNotFoundError:
            print("File not found")
            return
    else:
        print("Invalid input")
        return
    
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
   

    # input from keyboard
   


    # checks if lenght of data is the same as the said lenght
    assert data is not None and len(data) == n

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
