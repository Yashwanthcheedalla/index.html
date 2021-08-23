# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:21:45 2021

@author: Yashwanth
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList: 
    def __init__(self):
        self.head=None
        self.last_node=None
    def append1(self,data):
        if self.head is None:
            self.head=Node(data)
            self.last_node=self.head 
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def insert_at_beginning(self,data):
        nb=Node(data)
        nb.next=self.head 
        self.head=nb
    def insert_at_end(self,data):
        ne=Node(data)
        temp=self.head 
        while(temp.next):
            temp=temp.next 
        temp.next=ne
        
    def insert_at_position(self,pos,data):
        np=Node(data)
        curr=self.head
        for i in range(pos-1):
            curr=curr.next
            np.next=curr.next
            curr.next=np
    def delete_at_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_at_end(self):
        temp=self.head.next
        prev=self.head
        while(temp.next):
            temp=temp.next
            prev=prev.next
        prev.next=None
    def delete_at_position(self,pos):
        temp=self.head.next 
        prev=self.head 
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next 
        prev.next=temp.next
        temp.next=None
    def reverse_List(self):
        t=self.head 
        count=0
        while(t.next):
            t=t.next
            count+=1
        i=0
        j=count
        p=self.head 
        q=self.head
        while(i<j):
            k=0
            while(k<j):
                q=q.next 
                k+=1
            p.data,q.data=q.data,p.data
            i+=1
            j-=1
            p=p.next
            q=self.head
       # L.display()
    def display(self):
         if self.head is None:
             print(" linked list is empty")
         else:
             curr=self.head 
             while(curr):
                 print(curr.data,end="-->")
                 curr=curr.next 
         print()

L=LinkedList()
n=int(input(" Enter the number of  nodes"))
for i in range(n):
    t=int(input("enter: "))
    L.append1(t)
L.display()
"""k=int(input("1.add at beginning, \
            2.add at end ,\
              3.add at position"))"""
p=1
while(p==1):
    print("1, Add at beginning")
    print("2, Add at end")
    print("3, Add at position")
    print("4, Add at delete at beginning")
    print("5, Delete a end")
    print("6,Delete at position")
    print("7, reverse the linked list")
    print("8, Display the list")
    #print("1, Add at beginning")
    k=int(input("Enter your option : "))
  

    if(k==1):
        t=int(input("enter a number"))
        L.insert_at_beginning(t)
        print("")
        
    elif(k==2):
        t=int(input("enter a number"))
        L.insert_at_end(t)
        print("")
        #L.display()
    elif(k==3):
        t=int(input("enter the position"))
        da=int(input("enter the data"))
        L.insert_at_position(t,da)
        print("")
        #L.display()
    elif(k==4):
        L.delete_at_beginning()
    elif(k==5):
        L.delete_at_end()
    elif(k==6):
        r=int(input("enter the position :"))
        L.delete_at_position(r)
    elif(k==7):
        L.reverse_List()
    elif(k==8):
        L.display()
    else:
        print("invalid input")
    p=int(input("for continue 1,for quit 0"))

        
        
           
    
    