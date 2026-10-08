#================================================================================================#
#                         PART-2: Opening and Closing Files
#================================================================================================#
#
# 5. open() Function
#    ├── File Name
#    ├── File Mode
#    └── File Path
#
# 6. File Modes
#    ├── "r"  → Read
#    ├── "w"  → Write
#    ├── "a"  → Append
#    ├── "x"  → Create
#    ├── "t"  → Text Mode
#    └── "b"  → Binary Mode
#
# 7. close() Function
#
#================================================================================================#




#================================================================================================#
# Structure-1: open() Function
#------------------------------------------------------------------------------------------------#
#
# open()
#
# Statement:
# The open() function is used to open a file so that
# Python can read from or write to the file.
#
# Structure:
#
# file_variable = open("filename", "mode")
#
# filename      → Name or path of the file
# mode          → Specifies how the file will be opened
# file_variable → Stores the file object
#
#================================================================================================#

#Example-1:
file = open("student.txt", "r")

file.close()