class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        b="aceg"
        w="bdfh"
        if coordinates[0] in b:
            return coordinates[0] in b and int(coordinates[1])%2==0 
        if coordinates[0] in w:
            return coordinates[0] in w and int(coordinates[1])%2!=0 
            
        
        