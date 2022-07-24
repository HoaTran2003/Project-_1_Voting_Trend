# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 23:02:20 2022

@author: Hoa Tran
Project 1: Polarize Politics
"""


import urllib.request as web
import matplotlib.pyplot as pyplot
import time



# Part 1:
def partyLine(year,number):
    time.sleep(0.01)
    url = "https://clerk.house.gov/cgi-bin/vote.asp?year=" + str(year) +"&rollnumber="+ str(number) # initilize the website to find the year and roll number
    webpage=web.urlopen(url) # open the url and named it webpage
    yes_R=0 # number of republicans who voted yes
    no_R=0 #number of repulicans who voted no
    yes_D=0 # number of democratics who voted yes
    no_D=0 #number of democratics who voted no
    web_list=[] # list to append each line of the XML file
    web_line=0 # count of line 
    for line in webpage: # for loop used to count the lines of the webpage
        line = line.decode('utf-8') 
        web_line=web_line+1
        web_list.append(line)
        
    
    for word in range(56, web_line): # for loop counting from line 57 till the ending line the XML file
            
            
           
                if 'party="D"' in web_list[word] and ("legislator><vote>Yea<" in web_list[word] and "legislator><vote>Aye<" in web_list[word]):# if statement used to find the number of Democrats who said voted Yes (Yay or Nay) 
                    yes_D=yes_D+1
                if 'party="D"' in web_list[word]   and ("legislator><vote>Nay<" in web_list[word] or "legislator><vote>No<" in web_list [word]): #if statement used to find the number of Democrats who said voted No(Aye or No)
                    no_D=no_D+1
        
            
                if 'party="R"' in web_list[word] and ("legislator><vote>Yea<" in web_list[word] or "legislator><vote>Aye<" in web_list[word]): # if statement used to find the number of Republicans who said voted Yes (Yay or Nay)
                    yes_R=yes_R+1
                if 'party="R"' in web_list[word] and ("legislator><vote>Nay<" in web_list[word] or "legislator><vote>No<" in web_list [word]):#if statement used to find the number of Republicans who said voted No (Aye or No)
                    no_R=no_R+1
                
    if (yes_R >= 0.5*(yes_R+no_R) and no_D >= 0.5*(no_D+yes_D)) or (no_R >= 0.5*(yes_R+no_R) and yes_D >= 0.5*(no_D+yes_D)): #if the condition for party line vote is True
        print("Party Line Vote")
        return True
   
    else:
        print("Not Party Line Vote")
        return False
    webpage.close()
    
''' 
Parameters: 
    year: The year of the election 
    number: Roll call number 
This function is used to investigate whether a specfic roll call number 
in a given election year has party line votes or not. 

Return value: 
    True (Party Line Vote)
    or False (Not party line vote)
'''

        
 #Part 2       
def countPartyLine(year, maxNumber):

    '''
 Parameters
 ----------
 year : Integer
     Year of election
 maxNumber : integer
     Total number of roll call last year

 This function is used to calculate the fraction of party line votes. 
Returns
 -------
 Fraction of party line votes


'''

   
    
    total_partyline=0 # initialize to count the number of party line vote
    for num in range(1,maxNumber+1,1): # for loop counting from the firsr roll call number to the last 
        results=partyLine(year,num) #calling the results of the function partyLine
        if results == True: #if the results return a party line vote 
            total_partyline=total_partyline+1 # 
    return total_partyline/maxNumber # return the fraction of party line votes





#Part 3:

def plotPartyLine():
    '''
    No parameters
    This function is used to plot the fraction of party line votes over the 
    span 20 years using the results of the previous function. 
    Return value:
        None
    '''
    
    
    list_year=[] # a list for the years
    fraction_vote_list=[] # a list for the fraction of party line vote
    for year in range(1999,2020): # for loops counting for each year in the 20 years
        
        list_year.append(year)
        fraction=countPartyLine(year,450)
        fraction_vote_list.append(fraction)
    pyplot.plot(list_year, fraction_vote_list) # Plot the fraction of party line votes over time
    pyplot.xlabel("Year")
    pyplot.ylabel("Fraction of party line vote")
    pyplot.show()


def main():
    '''
    Parameters: None
    This function is used to initalize input for years and number of roll call 
    votes and call the three functions above with their required parameters. 
    Return value: None 
    '''
    year=int(input('Enter the year:')) #input for the year
    number=int(input("Enter the vote number:")) # input for the roll call number
    maxNumber=int(input("Enter the last number of roll call vote of the year: "))
    print(partyLine(year, number))
    print(countPartyLine(year, maxNumber))
    plotPartyLine()
    
main()




