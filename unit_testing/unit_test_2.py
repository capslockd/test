class User:

    def __init__(self):
        self.profile = {'active': False, 'level': 1, 'points': 0}

    def activate(self):
        self.profile['active'] = True

    def is_active(self):
        return self.profile['active']

    def get_level(self):
        return self.profile['level']

    def get_points(self):
        return self.profile['points']

    def add_points(self, additional_points):
        self.profile['points'] += additional_points

        if self.get_points() > 300:
            self.profile['level'] = 3
        elif self.get_points() > 200:
            self.profile['level'] = 2