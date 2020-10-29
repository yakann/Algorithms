def insertion(unsorted_list):
    for i in range(1, len(unsorted_list)):
        j = i - 1
        while j >= 0:
            if unsorted_list[i] < unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
                i = j
                j -= 1
            else:
                break
    return unsorted_list


if __name__ == '__main__':
    print(insertion([12, 11, 13, 5, 6]))
