from ast import Add

import numpy as np
#1.	Create a list [1, 2, 3] and multiply it by 3. What happens?
list=[1,2,3]
#print(list*3)

#2.	Convert [1, 2, 3] into a NumPy array and multiply it by 3. How is the output different?
arr=np.array([1,2,3])
#print(arr*3)

#3.	Create an array [10, 20, 30, 40] and add 5 to every element without using a loop.
xyz=np.array([10, 20, 30, 40])
#print(xyz+5)

#4.	Create an array containing numbers 1 to 10 using arange().
a=np.arange(1,11)
#print(a)

#5.	Create a 3 × 4 array of zeros.
z=np.zeros((3, 4))
#print(z)

#6.	Create a 2 × 5 array filled with 9.
x=np.full((2,3),9)
#print(x)

#7.	Use linspace() to create 6 equally spaced values from 0 to 100.
c=np.linspace(0,100,6)
#print(c)

#8.	Create a 4 × 4 identity matrix.

n=np.eye(4)
#print(n)

#9.	Create a 2 × 3 array and print its ndim, shape, size and dtype.

b = np.array([[1, 2, 3], [4, 5, 6]])
#print("its dimension is ", b.ndim)
#print("its shape is ", b.shape)
#print("its size is ", b.size)
#print("its data type is ", b.dtype)

#10.	Create [1, 2, 3] with dtype float and inspect the output.

k=np.array([1,2,3],dtype=float)
#print(k)

#11.	Predict the shape and size of np.ones((4, 2, 3)) before running it.

#may be shape is 4,2,3 and and size is 24 

u=np.ones((4,2,3))
print(u.shape)
print(u.size)

#12. Fetch first, last, and middle two values

a = np.array([5, 10, 15, 20, 25, 30])

print("First:", a[0])         
print("Last:", a[-1])         
print("Middle two:", a[2:4])   

#13. Fetch element at row 2, column 3 from 3 × 4 array


# 3 rows, 4 columns array
m = np.arange(1, 13).reshape(3, 4)

print("Element at (2,3):", m[2, 3])
#14. Print second column from 3 × 3 array


m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("Second column:", m[:, 1])  # Output: [2 5 8]
#15. Slice top-left 2 × 2 block from 4 × 4 array


m = np.arange(1, 17).reshape(4, 4)

print("Top-left 2x2 block:\n", m[0:2, 0:2])

# 16. Calculate 10% increase without a loopPythonimport numpy as np

a = np.array([10, 20, 30])
result = a * 1.10
print(result)  # Output: [11. 22. 33.]
# 17. Add arrays and np.multiply element-wisePythona = np.array([1, 2, 3])
b = np.array([4, 5, 6])

addition = a + b
multiplication = np.multiply(a, b)

print("Addition:", addition)            # Output: [5 7 9]
print("Multiplication:", multiplication)  # Output: [ 4 10 18]
#18. 2 × 3 matrix addition & Broadcasting explanation


matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]])
vector = np.array([100, 200, 300])

result = matrix + vector
print(result)


import numpy as np

# Topic 7: Aggregation
# #18. Find sum, mean, minimum and maximum of [12, 18, 25, 5, 40].
arr = np.array([12, 18, 25, 5, 40])
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))

# #19. For a 3 x 2 array, calculate column-wise sums and row-wise sums.
m = np.array([[1, 2], [3, 4], [5, 6]])
print("Column-wise sums (axis=0):", np.sum(m, axis=0))
print("Row-wise sums (axis=1):", np.sum(m, axis=1))

# #20. Create marks of five students and compute mean and standard deviation.
marks = np.array([75, 82, 90, 64, 88])
print("Mean:", np.mean(marks))
print("Standard Deviation:", np.std(marks))


# Topic 8: Reshaping, Transpose, and Flattening
# #21. Create numbers 1 to 20 and reshape them into 4 x 5.
a = np.arange(1, 21).reshape(4, 5)
print("Reshaped Matrix:\n", a)

