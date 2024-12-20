import pygame
import numpy as np

def read_dataset(filename):
    data = np.loadtxt(filename)
    return data

def plot_dataset(data):
    pygame.init()

    width, height = 960, 540
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Dataset Visualization")

    # Білий фон
    screen.fill((255, 255, 255))

    # Малювання точок
    for point in data:
        x, y = point
        pygame.draw.circle(screen, (0, 0, 255), (int(x), height - int(y)), 3)  # Y-координата інвертована

    # Оновлення екрану
    pygame.display.flip()

    # Очікування закриття вікна
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    input_file = "DS3.txt"  

    try:
        dataset = read_dataset(input_file)
        plot_dataset(dataset)
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")