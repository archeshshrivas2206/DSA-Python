#it is also a linear data structure , the differehce is in the number of variable in the node ;
#doubly linked list have one extra variable which holds the address of previous node 
class Node:
    def __init__(self, data=None,prev= None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self,data):
        n=Node(data,None,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n

    def insert_at_end(self,data):
        if self.start==None:
            temp=None
        n=Node(data)
        temp=self.start
        while temp.next is not None:
            temp=temp.next
        n.prev=temp
        temp.next=n

    def search_an_element(self,data):
        temp= self.start
        while temp is not None:
            if temp.data==data:
                print("Element found at ", temp)
            temp=temp.next
        return None

    def insert_after(self, data,item):
        temp=self.start
        while temp is not None:
            if temp.data==item:
                n=Node(data,temp,temp.next)
                if temp.next is not None:
                    temp.next.prev=n
                temp.next=n
                return 
            temp=temp.next

    def print_all_elements(self):
        temp=self.start
        while temp is not None:
            print(temp.data, end=" ")
            temp=temp.next
        print()

    def delete_at_first(self):
        
        if self.start is None:
            print("the list is empty \n" )
        elif self.start.next is None:
            self.start=None
        else:
            self.start=self.start.next
            self.start.prev=None
    
    def delete_last(self):
        temp=self.start
        if self.start is None:
            return 
        if self.start.next is None:
            self.start=None
        while temp.next is not None:
            temp=temp.next
        temp.prev.next=None

    def delete_specific_node(self,item):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.data==item:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next
    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
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
    
obj=DLL()

obj.insert_at_start(6)
obj.print_all_elements()

obj.insert_at_end(48)
obj.print_all_elements()

obj.insert_after(14,6)

for x in obj:
    print(x, end=' ')