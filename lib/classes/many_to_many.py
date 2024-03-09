class Game:
    def __init__(self, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if len(title) == 0:
            raise ValueError("Title must not be empty")
        self._title = title
        self._results = []

    @property
    def title(self):
        return self._title

    @property
    def results(self):
        return self._results

    def players(self):
        players = set()
        for result in self._results:
            players.add(result.player)
        return list(players)

    def average_score(self, player):
        player_results = [
            result.score for result in self._results if result.player == player]
        if not player_results:
            return 0
        return sum(player_results) / len(player_results)


class GameWrapper:
    def __init__(self, game):
        self.game = game

    def __call__(self):
        return self.game.results


class Player:
    def __init__(self, username):
        if not isinstance(username, str):
            raise ValueError("Username must be a string")
        if not 2 <= len(username) <= 16:
            raise ValueError("Username must be between 2 and 16 characters")
        self._username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            raise TypeError("New username must be a string")
        if not 2 <= len(new_username) <= 16:
            raise ValueError(
                "New username must be between 2 and 16 characters")
        self._username = new_username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        return any(result.game == game for result in self.results())

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)


class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(score, int):
            raise ValueError("Score must be an integer")

        if score < 1:
            score = 1
        elif score > 5000:
            score = 5000

        self._player = player
        self._game = game
        self._score = score
        self._game.results.append(self)  # Associate the result with the game
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game
