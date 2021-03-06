# Merge-Excel-sheets
This is small script to merge 2 excel sheets based on a single common column


My algorithm to solve this problem is as follow:

1.	Go through all the elements of the file and remove all the special characters from each element in the list, also determine if the element is a string or int and store them in separate list. The time complexity for this step is O(N).
 
2.	Now that we have two separate list of integers and strings, sorted them separately using the sorted function in python. The sorted function runs in N log(N) time.

3.	Once we get the sorted list, go through the main unsorted list again and start replacing elements in them with elements from sorted integer and sorted string list. This step takes another O(N) time.

4.	Lastly just write the items into the file.


Now if you combine all the time complexities:

O(N) + N log(N) + O(N)  =  N log(N)

Because for Big O complexity, all you care about is the dominant term. N log(N) dominates n so that's the only term that you care about.

So now I can say that the algorithm runs in N log(N) time.

One other approch that could work here is the brute force one , where for each element you compare it with all other similar elements and move elements up or down by keeping in mind their position. The average time complexity for this algorithm will be O(N)square.

