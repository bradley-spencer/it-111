#!/usr/bin/env python3

name = input("Enter your name: ")
amount = input("Enter the amount of your purchase: ")

amount = float(amount)
tax = amount * 0.10
total = amount + tax

print("Hello", name + ",", "here is your sales receipt:")
print("Subtotal = $", format(amount, ',.2f').rjust(8, ' '))
print("     Tax = $", format(tax, ',.2f').rjust(8, ' '))
print("             --------")
print("   Total = $", format(total, ',.2f').rjust(8, ' '))
