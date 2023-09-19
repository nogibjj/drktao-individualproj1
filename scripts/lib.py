import pandas as pd
import matplotlib.pyplot as plt
import statistics


def compute_mean(data,feature):
    data_mean=data[feature].mean()
    return data_mean

def compute_median(data,feature):
    data_median=data[feature].median()
    return data_median

def compute_std(data,feature):
    data_std=data[feature].std()
    return data_std

