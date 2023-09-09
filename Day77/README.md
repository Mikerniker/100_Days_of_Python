# Day 77 Computation with Numpy and N-dimensional Arrays


## Overview

- Topics: Numpy


### The challenge

- Use Numpy to create and generate arrays, analyse the shape and dimensions of a ndarray, slice and subset a ndarray based on its indices
- Do linear algebra like operations with scalars and matrix multiplication
- Use NumPys broadcasting to make ndarray shapes compatible
- Manipulate images in the form of ndarrays


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Notes](#notes)

### Links

- Solution URL: [Computation with Numpy and N-dimensional Arrays](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day77)


### Numpy Notes

- To import NumPy: ```import numpy as np```
- An ndarray is a homogeneous n-dimensional array object, which means all the data have to have the same data type, for example all floating-point numbers.
- And n-dimensional means that we can work with everything from a single column (1-dimensional) to the matrix (2-dimensional) to a bunch of matrices stacked on top of each other (n-dimensional).
- Whereas a Python List or a Pandas DataFrame can contain a mix of strings, numbers, or objects (i.e., a mix of different types). 
- a 1-dimensional array (i.e., a “vector”) example: ```my_array = np.array([1.1, 9.2, 8.1, 4.7])```
- Elements can be accessed in a ndarray similar to Python List, by that element's index: ```my_array[2]```
- To check check the dimensions of the with the ndim attribute: ```my_array.ndim```
- A 2-dimensional array (i.e., a “matrix”)
```
array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])
```
- NumPy refers to the dimensions as axes.

- Again, you can access a particular row or a particular value with the square bracket notation. To access a particular value, you have to provide an index for each dimension. Example if there are two dimensions, so we need to provide an index for the row and for the column. ```array_2d[1,2]```
- To access an entire row and all the values therein, you can use the : operator,  just like a Python List. ```array_2d[0, :]```

#### N-Dimensions
- An array of 3 dimensions (or higher) is often referred to as a ”tensor”. A tensor refers to an n-dimensional array.

#### Generating and Manipulating ndarrays
- Use ```.arange()``` to createa a vector a with a range of values, example: ```a = np.arange(10,30)```
- To reverse the order an array, either use the (double) colon operator or use the built-in .flip() function:
```np.flip(a)``` or ```a[::-1]```
- To print out all the indices of non-zero elements: 
```
b = np.array([6,0,9,0,0,5,0])
nz_indices = np.nonzero(b)
nz_indices # note this is a tuple
``` 
- The ```.random()``` function is another way to quickly create a ndarray, two ways to use it:
```
from numpy.random import random
z = random((3,3,3))
z
```
or use the full path: 
```
z = np.random.random((3,3,3)) # without an import statement
print(z.shape)
z
```
- Use ```.linspace()``` to create a vector x of size n with values spaced out numbers over an interval
```
x = np.linspace(0, 100, num=9)
print(x)
x.shape
```
- A common use-case for .linspace() is to generate the points to plot on a chart.
```
y = np.linspace(start=-3, stop=3, num=9)
plt.plot(x, y)
plt.show()
```
- Use Matplotlib's ```.imshow()``` to display an array as an image. Example:
```
noise = np.random.random((128,128,3))
print(noise.shape)
plt.imshow(noise)
```

#### Broadcasting, Scalars and Matrix Multiplication

##### Linear Algebra with Vectors
- You can add two vectors together:
```
v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
```
And you add or multiply them together
```
v1 + v2
```
The result will be a ndarray where all the elements have been added together ```array([ 6, 6, 5, 10])```

##### Broadcasting
- To do some sort of operation between an array and a single number (aka as a "scalar" in mathematics), NumPy will make the shape of the smaller array - the scalar - compatible with the larger array. This is what;s known as  "broadcasting".

##### Matrix Multiplication
- If we're not multiplying our ndarray by a single number, e.g. by another vector or a 2-dimensional array, in this case, follow the rules of linear algebra.
- Use the .matmul() function or the @ operator. Example
```
c = np.matmul(a1, b1)
print(f"Matrix c has {c.shape[0]} rows and {c.shape[1]} columns.")
c
```
##### Manipulating Images as ndarrays

- Images are a collection of pixels and each pixel is a value for a colour and any colour can be represented as a combination of red, green, and blue (RGB).
- IMPORT STATEMENTS
```
from scipy import misc  # contains an image of a racoon
from PIL import Image  # for reading image files
```

##### Manipulating the ndarray to change the image
- To reverse the order of the rows and the columns in the NumPy array with the .flip() function of the image, example: ```plt.imshow(np.flip(img_gray), cmap='gray')```
- To rotate an image, rotate the array with .rot90()
```
print(a1)
print('a1 array rotated:')
np.rot90(a1)
```  or
```
plt.imshow(np.rot90(img))
```
- To open an image and put it into a NumPy array:
```
file_name = 'yummy_macarons.jpg'
``````
# Use PIL to open
```
my_img = Image.open(file_name)
img_array = np.array(my_img)
```