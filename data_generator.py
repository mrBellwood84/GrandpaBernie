from random import choice, randint
from input_handlers import handle_travels_data


def generate_data_set(countries, min_year, max_year, size):

    if size > (len(countries) * (max_year - min_year)) // 2:
        raise Exception("Requested lenght of dataset is to large")
    
    dataset = []
    itterator = 0

    while itterator < size:

        data = f"{choice(countries)} {randint(min_year, max_year)}"

        if data in dataset: continue

        dataset.append(data)
        itterator += 1
    
    return dataset



def generate_query_data(dataset, size):

    t_dict = handle_travels_data(dataset)
    keys = list(t_dict.keys())

    queryset = []
    itterator = 0
    killswitch = 1000


    while itterator < size:
        c = choice(keys)
        l = len(t_dict[c])
        r = randint(1, l)
        data = f"{c} {r}"

        if data in queryset:
            killswitch -= 1
            if killswitch <= 0: break
            continue

        queryset.append(data)
        itterator += 1

    return queryset
    

