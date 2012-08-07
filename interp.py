import sys

#1/3 arc second
step = 1.0 / 60 / 60 / 3

ifile = open(sys.argv[1],"r")
contents = ifile.read()
lines = contents.split("\n")
entries = lines[1:]
pairs = [map(float,x.split("\t")[1:3]) for x in entries]
newpairs = []
for i in range(len(pairs)-1):
  beginx,beginy = pairs[i]
  endx,endy = pairs[i+1]
  deltax = endx - startx
  deltay = endy - starty
  newpairs.append(pairs[0])
  deltat = 0.0
  if abs(deltax) > abs(deltay):
    
  if xbigger:
    while newx <
