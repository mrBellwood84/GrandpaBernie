from time import perf_counter_ns as timer
from data_generator import generate_data_set, generate_query_data
from input_handlers import handle_travels_data, handle_query_input

# Contry list
COUNTRIES = ["Norway", "Sweeden" ,"Denmark", "Finland", "Iceland", "Germany", "France", "Spain", "England","Italy", "Greece"]

MIN_YEAR = 1990
MAX_YEAR = 2021

DATA_SIZE = 10
QUERY_SIZE = 3


# geberate travelset and queryset
dataset = generate_data_set(COUNTRIES, MIN_YEAR, MAX_YEAR, DATA_SIZE)
querydata = generate_query_data(dataset, QUERY_SIZE)



if __name__ == "__main__":


    start = timer()

    travel_dict = handle_travels_data(dataset)

    data_sort_complete = timer()

    result = handle_query_input(travel_dict, querydata)

    result_complete = timer()

    for res in result:
        print(res)

    complete = timer()

    

    report = f"""
    REPORT

    Travels: .......... {DATA_SIZE}
    Travels quueryed: . {QUERY_SIZE}

    ------
    Sorting data time: .......... {(data_sort_complete - start) // 1000} ms
    Query data time: ............ {(result_complete - data_sort_complete) // 1000} ms
    Query data time from start: . {(result_complete - start) // 1000} ms
    Complete after print: ....... {(complete - start) // 1000} ms
    
    """

    print(report)