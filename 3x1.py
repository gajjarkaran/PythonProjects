while True:
 
    on = input("\nPlease Type a number to test: ")
    print ("\n\n\n")
 
    on = int(on)
 
    n = int(on)
    count = 0
 
    while n != 1 and n != -1:
      if n % 2 == 0: #even
 
          n = n / 2
          print (n)
          count = count + 1
 
      else:
          n = (3 * n + 1)
          print (n)
          count = count + 1
 
    count = str(count)
    on = str(on)
 
 
    print ("\n" + on + " took " + count + " steps")