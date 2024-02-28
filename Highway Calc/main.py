# Get and check input
highway_number = int(input())
if highway_number < 1 or highway_number > 999:
  print (highway_number, 'is not a valid interstate highway number.'.format (highway_number))
  quit()

if highway_number % 100 <= 0:
    print (highway_number, 'is not a valid interstate highway number.'.format (highway_number))
    quit()

# Type + serving
if highway_number > 100:
  road_type = 'auxiliary'
  serving = str(highway_number % 100)
else:
  road_type = 'primary'
  serving = ''

# Direction
if highway_number % 2 == 0:
  going = 'east/west.'
else:
  going = 'north/south.'

# Create output
output = ['I-{}'.format(highway_number), 'is', road_type + ',']
if serving:
  output.extend(['serving', 'I-{},'.format(serving)])
output.extend(['going', going])
print(' '.join(output))
