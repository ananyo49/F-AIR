from scrape import *
import pandas as pd
result = Scrape("DXB", "ORD", "2023-09-18")
ScrapeObjects(result)
print(result.data["Airline(s)"])
print(result.data["Price ($)"])
print(result)