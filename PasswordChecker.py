"""
Riley Deane
10/15/2023
SDEV 140
------------------------------------------------------------------------------------------------------
Password Checker -

Uses tkinter, breezypythonGUI, and a proprietary Library file in order to make the whole thing work. Takes a user's input being a password, and updates the score for each requirement
their password meets. The score is then passed into the Switch case and determines the strength of the user's password. In the Library.py file, there is a seperate statement that
dissallows the user from making their password "PASSWORD" "password" "1234" or anything that contains an empty character " "
"""


from breezypythongui import EasyFrame
from tkinter import PhotoImage
from Library import ContainsCharacters


# Initializes the GUI and sets the positions for each of the labels and buttons
class PasswordChecker(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Password Checker", width=300, height=250, background="gray", resizable=False)
        self.addLabel(text="Enter your password:", row=1, column=0)
        self.passwordField = self.addTextField(text="", row=1, column=1)
        self.resultField = self.addTextField(text="", row=2, column=0, columnspan=2, width=30, state="readonly")
        self.checkButton = self.addButton(text="Check Password", row=3, column=0, columnspan=2, command=self.checkPassword)

        # Creates the image and sets its position
        self.nameImage = PhotoImage(file="Lock.gif")
        self.nameLabel = self.addLabel(text="Lock", row=0, column=0)
        self.nameLabel["image"]=self.nameImage

    # gets the password from the init and passes it into the switch case
    def checkPassword(self):
        password = self.passwordField.getText() # Gets the password from the Library.py 
        score = ContainsCharacters(password) # Creates a score variable for this class, another is created in the Library.py, but is not the same

        # Creates a "Switch case" to check the strength of the user's password
        if score == 1:
            self.resultField.setText("Password Strength: Very Weak")
        elif score == 2:
            self.resultField.setText("Password Strength: Weak")
        elif score == 3:
            self.resultField.setText("Password Strength: Medium")
        elif score == 4:
            self.resultField.setText("Password Strength: Strong")
        elif score == 5:
            self.resultField.setText("Password Strength: Very Strong")
        else:
            self.resultField.setText("Invalid Password")
# Runs the GUI
if __name__ == "__main__":
    PasswordChecker().mainloop()