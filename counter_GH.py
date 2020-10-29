import os

folder = 'C:/Users/PathToFolder'
total = 0
for file in os.listdir(str(folder)):
    count = len(open(folder + '/' + file).readlines( ))
    total = total + count
    print ("Line Count: " + str(count) + " File: " + file)
    
print(total)
