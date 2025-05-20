import pygame
import random








# Initialize pygame
pygame.init()








# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Obsacle game")








# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)








you = pygame.image.load('you.jpg') # replace with your image path of the main character
enemy = pygame.image.load('enemy.jpg') # replace with your image path of the enemy character that you want to dodge
snow_rider = pygame.transform.scale(you, (50, 50))
obstacle = pygame.transform.scale(enemy, (50, 50))








# Player settings
player_x, player_y = WIDTH // 2, HEIGHT - 100
player_speed = 5








# Obstacle settings
obstacles = []
obstacle_speed = 5
generation_frequency=60








# Score
score = 0
font = pygame.font.Font(None, 36)








# Clock for controlling frame rate
clock = pygame.time.Clock()








running=True










# Add a paused variable
paused = False


# Game loop
while running:
    screen.fill(WHITE)
   
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Toggle pause when space is pressed
                paused = not paused


    if paused:
        # Display "Paused" message
        pause_text = font.render("Paused. Press SPACE to resume.", True, BLACK)
        screen.blit(pause_text, (WIDTH // 2 - 150, HEIGHT // 2))
        pygame.display.flip()
        clock.tick(30)
        continue  # Skip the rest of the game loop while paused


    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed


    # Adjust difficulty based on score
    if score >= 5000:
        obstacle_speed = 27
        generation_frequency = 1
    elif score >= 4500:
        obstacle_speed = 25
        generation_frequency = 14
    elif score >= 4000:
        obstacle_speed = 24
        generation_frequency = 15
    elif score >= 3500:
        obstacle_speed = 23
        generation_frequency = 15
    elif score >= 3000:
        obstacle_speed = 22
        generation_frequency = 16
    elif score >= 2500:
        obstacle_speed = 20
        generation_frequency = 17
        player_speed = 20
    elif score >= 2000:
        obstacle_speed = 19
        generation_frequency = 18
    elif score >= 1700:
        obstacle_speed = 18
        generation_frequency = 19
        player_speed = 10
    elif score >= 1500:
        obstacle_speed = 16
        generation_frequency = 20
    elif score >= 1200:
        obstacle_speed = 14
        generation_frequency = 20
    elif score >= 1000:
        obstacle_speed = 11
        generation_frequency = 25
        player_speed = 11
    elif score >= 500:
        obstacle_speed = 8  # Increase obstacle speed
        generation_frequency = 30  # More obstacles (1 in 30 chance)
    else:
        obstacle_speed = 5  # Default obstacle speed
        generation_frequency = 60  # Default frequency (1 in 60 chance)
        player_speed = 5  # Default player speed


    # Obstacle generation and movement
    if random.randint(1, generation_frequency) == 1:  # Generate obstacles randomly
        obstacles.append([random.randint(0, WIDTH - 50), -50])
    for obstacle_pos in obstacles:
        obstacle_pos[1] += obstacle_speed


    # Collision detection
    for obstacle_pos in obstacles:
        if (player_x < obstacle_pos[0] + 50 and
            player_x + 50 > obstacle_pos[0] and
            player_y < obstacle_pos[1] + 50 and
            player_y + 50 > obstacle_pos[1]):
            running = False  # End the game


    # Draw player and obstacles
    screen.blit(snow_rider, (player_x, player_y))
    for obstacle_pos in obstacles:
        screen.blit(obstacle, (obstacle_pos[0], obstacle_pos[1]))


    # Draw score
    score += 1
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))


    # Update display
    pygame.display.flip()
    clock.tick(30)


pygame.quit()

