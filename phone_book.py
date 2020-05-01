# phone_book.py
#
# Craeted by Yurij Nechaev. Copyright@ 2020. Start project at 26 april 2020.

import sys
import pickle

class Phone_Book:

	def __init__(self):
		self.datafile = "phone_book.dat"
		self.Name = []
		self.country_code = []
		self.phone_number = []
		
	def command(self):
		cmd = str(input("\n Please enter command -> [c] to create record, [q] for quit: "))
		while cmd != "q":
			if cmd == 'c':
				self.input_rec(self.Name, self.country_code, self.phone_number)
			else:
				self.command()
		exit()
	
	def delete_record(self, Name, country_code, phone_number):
		pass
	
	def load_from_file(self, Name, country_code, phone_number):
		pass
	
	def input_rec(self, Name, country_code, phone_number):
		name = ""
		name = str(input("Enter name please: "))
		self.Name.append(name)
		code = ""
		code = str(input("Enter country code only digits: "))
		self.country_code.append(code)
		number = ""
		number = str(input("Enter phone number: "))
		self.phone_number.append(number)
		
		self.print_record(Name, country_code, phone_number)
		
	def print_record(self, Name, country_code, phone_number):
		ID = 0
		for item in Name:
			print("ID:#" + str(ID+1) + " Name: " + (Name[ID]) + " phone number: +" + country_code[ID] + " " + phone_number[ID])
			ID += 1
			
		self.command()
	
	def save_record(self, Name, country_code, phone_number):
		pass



def main ():
	My_book = Phone_Book()
	My_book.command()
	
main()
