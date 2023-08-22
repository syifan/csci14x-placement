# CSCI140/141 Placement Exam

**Purpose:** The objective of this exam is to assess whether students possess the necessary proficiency to bypass the CSCI140/141 courses and enroll directly in the 2XX-level courses.

**Format:** The exam comprises four programming challenges.

**Duration:** Students are allotted 2 hours to complete the exam.

**Resources:** Exam participants are permitted to search the internet for basic Python syntax, such as "how to append to a list". However, seeking direct solutions to the exam problems or using generative AI tools is strictly prohibited.

**How to take the exam:** You can fork this repo and solve the problems within your repo. When you commit and push the repo, GitHub will run the tests. If you can pass the test within 2 hours, you pass the exam. You can also run `python3 -m unittest` to run the tests locally. You can run any time you want and fix your code according to the test requirement. 

Once you pass the test, there is no need to report the test result to anyone. If you pass, you can directly select CSCI2XX courses (assuming you have AP courses to fulfill the prerequisite). If you fail, it is recommended to take CSCI140/141 courses. If you have any questions, please contact the instructor.

## Problem 1. N-th Prime Number

**Objective:** Write a Python function called `nth_prime` that takes an integer `n` as its argument and returns the n-th prime number.

### Background:

A prime number is a whole number greater than 1 that cannot be divided by any other whole numbers except 1 and itself. The first six prime numbers are 2, 3, 5, 7, 11, and 13.

### Task:

Given an integer `n`, return the n-th prime number.

**Function signature:**
```python
def nth_prime(n):
    pass  # Your code goes here
```

### Examples:

```python
assert nth_prime(1) == 2
assert nth_prime(2) == 3
assert nth_prime(3) == 5
assert nth_prime(4) == 7
assert nth_prime(6) == 13
```

### Constraints:

* \( 1 \leq n \leq 1000 \)


## Problem 2: Two-Sum Problem

**Objective:** Write a Python function named `two_sum` that takes a list of integers and a target integer. It should return the indices of the two numbers in the list that add up to the target.

### Background:

Given a list of integers, you need to find two numbers in the list such that their sum is equal to a specific target. You can assume that each input has exactly one solution, and you may not use the same element twice.

### Task:

Given a list of integers, `numbers`, and an integer `target`, your `two_sum` function should return a list containing the indices of the two numbers such that they add up to the `target`.

**Function signature:**
```python
def two_sum(numbers, target):
    pass  # Your code goes here
```

### Examples:

```python
assert two_sum([2, 7, 11, 15], 9) == [0, 1]  # 2 + 7 = 9
assert two_sum([3, 2, 4], 6) == [1, 2]  # 2 + 4 = 6
assert two_sum([3, 3], 6) == [0, 1]  # 3 + 3 = 6
```

### Constraints:

* The list `numbers` will have a length between 2 and \(10^4\).
* Each element in the list is an integer between \(-10^4\) and \(10^4\).
* There is exactly one solution for each input set.


## Problem 3: String Multiplication

**Objective:** Write a Python function named `string_multiply` that takes two strings, representing non-negative integers, and returns their product as a string.

### Background:

You're likely familiar with how multiplication works with numbers. However, this time, you will implement multiplication without converting the entire string into an integer. This exercise will challenge your understanding of both strings and arithmetic operations.

### Task:

Given two non-negative number strings, `num1` and `num2`, your `string_multiply` function should return their product as a string.

**Function signature:**
```python
def string_multiply(num1, num2):
    pass  # Your code goes here
```

### Examples:

```python
assert string_multiply("2", "3") == "6"
assert string_multiply("123", "456") == "56088"
assert string_multiply("0", "1234") == "0"
assert string_multiply("1000", "1000") == "1000000"
```

### Constraints:

* The lengths of both `num1` and `num2` are less than or equal to 200.
* Both `num1` and `num2` contain only digits 0-9.
* Both `num1` and `num2` do not contain any leading zeros except the number 0 itself.
* Do not use any inbuilt big integer library or convert the entire string to integers directly.


Of course! Here's a problem that introduces students to Object-Oriented Programming (OOP) concepts such as classes, objects, attributes, and methods:

## Problem 4: Simple Bank System

**Objective:** Design a basic OOP system for a bank that can create accounts, deposit money, withdraw money, and display balance.

### Background:

In this task, you will create a simplified banking system. Your bank should be able to handle multiple accounts, each with its own balance.

### Task:

1. Design a `BankAccount` class that has the following attributes:
    * `account_number` (a unique identifier for the account)
    * `balance` (a float that keeps track of the account's money)
    
2. The `BankAccount` class should have the following methods:
    * `deposit(amount)`: Add `amount` to the balance.
    * `withdraw(amount)`: Subtract `amount` from the balance. If the amount is greater than the balance, print "Insufficient funds" and do not change the balance.
    * `display_balance()`: Print the current balance.

3. Make sure to provide proper encapsulation principles for attributes and methods (i.e., think about what should be public and what should be private).

**Example code structure:**
```python
class BankAccount:
    def __init__(self, account_number):
        pass  # Your code goes here
    
    # Additional methods go here

# Testing your class
account1 = BankAccount(12345)
account1.deposit(500)
account1.withdraw(100)
account1.display_balance()  # This should display 400
```

### Constraints:

* `account_number` is a unique integer.
* `balance` is initialized to 0.0 for every new account.
* You can assume that all input amounts for deposit and withdrawal will be positive.