'''
File: triangle.py
Author: Foster C. Williams 
Version: Python 3.8.5

Purpose: Write a program that takes input as integer and displays the reverse triangle on the basis of
that integer.

This program can either take input from the command line args or direct input from the user.

'''

import sys



def main():
	try:
		if(len(sys.argv) > 2):
			print("Too many arguments, please only put one integer argument or none");
		elif(len(sys.argv)==2):
			tri_length = int(sys.argv[1]);
		elif(len(sys.argv)==1):
			tri_length = int(input("Please input an integer: "));
		draw_triangle(tri_length);
	except:
		print("Invalid input please either use 'python3 triangle.py 5' or 'python3 triangle.py'");
		print("You can replace the 5 with any integer");
'''
Function draw_triangle( tri_length)

tri_length is an int

This function draws the reverse triangle based on the passed in integer value.


'''
def draw_triangle(tri_length):
	dashes = "";
	line = "";
	for i in range(tri_length+1, 1, -1):
		line = dashes;
		for x in range(1,i,1):
			line = line + str(x);
		print(line);
		dashes = dashes + "-";
main()