"""VIKTIGT!!!!!!!!! jag lekte runt med __ och nu funkar inte min cod vet inte varför tror något blev super fel."""



import matplotlib.pyplot as plt
import matplotlib.patches as patches
class Geomatry_shapes:

    def __init__(self, x:float,y:float) -> None:
        
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
    """Definerar cirkel klassen"""
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
        """plotar ut cirkel omlkrets"""
        cirlek_omkrets = plt.Circle((self.x,self.y), self.radius,facecolor = "None" ,lw = 1, edgecolor="r")
        fig, ax = plt.subplots()

        """Ritar ut hur bakrunden ska vara i graphen"""
        ax.spines.left.set_position('center')
        ax.spines.bottom.set_position('center')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        ax.add_patch(cirlek_omkrets)

        
        

    def cirkel_area (self):
        """plotar ut cirkel area"""
        cirkel_are=plt.Circle((self.x,self.y), self.radius,facecolor = "g" , edgecolor="None")
        fig, ax = plt.subplots()
        """Ritar ut hur bakrunden ska vara i graphen"""
        ax.spines.left.set_position('center')
        ax.spines.bottom.set_position('center')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        ax.add_patch(cirkel_are)


        
    def isInside(self, x_test, y_test):
        #x_test,y_test = 1,1
        """räknar ut om en punt är i cirkeln"""

        if ((x_test-self.x)*(x_test-self.x)+(y_test-self.y)*(y_test-self.y)<= self.radius*self.radius):        
            return True
        else:
            return False
   
    def translate( self, x:int, y:int):
        """flyttar på xy mitt punkten"""
        self.x = x
        self.y = y

    def __repr__(self) -> float:
        return f"x is {self.x}, y is {self.y}, radius is {self.radius}"

"""MIN KERNEL DOG VET INTE VARFÖR HAN INTE KLART MED """

"""
def iscirkel(self, ) 
        if not isinstance()
        return self.radius  ==   
"""
    
class Rektangel(Geomatry_shapes): 

    def __init__(self, x:float, y:float, side1: float, side2:float ) -> None:
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2
        

    @property
    def side1(self):
        return self._side1

    @side1.setter
    def side1 (self, value):
        if not isinstance(value, int):
            raise TypeError("must be int")
        self._side1 = value   

    @property
    def side2(self):
        return self._side2

    @side2.setter
    def side2 (self, value):
        if not isinstance(value, int):
            raise TypeError("must be int")
        self._side2 = value   




    def rektangel_omfong(self):
        """Räknar ut och rittar upp rektangels på omkretsen och mittpunkt """
        self._x = self.x - self.side1/2#räknar ut mitt punketn av rektangeln
        self._y = self.y - self.side2/2#räknar ut mitt punketn av rektangeln

        fig, ax = plt.subplots()
        rektangel_omkrets = patches.Rectangle((self._x,self._y), self.side1,self.side2,facecolor = "None" ,lw = 5, edgecolor="r")
        """Ritar ut hur bakrunden ska vara i graphen"""
        ax.spines.left.set_position('center')
        ax.spines.bottom.set_position('center')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        ax.add_patch(rektangel_omkrets)

        
        

    def rektangel_area (self):
        """Räknar ut och rittar upp rektangels på area och mittpunkt """
        self._x = self.x - self.side1/2 #räknar ut mitt punketn av rektangeln
        self._y = self.y - self.side2/2 #räknar ut mitt punketn av rektangeln
        fig, ax = plt.subplots()
        rektangel_are=patches.Rectangle((self._x,self._y), self.side1,self.side2,facecolor = "g" , edgecolor="None")
        """Ritar ut hur bakrunden ska vara i graphen"""
        ax.spines.left.set_position('center') 
        ax.spines.bottom.set_position('center')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        ax.add_patch(rektangel_are)


        
    def isInside(self, x_test, y_test):
        #x_test,y_test = 1,1
        """räknar ut om det finns en punkt i rektangeln"""
        if (self.x - (self.side1/2)) <= x_test <= (self.x + (self.side1/2)) and (self.y - (self.side2/2)) <= y_test <= (self.y + (self.side2/2)):        
            return True
        else:
            return False
   
    def translate( self, x:int, y:int):
        """flyttar på mittpunkten"""
        self.x = x
        self.y = y

    def __repr__(self) -> float:
        return f"x is {self.x}, y is {self.y}, side1 is {self.side1} side2 is {self.side2}"

    """MIN KERNEL DOG VET INTE VARFÖR HAN INTE KLART MED """
    """ def isrektangel(self, ) 
        if not isinstance()
        return self.side1 and self.side2 ==    """ 



"""Gjorde allt i en sitning det är derför det inte finns många upladningar mot githuib. 
jag har inte löst mitt kernel problem och jag vet inte om det kvarsår om jag laddar det 
till git hub men förhoppnings vis fungerar det. jag har tagit bort alla __ som jag la till men jag kan inte få det att funka"""