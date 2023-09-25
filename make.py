#######EXPERIMENTAL FEATURE########

def send():
    grid = [[' ' for _ in range(15)] for _ in range(15)]
    words = ["multiplication","labyrinth","happy","ambassador","architecture","navigate","deliberate"]

    for index,letters in enumerate(words[0]):
        grid[index][7] = letters

    for row in grid:
        print(row)

    def find_pos(index):
        for row in range(len(grid)):
            for col in range(len(grid[row])):  
                for i in range(len(words[index])):  
                    if words[index][i] == grid[row][col]:
                        [cond , dir] = check_space(words[index][:i][::-1],words[index][i+1:],row,col)
                        if cond:
                            print("Entered if")
                            before = words[index][:i][::-1]
                            after = words[index][i+1:]
                            if dir == 'v':
                                for i in range(len(before)):    
                                    grid[row-i-1][col] = before[i]
                                for i in range(len(after)):
                                    grid[row+i+1][col] = after[i]
                                
                            else:
                                for i in range(len(before)):    
                                    grid[row][col-i-1] = before[i]
                                for i in range(len(after)):
                                    grid[row][col+i+1] = after[i]
                                
                            return

                        
    def check_space(pre,post,row,col):
        if grid[row - 1][col] == ' ' or grid[row + 1][col] == ' ':
            print("Entered vert")
            for i in range(len(pre)):
                if row-i > 0 and col +1 < 15 and col - 1 >= 0:
                    if grid[row - i - 1][col] != ' ' or grid[row  - i - 1][col- 1] != ' ' or grid[row  - i - 1][col + 1] != ' ':
                        print("im false")
                        return [False,' ']
                else:
                    return [False,' ']
            for j in range(len(post) + 1):
                if row+j < 14 and col + 1 < 15 and col - 1 >= 0:
                    if grid[row + j + 1][col] != ' ' or grid[row  + j + 1][col- 1] != ' ' or grid[row  + j + 1][col + 1] != ' ':
                        print("no iam")
                        return [False,' ']
                else:
                    return [False,' ']
            print("This line is vertical")
            return [True,'v']    
        
        if grid[row][col- 1] == ' ' or grid[row][col + 1] == ' ':
            print("Entered hor")
            for i in range(len(pre)):
                if col-i > 0 and row + 1 < 15 and row - 1 >= 0:
                    if grid[row][col - i - 1] != ' ' or grid[row - 1][col - i - 1] != ' ' or grid[row + 1][col - i -1] != ' ':
                        return [False,' ']
                else:
                    return [False,' ']
            for j in range(len(post) + 1):
                if col+j < 14 and row + 1 < 15 and row - 1 >= 0:
                    if grid[row][col + j + 1] != ' ' or grid[row - 1][col + j + 1] != ' ' or grid[row + 1][col + j + 1] != ' ':
                        return [False,' ']
                else:
                    return [False,' ']
            print("This line is horizontal")
            return [True,'h']
        return [False," "]

    for i in range(6):
        find_pos(i+1)
    for row in grid:
        print(row)
    
    return grid