# #22. Transpose a 2 x 3 array and write the new shape before running.
# Expected New Shape: (3, 2)
arr_2x3 = np.array([[1, 2, 3], [4, 5, 6]])
transposed = arr_2x3.T
print("Transposed Matrix:\n", transposed)
print("New Shape:", transposed.shape)

# #23. Flatten a 3 x 3 matrix into one dimension.
m_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Flattened Array:", m_3x3.flatten())


# Topic 9: Boolean Filtering, np.where(), Sorting, Unique
# #24. From [35, 60, 72, 44, 91], print only values >= 60.
scores = np.array([35, 60, 72, 44, 91])
print("Values >= 60:", scores[scores >= 60])

# #25. Use np.where() to label marks >= 40 as Pass and the rest Fail.
marks = np.array([35, 60, 72, 44, 91])
labels = np.where(marks >= 40, 'Pass', 'Fail')
print("Pass/Fail Status:", labels)

# #26. Find unique values in [1, 2, 2, 3, 3, 3, 4] and sort the original array.
x = np.array([1, 2, 2, 3, 3, 3, 4])
print("Unique Values:", np.unique(x))
print("Sorted Array:", np.sort(x))


# Topic 10: Combining and Splitting Arrays
# #27. Concatenate [1, 2] and [3, 4, 5].
a = np.array([1, 2])
b = np.array([3, 4, 5])
print("Concatenated:", np.concatenate([a, b]))

# #28. Stack [10, 20, 30] and [40, 50, 60] as two rows.
row1 = np.array([10, 20, 30])
row2 = np.array([40, 50, 60])
print("VStacked Rows:\n", np.vstack([row1, row2]))

# #29. Split np.arange(12) into three equal parts.
arr_12 = np.arange(12)
parts = np.split(arr_12, 3)
print("Split Parts:", parts)


# Topic 11: Random Numbers
# #30. Generate 10 random integers from 1 to 100 using a fixed seed.
rng = np.random.default_rng(42)
print("Random Integers:", rng.integers(1, 101, size=10))

# #31. Generate a 2 x 3 array of random values between 0 and 1.
print("2x3 Random Floats:\n", rng.random((2, 3)))

# #32. Run the same seeded code twice. Are the numbers the same? Explain why.
rng1 = np.random.default_rng(42)
print("First Run:", rng1.integers(1, 100, size=3))
rng2 = np.random.default_rng(42)
print("Second Run:", rng2.integers(1, 100, size=3))
# Explanation: Yes, the numbers are identical because setting a fixed seed forces the random number generator to follow the exact same deterministic mathematical sequence.


# Topic 12: Missing Values and Type Conversion
# #33. Create [1.0, np.nan, 5.0] and calculate its nan-aware mean.
nan_arr = np.array([1.0, np.nan, 5.0])
print("NaN-aware Mean:", np.nanmean(nan_arr))

# #34. Convert [1, 2, 3] to float dtype.
int_arr = np.array([1, 2, 3])
float_arr = int_arr.astype(float)
print("Float Array:", float_arr)

# #35. Predict the result of np.array([2.9, 3.1]).astype(int).
# Prediction: [2, 3] because integer conversion truncates the decimal portion instead of rounding.
print("Converted Ints:", np.array([2.9, 3.1]).astype(int))


# Topic 13: Copy vs View
# #36. Create an array and a slice. Change the slice and observe whether the original changes.
orig = np.array([10, 20, 30, 40])
view_slice = orig[1:3]
view_slice[0] = 999
print("Original after modifying view:", orig)  # Original changes

# #37. Repeat using .copy(). Explain the difference in one sentence.
orig2 = np.array([10, 20, 30, 40])
copy_slice = orig2[1:3].copy()
copy_slice[0] = 999
print("Original after modifying copy:", orig2)  # Original stays unchanged
# Explanation: Using .copy() creates an independent block of memory, so modifying the copy does not affect the original array.


# Topic 14: Basic Matrix Operations
# #38. Multiply two 2 x 2 arrays element-wise and then with @. Compare outputs.
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Element-wise Multiply:\n", A * B)
print("Matrix Multiply (@):\n", A @ B)

# #39. Calculate dot product of [2, 3, 4] and [0.5, 1, 2].
x = np.array([2, 3, 4])
w = np.array([0.5, 1, 2])
print("Dot Product:", np.dot(x, w))

