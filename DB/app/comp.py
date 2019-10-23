

from app.orm import ORM

class Comp(ORM):

    tablename = 'comps'
    fields = ['comp_id', 'comp_name', 'sub_comp_id', 'sub_comp_name', 'start_date', 'end_date', 'league']

    def __init__(self, *args, **kwargs):
        self.comp_id = kwargs.get('comp_id')
        self.comp_name = kwargs.get('comp_name')
        self.sub_comp_id = kwargs.get('sub_comp_id')
        self.sub_comp_name = kwargs.get('sub_comp_name')
        self.start_date = kwargs.get('start_date')
        self.end_date = kwargs.get('end_date')
        self.league = kwargs.get('league')

        