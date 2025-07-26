- The call stack is a stack data structure used by a computer program to keep track of function calls and their corresponding execution contexts. It manages the order in which functions are called and ensures that each function's state is preserved until it completes.
	- **Function Calls:**
		- When a function is called, its information (such as local variables and the point of execution) is pushed onto the call stack.
		- The call stack keeps track of where the program should return after the function call completes.
	- **Execution Context:**
		- Each function call creates a new execution context that includes the function's parameters, local variables, and the instruction pointer (where the function should resume after returning).
	- **Returning from Functions:**
		- When a function completes, its execution context is popped from the call stack, and control returns to the calling function.
	- **Stack Frames:**
		- Each function call is represented as a stack frame on the call stack. A stack frame contains information about that specific function call.
- ```
  |------------------|     <- Top of the stack (current function)
  | factorial(0)     |
  |------------------|
  | factorial(1)     |
  |------------------|
  | factorial(2)     |
  |------------------|
  | factorial(3)     |     <- Bottom of the stack (initial call)
  |------------------|
  
  ```