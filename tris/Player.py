import math
import random

class Player:

    def __init__(self,letter):
        #letter può essere 'x' oppure 'o'
        self.letter = letter

    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):

    def __init__(self,letter):
        super().__init__(letter)
       
    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):

    def __init__(self,letter):
        super().__init__(letter)
       
    def get_move(self,game):
        valid_sqare = None
        val = None
        while not valid_sqare:
            square = input(self.letter+"'s turn. Input move (0-9)")

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_sqare = True
            except ValueError:
                print("Invalid square. Try again")
        return val



class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  
        other_player = 'O' if player == 'X' else 'X'

        # controllo se c'è vincitore 
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_square() + 1) if other_player == max_player else -1 * (
                        state.num_empty_square() + 1)}
        elif not state.empty_square():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # set a -infinito del punteggio da massimizzare
        else:
            best = {'position': None, 'score': math.inf}  # set a -infinito del punteggio da minimizzare
        for possible_move in state.available_moves():
            #prova una mossa
            state.make_move(possible_move, player)
            # simula il game
            sim_score = self.minimax(state, other_player)  
            #cancella mossa
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  
            #aggiorno dizionario
            if player == max_player: 
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

