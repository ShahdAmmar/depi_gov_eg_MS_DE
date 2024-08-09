""" This script implement SUDOKU game using Pygame"""
import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((500, 570))
pygame.display.set_caption('SUDOKU Game!')

x, y = 0, 0
diff = 500 / 9
val = 0
defaultGrid = [
        [0, 0, 4, 0, 6, 0, 0, 0, 5],
        [7, 8, 0, 4, 0, 0, 0, 2, 0],
        [0, 0, 2, 6, 0, 1, 0, 7, 8],
        [6, 1, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 7, 5, 4, 0, 0, 6, 1],
        [0, 0, 1, 7, 5, 0, 9, 3, 0],
        [0, 7, 0, 3, 0, 0, 0, 1, 0],
        [0, 4, 0, 2, 0, 6, 0, 0, 7],
        [0, 2, 0, 0, 0, 7, 4, 0, 0],
    ]
font1 = pygame.font.SysFont('Arial', 40)
font2 = pygame.font.SysFont('Arial', 30)


def cord(pos):
    """ The function converts mouse click positions into grid coordinates.
    Args:
        pos: a tuple contains the x and y coordinates of the mouse position
    """
    global x, y
    x = pos[0] // diff
    y = pos[1] // diff


def highlightBox():
    """ The function draws thick black lines around the selected cell."""
    for k in range(2):
        pygame.draw.line(screen, (0, 0, 0), (x * diff-3, (y + k)*diff), (x * diff + diff + 3, (y + k) * diff), 7)
        pygame.draw.line(screen, (0, 0, 0), ((x + k) * diff, y * diff), ((x + k) * diff, y * diff + diff), 7)


def drawLines():
    """ The function display non-zero numbers from defaultGrid in their corresponding cells.
    It also draws the main grid lines and the smaller grid lines.
    """
    for i in range(9):
        for j in range(9):
            if defaultGrid[i][j] != 0:
                pygame.draw.rect(screen, (255, 255, 0), (i * diff, j * diff, diff + 1, diff + 1))
                txt1 = font1.render(str(defaultGrid[i][j]), 1, (0, 0, 0))
                screen.blit(txt1, (i * diff + 15, j * diff + 15))

    for l in range(10):
        if l % 3 == 0:
            thickness = 7
        else:
            thickness = 1
        pygame.draw.line(screen, (0, 0, 0), (0, l * diff), (500, l * diff), thickness)
        pygame.draw.line(screen, (0, 0, 0), (l * diff, 0), (l * diff, 500), thickness)


def fillValue(val):
    """ The function displays the entered number to the currently selected cell.
    Args:
        val: the entered number
    """
    txt1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(txt1, (x * diff + 15, y * diff + 15))


def validValue(m, k, l, val):
    """ The function checks if the entered value is valid for the specified cell.
    Args:
        m: the soduko grid
        k: the row index of the cell being checked
        l: the column index of the cell being checked
        val: the number being checked
    Return:
        True if val is valid, otherwise False
    """
    for it in range(9):
        if m[k][it] == val:
            return False
        if m[it][l] == val:
            return False

    it = k // 3
    jt = l // 3
    for k in range(it * 3, it * 3 + 3):
        for l in range(jt * 3, jt * 3 + 3):
            if m[k][l] == val:
                return False
    return True


def solveGame(defaultGrid, i, j):
    """ The functions checks if the game is solved or not and attempts to solve it.
    Args:
        defaultGrid: the sudoku grid
        i: the current row index
        j: the current column index
    Return:
        True if the game is solved successfully, otherwise False
    """
    while defaultGrid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True

    pygame.event.pump()
    for it in range(1, 10):
        if validValue(defaultGrid, i, j, it):
            defaultGrid[i][j] = it
            global x, y
            x = i
            y = j
            screen.fill((255, 255, 255))
            drawLines()
            highlightBox()
            pygame.display.update()
            pygame.time.delay(20)
            if solveGame(defaultGrid, i, j) == 1:
                return True
            else:
                defaultGrid[i][j] = 0
            screen.fill((0, 0, 0))

            drawLines()
            highlightBox()
            pygame.display.update()
            pygame.time.delay(50)
    return False


def gameResult():
    """ The functions displays a message when the puzzle is solved successfully."""
    txt1 = font1.render('Game finished.', 1, (0, 0, 0))
    screen.blit(txt1, (150, 520))


def raiseError1():
    """ The function displays an error message if the puzzle is not solved."""
    txt1 = font2.render('Wrong!', 1, (0, 0, 0))
    screen.blit(txt1, (200, 520))


def raiseError2():
    """ The function displays an error message if the key or value entered is invalid"""
    txt1 = font2.render('Wrong! Enter a valid key for the game.', 1, (0, 0, 0))
    screen.blit(txt1, (20, 520))


run = True
flag1 = 0
flag2 = 0
result = 0
error = 0
while run:
    screen.fill((255, 180, 190))
    for event in pygame.event.get():
        # Check for quit event
        if event.type == pygame.QUIT:
            run = False

        # Check for a mouse event
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            cord(pos)

        # Check for key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
            if event.key == pygame.K_r:
                result = 0
                error = 0
                flag2 = 0
                defaultGrid = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            if event.key == pygame.K_r:
                result = 0
                error = 0
                flag2 = 0
                defaultGrid = [
                    [0, 0, 4, 0, 6, 0, 0, 0, 5],
                    [7, 8, 0, 4, 0, 0, 0, 2, 0],
                    [0, 0, 2, 6, 0, 1, 0, 7, 8],
                    [6, 1, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 7, 5, 4, 0, 0, 6, 1],
                    [0, 0, 1, 7, 5, 0, 9, 3, 0],
                    [0, 7, 0, 3, 0, 0, 0, 1, 0],
                    [0, 4, 0, 2, 0, 6, 0, 0, 7],
                    [0, 2, 0, 0, 0, 7, 4, 0, 0],
                ]

    if flag2 == 1:
        if not solveGame(defaultGrid, 0, 0):
            error = 1
        else:
            result = 1
        flag2 = 0

    if val != 0:
        fillValue(val)
        if validValue(defaultGrid, int(x), int(y), val):
            defaultGrid[int(x)][int(y)] = val
            flag1 = 0
        else:
            defaultGrid[int(x)][int(y)] = 0
            raiseError2()
        val = 0

    if error == 1:
        raiseError1()
    if result == 1:
        gameResult()
    if flag1 == 1:
        highlightBox()
    drawLines()

    pygame.display.update()
    pygame.time.delay(300)

pygame.quit()
