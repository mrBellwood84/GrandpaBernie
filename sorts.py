def quick_sort(input_list, startIndex = 0, endIndex_p1 = None):

    # get indexes and pivot
    endIndex_p1 = len(input_list) if endIndex_p1 == None else endIndex_p1
    if (endIndex_p1 - startIndex) <= 1: return
    pivot_value = input_list[endIndex_p1 - 1]
    high_point = startIndex

    # sort looper
    for index in range(startIndex, endIndex_p1):
        if input_list[index] <= pivot_value:
            swap(input_list, index, high_point)
            high_point += 1
    high_point -= 1
    
    # sort low range
    quick_sort(input_list, startIndex, high_point)

    # sort high range
    quick_sort(input_list, high_point, endIndex_p1) 


def swap(lst, a, b):
    t = lst[a]
    lst[a] = lst[b]
    lst[b] = t
