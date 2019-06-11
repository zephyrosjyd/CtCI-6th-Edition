from LinkedList import LinkedList


def partition(ll, x):
    current = ll.tail = ll.head
    print(current, ll.tail, ll.head)

    while current:
        nextNode = current.next
        current.next = None
        if current.value < x:
            print(current.value, current.next, ll.head)
            current.next = ll.head
            ll.head = current
            print(current.value, current.next, ll.head, current.next.next)
        else:
            ll.tail.next = current
            ll.tail = current
        current = nextNode
        
    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None

#def partition2(ll, x):
#    curr = 


ll = LinkedList()
ll.generate(8, 1, 10)
print(ll)
partition(ll, 5)
print(ll)
