import pygame
import os
import time

# Initialize Pygame
pygame.init()

# Window settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
WHITE = (255, 255, 255)

# Load Uno cards
def load_cards():
    card_images = []
    for card_name in sorted(os.listdir('./uno')):
        if card_name.endswith('.png'):
            card_image = pygame.image.load(os.path.join('./uno', card_name))
            card_images.append(card_image)
    return card_images

# Insertion sort with animation
def insertion_sort(cards):
    for i in range(1, len(cards)):
        key_card = cards[i]
        j = i-1
        while j >=0 and card_value(cards[j]) > card_value(key_card): # Assuming a card_value function exists
            cards[j + 1] = cards[j]
            j -= 1
            draw_cards(cards)
            time.sleep(1) # Delay for the animation effect
        cards[j + 1] = key_card
        draw_cards(cards)
        time.sleep(1)

# Function to extract card value from the image filename or another method
def card_value(card):
    # Implement based on your card naming scheme
    pass

# Draw cards on screen
def draw_cards(cards):
    screen.fill(WHITE)
    x_offset = 50
    for card in cards:
        screen.blit(card, (x_offset, screen_height // 2 - card.get_height() // 2))
        x_offset += card.get_width() + 10
    pygame.display.flip()

# Main function
def main():
    cards = load_cards()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_cards(cards)
        time.sleep(2)
        insertion_sort(cards)

        # Break the loop after sorting to end the program
        running = False

    pygame.quit()

if __name__ == "__main__":
    main()
