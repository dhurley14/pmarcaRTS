import os
import sys
import ast
""" useful for parsing the file with the mapped URLs to tweets
as a python dict

"""
some_data = open(sys.argv[1]).read()
result = ast.literal_eval(some_data)
#print result.keys()
print("\n\n"+result['http://pib.nic.in/newsite/mbErel.aspx?relid=114259'])
