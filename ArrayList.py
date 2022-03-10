from array import array


class ArrayList():
    def __init__(self):
        # self.value = None
        self.arr = []

    def adding_elem(self, val):
        arraylist = self.arr
        for i in range(len(val)):
            arraylist.append(val[i])
        return arraylist

    def delete(self, item):
        list = self.arr
        list.pop(item)
        print("Elemt wurde gelöscht")

    def search(self, item):
        list = self.arr
        for i in range(len(list)):
            if list [i] == item:
                print("Element existiert in der Liste: " + str(i))

    def output(self,alist):
        print("Länge : %i" % alist.length_list())
        arraylist = self.arr
        output = []
        for i in range(len(arraylist)):
                output.append(arraylist[i])
        print(output)

    def length_list(self):
        count = 0
        arraylist = self.arr
        for i in range(len(arraylist)):
            count = count + 1
        return count

    def insertBefore(self, item , item_id):
        arraylist = self.arr
        for i in range(len(arraylist)):
            if arraylist [i] == item_id:
                arraylist.insert(item_id - 1,item)
        return arraylist

    def insertAfter(self, item_id, item):
        pass

    def deleteBefore(self, number):
        pass

    def deleteAfter(self, number):
        pass

    def sortAsc(self):
        array = self.arr
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array

    def sortDesc(self):
        array = self.arr
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key > array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array

    def insertionSortAscO(self,list):
        list.sortAsc()
        self.output(list)

    def insertionSortDescO(self,list):
        list.sortDesc()
        self.output(list)

    def delete_elem(self,list):
        item_id = int(input("Welches Element sollte gelöscht werden?: "))
        list.delete(item_id)
        self.output(list)

    def search_elem(self,list):
        item_value = int(input("Welches Element sollte gesucht werden?: "))
        list.search(item_value)

    def insert_before_Node(self,list):
        item_value = int(input("Vor welchem Element sollte es eingefügt werden?: "))
        item_value_before = int(input("Welches Element sollte vorher eingefügt werden?: "))
        list.insertBefore(item_value_before, item_value)
        self.output(list)

    def menu(self, list):
        repeat = True
        answer = None
        while (repeat):
            answer = input("Löschen [l] - Suche [s] - Einfügen nachher [a] - Einfügen davor [b] "
                           "- Element danach entfernen [d] - Element davor entfernen [v] - "
                           "Sortieren ASC [o] - Sortieren DESC [u] - Beenden [any] ").lower()
            if answer == "l":
                self.delete_elem(list)
            elif answer == "s":
                self.search_elem(list)
            elif answer == "a":
                self.insert_after_node(list)
            elif answer == "b":
                self.insert_before_Node(list)
            elif answer == "d":
                self.delete_after_node(list)
            elif answer == "v":
                self.delete_before_node(list)
            elif answer == "o":
                self.insertionSortAscO(list)
            elif answer == "u":
                self.insertionSortDescO(list)
            else:
                repeat = False
                print("Verlassen")