from uk_covid19 import Cov19API

from django.core.cache import cache
from uk_covid19.api_interface import StructureType

def GetUKData(area_name):

    area = [
        "areaType=utla",
        f"areaName={area_name}",
    ]

    cases: StructureType = {
        "date": "date",
        "areaName": "areaName",
        "newCasesBySpecimenDate": "newCasesBySpecimenDate",
        "cumCasesBySpecimenDate": "cumCasesBySpecimenDate",
        "cumCasesBySpecimenDateRate": "cumCasesBySpecimenDateRate",
    }

    api = Cov19API(
        filters=area,
        structure=cases,
    )

    df = cache.get_or_set(area_name, api.get_dataframe(), 5 * 60)

    df = df[::-1]

    return df

