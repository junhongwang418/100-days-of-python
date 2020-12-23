import os
import sys
import csv
import pandas

data = pandas.read_csv(os.path.join(
    sys.path[0], '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'))

data.groupby("Primary Fur Color").size().to_csv(
    os.path.join(sys.path[0], "squirrel_count.csv"))
