import numpy as np
import matplotlib.pyplot as plt

def read_dataset(filename):
    data = np.loadtxt(filename)
    return data

def affine_transformation(points, center, angle):
    angle_rad = np.radians(angle)
    cos_theta, sin_theta = np.cos(angle_rad), np.sin(angle_rad)
    rotation_matrix = np.array([
        [cos_theta, -sin_theta],
        [sin_theta, cos_theta]
    ])
    shifted_points = points - center
    rotated_points = np.dot(shifted_points, rotation_matrix.T)
    result_points = rotated_points + center
    return result_points

def plot_and_save(points, canvas_size, output_file):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(points[:, 0], points[:, 1], color='blue', s=5)
    ax.axis('off')
    plt.savefig(output_file, dpi=96, bbox_inches='tight', pad_inches=0)
    plt.close()

def main():
    input_file = 'DS3.txt'
    output_file = 'result.png'
    center = np.array([480, 480])
    angle = 40
    canvas_size = 960
    points = read_dataset(input_file)
    transformed_points = affine_transformation(points, center, angle)
    plot_and_save(transformed_points, canvas_size, output_file)
    print(f"Результат збережено у файл: {output_file}")

if __name__ == '__main__':
    main()
