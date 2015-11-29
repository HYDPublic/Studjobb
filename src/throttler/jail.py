class Jail(object):

    def __init__(self):
        self._cells = {}

    def add_prisoner(self, prisoner):
        if not self.cell_exists_for(prisoner):
            self.create_cell_for(prisoner)
        self.throw_in_cell(prisoner)

    def throw_in_cell(self, prisoner):
        self._cells[prisoner.identifier].append(prisoner)

    def create_cell_for(self, prisoner):
        self._cells[prisoner.identifier] = []

    def delete_cell_for(self, prisoner):
        del self._cells[prisoner.identifier]

    def add_prisoners(self, prisoners):
        for prisoner in prisoners:
            self.add_prisoner(prisoner)

    def get_total_number_of_prisoners(self):
        return sum(map(len, self._cells.values()))

    def cell_exists_for(self, prisoner):
        return self._cells.has_key(prisoner.identifier)

    def get_prisoners_in_same_cell_as(self, prisoner):
        if self.cell_exists_for(prisoner):
            return self._cells[prisoner.identifier]
        return []

    def get_number_of_similar_prisoners_as(self, prisoner):
        return len(self.get_prisoners_in_same_cell_as(prisoner))

    def release_prisoners_similar_to(self, prisoner):
        if self.cell_exists_for(prisoner):
            self.delete_cell_for(prisoner)
