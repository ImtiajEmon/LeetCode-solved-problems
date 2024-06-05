import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    mask = ((products["low_fats"] == "Y") & (products["recyclable"] == "Y"))
    #return pd.DataFrame(products[mask]["product_id"])
    return products[mask][["product_id"]]
