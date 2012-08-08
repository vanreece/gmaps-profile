import sys, numpy

#1/3 arc second
step = 1.0 / 60 / 60 / 3

ifile = open(sys.argv[1],"r")
contents = ifile.read()
lines = contents.split("\n")
entries = lines[1:]
pairs = [map(float,x.split("\t")[1:3]) for x in entries]
newpairs = []
for i in range(len(pairs)-1):
  begin      = numpy.array(pairs[i])
  end        = numpy.array(pairs[i+1])
  difference = end - begin
  distance   = numpy.linalg.norm(difference)
  #print pairs[0]
  newpairs.append(pairs[0])
  biggest_delta = max(numpy.abs(difference[0]), numpy.abs(difference[1]))
  t_step = step * distance / biggest_delta
  max_t = biggest_delta / step
  t = 0.0
  while t < max_t:
    pair = begin + difference * t
    #print pair
    newpairs.append(pair)
    t += t_step
#print pairs[-1]
newpairs.append(pairs[-1])
print len(newpairs)
print newpairs
