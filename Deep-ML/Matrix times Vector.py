'''
Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector


Example:
        input: a = [[1,2],[2,4]], b = [1,2]
        output:[5, 10] 
        reasoning: 1*1 + 2*2 = 5;
                   1*2+ 2*4 = 10
'''

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    if len(a[0])!= len(b):
      return -1
    c = []
    for i in a: 
      hold = 0
      for j in range (len(i)):
        hold+=(i[j]*b[j])
      c.append(hold)
    return c