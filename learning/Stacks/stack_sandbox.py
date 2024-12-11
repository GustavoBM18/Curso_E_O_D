from Node import Node
import logging
# setting logging for pass the test
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
    def peek(self):
        if self.top_item is None:
            raise AttributeError("Stack is empty. No top item to peek.")
        return self.top_item.get_value()
    
class Stack:
    def __init__(self):
        self.top_item = None

    def peek(self):
        # Return the value of the top item if it exists
        if self.top_item is None:
            raise AttributeError("Stack is empty. No top item to peek.")
        return self.top_item.get_value()
    def push(self, value):
        item = Node(value)
        item.set_next_node(self.top_item)
        self.top_item = item
    def pop(self):
        if self.top_item is None: # check if it is none
            raise AttributeError("Stack is empty. No item to pop.")
        # save
        item_to_remove = self.top_item
        # update the top_item to the next node
        self.top_item = item_to_remove.get_next_node()
        # return value of removed item
        return item_to_remove.get_value()