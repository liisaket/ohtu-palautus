class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1
    
    def if_draw(self, score, points):
        if points == 0:
            score = "Love-All"
        elif points == 1:
            score = "Fifteen-All"
        elif points == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score

    def if_points_four_or_more(self, score, minus_result):
        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def none_of_the_above(self, score):
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_score
            else:
                score = score + "-"
                temp_score = self.player2_score

            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
        return score

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.if_draw(score, self.player1_score)
        elif self.player1_score >= 4 or self.player2_score >= 4:
            minus_result = self.player1_score - self. player2_score
            score = self.if_points_four_or_more(score, minus_result)
        else:
            score = self.none_of_the_above(score)

        return score