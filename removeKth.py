from linkedList import Node

def remove_kth(head, position):
    original_head = head
    
    size = 0
    while head != None:
        size += 1
        head = head.next
    
    k = size - position

    while k > 0:
        original_head = original_head.next
        k -= 1
    
    print(original_head.value)

a = Node(1, None)
b = Node(8, a)
c = Node(3, b)
d = Node(9, c)
e = Node(10, d)
f = Node(4, e)

remove_kth(f, 6)