# Technical Specification

## Dependencies

Python version 3.11 or later

PySide version 6.10 or later

PyTest version 9.0 or later

## Architecture

The code is divided into modules,

ui.py: Creates the Qt GUI window, receives keypresses from the user, and updates the displayed values.

calc.py: Holds the calculator state, receives commands from the GUI or can be operated independently.

## ui.py

    +-------------------------+
    | 3 [   stack value 3   ] |
    | 2 [   stack value 2   ] |
    | 1 [   stack value 1   ] |
    | 0 [   stack value 0   ] |
    +-------------------------+
    | [ < ] [X>Y] [  Enter  ] |
    | [ 7 ] [ 8 ] [ 9 ] [ \ ] |
    | [ 4 ] [ 5 ] [ 6 ] [ * ] |
    | [ 1 ] [ 2 ] [ 3 ] [ - ] |
    | [    0    ] [ . ] [ + ] |
    +-------------------------+

### Layout & Appearance

Stack entries are shown at the top of the screen.
Labels on the left show the depth of the stack.
Stack values beyond the fourth are not shown.
If the calculator stack has fewer entries than the screen, the unused entries are shown as "-".

Keys are divided into three types for easier identification:
Numeric: digits (0-9) and the decimal point.
Arithmetic: add, substract, multiply, divide
Stack: drop, swap, enter

And are styled based on the computer's color scheme:

Keys | Light Scheme | Dark Scheme
---------------------------------
Numeric | Light Gray | Dark Gray
Arithmetic | Light Blue | Dark Blue
Stack | Light Blue | Dark Blue

### State & Input

The UI can be in one of two states,

#### Insert

If the user presses a numeric key, a new value will be created and the state changed to edit.

#### Edit

Display of the stack values will be offset by one.
The value being edited is shown at location zero.

If the user presses a numeric key, that digit is appended to the value being edited.

If the user presses an operator key, the value being edited is pushed onto the stack before computing the operation.


### Helper Functions

make\_numpad\_button( digit )
: Creates a button for the numeric keypad applying the appropriate styles and automatically appending the value to the value being entered.

make\_operator\_button( text, function )
: Creates a button with `text`.  When pressed it will push the entered value onto the stack (if in Edit mode), run the specified operation, then update the displayed stack to match the calculator state.

do\_operation( function )
: Wrap call to `function` by first pushing the entered value (if in Edit mode) onto the stack, and on return update the stack display to match the calculator state.

push\_edit()
: If in Edit mode, pushes the entered value onto the stack and return to Insert mode.

update\_display()
: Update the four displayed stack entries to match the state of the calculator.  If in Edit mode, the calculator's stack will be shown one position lower and position zero will be the partial user input.

## calc.py

### API

\_\_init\_\_()
: Creates a new calculator with an empty stack

#### Stack Operations

peek(n)
: Returns the nth value in the stack, or None if n exceeds the size of the stack.

push(v)
: Adds v to the top of the stack

pop()
: Removes the value from the top of the stack and returns it, or None if the stack is empty.

exchange()
: Swaps the two values at the top of the stack.

#### Math Operations

add()
: Adds the top two values of the stack and pushes the result.

sub()
:  Subtracts the value from the top of the stack from the value second from the top and pushes the result.

mul()
: Multiplies the top two values of the stack and pushes the result.

div()
: Divides the value from the top of the stack into the value second from the top and pushes the result.


## Unit Tests

The test directory contains unit tests of calc.py.
Execute these test with `uv run pytest`

test\_calc\_arith.py
: Test arithmetic operations of the calculator

test\_calc\_stack.py
: Test stack operations of the calculator
