import LinkedList
import ArrayList
from time import perf_counter_ns as timestamp


def create_random_values():
    import random
    values = []
    for i in range(10000):
        values.append(random.randint(0, 10000))
    return values


"""Methode mit Zeitmessung außerhalb der Main-Methode schreiben"""


def time_measure(time_start):
    time_end = timestamp()
    time_diff = time_end - time_start
    return time_diff


def main():
    time_Start_Linked_Insert = timestamp()
    llist = LinkedList.LinkedList()
    val = create_random_values()
    llist.adding_random(val)
    print("Linked-List: ")
    llist.output()
    time_insert_linked = time_measure(time_Start_Linked_Insert)
    print("Zeitmessung LinkedList Einfügen: {:.2f} Sekunden".format(time_insert_linked / 1000000000) + "\n")
    time_Start_Linked_Search = timestamp()
    print("Search:")
    llist.search()
    time_search_linked = time_measure(time_Start_Linked_Search)
    print("Zeitmessung LinkedList Suche: {:.2f} Sekunden".format(time_search_linked / 1000000000) + "\n")
    time_Start_Linked_Sort = timestamp()
    print("Sortierung ASC")
    llist.insertionSortAscO()
    time_sort_linked = time_measure(time_Start_Linked_Sort)
    print("Zeitmessung LinkedList Sortierung: {:.2f} Sekunden".format(time_sort_linked / 1000000000) + "\n")

    time_Start_Array_Insert = timestamp()
    alist = ArrayList.ArrayList()
    alist.adding_elem(val)
    print("Array-List: ")
    alist.output()
    time_insert_array = time_measure(time_Start_Array_Insert)
    print("Zeitmessung ArrayList Einfügen: {:.2f} Sekunden".format(time_insert_array / 1000000000) + "\n")
    time_Start_Array_Search = timestamp()
    print("Search:")
    alist.search_elem()
    time_search_array= time_measure(time_Start_Array_Search)
    print("Zeitmessung ArrayList Suche: {:.2f} Sekunden".format(time_search_array / 1000000000) + "\n")
    time_Start_Array_Sort = timestamp()
    print("Sortierung ASC")
    alist.insertionSortAscO()
    time_sort_array = time_measure(time_Start_Array_Sort)
    print("Zeitmessung ArrayList Sortierung: {:.2f} Sekunden".format(time_sort_array / 1000000000) + "\n")

    """print("Menu Linked-List: ")
    llist.menu()
    print("Menu Array-List: ")
    alist.menu()"""


if __name__ == '__main__':
    main()
