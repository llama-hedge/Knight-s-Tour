import random

# across, vertical
valid_moves = [(+2, +1), (+2, -1), (+1, +2), (-1, +2), (-2, +1), (-2, -1), (-1, -2), (+1, -2)]
positions = [(i, j) for i in range(8) for j in range(8)]


class Knight:
    def __init__(self, grid, start_position=(0, 0)):
        self.grid = grid
        self.x, self.y = start_position
        self.grid[self.y][self.x] = '0 '
        self.remembered_states = []
        self.count = 0
        self.true_count = 0

    def display(self):
        print('='*40)
        for row in self.grid:
            print(row)

    def move(self, horizontal, vertical):
        self.x = horizontal
        self.y = vertical
        self.count += 1
        self.true_count += 1
        self.grid[self.y][self.x] = str(self.count)
        if len(str(self.count)) < 2:
            self.grid[self.y][self.x] += ' '

    def moves_from_point(self, x, y):
        """Returns a list of valid knight moves to squares that exist and have not already been visited"""
        return [(x + i, y + j) for (i, j) in valid_moves if -1 < x + i < 8 and -1 < y + j < 8 and self.grid[y + j][x + i] == '__']

    def equivalent_options(self):
        """determines all the available moves, counts how many available moves each of those positions have, and then
        returns a list containing the moves with thhe least amount of options"""
        # very similar to check2, but only returns equal least options, not all of them. They are all equal so sorting
        # is unnecessary
        available_unvisited = self.moves_from_point(self.x, self.y)
        if self.count == 62:
            # if this is the last move, there will be at most one option
            return available_unvisited
        else:
            list_of_tuples = []
            for square in available_unvisited:
                x, y = square
                options = len(self.moves_from_point(x, y))
                # remove dead ends
                if options == 0:
                    pass
                else:
                    list_of_tuples.append((square, options))
            length_list = [number for (square, number) in list_of_tuples]
            try:
                least_length = min(length_list)
            except ValueError:
                return []
            least_options_unvisited = [square for (square, number) in list_of_tuples if number == least_length]
            return least_options_unvisited


def randomized(x, y):
    new_knight = Knight([['__' for i in range(8)] for j in range(8)], start_position=(x, y))
    while new_knight.count < 63:
        if new_knight.equivalent_options():
            equivalents = new_knight.equivalent_options()
            rand = random.randint(1, len(equivalents))
            a, b = equivalents[rand-1]
            new_knight.move(a, b)
        else:
            # dead end, start over
            new_knight = Knight([['__' for i in range(8)] for j in range(8)], start_position=(x, y))
    new_knight.display()


if __name__ == '__main__':
    for start in positions:
        p, q = start
        randomized(p, q)
