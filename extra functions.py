from tour import positions, Knight, brute_force

def test_all():
    for start in positions:
        board = [['__' for i in range(8)] for j in range(8)]
        new_knight = Knight(board, start_position=start)
        while new_knight.count < 63 and new_knight.true_count < 120:
            if new_knight.check2() and new_knight.path_still_possible():
                a, b, = new_knight.check2()[0]
                new_knight.move(a, b)
                new_knight.record()
            else:
                # this happens if the knight gets stuck in a dead end or a square gets isolated
                new_knight.find_decision_point()
                # now find a path that hasn't already been taken
                # skip the first option
                for square in new_knight.check2()[1:]:
                    a, b = square
                    new_knight.move(a, b)
                    if new_knight.grid in new_knight.remembered_states:
                        # if this is a path already taken, go back and try again
                        new_knight.step_backwards()
                    else:
                        # if this is a new route, record the state and leave the for loop
                        new_knight.record()
                        break
                else:
                    # this happens if all of the options at this decision point have already been taken
                    # so take another step backwards and find a new decision point
                    new_knight.step_backwards()
                    new_knight.find_decision_point()
        # displays the end route
        new_knight.display()


def test_specific(x, y):
    board = [['__' for i in range(8)] for j in range(8)]
    new_knight = Knight(board, start_position=(x, y))
    starts = 0
    while new_knight.count < 63:
        if new_knight.check2() and new_knight.path_still_possible():
            a, b, = new_knight.check2()[0]
            new_knight.move(a, b)
            new_knight.record()
        else:
            # start again with a slightly different beginning
            print('starting over')
            starts += 1
            print(starts)
            new_knight = Knight([['__' for i in range(8)] for j in range(8)], start_position=(x, y))
            new_knight.display()
            a, b, = new_knight.check2()[starts]
            new_knight.move(a, b)
    new_knight.display()


def test_all2():
    for start in positions:
        x, y = start
        test_specific(x, y)


def test_all3():
    for start in positions:
        x, y = start
        brute_force(x, y)


