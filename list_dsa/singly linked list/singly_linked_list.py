#to implement a singly linked list we will use the concept of class 

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class SLL:
    def __init__(self, start=None):
        self.start=start

#elementry functions applicable on linked list 
    def is_empty(self):
        return self.start is None
    
    def insert_at_beginning(self,data):
        n=Node(data,self.start)
        self.start=n
    
    def insert_at_end(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    
    def search_node(self,data):
        temp=self.start
        while temp is not None:
            if temp.data==data:
                return temp
            temp=temp.next
        return None
    
    def insert_after(self,data,item):
        temp=self.start
        while temp is not None:
            if temp.data==data:
                n=Node(item,temp.next)
                temp.next=n
                return 
            temp=temp.next
        return None
    
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
        print()#to move to a new line 
    
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
        # if self.start is not None:
        #     temp=self.start
        #     temp=temp.next
        #     self.start=temp

    def delete_last_node(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None 
    
    def delete_node(self,item):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.data==item:
                self.start=None
        else:
            temp=self.start
            if temp.data==item:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.data==item:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    
    def __iter__(self):
        return SLLIterator(self.start)
    
# the object or our list is made successfully butr there is an issue , the list is not iterable , to make it iterable we have to make a class

class SLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        return data

mylist=SLL()

mylist.insert_at_beginning(14)
mylist.print_list()

mylist.insert_at_end(48)
mylist.print_list()

mylist.insert_after(14,15)
mylist.print_list()


mylist.insert_after(15,16)
mylist.insert_after(16,17)
mylist.insert_after(17,19)
mylist.insert_after(19,20)
mylist.insert_after(20,29)
mylist.insert_after(29,33)
mylist.print_list()

mylist.insert_at_beginning(6)
mylist.print_list()

print(mylist.search_node(15))

mylist.insert_at_beginning(4)
mylist.print_list()
mylist.delete_first()
mylist.print_list()

mylist.delete_node(14)
mylist.print_list()

for i in mylist:
    print(i,end=' ')