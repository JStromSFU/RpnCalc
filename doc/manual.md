# User Manual

## Concepts

A calculator is used to perform numeric computations with greater speed and accuracy than by hand.

Typically computations are entered in standard algebraic notation, `1 + 2 x 3`.
A reverse polish notation calculator changes the order.
The operands are entered first, then the operation, `1 ENTER 2 + 3 x`.
This eliminates any confusion with order of operations and allows for operands with different number of operands to be implemented in the same manner.

Values entered are stored on a stack.
The newest value is added at location zero, moving all previous values to the next positions.
When a math operation is invoked, the last values are removed from the stack, the operation is performed, and the result is added to the stack.

## Interface

    +-------------------------+  -
    | 3 [   stack value 3   ] |  |
    | 2 [   stack value 2   ] |  | Stack display
    | 1 [   stack value 1   ] |  |
    | 0 [   stack value 0   ] |  |
    +-------------------------+  -
    | [ < ] [X-Y] [  Enter  ] |  |
    | [ 7 ] [ 8 ] [ 9 ] [ \ ] |  |
    | [ 4 ] [ 5 ] [ 6 ] [ * ] |  | Keypad
    | [ 1 ] [ 2 ] [ 3 ] [ - ] |  |
    | [    0    ] [ . ] [ + ] |  |
    +-------------------------+  -

The stack display shows the top four values on the stack with the newest entry at the bottom.

The numeric keypad is used to enter new values into stack location 0.
When you begin to type a number, values already on the stack will be moved to the next position.
Entry can be completed with the enter key, or be using any operation.
Unwanted entries can be removed from the stack with the "Drop" button.

## Usage

Enter a number with the numeric keypad.
Press "Enter" to add that value to the stack.

When there are values on the stack, press an operation button to perform the computation.

### Operations

    Operation       Button    Result
    ---------       ------    ------
    Addition        +         s1 + s0
    Subtraction     -         s1 - s0
    Multiplication  *         s1 * s0
    Division        /         s1 / s0

### Stack Functions

    Operation       Button    Result
    ---------       ------    ------
    Duplicate       Enter     place a copy of s0 on the stack
    Exchange        x-y       reverse the order of s0 and s1 on the stack
    Drop            <-        remove s0

## Examples

### Arithmetic Operations

#### Addition

To add two numbers: 20 + 5,

    [2] [0] [Enter] [5] [+]

The stack will show the result, 25, in location 0.

#### Subtraction

To subtract two number: 20 - 5

    [2] [0] [Enter] [5] [-]

The stack will show the result, 15, in location 0.

#### Multiplication

To multiply two numbers: 20 x 5,

    [2] [0] [Enter] [5] [*]

The stack will show the result, 100, in location 0.

#### Division

To divide two numbers: 20 / 5,

    [2] [0] [Enter] [5] [/]

The stack will show the result, 4, in location 0.

### Stack Operations

#### Duplicate Entry

With some number on the stack to begin with,

    [2] [0] [Enter]

Duplicate that entry,

    [Enter]

The stack will show the value 20 in both locations 1 and 0.

#### Exchange

With some number on the stack to begin with,

    [2] [0] [Enter]

Place a new value, 5, on the stack but leave 20 at location 0.

    [5] [X-Y]

The stack will show 5 at location 1, and 20 at location 0.

#### Drop

With some number on the stack to begin with,

    [2] [0] [Enter]

Remove the value

    [<]

The stack will be empty.

### Complete Example

The stack can be used to store values while you work on intermediate calculations.

Compute the total bill:

    Case          1x  $ 73
    Power Supply  1x  $103
    Motherboard   1x  $137
    CPU           1x  $ 90
    Hard Disk     1x  $ 60
    Memory        2x  $ 45
    
    Sales Tax: 6%  

Start adding each element of the bill

    [7] [3] [Enter]
    [1] [0] [3] [+]
    [1] [3] [7] [+]
    [9] [0] [+]
    [6] [0] [+]

Line items can be computed leaving the accumulated value on the stack

    [4] [5] [Enter]
    [2] [*]
    [+]

The tax can be computed on a copy of the subtotal

    [Enter]
    [.] [0] [6] [*]
    [+]

