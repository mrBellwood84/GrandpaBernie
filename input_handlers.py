from sorts import quick_sort

# process input for travels
def handle_travels_data(input_data):

    travel_dict = {}    # dictionary for travels
    travel_keys = []    # list for holding keys in travels dict
    
    for data in input_data:
        str_split = data.split(" ")
        if str_split[0] in travel_keys:
            travel_dict[str_split[0]].append(str_split[1])
            continue
        travel_dict[str_split[0]] = [str_split[1]]
        travel_keys.append(str_split[0])
    
    for key in travel_keys:
        quick_sort(travel_dict[key])

    return travel_dict

def handle_query_input(travel_dict, querydata):
    
    result = []

    for data in querydata:
        str_split = data.split(" ")
        index = int(str_split[1]) - 1
        year = travel_dict[str_split[0]][index]
        result.append(f"{str_split[0]} {year}")
    
    return result