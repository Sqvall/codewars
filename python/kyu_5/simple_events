""" https://www.codewars.com/kata/52d3b68215be7c2d5300022f """


class Event():
    def __init__(self):
        self.handlers = []
        
    def subscribe(self, func):
        self.handlers.append(func)
        
    def unsubscribe(self, func):
        self.handlers.remove(func)
        
    def emit(self, *args):
        for handler in self.handlers:
            handler(*args)
