#Import our dependency Pandas
import pandas as pd

#Modify the query string and the filename as needed
query = input('enter the query:  ')
file_name = 'patents_'+query+'.csv'

#Functions to Scrape 
def create_url(query):
    try:
        query_list = query.split(' ')
    except:
        query_list = query
    
    if len(query_list) == 1:
        url = 'https://patents.google.com/xhr/query?url=q%3D' + query + '%26after%3D20101231&exp=&download=true'
        return url
    else:
        url_temp = 'https://patents.google.com/xhr/query?url=q%3D' + query_list[0]
        for i in range(1, len(query_list)):
            url_append = '%2B' + query_list[i]
            url_temp += url_append
        url = url_temp +  '%26after%3D20101231&exp=&download=true'
        return url

def main_loop(query, file_name):
    url = create_url(query)
    
    try:
        data = pd.read_csv(url, sep = ',', skiprows = 1)
        data.to_csv(file_name)
    except:
        print('Cannot Scrape! Try again later.')        


#Perform the scraping
print('Scraping!')
main_loop(query, file_name)