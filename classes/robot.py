class Robot:

    def __init__(self, name, friend, color, height): #Chett called it magic method
        print("Building A Robot")
        self.name = name
        self.friend = friend
        self.color = color
        self._height = height # private variable or attribute
        print("Building Complete")
        #should not be returning any String => innit create something and return it for ya!

    def __repr__(self):
        return f"Robot(name = {self.name} friend={self.friend} color={self.color} height={self._height})"
    
    def walk(self):
        print('Robot is walking! Boop! Beep!')
        print(self) # self is instant

    #Reader/Getter
    @property # => to modify the height
    def height(self):
        return self._height # if call .height this is what is called
    
    #Writer/Setter
    @height.setter # to set new height
    def height(self, new_height):
        if type(new_height) == int or type(new_height) == float: 
        # if isinstance(new_height, int) or isinstance(new_height, float): # this one works too
            self._height = new_height # .height = "???" is calling this one
        else:
            raise TypeError("Height must be an integer")
        
    # @height.setter # this one is for read-only, data cannot be set again
    # def height(self, new_height):
    #         raise TypeError("You may not change this property") 

c3po = Robot("C3PO", "R2D2", "White", 6.3) # Does not have to be in order, switchble
c3po.walk()

c3po.planet_of_origin = "Tatooine"
c3po.height = 7.4

print(c3po.planet_of_origin)
print(c3po.height)

