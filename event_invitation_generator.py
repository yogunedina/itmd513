'''
Author: Yewande Ogunedina
Course: ITMD513
This program demonstrates generating personalized invitations for an event using the provided guest list and event details
'''
import os

def main():
    guest = input("Enter guest name: ")
    #open event detail file
    if guest == "Peter Parker":
        inputfile = open("/Users/WendyAdedoyin/Documents/event_details.txt", "r")

        #write guest name in new file . create file if it does not exist. 
        outfile = open("/Users/WendyAdedoyin/Documents/Invitations/Peter_Parker.txt", "w")
        outfile.write(guest + "\n")
        for line in inputfile:
            outfile.write(line)
            
        #print new file 
        outfile = open("/Users/WendyAdedoyin/Documents/Invitations/Peter_Parker.txt", "r")
        guest_1 = outfile.read()
        print(guest_1)
        inputfile.close()
        outfile.close()

    elif guest == "Clark Kent":
        #open event detail file
        inputfile = open("/Users/WendyAdedoyin/Documents/event_details.txt", "r")

        #write guest name in new file . create file if it does not exist. 
        outfile = open("/Users/WendyAdedoyin/Documents/Invitations/Clark_Kent.txt", "w")
        outfile.write(guest + "\n")
        for line in inputfile:
            outfile.write(line)

        #print newly created file
        outfile = open("/Users/WendyAdedoyin/Documents/Invitations/Clark_Kent.txt", "r")
        guest_2 = outfile.read()
        print(guest_2)
        inputfile.close()
        outfile.close()

    elif guest == "Tony Stark":
        inputfile = open("/Users/WendyAdedoyin/Documents/event_details.txt", "r")

        #create new file for Tony Stark
        outfile = open("/Users/WendyAdedoyin/Documents/Invitations/Tony_Stark.txt", "w")
        outfile.write(guest + "\n")
        for line in inputfile:
            outfile.write(line)

        outfile = open("/Users/WendyAdedoyin/Documents/Invitations/Tony_Stark.txt", "r")
        guest_3 = outfile.read()
        print(guest_3)
        inputfile.close()
        outfile.close()

    elif guest == "Bruce Wayne":
        inputfile = open("/Users/WendyAdedoyin/Documents/event_details.txt", "r")

        #create new file for Bruce Wayne
        outfile = open("/Users/WendyAdedoyin/Documents/Invitations/Bruce_Wayne.txt", "w")
        outfile.write(guest + "\n")
        for line in inputfile:
            outfile.write(line)

        outfile = open("/Users/WendyAdedoyin/Documents/Invitations/Bruce_Wayne.txt", "r")
        guest_4 = outfile.read()
        print(guest_4)
        inputfile.close()
        outfile.close()

    elif guest == "Dr. Bruce Banner":
        inputfile = open("/Users/WendyAdedoyin/Documents/event_details.txt", "r")

        #write guest name in new file . create file if it does not exist. 
        outfile = open("/Users/WendyAdedoyin/Documents/Invitations/Bruce_Banner.txt", "w")
        outfile.write(guest + "\n")
        for line in inputfile:
            outfile.write(line)

        outfile = open("/Users/WendyAdedoyin/Documents/Invitations/Bruce_Banner.txt", "r")
        guest_5 = outfile.read()
        print(guest_5)
        inputfile.close()
        outfile.close()

    elif guest == "Diana Prince":
        inputfile = open("/Users/WendyAdedoyin/Documents/event_details.txt", "r")

        #write guest name in new file . create file if it does not exist. 
        outfile = open("/Users/WendyAdedoyin/Documents/Invitations/Diana_Prince.txt", "w")
        outfile.write(guest + "\n")
        for line in inputfile:
            outfile.write(line)

        outfile = open("/Users/WendyAdedoyin/Documents/Invitations/Diana_Prince.txt", "r")
        guest_6 = outfile.read()
        print(guest_6)
        inputfile.close()
        outfile.close()
        #if input is different from all 6 guest, return invalid
    else:
        print("Guest does not exist. Please re-enter")
        
#restart program after guest invitation is printed
restart = 'y'
while (restart == 'y'):
    main()
    restart = input("Do you want to print another invitation? y/n: ")
