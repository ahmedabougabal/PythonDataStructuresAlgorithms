"""
You are given an array of integers nums and a non-negative integer k. 
You can perform operations where you increase or decrease any element 
of the array by 1. Your task is to determine the minimum number of operations 
required to adjust the elements of nums such that the median of the array 
becomes exactly k.

The median is defined as the middle element in the sorted version of the array. 
If the array has an even number of elements, the median is the larger of the 
two middle values.

Examples

Input: nums = [3,7,1,4,6], k = 5
Output: 1
Explanation: After sorting, the array becomes [1,3,4,6,7]. 
The median is the 3rd element (4). Increasing it to 5 requires 1 operation.

Input: nums = [1,4,5,9,10], k = 8
Output: 3
Explanation: After sorting, the median is the 3rd element (5). 
Increasing it to 8 requires 3 operations.

Input: nums = [10,12,14,16,18], k = 14
Output: 0
Explanation: The median is already 14, so no operations are needed.

Constraints

1 <= nums.length <= 2 * 10^5
"""
from typing import List
from statistics import median
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Calculate minimum operations to make k the median of nums.
        
        Args:
            nums: List of integers
            k: Target median value
            
        Returns:
            int: Minimum number of operations required
        """
        # Your implementation here
        #! approach 1 (passes all testcases but not covering the edge ones)
        # nums.sort()
        # res = 0
        # my_median = median(nums)
        # if(my_median == k):
        #     res = 0
        # elif my_median < k:
        #     res = k - my_median
        # else:
        #     res = my_median -k
        # return res
        #* solution 2 
        nums.sort()
        n = len(nums)
        res = 0
        if(n %2==0):
            median1 = n // 2 - 1
            median2 = n // 2
            m1 = max(nums[median1], nums[median2])
            res = abs( k - m1)
        else :
            m2 = nums[n//2]
            res = abs(k - m2)
        return res


def test_cases():
    solution = Solution()
    tests_passed = 0
    total_tests = 6  # Updated total tests to 6
    
    # Test case 1
    nums1 = [3, 7, 1, 4, 6]
    k1 = 5
    expected1 = 1
    result1 = solution.minOperations(nums1, k1)
    print(f"Test case 1: nums = {nums1}, k = {k1}")
    print(f"Your output: {result1}")
    print(f"Expected output: {expected1}")
    if result1 == expected1:
        print("✓ Test case 1 passed")
        tests_passed += 1
    else:
        print("✗ Test case 1 failed")
    print()
    
    # Test case 2
    nums2 = [1, 4, 5, 9, 10]
    k2 = 8
    expected2 = 3
    result2 = solution.minOperations(nums2, k2)
    print(f"Test case 2: nums = {nums2}, k = {k2}")
    print(f"Your output: {result2}")
    print(f"Expected output: {expected2}")
    if result2 == expected2:
        print("✓ Test case 2 passed")
        tests_passed += 1
    else:
        print("✗ Test case 2 failed")
    print()
    
    # Test case 3
    nums3 = [10, 12, 14, 16, 18]
    k3 = 14
    expected3 = 0
    result3 = solution.minOperations(nums3, k3)
    print(f"Test case 3: nums = {nums3}, k = {k3}")
    print(f"Your output: {result3}")
    print(f"Expected output: {expected3}")
    if result3 == expected3:
        print("✓ Test case 3 passed")
        tests_passed += 1
    else:
        print("✗ Test case 3 failed")
    print()
    
    # Test case 4 (Even length array)
    nums4 = [1, 2, 3, 4]
    k4 = 3
    expected4 = 0
    result4 = solution.minOperations(nums4, k4)
    print(f"Test case 4: nums = {nums4}, k = {k4}")
    print(f"Your output: {result4}")
    print(f"Expected output: {expected4}")
    if result4 == expected4:
        print("✓ Test case 4 passed")
        tests_passed += 1
    else:
        print("✗ Test case 4 failed")
    print()
    
    # Test case 5 (Array with duplicate elements)
    nums5 = [1, 2, 2, 3, 4]
    k5 = 3
    expected5 = 1
    result5 = solution.minOperations(nums5, k5)
    print(f"Test case 5: nums = {nums5}, k = {k5}")
    print(f"Your output: {result5}")
    print(f"Expected output: {expected5}")
    if result5 == expected5:
        print("✓ Test case 5 passed")
        tests_passed += 1
    else:
        print("✗ Test case 5 failed")
    print()
    
    # Test case 6 (Single element array)
    nums6 = [5]
    k6 = 3
    expected6 = 2
    result6 = solution.minOperations(nums6, k6)
    print(f"Test case 6: nums = {nums6}, k = {k6}")
    print(f"Your output: {result6}")
    print(f"Expected output: {expected6}")
    if result6 == expected6:
        print("✓ Test case 6 passed")
        tests_passed += 1
    else:
        print("✗ Test case 6 failed")
    print()
    
    # Print summary
    print(f"Test Results: {tests_passed} out of {total_tests} tests passed")
    if tests_passed == total_tests:
        print("Congratulations! All tests passed! 🎉")
    else:
        print(f"Keep trying! {total_tests - tests_passed} test(s) failed.")

if __name__ == "__main__":
    test_cases()