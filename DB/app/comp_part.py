
from app.orm import ORM

class Comp_Part(ORM):

    tablename = 'comp_participants'
    fields = ['comp_id', 'sub_comp_id', 'user_id', 'points']

    def __init__(self, *args, **kwargs):
        self.comp_id = kwargs.get('comp_id')
        self.sub_comp_id = kwargs.get('sub_comp_id')
        self.user_id = kwargs.get('user_id')
        self.points = kwargs.get('points')
        