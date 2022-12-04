#karta = [[0 for y in range(4)] for x in range(4)]
#karta[0].append(1)
#print (karta) 
player_location = ''
karta2 = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
#      for row in karta2]))
#print (karta2[0][2])
print ("Starting game")
player_location == karta2[0][0]
if player_location == karta2[0][0]:
    print ("hello, choose left, north, right or south")
    x = input("")