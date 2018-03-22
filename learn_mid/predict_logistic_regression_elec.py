#!/usr/bin/python3

import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

path = os.getcwd() +os.sep + 'data' + os.sep + 'bankloan.csv'
data = pd.read_csv(path)
print(data)