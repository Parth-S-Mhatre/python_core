class Degree:
    def getDegree(self):
        print("I got a degree.")

class Undergraduate(Degree):
    def getDegree(self):
        print("I am an Undergraduate.")

class Postgraduate(Degree):
    def getDegree(self):
        print("I am a Postgraduate.")

# Example usage
if __name__ == "__main__":
    # Create objects of each class
    degree = Degree()
    undergraduate = Undergraduate()
    postgraduate = Postgraduate()

    # Call the getDegree method for each object
    degree.getDegree()         # Output: I got a degree.
    undergraduate.getDegree()  # Output: I am an Undergraduate.
    postgraduate.getDegree()   # Output: I am a Postgraduate.