import sys
import pandas as pd
sys.path.append('../src/')
from LingoOut import LingoOut

filename = 'sample1.txt'

out1 = LingoOut(filename)

print(pd.DataFrame(out1.variable).head())


# test = LingoOut('test.txt')
# test.dict
#
# print(test)
#
# test.variable
