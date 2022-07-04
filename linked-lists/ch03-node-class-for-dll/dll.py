class DllNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return f"SLLNode object: {self.data}"

    def get_data(self):
        """return self.data attribute"""
        return self.data

    def set_data(self, new_data):
        """replace the existing self.data attribute with the new_data parameter"""
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        """replace the existing self.next attribute with the new_next parameter"""
        self.next = new_next

    def get_previous(self):
        return self.previous

    def set_previous(self, new_previous):
        """replace the existing self.previous attribute with the new_previous parameter"""
        self.previous = new_previous


node1 = DllNode(1)
node2 = DllNode(2)
node3 = DllNode(3)
node2.set_previous(node1)
node2.set_next(node3)
node2.get_previous()
node2.get_next()
