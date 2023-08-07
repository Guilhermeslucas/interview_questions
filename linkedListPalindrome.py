from linkedList import Node

def is_palindrome(head):
    aux_array = []

    while head != None:
        aux_array.append(head.value)
        head = head.next

    print(aux_array)

    left = 0
    right = len(aux_array) - 1
    while left <= right:
        if aux_array[left] != aux_array[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

a = Node(1, None)
b = Node(2, a)
c = Node(3, b)
d = Node(3, c)
e = Node(2, d)
f = Node(1, e)

print(is_palindrome(f))