# needs to convert to csv
from craigslist import CraigslistForSale
import pandas as pd
df = pd.DataFrame

cl_c = CraigslistForSale(site='orlando',category='cto',filters={'max_price':10000})
for results in cl_c.get_results(sort_by='newest'):
	print(results)