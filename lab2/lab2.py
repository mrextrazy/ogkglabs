import matplotlib.pyplot as plt
import numpy as np

# Зчитування датасету з файлу
def read_dataset(filename):
    data = np.loadtxt(filename)
    return data

# Основна функція
def plot_dataset(data, output_file):
    # Розділення координат X і Y
    x, y = data[:, 0], data[:, 1]

    # Створення фігури з заданими розмірами
    fig, ax = plt.subplots(figsize=(960 / 100, 540 / 100), dpi=100)  # 960x540 пікселів

    # Відображення точок
    ax.scatter(x, y, color='blue', s=10)

    # Відключення осей і шкал
    ax.axis('off')

    # Збереження результату
    plt.savefig(output_file, format='png', bbox_inches='tight', pad_inches=0)
    print(f"Графік збережено у файл: {output_file}")

# Приклад використання
if __name__ == "__main__":
    input_file = "DS3.txt"  # Файл із даними
    output_file = "output_plot.png"  # Файл для збереження графіку

    try:
        dataset = read_dataset(input_file)
        plot_dataset(dataset, output_file)
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
