def get_init_last(first_name, last_name):
    return '{}.{}'.format(first_name[0], last_name)


people = []

person0 = {
    'first_name': None,
    'last_name': None,
    # Methods
    'get_init_last': get_init_last
}

people.append(person0)

print(people[0]['get_init_last']('jimmy', 'guy'))


class person(obejct):

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def get_init_last(self):
        return '{}.{}'.format(slef.first_name[0], self.last_name)
