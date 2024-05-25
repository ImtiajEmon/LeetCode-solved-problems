import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pt = weather.pivot(index = 'month', columns = 'city', values = 'temperature')
    return pt
