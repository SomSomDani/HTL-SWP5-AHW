class ArrayList():
    def __init__(self):
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
            if list[i] == item:
                print("Element existiert in der Liste: " + str(i))

    def output(self):
        print("Länge : %i" % self.length_list())
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

    def insertBefore(self, item, item_id):
        arraylist = self.arr
        for i in range(len(arraylist)):
            if i == item_id:
                arraylist.insert(item_id - 1, item)
        return arraylist

    def insertAfter(self, item_id, item):
        arraylist = self.arr
        for i in range(len(arraylist)):
            if i == item_id:
                arraylist.insert(item_id + 1, item)
        return arraylist

    def deleteBefore(self, number):
        arraylist = self.arr
        for i in range(len(arraylist)):
            if i == number:
                arraylist.pop(number - 1)
        return arraylist

    def deleteAfter(self, number):
        arraylist = self.arr
        for i in range(len(arraylist)):
            if i == number:
                arraylist.pop(number + 1)
        return arraylist

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

    def insertionSortAscO(self):
        self.sortAsc()
        self.output()

    def insertionSortDescO(self):
        self.sortDesc()
        self.output()

    def delete_elem(self):
        item_id = int(input("Welches Element sollte gelöscht werden?: "))
        self.delete(item_id)
        self.output()

    def search_elem(self):
        item_value = int(input("Welches Element sollte gesucht werden?: "))
        self.search(item_value)

    def insert_before_Node(self):
        item_value = int(input("Vor welchem Element sollte es eingefügt werden?: "))
        item_value_before = int(input("Welches Element sollte vorher eingefügt werden?: "))
        self.insertBefore(item_value_before, item_value)
        self.output()

    def insert_after_node(self):
        item_value = int(input("Welches Element sollte ausgewählt werden?: "))
        item_value_after = int(input("Welches Element sollte danach eingefügt werden?: "))
        self.insertAfter(item_value, item_value_after)
        self.output()

    def delete_after_node(self):
        item_value = int(input("Welches Element sollte danach entfernt werden: "))
        self.deleteAfter(item_value)
        self.output()

    def delete_before_node(self):
        item_value = int(input("Welches Element sollte davor entfernt werden: "))
        self.deleteBefore(item_value)
        self.output()

    def menu(self):
        repeat = True
        answer = None
        while (repeat):
            answer = input("Löschen [l] - Suche [s] - Einfügen nachher [a] - Einfügen davor [b] "
                           "- Element danach entfernen [d] \n - Element davor entfernen [v] - "
                           "Sortieren ASC [o] - Sortieren DESC [u] - Beenden [any] ").lower()
            if answer == "l":
                self.delete_elem()
            elif answer == "s":
                self.search_elem()
            elif answer == "a":
                self.insert_after_node()
            elif answer == "b":
                self.insert_before_Node()
            elif answer == "d":
                self.delete_after_node()
            elif answer == "v":
                self.delete_before_node()
            elif answer == "o":
                self.insertionSortAscO()
            elif answer == "u":
                self.insertionSortDescO()
            else:
                repeat = False
                print("Verlassen")
