import ast
class ListNode:
    def __init__(self,val=0,next=None):
        self.val =  val
        self.next = next

class solution:
    def mergeTwolists(self,list1,list2):
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next  = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2
        return dummy.next
def create_linkeedlist(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_linklist(head):
    while head:
        print(head.val, end="->" if head.next else " ")
        head = head.next
    print() 
num1 = ast.literal_eval(input("enter the list1"))
num2 = ast.literal_eval(input("enter the list2"))
list1 =create_linkeedlist(num1)
list2 =create_linkeedlist(num2)
merge = solution()
merged = merge.mergeTwolists(list1,list2)
print("Merged linked List ")
print_linklist(merged)