'''
#Python program to get the student details
#Author:Alwin Joshy
#Date:01-10-2024
Version: 1.0
'''
name=input("Enter the name:")
roll_no=int(input("Enter the roll no"))
roll_no=roll_no+1
cgpa=float(input("Enter your cgpa"))
percentage=cgpa*10
print("Name of the student:",name)
print("roll_no:",roll_no)
print("your cgpa:",percentage,"%")