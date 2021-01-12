import requests
from bs4 import BeautifulSoup
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')
results = soup.find(id='ResultsContainer')
print(results.prettify())
job_elems = results.find_all('section', class_='card_content')
for job_elem in job_elems:
  print(job_elem, end= '/n'*2)
  title_elem = job_elem.find('h2', class_='title')
company_elem = job_elem.find('div', class_='company')
location_elem = job_elem.find('div', class_='location')
print(title_elem)
print(company_elem)
print(location_elem)
print()
if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
python_jobs = results.find_all('h2', string='Python Developer')