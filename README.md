MindBreak
An enhanced version of MindFuck

Why?
Because I can.
So, it's pretty much the same as MindFuck but it has ques from assembly.
I recomend learning BrainFuck before using this.

How to use:
	* any operator marked with a star (*) was either added or modifyed from source material

The Tape:
	You have a read/write head on a tape of 1000 descrete cells.
	Each cell is an interger.
	A cell can only be worked with if the tapehead has selected it.


Basic Operators:
	(>) - Moves the tapehead one (1) position to the right,
	(<) - Moves the tapehead one (1) position to the left,
	(+) - Increments the value of the current cell selected by the tapehead by one (1),
 	(-) - Increments the value of the current cell selected by the tapehead by negative-one (-1),
	(#)* - A No-Op, can be used more than one with Numbers,

In-Out:
	(.) - Outputs the currently selected cell as an ASCII Character,
	(,) - Takes input one-cell-at-a-time as an ASCII value, and not a character, no input defualts to a zero (0),

Numbers:
	The Numbers system is denoted as any base-ten numbers between zero and nine (0-9).
	The Numbers repeat the last Basic Operator X times, where X is the number.
	NOTE: The numbers are used one-at-a-time, 15 is (1+5=6), not the number 15.

Skip-if-Zero:
	([ ])* - Skip-if-Zero operator. Instead of the loop operator of regular BrainFuck,
		 It just skips the code inside if the current cell's value is 0.
		 Hovever, these cannot be nested. this is by design.

Pointers:
	Now we get to the most advance part of the language. This is a powerful but unpredictable feature, use it wisely.
	
	($)* - Type T pointer declaration. It records the value in the current cell as a Tape Index, which can be jumped to from
	      Anywhere else.
	(&)* - Program Pointer, p type. It records the current value in the selected cell as a Code Index,
	      A code index is an index that records a the spot of a particular character (Operator) within your code.
	      You can jump back to that point from anywhere else.
	(*)* - Jump-To-Pointer operator. It uses the value in the current cell as the index to jump to any defined operator.
	      It takes into account the pointer type by itself.
	The index of the pointers is a zero-indexed array where a new pointer is added to the bottom of the stack
	in order of definition.
