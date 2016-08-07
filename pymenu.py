# ------------------------------------
# Console based menu application for python
#
# Authors: gruiz, et.at. <put your names here if credit wanted or needed..>
# Aug 12th 2016
# -------------------------------------

import sys


class Menu:
    """
        Display a menu and respond to choices when run.

        Usage:
            a. Modify the constructor __init__ to add the new choices you have in your menu
            b. Add a new method to the class to perform the required action when the menu is selected.

    """

    def __init__(self):
        ''' Default constructor '''
        self.choices = {
            "1": self.upload_file,
            "2": self.download_file,
            "a": self.authenticate,
            "q": self.quit,
            "Q": self.quit
            }


    def display_menu(self):
        ''' Display the menu options '''
        print("""
            Notebook Menu
            1. Upload file
            2. Download file
            a. Authenticate
            q. Quit
            """)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))


    def upload_file(self):
        ''' 
            Menu option to upload a file. 
            Modify as needed. Replace the menu option by changing the 
            description in the display_menu() method and editing the constructor
            to assign the proper method to the call.
        '''
        print('upload file...')


    def download_file(self):
        print('download file...')
        filter = input("Search for: ")


    def authenticate(self):
        '''Authenticate OneDrive '''
        pass


    def quit(self):
        print("Thank you for using your OneDriver today.")
        sys.exit(0)


if __name__ == "__main__":
        Menu().run()