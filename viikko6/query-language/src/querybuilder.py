from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, pino = All()):
        self.pino = pino
    
    def playsIn(self, team):
        return QueryBuilder(And(self.pino, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.pino, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.pino, HasFewerThan(value, attr)))

    def oneOf(self, query1, query2):
        return QueryBuilder(And(self.pino, Or(query1, query2)))

    def build(self):
        return self.pino