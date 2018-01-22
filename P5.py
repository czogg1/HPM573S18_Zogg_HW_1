
#Problem 5: Dictionaries (Weight 2). Create a dictionary for the months of the year that can be called by
#the number of months (i.e. 1, 2, ..., 12) or the name of months (i.e. January, February, ..., December).
#Write a statement that prints ‘The sixth month is June.’ and another statement that prints
#‘February is month 2.’

year = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September',
        10:'October', 11:'November', 12:'December', 'December':'12', 'November':'11', 'October':'10', 'September':'9',
        'August':'8', 'July':'7', 'June':'6', 'May':'5', 'April':'4', 'March':'3', 'February':'2', 'January':'1'}

print("The sixth month is "+year[6]+".")
print(year[2]+" is month "+year['February']+".")
