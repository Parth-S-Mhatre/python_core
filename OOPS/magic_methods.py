class Movie:
    def __init__(self,name,box_office):
        self.name=name
        self.box_office=box_office
    
    def __str__(self):
        return f"{self.name} of Box-Collection ${self.box_office} billon"

    def __add__(self,other):
        return self.box_office+other.box_office 
    def __eq__(self, value):
        return self.name==value.name
   
    

movie1=Movie("Avengers infinite-war",1.3)
movie2=Movie("Avernger End-game",2.1)
print(movie1)
print(f"total Collection of both movies is ${movie1+movie2} Billon")