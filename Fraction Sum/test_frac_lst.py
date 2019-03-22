#! usr/bin/env python3
from fractions import Fraction
import collections

def main():
    f_lst = eval(input())
    print(sum(f_lst))
    print(len(f_lst))
    if len(f_lst) == len(set(f_lst)):
    	print(True)
    else:
    	print([item for item, count in collections.Counter(f_lst).items() if count > 1])

"""
    	offset = 0
    	for i in range(len(f_lst)):
    		if f_lst[i+offset] == list(set(f_lst)):
    			pass
    		else:
    			print(f_lst[i+offset])
    			offset += 1
"""

if __name__ == "__main__":
    main()