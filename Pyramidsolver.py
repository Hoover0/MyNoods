blocks = int(input('Enter the number of blocks: ')) #Number of blocks the user wants
layers = 0 #height of pyramid
rows = 0 #rows of blocks in each layer

#Adds rows and layers, and removes blocks gradually to calculate pyramid height
while rows < blocks:
    rows += 1
    layers += 1
    blocks -= 1*rows

print('The height of the pyramid:', layers)