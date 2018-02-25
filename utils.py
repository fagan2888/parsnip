import numpy as np
import math


def raise_power(elt, exponent):
    return math.pow(elt, exponent)


raise_power_v = np.vectorize(raise_power)


def logistic(xb):
    return np.exp(xb) / (1 + np.exp(xb))


def odds(arr):
    num_ones = np.sum(arr)
    numerator = num_ones / arr.size
    denominator = (arr.size - num_ones) / arr.size
    if denominator == 0:
        return np.Inf
    return numerator / denominator


def log_odds(arr):
    arr_odds = odds(arr)
    if arr_odds == 0:
        return -np.Inf
    return math.log(arr_odds)


def initList(size):
    return [None] * size


def infer_variable_type(series):
    if series.dtype == "object":
        return "multinomial"
    elif series.value_counts().size == 2:
        return "binary"
    return "continous"
