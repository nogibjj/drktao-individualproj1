import pandas as pd
import matplotlib.pyplot as plt


def compute_mean(data, feature):
    data_mean = round(data[feature].mean(), 2)
    return data_mean


def compute_median(data, feature):
    data_median = round(data[feature].median(), 2)
    return data_median


def compute_std(data, feature):
    data_std = round(data[feature].std(), 2)
    return data_std


def visualize_hist(data, feature):
    plt.hist(
        data[feature],
        bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        edgecolor="black",
    )
    plt.title("Rotten Tomatoes Score Distribution of Robert De Niro Movies")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("data/deniro.csv")
    col = "Score"
    print("Mean RT Score: ", round(compute_mean(df, col), 2))
    print("Median RT Score: ", round(compute_median(df, col), 2))
    print("Standard Deviation of RT Scores: ", round(compute_std(df, col), 2))
