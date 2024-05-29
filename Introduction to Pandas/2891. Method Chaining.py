import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    mask = animals['weight'] > 100
    return pd.DataFrame(animals[mask].sort_values('weight', ascending = False)['name'])
