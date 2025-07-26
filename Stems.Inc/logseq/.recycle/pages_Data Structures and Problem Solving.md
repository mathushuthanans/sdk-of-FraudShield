- Backtracking:
  collapsed:: true
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
- LinkedList:
- query-table:: true
  #+BEGIN_QUERY
  {:title "Projects"
   :query [:find (pull ?b [*])
           :where
           [?b :block/refs ?p]
           [?p :block/name "projects"]]}
  #+END_QUERY
- ### Areas
  query-table:: false
  collapsed:: true
  #+BEGIN_QUERY
  {:title "Areas"
  :query [:find (pull ?b [*])
         :where
         [?b :block/refs ?p]
         [?p :block/name "areas"]]}
  #+END_QUERY_