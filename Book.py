'''
File: Book.py
Author: Foster C. Williams 
Version: Python 3.8.5

Purpose: Create an abstract class called Book. Include a String field for the books title and a double
field for the books price. Within the class, include a constructor that requires the book title
and two get methods: one that returns the title and one that returns the price. Also include an
abstract method named setPrice(). Create two child classes of
Book: Fiction and NonFiction. Create a list containing multiple instances of each type of
book and store all the books in a single array.
Create an application (terminal or GUI) that allows the following functions to be performed
interactively:
1. List all books in the list
2. List all fiction titles
3. List all non-fiction titles
4. Allow multiple books to be selected from the list and present the user with a total cost


'''

from abc import ABC, abstractmethod;

'''
Abstract Class Book extends ABC

Constructors:
Book(title) - title is a string, sets self.title to passed string.

Class Variables:
price - float representing the price of the book
title - string representing the title of the book

Methods:
get_title - returns title of book
ge_price - returns price of book

Abstract Methods:
setPrice(float) 

'''
class Book(ABC):
	price = 0.0;
	title = "";
	def __init__(self,title):
		self.title = title;
	def get_title(self):
		return  self.title;
	def get_price(self):
		return self.price;
	@abstractmethod
	def setPrice(price):
		pass
'''
Class Fiction extends Book

Methods:
setPrice(float) - sets self.price to passed float

'''
class Fiction(Book):

	def __init__(self,title):
		self.title = title;
	
	def setPrice(self, price):
		self.price = price;
'''
Class NonFiction extends Book

Methods:
setPrice(float) - sets self.price to passed float

'''
class NonFiction(Book):
	def __init__(self,title):
		self.title = title;
	
	def setPrice(self, price):
		self.price = price;
'''
Method create_book_array

Parameters:
file_name - string, represents the name of the file that holds information on books.

Purpose:
reads a text file and constructs a Book list full of fiction and nonfiction books from the text file
'''
def create_book_array(file_name):
	book_file = open(file_name, 'r');
	lines = book_file.readlines();
	books = [];
	for line in lines:
		currLine = line.split(";");

		if(currLine[1] == "fiction"):
			book = Fiction(currLine[0]);
			book.setPrice(float(currLine[2]));
			books.append(book);
		elif(currLine[1] == "nonfiction"):
			book = NonFiction(currLine[0]);
			book.setPrice(float(currLine[2]));
			books.append(book);
	return books;
'''
Method book_details

Parameters:
book - a book object, either fiction or nonfiction

Returns:
String

Purpose:
Properly formats a books title and price and returns string representing it.

'''
def book_details(book):
	return book.get_title() + " " + "${:,.2f}".format(book.get_price());

'''
Method print_fiction

Parameters:
books - a list containing numerous fiction and nonfiction objects

Purpose:
prints all books that are of type fiction
'''
def print_fiction(books):
	print("");
	for book in books:
		if("NonFiction" in str(type(book))):
			pass
		else:
			print(book_details(book));
	print("");
'''
Method print_fiction

Parameters:
books - a list containing numerous fiction and nonfiction objects

Purpose:
prints all books that are of type nonfiction
'''
def print_nonfiction(books):
	print("");
	for book in books:
		if("NonFiction" in str(type(book))):
			print(book_details(book));
		else:
			pass;
	print("");

'''
Method print_all

Parameters:
books - a list containing numerous fiction and nonfiction objects

Purpose:
prints all books in list
'''
def print_all(books):
	print("");
	for book in books:
		print(book_details(book));
	print("");

'''
Method price_check

Parameters:
books - a list containing numerous fiction and nonfiction objects
choices - a string array containing user input

Purpose:
prints the combined price of all the choices the user has selected.

Note:
the check and counter variables are used to determine if the amount of choices represents 
the amount of books found.
'''
def price_check(books, choices):
	print("");
	price = 0.0;
	check = len(choices);
	counter = 0;
	for choice in choices:	
		for book in books:
			if(choice.lower() == book.get_title().lower()):
				price = price + book.get_price();
				counter = counter + 1;
	if(counter!=check):
		print("One or more of the titles you entered are not available, make sure everything is spelled correctly");
		print("");
		return;
	print("")
	print("Your selections are: ")
	for choice in choices:
		print(choice)
	print("");
	print("total price is " + "${:,.2f}".format(price));
	print("");
'''
Method commands

Purpose:
prints out the list of commands the user can input.
'''	
def commands():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("COMMANDS:");
	print("No commands are case sensitive");
	print("'all' -> prints all available books.");
	print("'fiction' -> prints all available fiction books.");
	print("'non-fiction' -> prints all available non-fiction books");
	print("'exit' -> exits this program");
	print("'help' -> lists these commands again");
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

'''
Method main

Purpose:
Main function, cycles through a loop allowing the user to continually access the book lists
and recieve price checks on selecting multiple books.
'''
def main():
	books = create_book_array('booklist.txt');
	print("");
	print("#################################");
	print("### Welcome to the Bookstore! ###");
	print("#################################");
	loop_input = "";
	commands();
	while (loop_input.lower() != "exit"):
		print("Enter the names of the books you want to purchase seperated by a comma, and I'll tell you the total price");
		print("You can also type 'help' to get the list of commands");
		loop_input = input("");
		if(loop_input.lower() == "exit"):
			break;
		elif(loop_input.lower() == "non-fiction"):
			print_nonfiction(books);
		elif(loop_input.lower() == "fiction"):
			print_fiction(books);
		elif(loop_input.lower() == "all"):
			print_all(books);
		elif(loop_input.lower() == "help"):
			commands();
		else:
			choices = loop_input.split(",");
			price_check(books,choices)


main();

