#!/usr/bin/env python3
import ipdb

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count_parameter):
        if(type(page_count_parameter) == int):
            self._page_count = page_count_parameter
        else:
            print("page_count must be an integer")
        
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
    def __repr__(self):
        return f"Book name is {self.title} and the page I am on is {self.page_count}"

#ipdb.set_trace()