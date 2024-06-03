#file handling - 
#create connection with file open("file_name",mode)
# mode - read("r"), write("w"), append("a")

# Python allows to create files, read from files, write content to file and append content to existing content through inbuilt functions!
# Method
	
# Description


# open(file_path,operation)
	
# This method is used to open the file for the specified operation. The operation can either be r,w,a for read, write and append.


# close()
	
# This method is used to close a file which is already open.


# write()
	
# This method is used to write a string to a file, if file is present. If not, it creates the file and writes the string into it.


# read()
	
# This method is used to read all the contents of a file into a string.

# The number of files that can be simultaneously opened by a program is limited. So it is very important to close all the files, once the operations are completed.
flight_file=open("flight.txt","w")
flight_file.write("Hello")
flight_file.close()

# Note: You can execute all the codes related to file handling in Eclipse Plug-in and observe the output

# try:
#     f=open('flight.txt','r')
#     data=f.read()
#     print("Data from read mode : ",data)
# except Exception as e:
#     print('Error occured!!')
# finally:
#     if f.closed:
#         print('file is closed')
#     else:
#         f.close()

# try:

#     flight_file=open("flight.txt","r")

#     text=flight_file.read()

#     print(text)

#     flight_file.write(",Good Morning")

# except:

#     print("Error occurred")

# finally:

#     print("File is being closed")

#     flight_file.close()

#     if flight_file.closed:

#         print("File is closed")

#     else:

#         print("File is open")


# When we want to write a code that will run in all situations, we can put it in a finally block.
# Since closing a file is necessary we can do it in the finally block instead of in the try block.

try:
    hello_file=open("flight.txt","w")
    text="Hello everyone! Welcome"
    hello_file.write(text)
    print(hello_file.write(text),len(text))
except:
    print("Error occurred, not able to write to file")
finally:
    hello_file.close()
    
try:
    # hello_file=open("flights.txt","r")
    hello_file=open("flight.txt","r")
    text_from_file=hello_file.read()
    print(text_from_file)
except:
    print("Error Occurred, not able to read from file") #x
finally:
    hello_file.close()
    
try:
    hello_file=open("flight.txt","w")
    text="Hello everyone! Welcome"
    hello_file.write(text)
except:
    print("Error occurred, not able to write to file")
finally:
    hello_file.close()
    
try:
    hello_file=open("flight.txt","r")
    text_from_file=hello_file.read()
    print(text_from_file)
except:
    print("Error Occurred, not able to read from file")
finally:
    hello_file.close()