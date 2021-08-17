import pybithumb
import openpyxl
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pybithumb.get_ohlcv("BTC")
df.to_excel("btc.xlsx")

"""
class actions:
    def __init__(self, m):
        self.m = m
        self.mean = 0
        self.N = 0

class policy:
    pass

class agent:
    def __init__(self):

def D(i):
    df[i]


def loss(w):
    


if __name__ == '__main__':
"""