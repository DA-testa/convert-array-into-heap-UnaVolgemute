# python3


def build_heap(data):
    swaps = []
    size = len(data)

    for i in range((size // 2) - 1, -1, -1):
        sift_down(data, i, size, swaps)

    for i in range(size - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        swaps.append((0, i))
        sift_down(data, 0, i, swaps)
    return swaps


def sift_down(data, i, size, swaps):
    max_index = i
    left_child = (2 * i) + 1
    right_child = (2 * i) + 2

    if left_child < size and data[left_child] > data[max_index]:
        max_index = left_child

    if right_child < size and data[right_child] > data[max_index]:
        max_index = right_child

    if i != max_index:
        data[i], data[max_index] = data[max_index], data[i]
        swaps.append((i, max_index))
        sift_down(data, max_index, size, swaps)


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    n = int(input())
    data = list(map(int, input().split()))

    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) < 4 * len(data)
    print(len(swaps))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
