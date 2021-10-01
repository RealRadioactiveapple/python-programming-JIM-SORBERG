from vector import Vector
import unittest




#v1 = Vector(1,1)

#print(v1)


class TestVector(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1,2

    def create_2D_vector(self) -> "Vector":
        return Vector(self.x, self.y)

    #test starts here - all test must start whit the word test_

    #test creating vectors
    def test_create_2D_vector(self)-> None:
        v = self.create_2D_vector()
        self.assertEqual(v.numbers, (self.x, self.y))

    def test_creat_5D_vector(self):
        v = Vector(1,2,3,4,5)
        self.assertEqual(v.numbers, (1,2,3,4,5))

    def test_empty_vector(self):
        with self.assertRaises(ValueError):
            v = Vector()

    def test_creat_invalid_vector(self):
        with self.assertRaises(TypeError):
            v = Vector("1","Two")
    
    #test __eq__=

    def test_2_vector_equal(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1,2)
        self.assertEqual(v1,v2)
    
    def test_2_vectors_not_equal(self):
        v1 = self.create_2D_vector()
        v2 = Vector(-1,2)
        self.assertNotEqual(v1,v2)

    def test_2_vectors_not_equal_diff_dim(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1,2,3)
        
        with self.assertRaises(TypeError):
            v1 == v2

if __name__=="__main__":
    unittest.main()