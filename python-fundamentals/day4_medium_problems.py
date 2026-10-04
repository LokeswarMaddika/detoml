# Day 4 - Medium LeetCode Problems

# Problem 49 - Group Anagrams
def groupAnagrams(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    return list(groups.values())

# Problem 347 - Top K Frequent Elements
def topKFrequent(nums, k):
    cnt = {}
    for num in nums:
        if num in cnt:
            cnt[num] += 1
        else:
            cnt[num] = 1
    sorted_cnt = sorted(cnt, key=lambda x: cnt[x], reverse=True)
    return sorted_cnt[:k]

# Problem 238 - Product of Array Except Self
def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    
    # Left pass
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Right pass
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

# SQL Solutions (for reference)
# 175 - Combine Two Tables
# SELECT p.firstName, p.lastName, a.city, a.state 
# FROM person p LEFT JOIN address a ON p.personId = a.personId

# 177 - Nth Highest Salary
# SET N = N - 1; RETURN (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET N)

# 178 - Rank Scores
# SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS `rank` FROM Scores

# 180 - Consecutive Numbers
# SELECT DISTINCT num AS ConsecutiveNums FROM (SELECT num, LAG(num,1) OVER (ORDER BY id) AS prev1, LAG(num,2) OVER (ORDER BY id) AS prev2 FROM Logs) t WHERE num = prev1 AND num = prev2

# 181 - Employees Earning More Than Managers
# SELECT e2.name as Employee FROM employee e1 INNER JOIN employee e2 ON e1.id = e2.managerId WHERE e2.salary > e1.salary

# 184 - Department Highest Salary
# SELECT d.name as Department, e.name as Employee, e.salary as Salary FROM Employee e INNER JOIN Department d ON e.departmentId = d.id WHERE e.salary = (SELECT MAX(salary) FROM Employee WHERE departmentId = e.departmentId)