class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "SLLNode object: data = {}".format(self.data)

    def get_data(self):
        """Return the self.data attribute."""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data
        parameter."""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next
        parameter."""
        self.next = new_next


class SLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"SLL object: head = {self.head}"

    def is_empty(self):
        """checks if the Linked List is empty"""
        return self.head is None

    def add_front(self, new_data):
        """create a temporary node and assign it with the new data we want to add front
        then set the next to the self.head node
        then move the head node to the newly created node
        Adding a head Node with new_data to the front of the list"""
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """Traverse the Linked List and return an int value with the numiber of nodes

        Time complexity is O(n) because every node must be visited to get the size of the LL"""
        size = 0
        if self.is_empty():
            # print("already empty")
            return 0
        current = self.head
        while current:  # while there are still nodes left to count
            size += 1
            current = current.get_next()
        return size

    def search(self, data=None):
        """Traverse the Linked List, return True if the data is found in the LL, otherwise False

        The time complexity is O(n) because in worst case we would need to check every Node
        """
        if not data:
            return "search request is empty"
        if self.is_empty():
            return "Linked List is empty. No nodes to search"

        current = self.head
        while current:
            if current.get_data() == data:
                return True
            current = current.get_next()
        return False

    def remove(self, data):
        pass
