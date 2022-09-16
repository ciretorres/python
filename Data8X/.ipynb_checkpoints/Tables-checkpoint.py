# Don't change this cell
from datascience import *
#%matplotlib inline

school = Table.read_table('db/school.csv')
# school

top_1970_with_2009 = school.select('Row Labels', '1970', '2009').sort('1970', descending=True)
print(top_1970_with_2009)

#top_1970_with_2009.barh('Row Labels')