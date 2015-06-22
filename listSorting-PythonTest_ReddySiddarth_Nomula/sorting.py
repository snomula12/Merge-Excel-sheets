'''
	@author: Siddarth
	The purpose of this script is to sort interger and strings in place and also remove all ascii symbols from them.

	please run the script in the following format
	python sorting.py  input.txt output.txt
'''

import re
import sys


def sorting(unsorted_list):
	'''
		In this method, we scan though the list of elements and for each element we remove all the ascii sysbols in them .
		Based on if the element is a int or string we put them in a repective list. 
		Then  sort the int and string list separately and rearrage them back in the main list.

	'''
	int_list_counter , string_list_counter = 0, 0	
	int_list, string_list = [], []
	
	for counter, item in enumerate(unsorted_list):
		item = re.sub('[^A-Za-z0-9]+', '', item)
		unsorted_list[counter] = item
		try:
			int_list.append(int(item))
		except:
			string_list.append(item)

	
	int_list = sorted(int_list)
	string_list = sorted(string_list)
	
	for i in range(0,len(unsorted_list)):
		
		try:
			int(unsorted_list[i])
			unsorted_list[i] = int_list[int_list_counter]
			int_list_counter += 1
		except:
			unsorted_list[i] = string_list[string_list_counter]
			string_list_counter += 1
	
	return unsorted_list 	



"""
	Script Starts here
	1. Check  number of arguments passed, there should to alteast 2 files.
 	2. Check if the input file excist, if not print the error and terminate the script
 	3. If the output does not excist it will the script will create one.
 	4. Call the sorting method with the file contents and them write to the output
"""

if len(sys.argv) != 3:
	print "Please use to following format , sorting.py input.txt output.txt"
	sys.exit()

try:
	read_file = open(sys.argv[1])
	file_content = read_file.read()
except:
	print "File %s not found"%sys.argv[1]
	sys.exit()

try:
	write_file = open(sys.argv[2], "w")
except:
	print "File %s not found"%write_file
	sys.exit()

if file_content is not None:
	sorted_list =  sorting(file_content.split(' '))
	for item in sorted_list:
		write_file.write(str(item) + ' ')


