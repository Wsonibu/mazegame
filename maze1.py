import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 600, 600

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Kích thước ô mê cung
CELL_SIZE = 40

# Số ô mê cung trên mỗi hàng và cột
ROWS = WIDTH // CELL_SIZE
COLS = HEIGHT // CELL_SIZE

# Hình chữ L
L_WALLS = [(2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5)]

# Kích thước đối tượng
player_size = CELL_SIZE

# Tốc độ di chuyển
speed = CELL_SIZE

# Khởi tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Hàm vẽ mê cung
def draw_maze():
    for row in range(ROWS):
        for col in range(COLS):
            if (row, col) in L_WALLS:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Hàm vẽ đối tượng và vật phẩm
def draw_objects():
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, WHITE, (item_pos[0] * CELL_SIZE, item_pos[1] * CELL_SIZE, player_size, player_size))

# Hàm kiểm tra va chạm
def check_collision():
    if player_pos == item_pos:
        return "win"
    elif (player_pos[1] // CELL_SIZE, player_pos[0] // CELL_SIZE) in L_WALLS:
        return "lose"
    else:
        return None

# Vị trí bắt đầu của đối tượng
player_pos = [0, 0]

# Vị trí vật phẩm
item_pos = [COLS - 1, ROWS - 1]

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_pos[1] - speed >= 0:
        player_pos[1] -= speed
    if keys[pygame.K_DOWN] and player_pos[1] + speed < HEIGHT:
        player_pos[1] += speed
    if keys[pygame.K_LEFT] and player_pos[0] - speed >= 0:
        player_pos[0] -= speed
    if keys[pygame.K_RIGHT] and player_pos[0] + speed < WIDTH:
        player_pos[0] += speed

    # Kiểm tra va chạm
    result = check_collision()
    if result == "win":
        print("You win!")
        pygame.quit()
        sys.exit()
    elif result == "lose":
        print("You lose!")
        pygame.quit()
        sys.exit()

    # Xóa màn hình
    screen.fill((0, 0, 0))

    # Vẽ mê cung và đối tượng
    draw_maze()
    draw_objects()

    # Cập nhật màn hình
    pygame.display.flip()
    pygame.time.Clock().tick(30)
