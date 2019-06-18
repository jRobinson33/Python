#Python class creation
#6/18/2019

#to create a class:
#class <name of class>
import datetime

class User:
    #doc strings will show up when hovering over an instanciation of "User"
    #and give information about the class if help(<class name>) is used
    """A member of FriendFace. For now we are 
    only storing their name and birthday.
    But soon we will store an uncomfortable
    amount of user information."""

    #class initializer, initializers are like constructors in other languages
    def __init__(self, full_name, birthday):

        #self is similar to the "this" keyword in other languages
        #we have to use 'self' so that the variable names become
        #attributes of the class, and live longer than the function
        #they are created in
        self.name = full_name
        self.birthday = birthday  #yyyymmdd

        # Extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) # Date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)
    


user1 = User("Dave Bowman", "19710315")
print(user1.name)
print(user1.birthday)
print(user1.first_name)
print(user1.last_name)
print(user1.age())