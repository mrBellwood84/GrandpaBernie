def binary(data_list, item):

    bot = 0
    top = len(data_list)
    mid = (top - bot) // 2

    while True:

        if data_list[mid] == item: return mid
        if bot == mid: return -1
        if data_list[mid] < item: bot = mid
        if data_list[mid] > item: top = mid
        mid = ((top - bot) // 2) + bot
