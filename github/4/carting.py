class Carting:
    def __init__(self):
        self.players = []
        self.health = []
        self.scores = [0, 0]
        self.damages = []

    
    def play_round(self, player_cards):
        selected_damage = [self.damages["ABC".index(card)] for card in player_cards]
        self.health[1] -= selected_damage[0]
        self.health[0] -= selected_damage[1]
        if selected_damage[0] > selected_damage[1]:
            self.scores[0] += 1   
        elif selected_damage[1] > selected_damage[0]:
            self.scores[1] += 1  
        else:
            pass

    def start_game(self):
        try:
            self.players = input().split()
            if len(self.players) != 2:
                raise SyntaxError
        
            self.health = list(map(int, input().split()))

            self.damages = list(map(int, input().split()))
        
            for i in range(3):
                cards = input().split()
                self.play_round(cards)
                
        except SyntaxError:
            print("Invalid Command.")
            return
        
        except ValueError:
            print("Invalid Command.")
            return
        
        self.display_results()
        #self.write_results()

    def display_results(self):
        for idx, player in enumerate(self.players):
            print(f"{player} -> Score: {self.scores[idx]}, Health: {self.health[idx]}")

    def write_results(self):
        try:
            file = open('result.txt', 'a')
            for idx, player in enumerate(self.players):
                line = f"{player} -> Score: {self.scores[idx]}, Health: {self.health[idx]}"
                file.write(line + "\n")
        except FileNotFoundError:
            print("Something went wrong when writing to the file")
        finally:
            file.close() 


game = Carting()
game.start_game()
