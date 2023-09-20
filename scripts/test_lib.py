import pandas as pd
import matplotlib.pyplot as plt
from lib import compute_mean, compute_median, compute_std, visualize_hist

df = pd.read_csv("data/deniro.csv")
col = "Score"


def test_lib_mean():
    assert compute_mean(df, col) == 58.20


def test_lib_median():
    assert compute_median(df, col) == 65.00


def test_lib_std():
    assert compute_std(df, col) == 28.07


def test_lib_hist():
    visualize_hist(df, col)
    assert (
        plt.gca().get_title()
        == "Rotten Tomatoes Score Distribution of Robert De Niro Movies"
    )
