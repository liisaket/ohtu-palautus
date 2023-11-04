from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, reader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=1):
        category = SortBy(sort_by).name
        if category == "POINTS":
            sort_key = lambda player:player.points
        if category == "GOALS":
            sort_key = lambda player:player.goals
        if category == "ASSISTS":
            sort_key = lambda player:player.assists
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_key
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
