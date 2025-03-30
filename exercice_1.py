"""
Initial code was created by Vishal Sharma
See:  https://towardsdatascience.com/the-zen-of-python-a-guide-to-pythons-design-principles-93f3f76d088a
"""
def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

number = input("Enter a number: ")

while number != 1:
    number = collatz(int(number))
    print(number)

"""
Enter a number: 5
16
8
4
2
1
"""