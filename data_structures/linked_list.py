"""Linked list in object-oriented style"""


class LinkedList:
    """Singly linked list realization

        Attributes:
            header - header entry, only contains link to first entry
            size - size of the list
        """

    def __init__(self):
        self.header = Entry(None, None)
        self.size = 0

    def __iter__(self):
        """Iterates through list items. Starts at first item ignoring the header

        Returns:
            Entry: next list item
        """
        current = self.header
        while current.next is not None:
            current = current.next
            yield current

    def __getitem__(self, index):
        """Get list item by index

        Args:
            index - item index

        Returns:
            Entry: item at given index
        """
        if (index + 1) < 0 or (index + 1) > self.size:
            raise IndexError("Index out of bounds:", index)
        current = self.header
        for entry_index in range(index + 1):
            current = current.next
        return current

    def __setitem__(self, key, value):
        """Set new value to list item

        Args:
            key - item index
            value - item new value
        """
        if (key + 1) < 0 or (key + 1) > self.size:
            raise IndexError("Index out of bounds:", key)
        current = self.header
        for entry_index in range(key):
            current = current.next
        current.next = Entry(value, current.next.next)

    def __contains__(self, item):
        """Checks whether list contains item

        Args:
            item - checked item

        Returns:
            bool: True if list contains item, False otherwise
        """
        for entry in self:
            if entry.item == item:
                return True
        return False

    def __len__(self):
        """Returns length of the list

        Returns:
            int: length of the list
        """
        return self.size

    def __bool__(self):
        """Returns boolean value of the list

        Returns:
            bool: False if list is empty, False otherwise
        """
        return len(self) > 0

    def add(self, item):
        """Adds item to the list

        Args:
            item - item value
        """
        current = self.header
        for entry in self:
            current = entry
        new_entry = Entry(item, None)
        current.next = new_entry
        self.size += 1


class Entry:
    """Linked list entry

    Args:
        item - list item value
        next - link to the next list item

    Attributes:
        item - list item value
        next - link to the next list item
    """

    def __init__(self, item, next):
        self.item = item
        self.next = next

if __name__ == '__main__':
    list = LinkedList()
    list.add(0)
    list.add(1)
    list.add(3)
    print(1 in list)
    list[1] = 2
    for i in list:
        print(i.item)
