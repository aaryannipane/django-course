
class ListNode():
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

def insertEnd(data):
    global head
    if(head == None):
       head = ListNode(data)
    else:
        temp = head
        while(temp.next != None):
            temp = temp.next

        temp.next = ListNode(data)

def display():
    if(head == None):
        print("list is empty")
    else:
        current = head
        while(current != None):
            print(current.data, end=" --> ")
            current = current.next
        print("None")

insertEnd(10)
insertEnd(20)
insertEnd(30)

display()