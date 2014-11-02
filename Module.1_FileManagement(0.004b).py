"""Module.1:FileManagement(ver:0.004b)
Reads a file containing stock data in the correct format (LIST FORMAT CONVENTION HERE) and writes the data to an---
array"""
##Module.1:FileManagement(ver:0.004b) Nov 1, 2014 @ 6:19PM-date of modified version upon save
#Parent-Project: SSGG
#Oct 31, 2014 @ 5:36PM-date started
##Dev Notes: -Notes on current development and planned features
#1.It should parse(the parsing loops as seen bellow) one line at a time which will require the use of a stock class--
#   to be stored in a list.
##CODE (followed by two blank lines)


def module_1():
    #fname = input("Enter name of file to be graphed: ")                #gets file name from user
    fname = "DowTestData.txt"                                           # here for testing purposes
    #numberofdatapoints = input("Enter number of data points in file: ")
    infile = open(fname, "r")                                           # opening file and reading it
    data = infile.read()                                                # converting file to one big string
    tmplist = data.split()                                    # splitting data at every white space and populating array
    numberofdatapointstmp = 10
    datalist_1 = []
    for i in range(numberofdatapointstmp):
        datelist = []
        followsix = []
        datelist = tmplist[0:3]                                         # saves the first 3 indexes of tmplist
        for r in range(3):
            tmplist.pop(0)                                              # deletes the first 3 indexes of tmplist
        followsix = tmplist[0:6]                                        # saves the following 6 numbers
        for z in range(6):
            tmplist.pop(0)                                              # deletes the next 6 indexes of tmplist

        datestring = ' '.join(datelist)                                 # takes datelist and converts to a string
        #datalist_1.append(datestring)                                  # adds date in first index space
        tmlist = []                                                     # creates tmlist not to be confused w/ tmplist
        tmlist.append(datestring)
        datalist_1 = datalist_1 + tmlist
        #datalist_1.append(followsix)             # adds the following six indexes from tmplist
        datalist_1 = datalist_1 + followsix
    print(datalist_1)
module_1()