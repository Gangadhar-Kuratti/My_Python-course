class user:
    def __init__(self,username):
        self.surname=username
    
    def login(self):
        print(f"{self.username} logged in successfully")

class admin(user):
    def delete(self):
        print("Admin deleted")

a=admin("nikhil")
a.delete()

    