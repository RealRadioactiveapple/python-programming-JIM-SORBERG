"""VIKTIGT!!!!!!!!! jag lekte runt med __ och nu funkar inte min cod vet inte varför tror något blev super fel."""
""" 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
class Geomatry_shapes:

    def __init__(self, x:float,y:float) -> None:
        #print(numbers)
        for number in x,y,:
            if not isinstance(number, (float,int)):
                raise TypeError(f"{number} must be a float or int not {type(number)}")
        

        self.x = x
        self.y = y
        self._x_test = []
        self._y_test = []
    @property
    def x(self):
        return self._x

    @x.setter
    def x (self, value):
        self._x = value
    @property
    def y(self):
        return self._y

    @y.setter
    def y (self, value):
        self._y = value



class Cirkel(Geomatry_shapes):

    def __init__(self, x:float, y:float, radius: float, ) -> None:
        super().__init__(x, y)
        self.radius = radius
        

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius (self, value):
        if not isinstance(value, int):
            raise TypeError("must be int")
        self._radius = value   


    def cirkel_omfong (self):
        cirlek_omkrets = plt.Circle((self.x,self.y), self.radius,facecolor = "None" ,lw = 1, edgecolor="r")
        fig, ax = plt.subplots()
        ax.spines.left.set_position('center')
        ax.spines.bottom.set_position('center')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        ax.add_patch(cirlek_omkrets)

        
        

    def cirkel_area (self):
        cirkel_are=plt.Circle((self.x,self.y), self.radius,facecolor = "g" , edgecolor="None")
        fig, ax = plt.subplots()
        ax.spines.left.set_position('center')
        ax.spines.bottom.set_position('center')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        ax.add_patch(cirkel_are)


        
    def isInside(self, x_test, y_test):
        #x_test,y_test = 1,1

        if ((x_test-self.x)*(x_test-self.x)+(y_test-self.y)*(y_test-self.y)<= self.radius*self.radius):        
            return True
        else:
            return False
   
    def translate( self, x:int, y:int):
        self.x = x
        self.y = y

    def __repr__(self) -> float:
        return f"x is {self.x}, y is {self.y}, radius is {self.radius}"



    
class Rektangel(Geomatry_shapes): 

    def __init__(self, x:float, y:float, side1: float, side2:float ) -> None:
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2
        

    @property
    def side1(self):
        return self.side1

    @side1.setter
    def side1 (self, value):
        if not isinstance(value, int):
            raise TypeError("must be int")
        self.side1 = value   

    @property
    def side2(self):
        return self.side2

    @side2.setter
    def side2 (self, value):
        if not isinstance(value, int):
            raise TypeError("must be int")
        self.side2 = value   




    def rektangel_omfong(self):
        self._x = self.x - self.side1/2
        self._y = self.y - self.side2/2

        fig, ax = plt.subplots()
        rektangel_omkrets = patches.Rectangle((self._x,self._y), self.side1,self.side2,facecolor = "None" ,lw = 5, edgecolor="r")
        
        ax.spines.left.set_position('center')
        ax.spines.bottom.set_position('center')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        ax.add_patch(rektangel_omkrets)

        
        

    def rektangel_area (self):
        self._x = self.x - self.side1/2
        self._y = self.y - self.side2/2
        fig, ax = plt.subplots()
        rektangel_are=patches.Rectangle((self._x,self._y), self.side1,self.side2,facecolor = "g" , edgecolor="None")
        
        ax.spines.left.set_position('center')
        ax.spines.bottom.set_position('center')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        ax.add_patch(rektangel_are)


        
    def isInside(self, x_test, y_test):
        #x_test,y_test = 1,1

        if (self.x - (self.side1/2)) <= x_test <= (self.x + (self.side1/2)) and (self.y - (self.side2/2)) <= y_test <= (self.y + (self.side2/2)):        
            return True
        else:
            return False
   
    def translate( self, x:int, y:int):
        self.x = x
        self.y = y

    def __repr__(self) -> float:
        return f"x is {self.x}, y is {self.y}, side1 is {self.side1} side2 is {self.side2}"
 """