import pandas as pd
import streamlit as st
League = (input("Enter the League Name: "))
df = pd.read_excel(r'C:\Users\anshu\OneDrive\Desktop\Python_projects\Football Quiz.xlsx', League)
Q = input("The number of Questions is:")
R = int(Q)
Row = 0
Mark = 0
while Row in range(R):
    Question = df.iloc[Row,0]
    Answer = df.iloc[Row,1]
    print(Question)
    A = str(input("The answer is:")).title()
    if A == Answer:
        Mark = Mark + 1
    else:
        print("The answer is incorrect.")
    Row = Row + 1
print("The obtained mark is " + str(Mark) + ".")



