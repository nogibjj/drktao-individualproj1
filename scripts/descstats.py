import pandas as pd
import lib


def denirostats(data, feature):
    sumstats = pd.DataFrame(
        {
            "Mean RT Score": round(lib.compute_mean(data, feature), 2),
            "Median RT Score": round(lib.compute_median(data, feature), 2),
            "Standard Deviation of Scores": round(lib.compute_std(data, feature), 2),
        },
        index=[0],
    )
    return sumstats


def denirohist(data, feature):
    lib.visualize_hist(data, feature)


if __name__ == "__main__":
    df = pd.read_csv("data/deniro.csv")
    col = "Score"
    summary = denirostats(df, col)
    denirohist(df, col)
    str1 = f"{summary.to_markdown()}"
    str2 = "![Alt text](visualizations/denirohist.png)"

    file_path = "./report.md"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str1 + "\n" * 3 + str2)
