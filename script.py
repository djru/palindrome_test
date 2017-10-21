# converts int to base b, returns list of ints
def conv(num, b, list=[]):
  if num<b:
      return list + [num]
  else:
    # divides by b rounding down, and appends the remainder to the list
    return conv(num//b,b, list + [num%b])

def find_min_base(i):
  j = 2
  base_x = conv(i,j)
  while base_x != base_x[::-1]:
    j += 1
    base_x = conv(i,j)
  return j
  
print("decimal", "smallest base in which the number is a palindrome")
for i in range(1,1001):
  print(i,find_min_base(i))
  
  
  
#test first 20
print("first 20 correct: {}".format([find_min_base(i) for i in range(1,21)] == [2,3,2,3,2,5,2,3,2,3,10,5,3,6,2,3,2,5,18,3]))
    
  
