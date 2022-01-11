import random
import pygame
pygame.font.init()
col = 10  # 10 columns
row = 20  # 20 rows
s_width = 800  # window width
s_height = 750  # window height
play_width = 300  # play window width; 300/10 = 30 width per block
play_height = 600  # play window height; 600/20 = 20 height per block
block_size = 30  # size of block
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height - 50
filepath = 'record.txt'
fontpath = 'arcade.ttf'
fontpath_mario = 'fonts.ttf'
A = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
I = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
B = [['.....',
      '..0..',
      '..0..',
      '..0..',
      '..0..'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
Y = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
K = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
U = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
S = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
shapes = [A, I, B, Y, K, U, S]
get_color = lambda: (random.randrange(30, 256), random.randrange(30, 256), random.randrange(30, 256))
shape_colors = [(255, 84, 136), (203, 153, 255), (222, 247, 254), (177, 7, 200), (23, 188, 16), (255, 8, 88), (203, 101, 204)]
class Piece():
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)] 
        self.rotation = 0
def create_grid(locked_pos={}):
    grid = [[(255, 185, 255) for x in range(col)] for y in range(row)] 
    return grid
def convert_shape_format(piece):
    positions = []
    shape_format = piece.shape[piece.rotation % len(piece.shape)] 
    for i, line in enumerate(shape_format):
        row = list(line)  
        for j, column in enumerate(row):
            if column == '0':
                positions.append((piece.x + j, piece.y + i))
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    print(positions)
    return positions
def valid_space(piece, grid):
    accepted_pos = [[(x, y) for x in range(col) if grid[y][x] == (255, 185, 255)] for y in range(row)]
    accepted_pos = [x for item in accepted_pos for x in item]
    formatted_shape = convert_shape_format(piece)
    for pos in formatted_shape:
        if pos not in accepted_pos:
            if pos[1] >= 0:
                return False
    return True
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False
def get_shape():
    return Piece(5, 0, random.choice(shapes))
def draw_text_middle(text, size, color, surface):
    font = pygame.font.Font('arcade.ttf', size, bold=False, italic=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), top_left_y + play_height/2 - (label.get_height()/2)))
def draw_grid(surface):
    grid_color = (255, 230, 255)
    for i in range(row):
        pygame.draw.line(surface, grid_color, (top_left_x, top_left_y + i * block_size),
                         (top_left_x + play_width, top_left_y + i * block_size))
        for j in range(col):
            pygame.draw.line(surface, grid_color, (top_left_x + j * block_size, top_left_y),
                             (top_left_x + j * block_size, top_left_y + play_height))
def clear_rows(grid, locked):
    increment = 0
    for i in range(len(grid) - 1, -1, -1):
        grid_row = grid[i]                
        if (255, 185, 255) not in grid_row:         
            increment += 1
            index = i                          
            for j in range(len(grid_row)):
                try:
                    del locked[(j, i)]         
                except ValueError:
                    continue
    if increment > 0:
        for key in sorted(list(locked), key=lambda a: a[1])[::-1]:
            x, y = key
            if y < index:                       
                new_key = (x, y + increment)  
                locked[new_key] = locked.pop(key)
    return increment
def draw_next_shape(piece, surface):
    font = pygame.font.Font(fontpath, 30)
    label = font.render('Next figure', 0, (255, 0, 119))
    start_x = top_left_x + play_width + 50
    start_y = top_left_y + (play_height / 2 - 100)
    shape_format = piece.shape[piece.rotation % len(piece.shape)]
    for i, line in enumerate(shape_format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, piece.color, (start_x + j*block_size, start_y + i*block_size, block_size, block_size), 0)
    surface.blit(label, (start_x, start_y - 30))
