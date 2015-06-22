'''
	@author : Siddarth

	The purpose of this script is to merge n number of csv files into one file based on a common shared_key column.
	An assumption that is made for this script is that all the shared_keys in each file will be unique to that file and 
	all the columns that exisit in a csv file wont exisit in any other csv file except the shared_key column.

	After exceution of the script you should find a file called "output.csv" in your current folder. This file will contain all the merged data.

	please run the script in the following format
	
	python merge_excel.py shared_key_index first_input second_input ... nth_input_file

'''

from collections import defaultdict
import csv
import sys


merged_dict = defaultdict(dict)
column_header_list = []


def merge_excel(filename, shared_key):
	'''
		This function takes filename and shared_key index as input and creates a dict like this 'shared_key':{column_values}
		column_values is represented as another dict which keeps track of which column holds which data.
		Also we assume that the first row of the file will be all column names so a seprate dict is created to hold that information to use it later one while writing the data
	'''

	with open(filename,'rU') as file:
		file_content = csv.reader(file)	
		column_header_dict = {}

		for counter , row in enumerate(file_content):
			if len(row) < shared_key:
				print "shared_key_index is not valid, it is greater than number of rows in the file"
				sys.exit()

			if counter == 0:
				for header_counter, item in enumerate(row):
					column_header_dict[header_counter]= item
					if item not in column_header_list:
						column_header_list.append(item)
				break

		for counter , row in enumerate(file_content):
			for data_counter, item in enumerate(row):
				if data_counter != shared_key:
					merged_dict[row[shared_key]][column_header_dict.get(data_counter)] = item
					
'''
	File exceution start here.

	Check if there are atleast 3 arguments passed. The script should be excited in the following format 
	
	merge_excel.py shared_key_index first_input.csv second_input.csv ... nth_input_file.csv 

'''

if len(sys.argv) < 4:
	print "This script requires atleast 3 arguments (shared_key_index, first_input.csv, second_input.csv) %s given." %(len(sys.argv) - 1) 
	sys.exit()

#check if the shared_key_index passed is int
try:
	shared_key_index = int(sys.argv[1])
except:
	print "shared_key_index should be an int not %s" %sys.argv[1]
	sys.exit()	

'''
	For each file name passed in the command line argument , check if the file exisit.
	If the file exisit , call the merge_excel function with filename and shared_key_index as an argument
'''
for args in sys.argv[2:]:
	try:
		open_file = open(args)
	except:
		print "File %s does not exist" %args
		sys.exit()
	merge_excel(args,shared_key_index)

'''

Write contents to the file names output.csv

'''
with open('output.csv', 'w') as fp:
    a = csv.writer(fp)
    data = [column_header_list]

    for item , info in merged_dict.items():
    	sample_list = [item]
    	for header in column_header_list:
    		if header != "shared_key":
    			sample_list.append(info.get(header, None))
    	
    	data.append(sample_list)

    a.writerows(data)
