def binary_search(array, element):
    low = 0
    high = len(array)-1
    # step = 0

    while low<=high:
        # step+=1
        mid = (low + high)//2
        guess = array[mid]
        if guess == element:
            # print("steps:", step)
            return mid
        elif guess>element:
            high = mid-1
        else:
            low = mid + 1
    # print("steps:", step)
    return -1

if __name__ == "__main__":
    lis = range(256)
    index = binary_search(lis, 127)
    print("index:", index)
