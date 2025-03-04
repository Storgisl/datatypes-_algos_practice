from typing import Optional


#
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        if self.head is not None:
            print("\nLinked List is'nt empty")
            return True
        else:
            print("\nLinked List is empty")
            return False

    def append_to_begging(self, node: Optional[Node] = None) -> None:
        if node is None:
            node = Node(0)

        node.next = self.head

        self.head = node
        print(f"\nnode - {node.data} - appended to beggining")

    def append_node(self, node: Optional[Node] = None) -> None:
        if node is None:
            node = Node(0)

        current = self.head
        if current is None:
            self.head = node

        while current is not None:
            if current.next is None:
                current.next = node
                break
            current = current.next
        print(f"\nnode - {node.data} - appended to end")

    def append_after_node(self, node_value: int, node: Optional[Node] = None) -> None:
        if node is None:
            node = Node(0)
        appended = False
        current = self.head
        while current is not None and not appended:
            if current.data == node_value:
                node.next = current.next
                current.next = node
                appended = True
            current = current.next
        print(f"\nnode - {node.data} - appended after value - {node_value}")

    def append_at_index(self, index: int, node: Optional[Node] = None) -> None:
        if node is None:
            node = Node(0)

        appended = False
        index_count = 0
        current = self.head
        while current is not None:
            if index == index_count and not appended:
                node.next = current.next
                current.data = node.data
                appended = True
            index_count += 1
            current = current.next
        print(f"\nnode - {node.data} - appended at index - {index}")

    def delete_node(self, node: Optional[Node] = None) -> None:
        if node is None:
            node = Node(0)

        if node.data == self.head.data:
            print(f"\nnode - {node.data} - deleted at head")
            self.head = self.head.next
            return
        deleted = False
        current = self.head

        while current is not None:
            if current.next.data == node.data and not deleted:
                if current.next is not None:
                    node.next = current.next
                    current.next = node.next.next
                    deleted = True
                else:
                    break

            current = current.next
        print(f"\nnode - {node.data} - deleted")

    # def delete_node_at_index(self, index: int) -> None:
    #     index_count = 0
    #     current = self.head
    #     deleted = False
    #     while current:
    #         if index == (index_count + 1) and not deleted:
    #             current.data = current.next.data
    #             current.next.data = current.next.next.data
    #             deleted = True
    #         index_count += 1
    #         current = current.next
    #     print(f"\nnode deleted at index - {index}")

    def print_ll(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> " if current.next is not None else "\n")
            current = current.next


ll = LinkedList()

ll.is_empty()
ll.append_node(node=Node(2))
ll.print_ll()
ll.append_node()
ll.print_ll()
ll.append_to_begging(node=Node(11))
ll.print_ll()
ll.append_node(node=Node(0))
ll.print_ll()
ll.append_node(node=Node(1))
ll.print_ll()
ll.append_node(node=Node(12))
ll.print_ll()
# ll.append_node(node=Node(0))
# ll.print_ll()
ll.append_after_node(node=Node(20), node_value=0)
ll.print_ll()
ll.append_after_node(node=Node(20), node_value=0)
ll.print_ll()
ll.append_at_index(node=Node(30), index=0)
ll.print_ll()
ll.delete_node(node=Node(12))
ll.print_ll()
ll.delete_node(node=Node(30))
ll.print_ll()
ll.delete_node(node=Node(1))
ll.print_ll()
#ll.delete_node(node=Node(0))
ll.print_ll()
# ll.delete_node_at_index(index=0)
# ll.print_ll()
ll.is_empty()
