import math

def mult(x,y):
  n_x = len(str(x))
  n_y = len(str(y))

  n = max(n_x,n_y)


  b_x = int(str(x)[0:math.ceil(n/2)])
  a_x = int(str(x)[math.ceil(n/2):])
  print(a_x, b_x)

  b_y = int(str(y)[0:math.ceil(n/2)])
  a_y = int(str(y)[math.ceil(n/2):])
  print(a_y, b_y)

  s1 = a_x*a_y
  s2 = (a_x + b_x)*(a_y + b_y)
  s3 = b_x*b_y

  i = 10**(math.floor(n/2))
  print(i)
  print(a_x + i*b_x)
  print(a_y + i*b_y)

  return s1 + i*(s2 - s1 - s3) + i**2*s3


print(mult(12345,6789))
print(12345*6789)
