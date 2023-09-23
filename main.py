#Scott Ryvves
#Outcome 2
#24/4/2022
#Course notes files <---- Jimi
import os

#Checking Filename to the directory then reading the txt file
def FileName():
  UserName = input ("What is the first name of the Student? ")
  for x in (UserName): #This is gonna loop for each character
    open(f"{UserName}.txt", "r")
    if True:
      return (UserName)
    else:
      print ("User Not Found..")
      NewStudent = NameList()
      return (NewStudent)

def NameList():
  UserName = input ("Would you like to add a Student? Yes or No")
  if UserName.upper() == ("yes"):
    Student = input ("What is their first name? ")
    open.file(f"{Student}.txt" "w")
    while True:
      Marks = input ("Enter their marks accordingly.. and press N to save. ")
      if Marks.upper() == ("N"):
        return (Student)
      

#Main Program
def main(): 
  Students = os.listdir()#"Outcome2/Students"
  for files in Students:
    Student = FileName()
    print (f"{Student}")
  
  NewStudent = NameList()
  print (f"{NewStudent}")
  return

  

if __name__ == "__main__":
  main()



