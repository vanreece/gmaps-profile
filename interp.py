import sys, numpy

#1/3 arc second
step = 1.0 / 60 / 60 / 3

ifile = open(sys.argv[1],"r")
contents = ifile.read()
lines = contents.split("\n")
entries = lines[1:]
pairs = [map(float,x.split("\t")[1:3]) for x in entries]
newpairs = []
total_distance = 0.0
for i in range(len(pairs)-1):
  begin      = numpy.array(pairs[i])
  end        = numpy.array(pairs[i+1])
  #skip identical pairs
  if (begin == end).all():
    continue
  difference = end - begin
  distance   = numpy.linalg.norm(difference)
  total_distance += distance
  newpairs.append(pairs[0])
  biggest_delta = max(numpy.abs(difference[0]), numpy.abs(difference[1]))
  t_step = step * distance / biggest_delta
  max_t = biggest_delta / step
  for t in numpy.linspace(0.0, max_t, biggest_delta / step):
    pair = begin + difference * t
    newpairs.append(pair)
    t += t_step

print "type\tlatitude\tlongitude\taltitude (m)\tname"
for pair in newpairs:
  print "T\t" + str(pair[0]) + "\t" + str(pair[1]) + "\t\t"