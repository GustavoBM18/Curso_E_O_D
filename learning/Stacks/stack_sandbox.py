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