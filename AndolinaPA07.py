# North Seattle College
# Week 7 PA: Meteorite Data Processing
# Author: Luca Andolina
# Email: luca627@comcast.net



# This Function Displays the Options for which input the user can choose

def display_menu():


    
    print("Enter 1 to look up information on a meteorite by name.")
    print("Enter 2 to create a new csv file that contains all meteorites greater than a specified mass.")
    print("Enter 0 to exit.")



#This Function with Input Validation prompts the user to decide what the program is going to do next
    
def user_choice():

    good_input= False
    while (not good_input):
        user_input= input("what would you like to do? ")
        try:
            choice= int(user_input)
            if (choice < 0 or choice > 3):
                raise ValueError
            return choice
        except ValueError:
            print("input not an integer")
    print("What would you like to do?")

# Our main function starts here
# In our main function we call for the display menu function before the user inputs their decision

def main():

    met_dictionary = open("Meteorite_Landings.csv", "r")   #This line opens our Meteorite file and assigns it to a variable
    dictionary = {}               #Creating Our Empty Dictionary
     
    

    print("Welcome to the Meteorite Landings Database!")

    
    first_line = met_dictionary.readline().split(",")
    
    
    for line in met_dictionary:
        line = line.rstrip("\n") # Removed trailing new lines
        data_file = line.split(",") # Split line on comma to get list strings
        if data_file[1] == '': # This lets the code continue even though their might be a mass  with an empty string
            data_file[1] = '-1'
        if data_file[2] == '': # This lets the code continue even though their might be a latitude  value with an empty string
            data_file[2] = '-1'           
            if len(data_file) ==3: 
                data_file.append('')
        if data_file[3] == '': # This lets the code continue even though their might be a longitude value  with an empty string 
            data_file[3] ='-1'
        list1 =[ int(data_file[1]), float(data_file[2].strip("\"(")), float(data_file[3].strip(")\"\n"))]
        dictionary[data_file[0]] = list1 # Creating the dictionary , # Assign second item in list to dictionary with first item as key
        
    met_dictionary.close()   # Closing the program we opened 
    


# Based on if the user picks 1 or 2 it will call the function assigned to either 1 or 2

    
    choice=-1
    while (choice  != 0 ):
        display_menu()
        choice = user_choice()
        if (choice == 1 ):
            get_meteorite_info(dictionary)
            

        if (choice == 2 ):
            create_mass_file(dictionary)
            
# This function looks through the dictionary to find the name of a Meteorite           

def get_meteorite_info(met_dictionary):
    while True:
        try: 
            name =  input("Please enter the name of the meteorite you'd like to look up: ")
            info = met_dictionary[name]
            print('The meteorite named',name,'weighed',info[0],'grams and was found at latitude',info[1],'and longitude',info[2])
            return
        except KeyError:
            print('ERROR: no meteorite data found')

# This function creates a CSV file of all the Meteorites with a mass more than the mass thats entered by the user 

def create_mass_file(met_dictionary):
    while True:
        try:
            mass = float(input('Please enter a mass: '))
            break

        except ValueError:
            print('Please enter a valid mass')
    
    file = open(str(mass)+'.csv','w')
    print('File',str(mass)+'.csv','has been created')
    for key in sorted(met_dictionary.keys()):
        if met_dictionary[key][0]>mass:
            file.write(key+'\n')


    file.close()

        
# Call the Main function


main()






