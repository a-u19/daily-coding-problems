class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: [ListNode], l2: [ListNode]) -> [ListNode]:
    sum = get_num_from_linked_list(node) + get_num_from_linked_list(b_node)
    len_str_num = len(str(sum))
    list_nodes = [None] * len_str_num
    for i, num in zip(range(len_str_num - 1, -1, -1), str(sum)):
        list_nodes[i] = ListNode(int(num), next=list_nodes[i - 1])
    list_nodes[-1] = (ListNode(int(str(sum)[0])))
    return list_nodes

def get_num_from_linked_list(l: [ListNode]) -> int:
    res = ""
    while l:
        res += str(l.val)
        l = l.next
    return int(res)


node3 = ListNode(3)
node2 = ListNode(4, next=node3)
node = ListNode(2, next=node2)

b_node3 = ListNode(4)
b_node2 = ListNode(6, next=b_node3)
b_node = ListNode(5, next=b_node2)
