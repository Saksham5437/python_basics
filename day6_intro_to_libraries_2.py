#statistics module

import statistics
result = statistics.mean([100, 50, 90, 88, 89])
print(result)

#sys.argv

import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguements")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
print("Hi, Welcome", sys.argv[1])

