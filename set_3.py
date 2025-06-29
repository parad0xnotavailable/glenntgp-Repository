'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']:
        return 'friends'

    elif to_member in social_graph[from_member]['following']:
        return 'follower'

    elif from_member in social_graph[to_member]['following']:
        return 'followed by'

    else:
        return 'no relationship'


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    board_size = len(board)

    # 1. Check if any columns all have the same value
    
    for col in range(board_size):
        cols_checker = [] # list to be used to check the set
        
        for row in range(board_size):
            cols_checker.append(board[row][col])

        if len(set(cols_checker)) ==1 and cols_checker[0] != '':
            return cols_checker[0]

    # 2. Check if any rows all have the same value
    for row in range(board_size):

        if len(set(board[row])) ==1 and board[row][0] != '':
            return board[row][0]

    # 3. Check if left diagnonals all have the same value
    l_diag_list = []

    for i in range(board_size):
        l_diag_list.append(board[i][i])

    if len(set(l_diag_list)) == 1 and l_diag_list[0] != '':
        return l_diag_list[0]

       
    r_diag_col_val = board_size - 1
    r_diag_row_val = 0
    r_diag_list = []

    for i in range(board_size):
        r_diag_list.append(board[r_diag_row_val][r_diag_col_val])
        r_diag_col_val -= 1
        r_diag_row_val += 1

    if len(set(r_diag_list)) == 1 and r_diag_list[0] != '':
        return r_diag_list[0]

    return 'NO WINNER'


def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    current_stop = first_stop
    travel_time = 0

    while current_stop != second_stop:
        for (start, end), tdata in route_map.items():
            if start == current_stop:
                travel_time += tdata['travel_time_mins']
                current_stop = end
                break

    return travel_time
                