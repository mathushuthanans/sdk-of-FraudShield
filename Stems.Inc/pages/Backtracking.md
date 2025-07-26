- Backtracking is a recursive algorithm that incrementally builds solutions by exploring all possible solutions with discarding partial solutions (invalid path) that fail to meet problem constraints. It systematically searches through all possible configurations to find valid solutions.
	- It is Heavily depends on [[Recursion]]
- Constraints
	- Having Choices and Respective operation/Function
	  logseq.order-list-type:: number
	- Explore the Possible Solutions and
	  logseq.order-list-type:: number
	- Backtrack if it get to Invalid path
	  logseq.order-list-type:: number
	- Having a Base condition/case to terminate
	  logseq.order-list-type:: number
-
- ### Concept:
- A statement should be there for **leveling back** to the past state / recursion stack; here, the call stack will automatically control what function to be called.
- A statement should be there to **call the function** to go deeper until reaching the base case.
- Other statements/operations — e.g., a step to **take a decision**.
- If we need to **record anything**, take a **copy of it** (this is right for all cases), because the **future version might be modified**.
  
  ---
- ### Decision Set:
- The **decision move** to be made.
- **Repeat** that decision until the **base case**.
- To **explore other decisions**, we **remove the decision** made at that point.
  
  *(Here the delete part should be **after** the function call.)*
  
  ---
- ### The Patterns in Backtracking (Its Variations):
- **Choice-based Backtracking**
	- **If condition**: every `if` contains a **decision set**
	- **Direct transformation**: the superset of **inclusion & exclusion principle**. Try **every possibility** without any conditions (can say every decision set is involved here).
	- **For loops**: used when having **multiple choices** and need a **decision set** for all of them.
	- **Advanced Segmented Choice**: explore with `for-loop` and expand them in **subsets**.
- **Ordered decision**: input **sorting** and **comparing choices** to avoid duplicates.
- **Tracking visited elements** with a **boolean array**: to **avoid repetition**.
- **Bounding and Pruning**:
	- Here, the **removal statement is implicitly handled** by the recursive case.
	- **Bound** is applied automatically.
- **Inclusion and Exclusion Principle**:
	- **Forbidden constraints**
	- **Overlapping constraints**
	  
	  <!-- notionvc: f6bdbadc-2330-43b9-8967-d7ea866281ad -->