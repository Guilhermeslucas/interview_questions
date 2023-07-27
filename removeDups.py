from linkedList import Node

def remove_dups(head):
    occurrences = [False for _ in range(101)]
    occurrences[head.value] = True
    
    while head.next != None:
        if occurrences[head.next.value]:
            head.next = head.next.next
        else:
            occurrences[head.value] = True
        
        head = head.next
    
a = Node(1, None)
b = Node(2, a)
c = Node(3, b)
d = Node(2, c)
e = Node(4, d)
f = Node(4, e)

remove_dups(f)

head = f
while head != None:
    print(head.value)
    head = head.next