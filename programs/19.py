# Матрица.

numb = 5
for item in range(1, numb+1):
  for jtem in range(1, numb+1):
    if item == jtem:
      print(item, end=" ")
    else:
      print("0 ", end="")
  print("")

# 1 0 0 0 0 
# 0 2 0 0 0 
# 0 0 3 0 0 
# 0 0 0 4 0 
# 0 0 0 0 5 