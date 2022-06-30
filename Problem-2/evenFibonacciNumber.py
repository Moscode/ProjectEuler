def fibonacci():
  fib = [1, 2]
  for i, val in enumerate(fib):
    nextNum = fib[i] + fib[i + 1]
    if nextNum < 4000000:
      fib.append(nextNum)
    else:
      break
  print(fib)
  for index, value in enumerate(fib):
     if value % 2 == 0:
       continue
     else:
       fib[index] = 0
  return fib
  
print(sum(fibonacci()))