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
        then move the head node to the newly created node"""
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        pass

    def search(self, data):
        pass

    def remove(self, data):
        pass