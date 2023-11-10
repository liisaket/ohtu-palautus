class PlayerStats:
  def __init__(self, reader):
    self.reader = reader
  
  def top_scorers_by_nationality(self, nationality):
    players = self.reader.get_players()
    wantedPlayers = list(filter(lambda player: player.nationality == nationality, players))
    wantedPlayers.sort(key=lambda x: x.goals + x.assists, reverse=True)
    return wantedPlayers