# #40. If X has shape (100, 4) and weights have shape (4,), predict the shape of X @ weights.
# Prediction: (100,) because the inner dimension (4) cancels out during matrix multiplication.
X = np.ones((100, 4))
weights = np.ones(4)
print("Shape of X @ weights:", (X @ weights).shape)


# Topic 16: Final Practice Set
# #41. Read 5 numbers into a Python list, convert it to a NumPy array, and print each value increased by 10.
py_list = [5, 15, 25, 35, 45]
num_arr = np.array(py_list)
print("Values + 10:", num_arr + 10)

# #42. Create a 4 x 5 array containing 1 to 20. Print shape, ndim, size and dtype.
m4x5 = np.arange(1, 21).reshape(4, 5)
print("Shape:", m4x5.shape)
print("NDim:", m4x5.ndim)
print("Size:", m4x5.size)
print("Dtype:", m4x5.dtype)

# #43. From that array, print the third row, second column, and the middle 2 x 3 block.
print("Third Row:", m4x5[2])
print("Second Column:", m4x5[:, 1])
print("Middle 2x3 Block:\n", m4x5[1:3, 1:4])

# #44. Create marks [45, 88, 32, 76, 59, 91]. Print only passing marks >= 40 and count them.
student_marks = np.array([45, 88, 32, 76, 59, 91])
passing = student_marks[student_marks >= 40]
print("Passing Marks:", passing)
print("Count of Passing Marks:", len(passing))

# #45. Calculate mean, minimum, maximum and standard deviation of the marks.
print("Mean:", np.mean(student_marks))
print("Min:", np.min(student_marks))
print("Max:", np.max(student_marks))
print("Std Dev:", np.std(student_marks))

# #46. Convert numbers 1 to 24 into a 4 x 6 matrix, transpose it, and report the new shape.
m4x6 = np.arange(1, 25).reshape(4, 6)
transacted = m4x6.T
print("Transposed New Shape:", transacted.shape)

# #47. Generate 20 random integers from 1 to 100 with a fixed seed. Print values above 70.
rng_gen = np.random.default_rng(123)
rand_vals = rng_gen.integers(1, 101, size=20)
print("Values above 70:", rand_vals[rand_vals > 70])

# #48. Given two arrays of the same size, calculate their element-wise sum, product and difference.
arr1 = np.array([10, 20, 30])
arr2 = np.array([2, 4, 6])
print("Sum:", arr1 + arr2)
print("Product:", arr1 * arr2)
print("Difference:", arr1 - arr2)

# #49. Create a matrix of student features and calculate column-wise averages.
# Features: [CGPA, Attendance, Projects]
student_features = np.array([
    [3.5, 85, 4],
    [2.8, 70, 2],
    [3.9, 95, 5],
    [3.1, 80, 3]
])
print("Column-wise Averages:", np.mean(student_features, axis=0))

# #50. Demonstrate view vs copy using a slice and explain why this matters when modifying data.
base_arr = np.array([1, 2, 3, 4, 5])
view_mod = base_arr[:3]
copy_mod = base_arr[:3].copy()
view_mod[0] = 100
print("Original modified via view:", base_arr)
# Explanation: Views share memory with the original array, so accidental modifications in a sliced view will overwrite your raw dataset. Copies protect original data.

# #51. Create a vector x and weights w and calculate x @ w. Explain what the single output could represent in a simple model.
x_vec = np.array([3.5, 85, 4])  # student features
w_vec = np.array([0.5, 0.3, 0.2]) # weights
output = x_vec @ w_vec
print("Single Output Score:", output)
# Explanation: The single scalar output represents the final weighted prediction or score (such as an overall performance index) generated by combining input features with assigned model weights.

# #52. Mini challenge: normalize an array with (x - mean) / std using only NumPy. Check that the transformed mean is close to 0.
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
normalized = (data - np.mean(data)) / np.std(data)
print("Normalized Data:\n", normalized)
print("Transformed Mean (close to 0):", np.mean(normalized))


print("All tasks completed successfully.")