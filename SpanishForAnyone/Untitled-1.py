class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
        
def delete_tail(head):
    current = head
    while current:
        if current.next.next is None:
            current.next = None
    return head

def find_min(head):
    min = head.value
    curr = head
    while curr:
        if curr.value < min:
            min = curr.value
        curr = curr.next
    return min

    
butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle
# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))

head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
print(find_min(head2))