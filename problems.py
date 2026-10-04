# 1. Reverse an Array
arr = [10, 20, 30, 40, 50]
reversed_arr = []
for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])
print(reversed_arr)


# 2. Count Even, Odd and Zero
arr = [10, 5, 0, 7, 8, 0, 13, 4]
even = 0
odd = 0
zero = 0
for num in arr:
    if num == 0:
        zero += 1
    elif num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)
print("Zero:", zero)


# 3. Sum of Positive and Negative Numbers
arr = [10, -5, 20, -8, 15, -2]
positive_sum = 0
negative_sum = 0
for num in arr:
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_sum += num
print("Positive Sum:", positive_sum)
print("Negative Sum:", negative_sum)


# 4. Remove Duplicate Elements
arr = [10, 20, 10, 30, 20, 40, 30]
unique = []
for num in arr:
    if num not in unique:
        unique.append(num)
print(unique)


# 5. Find the Missing Number
arr = [1, 2, 3, 5, 6, 7]
n = len(arr) + 1
missing = n * (n + 1) // 2 - sum(arr)
print("Missing Number:", missing)


# 6. Rotate an Array
arr = [1, 2, 3, 4, 5]
k = 2
k = k % len(arr)
rotated = arr[-k:] + arr[:-k]
print(rotated)


# 7. Find the Most Frequent Element
arr = [2, 5, 2, 8, 5, 2, 3, 5, 2]
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
most_frequent = arr[0]
for num in freq:
    if freq[num] > freq[most_frequent]:
        most_frequent = num
print("Most Frequent Element:", most_frequent)
print("Frequency:", freq[most_frequent])


# 8. Maximum Subarray Sum
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = arr[0]
current_sum = arr[0]
start = 0
end = 0
temp_start = 0
for i in range(1, len(arr)):
    if current_sum < 0:
        current_sum = arr[i]
        temp_start = i
    else:
        current_sum += arr[i]
    if current_sum > max_sum:
        max_sum = current_sum
        start = temp_start
        end = i
print("Maximum Subarray Sum:", max_sum)
print("Subarray:")
print(arr[start:end + 1])


# 9. Check Whether Two Arrays are Equal
arr1 = [1, 2, 2, 3, 4]
arr2 = [4, 2, 1, 2, 3]
equal = len(arr1) == len(arr2)
if equal:
    count = {}
    for num in arr1:
        count[num] = count.get(num, 0) + 1
    for num in arr2:
        if count.get(num, 0) == 0:
            equal = False
            break
        count[num] -= 1
if equal:
    print("Arrays are Equal")
else:
    print("Arrays are Not Equal")