 # Object is a contruct for storing data and functions

#class instaProfile():
    #self.username = username
     #   self.email = email
      #  self.profileImg = profileImg
       # self.pw = "password123"

#    def resetPw():
 #       print("Password reset link has been sent to your email")

  #  def uploadImg():
   #     print("Image has been uplaoded to your profile")

    #def viewFollowers():
     #   print("Here is a list of your new followers")


# print("Welcome to Instagram")

class Car():
    def __init__ (self, name, model, year, color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.odometer_reading = 0

class Phone():
    def printDetails(self):
        print('Here are the datails of your car:')
        print('name: '+ self.name)
        print('modelo: '+ str(self.model))
        print('year: '+ str(self.year))

class phone:
     def __init__(self,name):
             self.name = name
             self.battery = 61
          
             phone1 = phone ("iPhone")
attempts = 3
