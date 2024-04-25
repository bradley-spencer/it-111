#!/usr/bin/env python3

turn_num = 1
point_num = 0
end_game = 0
result = "You haven't won or lost yet"

roll_num = int(input("Enter a dice roll number 2-12 (inclusive): "))

if roll_num < 2 or roll_num > 12:
    print("It needs to be between 2-12 (inclusive)")
    quit()

if turn_num == 1:
    if roll_num == 2 or roll_num == 3 or roll_num == 12:
        result = "You lose!"
        end_game = 1
    elif roll_num == 7 or roll_num == 11:
        result = "You win!"
        end_game = 1
    else:
        point_num += roll_num
        turn_num += 1

print("Turn number:", turn_num, "\nDie roll:", roll_num, "\nResult:", result)


if end_game == 1:
    quit()

roll_num = int(input("Enter a dice roll number 2-12 (inclusive): "))

if roll_num < 2 or roll_num > 12:
    print("It needs to be between 2-12 (inclusive)")
    quit()

if turn_num > 1:
    if roll_num == 7:
        result = "You lose!"
        end_game = 1
    elif roll_num == point_num:
        result = "You win!"
        end_game = 1
    else:
        turn_num += 1

print("Turn number:", turn_num, "\nDie roll:", roll_num, "\nResult:", result)
