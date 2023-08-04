LeetCodePractice1.py    

"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
# testcase  num = [2,7,1,5] target = 6

#return the indices
# create an empty dictionary- to hold keys : values --> indices : numbers from the list 
# loop through the list 
# count the indices  --> or use enumerate 
# target = x + y 
# target - x = y
# is y in dictionary? 
# if yes, return the key or index 

def twoSum(nums, target):
    dict = {}
    count = -1 # without enumerate we need to keep count the count becomes the index value. Begin at -1, otherwise the count will be out of range
    for num in nums:
        count += 1
        diff = target - num 
        if diff in dict:
            return [dict[diff], count]
        dict[num] = count

def twoSum (nums, target):
    
    # use an empty dictionary/hashmap to hold values and indices of the first number visited in the list. hshmap of value:index
    prevMap = {}
    for i, num in enumerate (nums):
        diff = target - num 
        if diff in prevMap:
            return[prevMap[diff] , i]
        #adds to the dictionary
        prevMap[num] = i 


"""Given an integer x, return true if x is a palindrome, and false otherwise.  Could you solve it without converting the integer to a string?"""
#palindrome intergers read the same from left to right 
#  x = 12121   ---> true 

#check if the number is negative 
#reverse the input and store in a new variable. 

# try a string conversion solution first


"""1480. Running Sum of 1D Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]."""

# go through the list of integers 
# define a new integer
# create a new list 
# return the new list

def runningSum(nums):
    
    newNum = 0 
    runningSumNums =[]
    for num in nums:
        newNum += num
        runningSumNums.append(newNum)
    
    return runningSumNums

# Another solution by modifying the input 
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums 
            

"""1672. Richest Customer Wealth
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 Input: accounts = [[1,2,3],[3,2,1]]
Output: 6

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17 

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
"""
# Time complexity O(m * n)
# create a variable for maxWealth = 0
# iterate over each customer's account in accounts 
# create a variable custWealth=0 to track the wealth of each customer's acct
# add the values for each customer assign the value to wealth
# compare wealth with max wealth. if it is greater it now becomes max wealth
# at the end of the loop return max wealth 

def richestCustomer(accounts):
    maxWealth = 0 
    for customer_acct in accounts:
        wealth = 0
        for amount in customer_acct:
            wealth += amount
        if wealth > maxWealth:
            maxWealth = wealth
    
    return maxWealth

"""412. Fizz Buzz
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Input: n = 3
Output: ["1","2","Fizz"]

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""
# empty list to hold the strings returned 
# print all numbers in the range of n 
# if n % 3 = 0 append Fizz, elif n % 5 append buzz...abs
# append list with str(i) from range
# return str array 

def fizzBuzzNum(n):
    
    fizz_buzz_result = []

    for i in range ( 1, n +1):
        if i % 3 == 0 and i % 5 == 0: 
            fizz_buzz_result.append("FizzBuzz")
        elif i % 3 == 0:
            fizz_buzz_result.append("Fizz")
        elif i % 5 ==0:
            fizz_buzz_result.append("Buzz")
        else:
            fizz_buzz_result.append(str(i))
        
    return fizz_buzz_result

"""1342. Number of Steps to Reduce a Number to Zero
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Input: num = 123
Output: 12

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0."""

# assign a variable 'steps' as a count to 0 
# begin a while loop, set condition != 0
#if even (num % 2 = 0 ) num //=2
#else (num -= 1)
#increase count by 1 

def num_steps_to_zero(num):

    steps = 0 
    while num !=0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps +=1
    
    return steps 

""" 876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100 """
