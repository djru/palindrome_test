def conv(num,b, list = []):
  if num<b:
      return [num] + list
  else:
    return conv(num//b,b) + [num%b]

print("decimal", "smallest base in which the number is a palindrome")
for i in range(1,1000):
  j = 2
  base_x = conv(i,j)
  while base_x != base_x[::-1]:
    j += 1
    base_x = conv(i,j)
  print(i,j)
    
  
