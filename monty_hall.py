from random import randint
import sys

class MontyHall:

    def __init__(self, N):
        """ Initialize the state of the game
            N is the number of iterations needed to run the simulation
        """ 
        self.doors = ["Car", "Goat", "Goat"]
        self.choice_of_host = None
        self.new_choice_of_player = None
        self.num_of_wins = 0
        self.num_of_doors = len(self.doors)
        self.N = N
     
     
    def reset_game(self):
        """ Shuffle the position of the doors
        """
        for n in range(1, len(self.doors)):
            i = self.pick_a_random_number(0,2)
            j = self.pick_a_random_number(0,2)
            self.doors[i], self.doors[j] = self.doors[j], self.doors[i]
    

    def start_game(self):
        """ Start a single game    
            Player chooses a door randomly 
            Host chooses a door, which has not been chosen by the player and has not the car prize
            Player chooses to switch the door 
        """
        doors = self.doors
        
        choice_of_player = self.pick_a_random_number(0,2)
        
        i = (choice_of_player - 1) % self.num_of_doors
        j = (choice_of_player + 1) % self.num_of_doors
        
        if doors[choice_of_player] != "Car":
            self.choice_of_host = i if doors[j] == "Car" else j
        else:
            self.choice_of_host = i if self.pick_a_random_number(0,1) <= 0.5 else j
                   
        self.new_choice_of_player = j if self.choice_of_host == i else i 
         
    
    def player_wins(self):
        """ Check if player wins
        """
        return self.doors[self.new_choice_of_player] == "Car"
        
    
    def start_simulation(self):
        """ Reset and repeat the game N times 
            Track the number of wins
        """ 
         
        for i in range(N):
            
            self.reset_game()
            self.start_game()
            if self.player_wins():
                self.num_of_wins += 1
            
                
           
    def print_results(self):
        """ Print win percentage obtained by switching doors
        """
        print("The estimation of probability winning by switching doors is: ", str(self.num_of_wins / float(self.N) * 100), "%")  
    
     
    def pick_a_random_number(self, min, max):
        """ Pick a number randomly within the interval [min,max]
        """
        return randint(min,max)


        
def to_int(str):
    """ Convert string to integer    
    """
    try:
        num = int(str)
        return num
    except ValueError:
        print("The argument should be integer")
        sys.exit(0)

        
N = to_int(sys.argv[1])
m = MontyHall(N)
m.start_simulation()
m.print_results()