import random
from make import send

# answers = [["multiplication","labyrinth","happy","ambassador","architecture","navigate","deliberate"],
#            ["microscope","independent","tent","calculator","rainbow","exploration","furniture"]]
# questions = [["1. An arithmetic operation, where we find the product of two or more numbers.", "2. A Maze.", "3. Feeling of pleasure.", "4. A representative of a specified activity.", "5. The art of designing and constructing buildings." ,"6. Plan and direct the course of a ship.", "7. Done consciously and intentionally."],
#              ["1. An instrument used to examine objects that are too small to be seen by the naked eye.","2. Not relying on another ","3. They were looking for a place at which they could pitch the ____.","4. Common device for solving math problems.","5. A natural arc with red, orange, yellow, green, blue, and violet.","6. Discovery of new lands or knowledge.", "7. Household items for seating and storage."]]
# grids = [[
#             [' ', ' ', ' ', ' ', ' ', ' ', 'm', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', 'u', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', 'l', 'a', 'b', 'y', 'r', 'i', 'n', 't', 'h'],
#             [' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             ['h', 'a', 'p', 'p', 'y', ' ', 'i', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', 'm', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' '],
#             [' ', 'b', ' ', ' ', ' ', ' ', 'l', ' ', ' ', ' ', ' ', ' ', 'e', ' ', ' '],
#             [' ', 'a', ' ', ' ', ' ', ' ', 'i', ' ', ' ', ' ', ' ', ' ', 'l', ' ', ' '],
#             [' ', 's', ' ', ' ', ' ', ' ', 'c', ' ', ' ', ' ', ' ', ' ', 'i', ' ', ' '],
#             [' ', 's', ' ', ' ', ' ', ' ', 'a', ' ', ' ', ' ', ' ', ' ', 'b', ' ', ' '],
#             [' ', 'a', 'r', 'c', 'h', 'i', 't', 'e', 'c', 't', 'u', 'r', 'e', ' ', ' '],
#             [' ', 'd', ' ', ' ', ' ', ' ', 'i', ' ', ' ', ' ', ' ', ' ', 'r', ' ', ' '],
#             [' ', 'o', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', 'a', ' ', ' '],
#             [' ', 'r', ' ', ' ', ' ', ' ', 'n', 'a', 'v', 'i', 'g', 'a', 't', 'e', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'e', ' ', ' '],
#         ],
# [
#             ['m', 'i', 'c', 'r', 'o', 's', 'c', 'o', 'p', 'e', ' ', ' ', ' ', ' ', ' '],
#             [' ', 'n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' '],
#             [' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
#             [' ', 'e', ' ', ' ', 'c', ' ', ' ', ' ', ' ', 'l', ' ', ' ', ' ', ' ', ' '],
#             [' ', 'p', ' ', ' ', 'a', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' '],
#             [' ', 'e', ' ', ' ', 'l', ' ', ' ', ' ', ' ', 'r', ' ', ' ', ' ', ' ', ' '],
#             [' ', 'n', ' ', ' ', 'c', ' ', ' ', ' ', ' ', 'a', ' ', ' ', ' ', ' ', ' '],
#             [' ', 'd', ' ', ' ', 'u', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' '],
#             [' ', 'e', ' ', ' ', 'l', ' ', ' ', ' ', ' ', 'i', ' ', ' ', ' ', ' ', ' '],
#             [' ', 'n', ' ', ' ', 'a', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' '],
#             [' ', 't', 'e', 'n', 't', ' ', 'f', 'u', 'r', 'n', 'i', 't', 'u', 'r', 'e'],
#             [' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', 'r', 'a', 'i', 'n', 'b', 'o', 'w', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#         ]
# ]

def crossword_gen():
    [grid , ans , quest] = send()
    return(quest , ans , grid)
