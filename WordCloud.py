# Word Cloud
# Anya Fitzgerald
# Created: 10/28/19
# This program creates a word cloud from user inputted text

from graphics import  *
from random import *

def byFreq(pair):  # returns first item 1 in pair
    return pair[1]

def randPoint(num):
    numsx=[]  # generates empty list
    numsy=[]  # generates empty list
    points=[] # generates empty list
    for i in range(num):  
        x=randrange(100,600) #random number within these bounds
        y=randrange(350,700) # random number within these boundaries
        while x in numsx:  # while x is in the list
            x=randrange(100,600) # set x to a random point
        numsx.append(x) # put x to end of list
        while y in numsy: # while y is in the list
            y=randrange(350,700) # set y to random point
        numsy.append(y) # put at the end of the list
        coord=(x,y) # put x and y into coord
        points.append(coord) #put coord list at end of points
    return points # return all the points to program
    
def fileReader(freq,num,win):  # reads file and imports variables freq, num, win
    print("This program analyzes word frequency in a file")  # prints instructions
    print("and prints a report on the n most frequent words.\n") # prints instructions

    # imports stop words from text file
    stopwords=open("stopwords.txt", "r").read()
    stopList=stopwords.split()

    # get the sequence of words from the file
    fname=freq # puts "freq" into fname
    if fname=='': # if user does not input file 
        fname="AliceInWonderland.txt" # use this text
    text = open(fname,'r').read() # opens file and reads it
    text = text.lower() # makes text lower
    
    for ch in '!"#$%&’()*+,‘-./:;<=>?@[\\]^_{|}~':   # stop words
        text = text.replace(ch, ' ')
    words = text.split()
    
    # removes words from text if they are in list
    for word in list(words):
        if word in stopwords:
            words.remove(word)

    #construct a dictionary of word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1
        
    coordList=randPoint(num)
    print(coordList)
    
    # output analysis of n most frequent words.
    items = list(counts.items()) 
    items.sort()
    items.sort(key=byFreq, reverse=True)
    for i in range(num):
        word, counts = items[i]
        print("{0:<15}{1:>5}".format(word, counts))
    word=[]
    # sets random point and color for each word
    for i in range(num):
        point=Point(coordList[i][0],coordList[i][1]) # links to randpoint
        text=Text(point,items[i][0])  # genreates random point
        r=randrange(0,255)
        g=randrange(0,255)
        b=randrange(0,255)
        text.setFill(color_rgb(r,g,b))  #ssets random color
        text.setSize(randrange(5,101)) # sets random size
        text.draw(win)  # draws

    #if __name__ == '__main__': fileReader()
    
def main():
    win = GraphWin("Word Cloud", 800,800)  # creates GUI

    # gives user instructions for entering phrase
    name_message=Text(Point(300,200), "Type the text file name:")
    name_message.draw(win)

    # draws entry box
    fileInput= Entry(Point(300,225),50)
    fileInput.draw(win)
 
    # gives user instructions for entering integer
    num_words_message = Text(Point(300,300), "Please type the number of words printed out in the window: ")
    num_words_message.draw(win)

    # draws entry box
    numWordsInput= Entry(Point(300,325),50)
    numWordsInput.draw(win)

    pt=win.getMouse()
    userInput1=fileInput.getText()    # gets user input from fileInput
    userInput2=int(numWordsInput.getText()) # gets input from numWordsInput
    
    fileReader(userInput1,userInput2,win) #calls file reader
    
main()
