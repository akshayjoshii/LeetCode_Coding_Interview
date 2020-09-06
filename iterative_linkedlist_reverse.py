from copy import deepcopy

# Constructor to create a node
class node:
    def __init__(self, data):
        self.node = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def reverse(self):
        prev = None
        current = self.head 
        try:
            while(current is not None): 
                next = current.next 
                current.next = prev 
                prev = current
                current = next
        except:
            print("No data found in the list")

        self.head = prev
        
    def push(self, new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printlist(self):
        try: 
            while(self.head):
                print(self.head.node)
                self.head = self.head.next
        except:
             print("No data found in the list")
    

if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.push(5)
    linkedlist.push(10)
    linkedlist.push(15)
    linkedlist.push(20)

    # Create a copy of the linkedlist object to demonstrate reverse operation
    reverse_linked_list = deepcopy(linkedlist)

    print("The original Linked List is:") 
    linkedlist.printlist()
    
    reverse_linked_list.reverse()
    print("\nThe iteratively reversed Linked List is:")
    reverse_linked_list.printlist()

