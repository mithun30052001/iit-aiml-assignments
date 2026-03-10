import pandas as pd

#Create a pandas DataFrame using the student data
students_data = '''StudentID,Name,Age,Marks,Grade
101,Alice,20,88,A
102,Bob,21,75,B
103,Charlie,19,92,A
104,Diana,22,65,C
105,Ethan,20,78,B
106,Fiona,21,85,A
107,George,23,70,B
108,Hannah,19,95,A
109,Ivan,22,60,C
110,Julia,20,80,B
'''

#Save the DataFrame as a CSV file named students.csv
with open("students.csv", "w") as f:
    f.write(students_data)

#Reload students.csv into a new DataFrame
students_df = pd.read_csv("students.csv")
print(f"loaded csv as a dataframe{students_df}")

#Display the first 3 rows 
print(f"First three rows of dataframe: {students_df.head(3)}")

# statistical summary
print(f"Statistical summary of dataframe: {students_df.describe()}")

#more methods
print(f"Shape of dataframe: {students_df.shape}")
print(f"Datatype of dataframe: {students_df.dtypes}")
print(f"Info about dataframe: {students_df.info()}")
print(f"Last 2 rows of dataframe: {students_df.tail()}")
print(f"Only student's name and score: {students_df[["Name","Marks"]]}")