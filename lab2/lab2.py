import matplotlib.pyplot as plt
import numpy as np

def read_dataset(filename):
    data = np.loadtxt(filename)
    return data

def plot_dataset(data, output_file):
    x, y = data[:, 0], data[:, 1]

    fig, ax = plt.subplots(figsize=(960 / 100, 540 / 100), dpi=100)  

    ax.scatter(x, y, color='blue', s=10)

    ax.axis('off')

    plt.savefig(output_file, format='png', bbox_inches='tight', pad_inches=0)
    print(f"Графік збережено у файл: {output_file}")

if __name__ == "__main__":
    input_file = "DS3.txt"  
    output_file = "output_plot.png"  

    try:
        dataset = read_dataset(input_file)
        plot_dataset(dataset, output_file)
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
