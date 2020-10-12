from dataclasses import dataclass, field
import json
import copy

def initialise_series():
    series_dict = {}
    series_dict['name'] = 'Series'
    series_dict['type'] = 'line'
    series_dict['data'] = []

    return series_dict

@dataclass
class Series:
    series_dict : dict = field(default_factory=initialise_series)

def initialise_options():
    options_dict = {}

    options_dict['chart']                       = {}
    options_dict['chart']['panning']            = {}
    options_dict['chart']['panning']['enabled'] = True
    options_dict['chart']['panning']['type']    = 'xy'
    options_dict['chart']['zoomType']           = 'xy'
    options_dict['chart']['panKey']             = 'shift'

    options_dict['title']         = {}
    options_dict['title']['text'] = 'My Chart'

    options_dict['series'] = []

    options_dict['xAxis']                  = {}
    options_dict['xAxis']['type']          = 'linear'
    options_dict['xAxis']['title']         = {}
    options_dict['xAxis']['title']['text'] = 'x-axis title'

    options_dict['yAxis']                  = {}
    options_dict['yAxis']['type']          = 'linear'
    options_dict['yAxis']['title']         = {}
    options_dict['yAxis']['title']['text'] = 'y-axis title'

    options_dict['legend']           = {}
    options_dict['legend']['layout'] = 'horizontal'
    
    options_dict['tooltip']                    = {}
    options_dict['tooltip']['followTouchMove'] = False

    return options_dict

@dataclass
class Options:
    options_dict : dict = field(default_factory=initialise_options)

    def SetTitle(self, text):
        self.options_dict['title']['text'] = text

    def SetxAxisTitle(self, title):
        self.options_dict['xAxis']['title']['text'] = title

    def SetxAxisType(self, type):
        self.options_dict['xAxis']['type'] = type

    def SetyAxisTitle(self, title):
        self.options_dict['yAxis']['title']['text'] = title

    def SetyAxisType(self, type):
        self.options_dict['yAxis']['type'] = type

    def ClearSeries(self):
        self.options_dict['series'].clear()

    def AddSeries(self, name, type, data):
        series = Series()
        series_dict = series.series_dict
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
