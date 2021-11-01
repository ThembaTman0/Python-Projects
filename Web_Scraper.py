### IMPORT LIBRARIES ###
from bs4 import BeautifulSoup
import requests
import pandas as pd
# ---------------STEP 1:SENDING A HTTP REQUEST TO A URL----------------
### URL ### 

# url="https://www.nfl.com/standings/league/2020/REG"
url="https://www.worldometers.info/coronavirus/"
### MAKE A GET REQUEST TO FETCH THE RAW HTML CONTENT `###

html_content=requests.get(url)

# ------------------STEP 2:PRASE THE HTML CONTENT-----------------------

soup=BeautifulSoup(html_content.text,"lxml")

### CHECKING IF CODE GETS HTML CONTENT NB.COMMENT ME OUT MESSY OUTPUT### 
# Print the parsed data of html
print(soup.prettify())
# Print title

print('\n The page title is: \n',soup.title.text)



# ------------------STEP 3:ANALYZE THE HTML CONTENT-----------------------
### Create a data dictionary to store data ### 
# GET TABLE CONTENT

table=soup.find('table',{'id':'main_table_countries_today'})


# GET ALL THE HEADINGS OF LISTS
# NB. th is headers for a table
headers=[]
for i in table.find_all('th'):
    # Remove any newlines and extra spaces from left to right
    # Get hearders for the table and use .strip() to remove all white space or space bar/tabs
    title=i.text.strip()
    headers.append(title)

print('\n HEADER OF THE TABLE \n',headers)

# CREATE A DATA FRAME WITH THE HEADERS
df=pd.DataFrame(columns=headers)
# Get the data within the table
for row in table.find_all('tr')[1:]:
    data=row.find_all('td')
    row_data=[td.text.strip() for td in data]
    lenght=len(df)
    df.loc[lenght]=row_data

# print('\n ALL DATA FROM THE TABLE \n ',df)
# ------------------STEP 4:DISPLAY AND SAVE THE TABLE-----------------------
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df)

# import csv
# with open('output.csv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     for row in df.items():
#         csvwriter.writerow(row)