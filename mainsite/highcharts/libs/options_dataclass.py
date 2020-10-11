from dataclasses import dataclass
import json
import copy

@dataclass
class Series:
    series_dict = {}
    series_dict['name'] = 'Series'
    series_dict['type'] = 'line'
    series_dict['data'] = []

@dataclass
class Options:
    options_dict = {}

    options_dict['title']         = {}
    options_dict['title']['text'] = 'My Chart'

    options_dict['series'] = []

    options_dict['xAxis']                  = {}
    options_dict['xAxis']['title']         = {}
    options_dict['xAxis']['title']['text'] = 'x-axis title'

    options_dict['yAxis']                  = {}
    options_dict['yAxis']['title']         = {}
    options_dict['yAxis']['title']['text'] = 'y-axis title'

    options_dict['legend'] = {}
    options_dict['legend']['layout']        = 'horizontal'

    def SetTitle(self, text):
        self.options_dict['title']['text'] = text

    def SetxAxisTitle(self, title):
        self.options_dict['xAxis']['title']['text'] = title

    def SetyAxisTitle(self, title):
        self.options_dict['yAxis']['title']['text'] = title

    def ClearSeries(self):
        self.options_dict['series'].clear()

    def AddSeries(self, name, type, data):
        series_dict = Series().series_dict
        series_dict['name'] = name
        series_dict['type'] = type
        series_dict['data'] = data
        self.options_dict['series'].append(copy.deepcopy(series_dict))

    def SetCategories(self, categories):
        self.options_dict['xAxis']['categories'] = categories

    def __str__(self) -> str:
        return f'{self.options_dict}'

    def to_json(self):
        return json.dumps(self.options_dict)

    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(self.__str__())
