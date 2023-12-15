#!/usr/bin/python3
"""Node Class Definition"""


class Node:
    """
    Class that define a Node of singly linked list
    
    Attributes:
        data: integer value to store in signly linked list
        next_node: next node on signly linked list
    """
    def __init__(self, data, next_node=None):
        """Creates instances of Node

        Args:
            __data(int): node value
            __next_node(node): next node
        """
        self.data = data
        self.next_node = next_node
    @property
    def data(self):
        """return data value
        """
        return self.__data
    @data.setter
    def data(self, value):
        """Set data value
        
        Args:
            value(int): value to put in data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    @property
    def next_node(self):
        """get next node
        """
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        """Set next node
        
        Args:
            value: to put in next node
        """
        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
    """Singly Linked List Class Definition"""

class SinglyLinkedList:
    """
    Class that define the singly linked list
        
     Attributes:
         head: private instance
    """
    def __init__(self):
        """instantation method"""
        self.__head = None
    def sorted_insert(self, value):
        """method to insert new node
       list should be sorted (increasing order) 
            
        Args:
            value(int): value to insert in node
        """
        
        new_node = Node(value)
        if self.__head == None:
             new_node.next_node = None
             self.__head = new_node
        else:
            head = self.__head
            if new_node.data > head.data and head.next_node == None:
                head.next_node = new_node
                new_node.next_node = None
            elif new_node.data <= head.data and head.next_node == None:
                new_node.next_node = head
                head.next_node = None
                self.__head = new_node
            else:
                curr_node = head
                prev_node = None
                while True:
                    if new_node.data > curr_node.data:
                        if curr_node.next_node == None and prev_node != None:
                            prev_node.next_node = curr_node
                            curr_node.next_node = new_node
                            new_node.next_node = None
                            break 
                        prev_node = curr_node
                        curr_node = curr_node.next_node
                        continue
                    elif new_node.data <= curr_node.data:
                        if prev_node == None:
                            new_node.next_node = curr_node
                            self.__head = new_node
                            break
                        else:
                            prev_node.next_node = new_node
                            new_node.next_node = curr_node
                            break
    def __str__(self):
        """Represents the class objects as a string.

        Returns: The class object represented as a string.
        """
        temp_head = self.__head
        node_list = []
        while temp_head:
            node_list.append(str(temp_head.data))
            temp_head = temp_head.next_node

        return ("\n".join(node_list))
