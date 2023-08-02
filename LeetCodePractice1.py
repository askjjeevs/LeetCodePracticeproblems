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
    
    prevMap = {} # use an empty dictionary/hashmap to hold values and indices of the first number visited in the list. hshmap of value:index


    for i, n in enumerate (nums):
        #the value we are looking for is the difference between the target and the number in the list that is being looped over. 
        #we can potentially make a hashmap of every value to in the list
        #
        diff = target - n 
        if diff in prevMap:
            return[prevMap[diff] , i]
        prevMap[n] = i 
    return


"""Given an integer x, return true if x is a palindrome, and false otherwise.  Could you solve it without converting the integer to a string?"""
#palindrome intergers read the same from left to right 
#  x = 12121   ---> true 

#check if the number is negative 
#reverse the input and store in a new variable. 

# try a string conversion solution first


"""Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

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
            