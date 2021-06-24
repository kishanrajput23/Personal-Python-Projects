from prettytable import PrettyTable
my_Table=PrettyTable(["S.no","Company_name","E.Name","Experience"])
#Adding the row in table..
my_Table.add_row(["1","TCS","Suhana","2 years"])
my_Table.add_row(["2","TCS","Pragati","3 years"])
my_Table.add_row(["3","TCS","Mohit","4 years"])
my_Table.add_row(["4","TCS","Rohit","5 years"])
#deleting the row from table...
my_Table.del_row(0)
#Clear the all rows....
my_Table.clear_rows()
print(my_Table)
