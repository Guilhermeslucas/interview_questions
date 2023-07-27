# a lot of repeting code but it works

from linkedList import Node

def sum_two_numbers(first_number, second_number):
    carry = 0
    final_number = ""
    
    while first_number != None and second_number != None:
        current_digit = (carry + first_number.value + second_number.value) % 10
        carry =  (carry + first_number.value + second_number.value) // 10
        final_number = str(current_digit) + final_number

        first_number = first_number.next
        second_number = second_number.next

    if first_number == None and second_number == None:
        if carry == 0:
            return final_number
        else:
            return carry + final_number
        
    if first_number == None:
        bigger_number = second_number
    else:
        bigger_number = first_number

    while bigger_number != None:
        current_digit = (carry + bigger_number.value) % 10
        carry =  (carry + bigger_number.value) // 10
        final_number = str(current_digit) + final_number

        bigger_number = bigger_number.next

    if carry == 0:
            return final_number
    else:
        return carry + final_number

        
a = Node(1, None)
b = Node(8, a)
c = Node(3, b)

d = Node(1, None)
e = Node(8, d)

print(sum_two_numbers(c, e))