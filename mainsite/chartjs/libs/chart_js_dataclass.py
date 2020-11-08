from dataclasses import dataclass, field
import json

def initialise_dataset():
    dataset_dict                   = {}
    dataset_dict['type']           = 'bar'
    dataset_dict['label']          = 'Dataset'
    dataset_dict['data']           = []
    dataset_dict['borderColor']    = 'dodgerblue'
    dataset_dict['borderWidth']    = 1
    dataset_dict['fill']           = False
    dataset_dict['pointRadius']    = 0
    dataset_dict['pointHitRadius'] = 5

    return dataset_dict

@dataclass
class Dataset:
    dataset_dict : dict = field(default_factory=initialise_dataset)

    def AddDataset(self, name, data, type, colour = 'dodgerblue'):
        self.dataset_dict['label'] = name
        self.dataset_dict['data'] = data
        self.dataset_dict['type'] = type
        self.dataset_dict['borderColor'] = colour
        self.dataset_dict['backgroundColor'] = colour

def initialise_axis():
    axis_dict            = {}
    axis_dict['display'] = True
    axis_dict['type']    = 'linear'

    return axis_dict

@dataclass
class Axis:
    axis_dict : dict = field(default_factory=initialise_axis)

def initialise_chart():
    chartjs_dict                                   = {}

    chartjs_dict['type']                           = 'bar'

    chartjs_dict['data']                           = {}
    chartjs_dict['data']['labels']                 = []
    chartjs_dict['data']['datasets']               = []

    chartjs_dict['options']                        = {}
    chartjs_dict['options']['scales']              = {}
    chartjs_dict['options']['scales']['xAxes']     = []
    chartjs_dict['options']['scales']['yAxes']     = []
    chartjs_dict['options']['responsive']          = True
    chartjs_dict['options']['maintainAspectRatio'] = False
    chartjs_dict['options']['legend']              = {}
    chartjs_dict['options']['legend']['display']   = False
    chartjs_dict['options']['title']               = {}
    chartjs_dict['options']['title']['text']       = 'Title'
    chartjs_dict['options']['title']['display']    = True
    chartjs_dict['options']['title']['fontSize']   = 20
    chartjs_dict['options']['title']['fontStyle']  = ''

    return chartjs_dict

@dataclass
class ChartJS:
    chartjs_dict : dict = field(default_factory=initialise_chart)

    def SetLabel(self, text):
        self.chartjs_dict['options']['title']['text'] = text

    def AddDataset(self, name, data, type, colour = 'dodgerblue'):
        dataset = Dataset()
        dataset.AddDataset(name, data, type, colour)
        self.chartjs_dict['data']['datasets'].append(dataset.dataset_dict)

    def SetCategories(self, categories):
        self.chartjs_dict['data']['labels'] = categories

    def SetxAxis(self, type):
        axis = Axis()
        axis_dict = axis.axis_dict
        axis_dict['type'] = type

        self.chartjs_dict['options']['scales']['xAxes'].append(axis_dict)

    def SetyAxis(self, type):
        axis = Axis()
        axis_dict = axis.axis_dict
        axis_dict['type'] = type

        self.chartjs_dict['options']['scales']['yAxes'].append(axis_dict)

    def __str__(self) -> str:
        return f'{self.chartjs_dict}'

    def to_json(self):
        return json.dumps(self.chartjs_dict)

    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(self.__str__())
