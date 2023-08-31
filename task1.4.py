
import random

class ChessPlayer:
    def __init__(self, name, age, elo, tenacity, is_boring):
        self.name = name
        self.age = age
        self.elo = elo
        self.tenacity = tenacity
        self.is_boring = is_boring
        self.tournament_score = 0

    def simulate_match(self, opponent):
        elo_difference = abs(self.elo - opponent.elo)
        tenacity_factor = random.randint(1, 10) * self.tenacity

        if elo_difference > 100:
            if self.elo > opponent.elo:
                self.tournament_score += 1
            else:
                opponent.tournament_score += 1
        elif 50 <= elo_difference <= 100:
            if self.elo <= opponent.elo + tenacity_factor:
                self.tournament_score += 1
            else:
                opponent.tournament_score += 1
        else:
            if self.tenacity > opponent.tenacity:
                self.tournament_score += 1
            elif self.tenacity < opponent.tenacity:
                opponent.tournament_score += 1
            elif self.is_boring or opponent.is_boring:
                # If either player is boring and ELO difference is <= 100, it's a draw
                pass
            else:
                # Randomly decide the outcome in case of equal tenacity
                if random.choice([True, False]):
                    self.tournament_score += 1
                else:
                    opponent.tournament_score += 1

# Create ChessPlayer instances for each player
players = [
    ChessPlayer("Courage the Cowardly Dog", 25, 1000.39, 1000, False),
    ChessPlayer("Princess Peach", 23, 945.65, 50, True),
    ChessPlayer("Walter White", 50, 1650.73, 750, False),
    ChessPlayer("Rory Gilmore", 16, 1700.87, 500, False),
    ChessPlayer("Anthony Fantano", 37, 1400.45, 400, True),
    ChessPlayer("Beth Harmon", 20, 2500.34, 150, False)
]

# Simulate matches among players
for i, player1 in enumerate(players):
    for j, player2 in enumerate(players):
        if i < j:
            player1.simulate_match(player2)
            player2.simulate_match(player1)

# Print the final table of results
print("Final Tournament Results:")
print("{:<30} {:<10}".format("Player", "Score"))
print("-" * 40)
for player in players:
    print("{:<30} {:<10}".format(player.name, player.tournament_score))