import LinkedList
import ArrayList
from time import perf_counter_ns as timestamp


def create_random_values():
    import random
    values = []
    for i in range(10000):
        values.append(random.randint(0, 10000))
    return values


def main():
    time_Start_Linked = timestamp()
    llist = LinkedList.LinkedList()
    val = create_random_values()
    llist.adding_random(val)
    print("Linked-List: ")
    llist.output()
    print("Sortierung ASC")
    llist.insertionSortAscO()
    time_End_Linked = timestamp()
    time_Linked = time_End_Linked - time_Start_Linked
    print("Zeitmessung Linked: {:.2f} Nanosekunden".format(time_Linked))

    time_Start_Array = timestamp()
    alist = ArrayList.ArrayList()
    alist.adding_elem(val)
    print("Array-List: ")
    alist.output()
    print("Sortierung ASC")
    alist.insertionSortAscO()
    time_End_Array = timestamp()
    time_Array = time_End_Array - time_Start_Array
    print("Zeitmessung Array: {:.2f} Nanosekunden".format(time_Array))

    """#print("Menu Linked-List: ")
    #llist.menu()
    #print("Menu Array-List: ")
    #alist.menu()"""

if __name__ == '__main__':
    main()
