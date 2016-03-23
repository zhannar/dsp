# Matrix Algebra

from numpy import matrix

A = matrix([[1,2,3],[2,7,4]])
B = matrix([[1,-1],[0,1]])
C = matrix([[5,-1],[9,1],[6,0]])
D = matrix([[3,-2,-1],[1,2,3]])

u = matrix([6,2,-3,5])
v = matrix([3,5,-1,4])
w = matrix([[1],[8],[0],[5]])

############ Part 1: Matrix Dimensions ############

# Write the dimensions of each matrix:

#1.1) A - 2 x 3
#1.2) B - 2 x 2
#1.3) C - 3 x 2
#1.4) D - 2 x 3
#1.5) u - 1 x 4
#1.6) w - 4 x 1

############ Part 2: Vector Operations ############

#Perform the following operations.
alpha = 6

#2.1) ⃗u + ⃗v =

u + v                   # matrix([[ 3,  5, -1,  4]])
#2.2) ⃗u - ⃗v =

u - v                   # matrix([[ 3, -3, -2,  1]])
#2.3) α⃗u =

alpha * u               # matrix([[ 36,  12, -18,  30]])
#2.4) ⃗u · ⃗v =

from numpy import inner
inner(u,v)              # 51

#2.5) ∥⃗u∥ =
from numpy import linalg
linalg.norm(u)          # 8.6023252670426267


############ Part 3: Matrix Operations ############

#Evaluate each of the following expressions, if it is defined;
# else fill in with ”not defined.”

# 3.1) A + C =
#Not Defined - Dimensions don't match

#3.2)A−CT =
from numpy import transpose
A - transpose(C)                    # matrix([[-4, -7, -3],
                                    #         [ 3,  6,  4]])


#3.3)CT +3D=
transpose(C) + (3 * D)              # matrix([[14,  3,  3],
                                    #        [ 2,  7,  9]])

#3.4) BA =
B * A                               # matrix([[-1, -5, -1],
                                    #        [ 2,  7,  4]])

#3.5) BAT
#Not Defined - Dimensions don't match

#3.6) BC =
#Not Defined - Dimensions don't match

#3.7) CB =
C * B                               # matrix([[ 5, -6],
                                    #       [ 9, -8],
                                    #       [ 6, -6]])

#3.8) B4 =
# Alternatively: B * B * B *B
B ** 4                              # matrix([[ 1, -4],
                                    #       [ 0,  1]])


#3.9) AAT =
A * transpose(A)                    #matrix([[14, 28],
                                    #       [28, 69]])


#3.10) DT D =
transpose(D) * D                    # matrix([[10, -4,  0],
                                    #         [-4,  8,  8],
                                    #         [ 0,  8, 10]])

"""
References:
http://stackoverflow.com/questions/3127404/how-to-represent-matrices-in-python
http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.inner.html
http://stackoverflow.com/questions/9171158/how-do-you-get-the-magnitude-of-a-vector-in-numpy
"""