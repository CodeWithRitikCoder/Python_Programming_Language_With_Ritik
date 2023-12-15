"""
Notes:-
    => Number System in Python.

        => Types of Number system.
            -> There are four types of Number system.
                1. Decimal Number system.
                2. Binary Number system.
                3. Octal Number system.
                4. Hexa-Decimal Number system.

        => What is Decimal Number system.
            -> Decimal number system contains (10) digits. and this number system can be resented using 10 digits.
            * These are [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
            * The Decimal number system has base (10) -> it means => (0-9)_10

        => What is Binary number system.
            -> Binary number system contains (2) digits. and this number system can be resented using 2 digits.
            * These are [0 and 1].
            * The Binary number system has base (2) -> it means => (0, 1)_2

        => What is Octal number system.
            -> Octal number system contains (8) digits and this number system can be resented using 8 digits.
            * These are [0, 1, 2, 3, 4, 5, 6, 7, 8].
            * The Octal number system has base (8) -> it means => (0-7)_8

        => What is Hexa-decimal number system.
            -> Hexa-decimal number system contains (16) digits. and this number system can be resented using 16 digits.
            * These are [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F].
            * The Hexa-decimal number system has base (16) -> it means => (0-9, A-F)_16

    => Table of Number system.
                                             |-------------------|
                                             |   Number System   |
                                             |-------------------|
                                                      ||
                        |-------------------|-------------------|--------------------|
                        |                   |                   |                    |
                        |                   |                   |                    |
                |---------------|    |---------------|  |---------------|   |---------------|
                |   Decimal     |    |    Binary     |  |     Octal     |   | Hexa-decimal  |
                |---------------|    |---------------|  |---------------|   |---------------|
                        |                    |                  |                   |
    Represent ->   Base-()_10           Base-()_2           Base-()_8           Base-()_16


    _________________________________________________________________________________________________________________
    | SR |                           |                          |                        |                          |
    | No |   Decimal Number (D)_10   |   Binary Number (B)_2    |   Octal Number (O)_8   |   Hexa-decimal Number    |
    | .. |                           |                          |                        |                          |
    |****|**********************************************************************************************************|
    | 0  |            0              |            0             |            0           |     0  ---->   0000      |
    | 2  |            1              |            1             |            1           |     1  ---->   0001      |
    | 2  |            2              |            X             |            2           |     2  ---->   0010      |
    | 3  |            3              |            X             |            3           |     3  ---->   0011      |
    | 4  |            4              |            X             |            4           |     4  ---->   0100      |
    | 5  |            5              |            X             |            5           |     5  ---->   0101      |
    | 6  |            6              |            X             |            6           |     6  ---->   0110      |
    | 7  |            7              |            X             |            7           |     7  ---->   0111      |
    | 8  |            8              |            X             |            X           |     8  ---->   1000      |
    | 9  |            9              |            X             |            X           |     9  ---->   1001      |
    | 10 |            X              |            X             |            X           |     A  ---->   1010      |
    | 11 |            X              |            X             |            X           |     B  ---->   1011      |
    | 12 |            X              |            X             |            X           |     C  ---->   1100      |
    | 13 |            X              |            X             |            X           |     D  ---->   1101      |
    | 14 |            X              |            X             |            X           |     E  ---->   1110      |
    | 15 |            X              |            X             |            X           |     F  ---->   1111      |
    |_______________________________________________________________________________________________________________|
    |***************************************************************************************************************|

    => Number system conversion.

    |***********************************************************************************************************|
    |   1. (D)_10 to ()_0     |   4. (B)_2 to ()_0      |     7. (O)_8 to ()_0     |   10. (H)_16 to ()_0       |
    |-------------------------|-------------------------|--------------------------|----------------------------|
    |   2. (D)_10 to ()_0     |   5. (B)_2 to ()_0      |     8. (O)_8 to ()_0     |   11. (H)_16 to ()_0       |
    |-------------------------|-------------------------|--------------------------|----------------------------|
    |   3. (D)_10 to ()_0     |   6. (B)_2 to ()_0      |     9. (O)_8 to ()_0     |   12. (H)_16 to ()_0       |
    |-------------------------|-------------------------|--------------------------|----------------------------|
    |       Group-1           |         Group-2         |         Group-3          |         Group-4            |
    |***********************************************************************************************************|


    ********* If your want to know more about it your can refer my Binary Number system png note directory. *********

"""
"""
=> Functions to Number system conversion.
bin(value) -> this will convert into Binary Number system.
oct(value) -> this will convert into Octal Number system.
hex(value) -> this will convert into Hexa-decimal Number system.
  

"""

print("Number system conversion in Python.")

x= 10
print("The binary number of %d is : %s"%(x, bin(x)))
print("The Octal number of %d is : %s"%(x, oct(x)))
print("The Hexa-decimal number of %d is : %s\n"%(x, hex(x)))

x= 0b1111
print("The Octal number of %d is : %s"%(x, oct(x)))
print("The Hexa-decimal number of %d is : %s\n"%(x, hex(x)))

x=0o31
print("The binary number of %d is : %s"%(x, bin(x)))
print("The Hexa-decimal number of %d is : %s\n"%(x, hex(x)))

x=0x19
print("The binary number of %d is : %s"%(x, bin(x)))
print("The Octal number of %d is : %s"%(x, oct(x)))
