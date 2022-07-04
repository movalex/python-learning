class SllNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"SLLNode objext: {self.data}"

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
