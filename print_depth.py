	
'''
	Solution-1
	This funtion below iterates through a dict and prints out all the key with its depth.
	If a valus of the key:value pait item is also a dict is calls another function to iterate through that dict. 

	This is function first tests with the input is valid and them performs the iteration,

	If the method signature is allowed to change and a new parameter called depth is allowed to pass then all the iteration can be
	done using the same function, see function called print_depth_single_funcation below for more details
'''	

def print_depth(data):

	if not isinstance(data, dict) or data is None:
		print "Invalid input"

	elif len(data)==0:
		print "Empty Dict"
	
	else:
		depth = 1	
		for item , info in data.iteritems():
			if isinstance(info, dict):
				print "Key:%s: Depth:%s" %(item , depth)
				print_nested_depth(item, info, depth+1)		
			else:
				print "Key:%s: Depth:%s" %(item , depth)


def print_nested_depth(item, data, depth):

	for item, info in data.iteritems():
		if isinstance(info, dict):
			print "Key:%s: Depth:%s" %(item , depth)
			print_nested_depth(item, info, depth+1) 
		else:
			print "Key:%s: Depth:%s" %(item , depth)

'''
	Solution - 2
	If the funtion signature was allowed to change, we can just use this function to perform the whole iteration
'''
def print_depth_single_funcation(data, depth=1):
	if not isinstance(data, dict) or data is None:
		print "Invalid input"

	elif len(data)==0:
		print "Empty Dict"
	
	else:
		for item , info in data.iteritems():
			if isinstance(info, dict):
				print "Key:%s: Depth:%s" %(item , depth)
				print_depth_single_funcation(info, depth+1)		
			else:
				print "Key:%s: Depth:%s" %(item , depth)

test_data_1 = {
		"key1":1,
		"key2":3,
		"key3":{"key4":1,"key5":{"key7":{"key10":1,"key11":1,},},},
}

#empty input
test_data_2 = {}

#invalid in put
test_data_3 = {"key1:1"}

print_depth(test_data_1)


