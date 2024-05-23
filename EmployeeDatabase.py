import json

def companyRegistry(key, value):

        employee_info = {   "John Appletree": 
                                {"salary":150000, 
                                "job title":"Chief Information Officer", 
                                "home address":"123 Road Avenue", 
                                "contact information": "Cell: (123)456-7890, E-mail: 123-dis-my-email@gmail.com"}
                        ,"Cesar Munguia": 
                                {"salary":300000, 
                                "job title":"Cybersecurity specialist", 
                                "home address":"123 Road Avenue", 
                                "contact information": "Cell: (123)456-7890, E-mail: 123-dis-my-email@gmail.com"}                                                    
                        ,"Ian Burres": 
                                {"salary":"one million", 
                                "job title":"Best professor at UTSA", 
                                "home address":"123 Road Avenue", 
                                "contact information": "Cell: (123)456-7890, E-mail: 123-dis-my-email@gmail.com"}                                                        
                        ,"Lionel Messi": 
                                {"salary":250000, 
                                "job title":"BEST PLAYER IN THE HISTORY OF FUTEBOL", 
                                "home address":"123 Road Avenue", 
                                "contact information": "Cell: (123)456-7890, E-mail: 123-dis-my-email@gmail.com"}
                        ,"Cristiano Ronaldo": 
                                {"salary":249000, 
                                "job title":"Second best player in history", 
                                "home address":"123 Road Avenue", 
                                "contact information": "Cell: (123)456-7890, E-mail: 123-dis-my-email@gmail.com"}}


        if key in employee_info:
                print(value, ":", sep='')
                print(employee_info[key][value])
        else:
                print("Employee was not found")
        
        with open('employee_database1.xlsx', 'w') as json_file:
                json.dump(employee_info, json_file)

        
