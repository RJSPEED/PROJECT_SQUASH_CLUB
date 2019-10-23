
from app.orm import ORM

class Match(ORM):

    tablename = 'matches'
    fields = ['comp_id', 'sub_comp_id', 'match_id', 'p1_user_id', 'p2_user_id', 'walkover', 
              'date_played', 'p1_games_won', 'p2_games_won', 'p1_g1_score', 'p2_g1_score',
              'p1_g2_score', 'p2_g2_score', 'p1_g3_score', 'p2_g3_score', 'p1_g4_score',
              'p2_g4_score', 'p1_g5_score', 'p2_g5_score']

    def __init__(self, *args, **kwargs):
        self.comp_id = kwargs.get('comp_id')
        self.sub_comp_id = kwargs.get('sub_comp_id')
        self.match_id = kwargs.get('match_id')
        self.p1_user_id = kwargs.get('p1_user_id')
        self.p2_user_id = kwargs.get('p2_user_id')
        self.walkover = kwargs.get('walkover')
        self.date_played = kwargs.get('date_played')
        self.p1_games_won = kwargs.get('p1_games_won')
        self.p2_games_won = kwargs.get('p2_games_won')
        self.p1_g1_score = kwargs.get('p1_g1_score')
        self.p2_g1_score = kwargs.get('p2_g1_score')
        self.p1_g2_score = kwargs.get('p1_g2_score')
        self.p2_g2_score = kwargs.get('p2_g2_score')
        self.p1_g3_score = kwargs.get('p1_g3_score')
        self.p2_g3_score = kwargs.get('p2_g3_score')
        self.p1_g4_score = kwargs.get('p1_g4_score')
        self.p2_g4_score = kwargs.get('p2_g4_score')
        self.p1_g5_score = kwargs.get('p1_g5_score')
        self.p2_g5_score = kwargs.get('p2_g5_score')