from pathlib import Path
import random

import pandas as pd
from requests.adapters import RetryError

# Function to return a random colour
def random_colour():
    return tuple([random.randrange(255), random.randrange(255), random.randrange(255)])

class CovidData():

    def __init__(self):
        # Initialise a random seed so we get the same colours every time
        random.seed(0)

        # Set the data folder
        data_folder = 'pickles'

        p = Path(data_folder)

        if p.exists() and p.is_dir():
            # List all files in the data folder
            self.file_list = sorted(list(p.glob('*.pickle')))

            global_path = Path('pickles/global.pickle')

            if global_path in self.file_list:
                self.file_list.remove(global_path)

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
