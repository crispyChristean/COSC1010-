# Instructions  

A company has determined that its annual profit is typically 23 percent of total sales. Write a program that asks the user to enter the projected amount of total sales, then displays the profit that will be made from that amount. Hint: Use the value 0.23 to represent 23 percent.

Review [The Sales Prediction Problem](https://mediaplayer.pearsoncmg.com/assets/_video.true/The_Sales_Prediction_Problem) VideoNotes. You will see the output you should have for this programming challenge as well as the code.




variable - annual profit percentage (23%)

user input - projected total sales

variable2 - Annual profit * user input 

print - variable2


* First run produced an error saying "Can only concatenate str (not float) to str"
SOLVED - The first run of mine failed due to the fact that I was using the + operator in a print function, which can only used when working with another string type variable. NOT with a string and a float. 

* TO print a variable in a print function, I have to pass the argument by using a comma, which when I did use produced my desired results.