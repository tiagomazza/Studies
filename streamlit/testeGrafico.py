import pandas as pd

df = pd.read_excel(
    io="mes.xlsx",
    engine="openpyxl",
    sheet_name= "Sheet1",
    skiprows=0,
    usecols="A:F",
    nrows=8000
)
