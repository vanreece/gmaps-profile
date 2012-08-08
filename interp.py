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
  begin_x,begin_y = pairs[i]
  end_x,end_y = pairs[i+1]
  delta_x = end_x - start_x
  delta_y = end_y - start_y
  distance = math.sqrt(delta_x*delta_x + delta_y*delta_y)
  newpairs.append(pairs[0])
  biggest_delta = max(math.abs(delta_x), math.abs(delta_y))
  t_step = step * distance / biggest_delta
  max_t = biggest_delta / step
  t = 0.0
  while t < max_t:
    
    newpairs.append(
