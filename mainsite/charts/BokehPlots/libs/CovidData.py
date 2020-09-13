import copy
from pathlib import Path
import random

import numpy as np
import pandas as pd

# Function to return a random colour
def random_colour():
    return tuple([random.randrange(255), random.randrange(255), random.randrange(255)])

class CovidData:

    def __init__(self):
        # Initialise a random seed so we get the same colours every time
        random.seed(0)

        # Set the data folder
        data_folder = 'pickles'

        p = Path(data_folder)

        if p.exists() and p.is_dir():
            # List all files in the data folder
            self.file_list = sorted(list(p.glob('*.pickle')))

            self.menu = list()
            self.df_dict = dict()
            self.colour_dict = dict()
            self.glyph_dict = dict()

            for file in self.file_list:
                country = str(file)[8:-7]
                self.menu.append(country)
                self.colour_dict[country] = random_colour()
                self.glyph_dict[country] = None

    def __iter__(self):
        self.iterator = iter(self.menu)
        return self.iterator

    def __next__(self):
        return next(self.iterator)

    def GetDataFrame(self, country):
        if country not in self.df_dict:
            self.df_dict[country] = pd.read_pickle('pickles/' + country + '.pickle')

        return self.df_dict[country]

    # Return the tail of a frame once the values in the requested column have got above a certain level
    def GetTail(self, country, index_label, column, threshold = 0):

        country_df = self.GetDataFrame(country)

        # Get the first index where the data is above the threshold
        first_index = np.argmax(country_df[column] > threshold)

        # Only tail if it's necessary, create a deep copy as we're adding a new column for the day count
        if first_index > 0:
            tailed_df = copy.deepcopy(country_df.tail(-first_index))
        else:
            tailed_df = copy.deepcopy(country_df)

        # Insert the Day Count column
        tailed_df[index_label] = np.arange(len(tailed_df))
        
        # Return the new Data Frame
        return tailed_df
