import math

physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

def calculate_Pearson_Correlation(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("Lists must have the same length")

    mean_x = sum(x) / n
    mean_y = sum(y) / n
    xi_mean_x = [xi - mean_x for xi in x]
    yi_mean_y = [yi - mean_y for yi in y]
    sum_xy = sum(xi * yi for xi, yi in zip(xi_mean_x, yi_mean_y))
    numerator = sum_xy

    xi_mean_x2 = [xi ** 2 for xi in xi_mean_x]
    yi_mean_y2 = [yi ** 2 for yi in yi_mean_y]
    sum_x2 = sum(xi_mean_x2)
    sum_y2 = sum(yi_mean_y2)
    denominator = math.sqrt(sum_x2 * sum_y2)

    if denominator == 0:
        return 0

    return numerator / denominator

if __name__ == "__main__":
    correlation = calculate_Pearson_Correlation(physics, history)
    print(f"Pearson Correlation Coefficient: {correlation:.3f}")
    