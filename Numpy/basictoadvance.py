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