from descstats import denirostats
from descstats import denirohist
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/deniro.csv")
col = "Score"


def test_deniro():
    assert denirostats(df, col).iloc[0, 0] == 58.20
    assert denirostats(df, col).iloc[0, 1] == 65.00
    assert denirostats(df, col).iloc[0, 2] == 28.07


def test_viz():
    denirohist(df, col)
    assert (
        plt.gca().get_title()
        == "Rotten Tomatoes Score Distribution of Robert De Niro Movies"
    )