def draw_window(surface, grid, score=0, last_score=0):
    surface.fill((255, 255, 255))
    pygame.font.init()
    
    font = pygame.font.Font(fontpath_mario, 65, bold=True)
    label = font.render('TETRIS', 1, (255, 0, 119))
    surface.blit(label, ((top_left_x + play_width / 2) - (label.get_width() / 2), 30))
    
    font = pygame.font.Font(fontpath, 30)
    label = font.render('SCORE   ' + str(score) , 1, (255, 0, 119))
    start_x = top_left_x + play_width + 50
    start_y = top_left_y + (play_height / 2 - 100)
    surface.blit(label, (start_x, start_y + 200))
    
    label = font.render('RECORD   ' + str(last_score), 1, (255, 0, 119))
    start_x = top_left_x - 240
    start_y = top_left_y + 200
    surface.blit(label, (start_x + 20, start_y + 200))
    
    for i in range(row):
        for j in range(col):
            pygame.draw.rect(surface, grid[i][j],
                             (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size), 0)
    draw_grid(surface)
    border_color = (255, 255, 255)
    pygame.draw.rect(surface, border_color, (top_left_x, top_left_y, play_width, play_height), 4)
def update_score(new_score):
    score = max_score().get_max_score()
    with open(filepath, 'w') as file:
        if new_score > score:
            file.write(str(new_score))
        else:
            file.write(str(score))
class max_score():
    def __init__(self): 
        self.score = 0
    def get_max_score(self):
        with open(filepath, 'r') as file:
            lines = file.readlines()        
            self.score = int(lines[0].strip()) 
        return self.score
class main_win:
    def main(self, window):
        locked_positions = {}
        create_grid(locked_positions)
        change_piece = False
        run = True
        current_piece = get_shape()
        next_piece = get_shape()
        clock = pygame.time.Clock()
        fall_time = 0
        fall_speed = 0.35
        level_time = 0
        score = 0
        last_score = max_score().get_max_score()
        while run:
            grid = create_grid(locked_positions)
            fall_time += clock.get_rawtime() 
            level_time += clock.get_rawtime()
            clock.tick()  
            if level_time/1000 > 5:   
                level_time = 0
                if fall_speed > 0.15:   
                    fall_speed -= 0.005
            if fall_time / 1000 > fall_speed:
                fall_time = 0
                current_piece.y += 1
                if not valid_space(current_piece, grid) and current_piece.y > 0:
                    current_piece.y -= 1
                    change_piece = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.display.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        current_piece.x -= 1 
                        if not valid_space(current_piece, grid):
                            current_piece.x += 1
                    elif event.key == pygame.K_RIGHT:
                        current_piece.x += 1 
                        if not valid_space(current_piece, grid):
                            current_piece.x -= 1
                    elif event.key == pygame.K_DOWN:
                        current_piece.y += 1
                        if not valid_space(current_piece, grid):
                            current_piece.y -= 1
                    elif event.key == pygame.K_UP:
                        current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                        if not valid_space(current_piece, grid):
                            current_piece.rotation = current_piece.rotation - current_piece.rotation
            piece_pos = convert_shape_format(current_piece)
            for i in range(len(piece_pos)):
                x, y = piece_pos[i]
                if y >= 0:
                    grid[y][x] = current_piece.color
            if change_piece: 
                for pos in piece_pos:
                    p = (pos[0], pos[1])
                    locked_positions[p] = current_piece.color      
                current_piece = next_piece
                next_piece = get_shape()
                change_piece = False
                score += clear_rows(grid, locked_positions) * 10    
                update_score(score)
                if last_score < score:
                    last_score = score
            draw_window(window, grid, score, last_score)
            draw_next_shape(next_piece, window)
            pygame.display.update()
            if check_lost(locked_positions):
                run = False
        draw_text_middle('You Lost', 40, (255, 255, 255), window)
        pygame.display.update()
        pygame.time.delay(2000)
        window.fill((0, 0, 0))
class Game:   
    def main_menu(window):
        run = True
        while run:
            draw_text_middle('Press any key to begin', 50, (255, 255, 255), window)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    main_win().main(window)
        pygame.quit()
    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Tetris')
    main_menu(win)
if __name__ == '__main__':
    Game()