class Node:
    def __init__(self,data=None):
        self.data=data
        self.next = None
        
class Linked_lists:
    def __init__(self):
        self.head = Node()
        
    def append(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node
            
    def length(self):
        cur = self.head
        total=0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)
        
    def delete(self,data):
        cur_node = self.head
        prev_node = None
        while cur_node.next!=None:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_node.data==data:
                prev_node.next=cur_node.next
                cur_node=None
                return
        print("Data not found")
        
    def insert(self,data,index):
        if index>= self.length():
            print("Index out of range")
            return
        cur_node = self.head
        prev_node = None
        cur_index = 0
        while cur_index!=index:
            prev_node=cur_node
            cur_node=cur_node.next
            cur_index+=1
        new_node = Node(data)
        prev_node.next=new_node
        new_node.next=cur_node
            
            
        
        
my_list = Linked_lists()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)


my_list.display()

my_list.delete(3)

my_list.display()
        
my_list.insert(5,2)

my_list.display()