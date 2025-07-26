- Time frame: [[May 13th, 2025]] - [[May 18th, 2025]]
- Status: [[DOING]]
-
- ### What is the Limitations and Use case
	- Read World
	- Competitive Programming
-
- ### Todolist
	- ### Functions and Operation Completion
		- DONE Insertion
		- DONE Deletion
		- DONE Update/Modify
		- DONE  Access
		- DONE Compare
	- TODO Check the questions that completes the above checklist.
- [[CP Questions]]
	- [1721. Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/)
	-
-
- ### Notes:
	- IF check head is `null` set head to node.
	- SET the node's `next` to the head then make the node as head.
	- ```java
	  node.next = thisNode // used to link
	  thisNode = node.next // .next points to the next
	  ```
	- Head is keep updated on every new node Modification
	- to add faster @ last:
	  `linkedlist.tail = insertLast(head, data)`
	-