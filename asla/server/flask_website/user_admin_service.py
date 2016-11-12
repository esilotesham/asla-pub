from pymongo import MongoClient


class UserAdminService:
    """
    Class that handles all tasks related to user administration
    """

    def __init__(self):
        """
        Constructor. bleh
        :return: nothing
        """
        self.mongo_client = MongoClient("mongodb://asla-website:asla@ds139277.mlab.com:39277/asla-users")
        self.database = self.mongo_client['asla-users']
        self.users = self.database['users']

    
    def make_new_user(self, form):
        """
        Makes a new user and puts him in the database
        :return:
        """                
        if self.users.find_one({"email": form['email']}) is None:
            # No such user exists, make him now
            user = {
                "name": form['name'],
                "email": form['email'],
                "pwd": form['pwd']
            }
            self.users.insert_one(user)
            return True
        else:
            # Someone already exists, deny creation
            return False
        
    
    def update_user(self):
        """
        Updates a user's data
        :return:
        """
        return None
    
    def authenticate_user(self, email, password):
        """
        Authenticates a user or login
        :return:
        """
        print "here"
        if self.users.find_one({"email": email, "pwd": password}):
            print "here 2"
            return True
        else:
            return False            
        return None
