# # T1
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        if self.draft-self.crew*1.5>20: return True
        else:   return False

# T2
class Block:
    def __init__(self,args):
        self.width = args[0]
        self.length = args[1]
        self.height = args[2]
        
    def get_width(self):
        return self.width
    def get_length(self):
        return self.length
    def get_height(self):
        return self.height
    
    def get_volume(self):
        return self.width*self.length*self.height
    def get_surface_area(self):
        return 2*(self.width*self.length + self.width*self.height+self.length*self.height)
        
# T3
import math
class   PaginationHelper:
    def __init__(self,collection,items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        
    def item_count(self):
        return len(self.collection)
    def page_count(self):
        return math.ceil(self.item_count()/self.items_per_page)
    def page_item_count(self,page_index):
        if page_index>=self.page_count() or page_index<0:
            return -1
        if page_index==self.page_count()-1:
            last_page = self.item_count()%self.items_per_page
            if last_page==0:    return self.items_per_page
            else:   return last_page
        else:
            return self.items_per_page
    def page_index(self,item_index):
        if item_index>=self.item_count() or item_index<0:   return -1
        else:   return item_index//self.items_per_page
        
# T4
from math import sqrt 
class Vector:
    def __init__(self,iterable):
        self.examples = tuple(i for i in iterable)
    def __str__(self):
        return str(self.examples).replace(' ','')
    def check(self,str2):
        if not len(self.examples)==len(str2.examples):
            raise ValueError('Vectors of different length')
    def add(self,str2):
        self.check(str2)
        return Vector(i+j for i,j in zip(self.examples,str2.examples))
    def subtract(self,str2):
        self.check(str2)
        return Vector(i-j for i,j in zip(self.examples,str2.examples))
    def dot(self,str2):
        self.check(str2)
        return sum(i*j for i,j in zip(self.examples,str2.examples)) 
    def norm(self):
        return sqrt(sum(x**2 for x in self.examples))
    def equals(self,str2):
        return self.examples==str2.examples
    
# T5
class User():
    def __init__(self):
        self.ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank = -8
        self.index = 0
        self.progress = 0
    
    def inc_progress(self,rank):
        index = self.ranks.index(rank)
        if index == self.index:
            self.progress+=3
        elif index==self.index-1 or (index==1 and self.index==-1):
            self.progress+=1
        elif index > self.index:
            if(index>0 and self.index<0):
                x = index-self.index+1
            else:
                x = index-self.index
            self.progress +=10*x*x
        while self.progress >= 100:
            self.index += 1
            self.rank = self.ranks[self.index]
            self.progress -=100
        if self.rank ==8 :
            self.progress=0
            return
                