from matplotlib import scale
import matplotlib.pyplot as plt

class PlotVectors:
    """Plotting several vectors in cartesian coordinate system"""

    def __init__(self, *vectors) -> None:
        x,y =[],[]

        for vector in vectors:
            x.append(vector[0])
            y.append(vector[1])

            self.x, self.y = x, y
            self.originx = self.originy = tuple(0 for _ in range(len(x)))
    

    def plot (self) -> None:
        """visualize vectors"""

        plt.quiver(self.originx, self.originy, self.x, self.y, scale = 1 , scale_units ="xy", angles="xy")
        
        plt.xlim(-2,10)
        plt.ylim(-2,10)
        plt.ylabel("y")
        plt.xlabel("x")
        title= "".join(f"{x,y}"for x,y in zip (self.x, self.y))
        plt.title(f"Vectors: {title}")
        plt.grid()
        
        plt.show()