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
            Any: next list item
        """
        current = self.header
        while current.next_item is not None:
            current = current.next_item
            yield current.item

    def __getitem__(self, index):
        """Get list item by index
        Raises IndexError if index is out of bounds

        Args:
            index - item index

        Returns:
            Any: item at given index
        """
        if isinstance(index, slice):
            returned_list = LinkedList()
            for slice_index in range(*index.indices(self.size)):
                returned_list.add(self[slice_index])
            return returned_list
        else:
            if self.__bad_index(index):
                raise IndexError("Index out of bounds:", index)
            if index < 0:
                index += self.size
            current = self.header
            for entry_index in range(index + 1):
                current = current.next_item
            return current.item

    def __setitem__(self, key, value):
        """Set new value to list item
        Raises IndexError if index is out of bounds

        Args:
            key - item index
            value - item new value
        """
        if self.__bad_index(key):
            raise IndexError("Index out of bounds:", key)
        current = self.header
        for entry_index in range(key):
            current = current.next_item
        current.next_item = Entry(value, current.next_item.next_item)

    def __contains__(self, item):
        """Checks whether list contains item

        Args:
            item - checked item

        Returns:
            bool: True if list contains item, False otherwise
        """
        for entry in self:
            if entry == item:
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

    def __str__(self):
        """Returns string representation of list

        Returns:
            str: list string representation
        """
        if self.size > 0:
            items = ''.join(str(item) + ', ' for item in self)[:-2]
        else:
            items = ''
        return '[{}]'.format(items)

    def __bad_index(self, index):
        """Checks whether index is acceptable

        Args:
            index (int) - checked index

        Returns:
            bool: True if index is not acceptable, False otherwise
        """
        return not ((index >= -self.size) and (index < self.size))

    def add(self, item):
        """Adds item to the back of the list. Same as push_back

        Args:
            item - item value
        """
        current = self.header
        while current.next_item is not None:
            current = current.next_item
        new_entry = Entry(item, None)
        current.next_item = new_entry
        self.size += 1

    def remove(self, index):
        """Removes item at given index from the list
        Raises IndexError if index is out of bounds

        Args:
            index (int) - item index
        """
        if self.__bad_index(index):
            raise IndexError("Index out of bounds:", index)
        current = self.header
        for entry_index in range(index):
            current = current.next_item
        current.next_item = current.next_item.next_item
        self.size -= 1

    def push_front(self, item):
        """Adds item to the front of the list

        Args:
            item - item value
        """
        self.header.next_item = Entry(item, self.header.next_item)

    def pop_front(self):
        """Removes item from the front of the list
        Raises IndexError if list is empty

        Returns:
            Any: original first item of the list
        """
        if self.size == 0:
            raise IndexError('pop from empty list')
        item = self[0]
        self.remove(0)
        return item

    def push(self, item):
        """Adds item to the back of the list. Same as add

        Args:
            item - item value
        """
        self.add(item)

    def pop(self):
        """Removes last element from the list and returns its value
        Raises IndexError if list is empty

        Returns:
            Any: original last item of the list
        """
        if self.size == 0:
            raise IndexError('pop from empty list')
        item = self[-1]
        self.remove(self.size - 1)
        return item

    def index(self, item):
        """If item is present is list returns its index
        Raises ValueError if item is not in the list

        Args:
            item (Any) - item to look for

        Returns:
            int: Items index in the list
        """
        current_index = 0
        for list_item in self:
            if list_item == item:
                return current_index
            else:
                current_index += 1
        raise ValueError('{} is not in the list'.format(item))


class Entry:
    """Linked list entry

    Args:
        item - list item value
        next_item - link to the next list item

    Attributes:
        item - list item value
        next_item - link to the next list item
    """

    def __init__(self, item, next_item):
        self.item = item
        self.next_item = next_item

if __name__ == '__main__':
    pass
