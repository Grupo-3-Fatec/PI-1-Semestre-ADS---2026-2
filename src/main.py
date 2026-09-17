import pandas
import os

df = pandas.read_csv(
    # os.path.join(os.getcwd(), 'data', 'data.csv'),
    'data/data.csv',
    delimiter=';'
)
