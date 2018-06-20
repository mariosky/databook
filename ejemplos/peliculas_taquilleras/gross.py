from bs4 import BeautifulSoup

import requests
import time

def get_movie_budgets( page_index):
    r = requests.get('https://www.the-numbers.com/movie/budgets/all/%s'% (page_index,))

    html_doc = r.content

    soup = BeautifulSoup(html_doc, 'html.parser')
    rows = [tr for tr in soup.find_all('tr') if len(tr) == 13 ]


    return [(row.contents[4].a.string.encode('utf-8').strip(), row.contents[6].string.encode('utf-8').strip(), row.contents[10].string.encode('utf-8').strip()) for row in rows]


def write_movie_data( filename="gross.dat",  max_page=120):
    page_index_list = [(100*i)+1 for i in range(max_page)]
    for index in  page_index_list:
        time.sleep(4)
        movies = get_movie_budgets( str(index))
        file = open(filename,'a')
        for m in movies:
            file.write('{}|{}|{}\n'.format(*m))
        file.close()


if __name__ == '__main__':
    write_movie_data()

