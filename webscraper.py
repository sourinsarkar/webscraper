from bs4 import BeautifulSoup
import requests
import time

print("Enter the skill you are not familiar with.")
unknown_skill = input("Enter here: ")
print(f"Filtering out {unknown_skill}")

def jobs_meta_data():
    url = ("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

        
    for index, job in enumerate (jobs):
        published = job.find('span', class_='sim-posted').text

        if 'few' in published:
            job_role = job.header.h2.a.find('strong', class_='blkclor').text.replace(' ','')
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            experience = job.ul.find('li').text
            skills = job.find('span', class_='srp-skills').text.replace(' ','')
            job_info = job.header.h2.a["href"]

            if unknown_skill not in skills:
                with open(f'metadata/{index}.txt', 'w') as file:
                    file.write(f"Role: {job_role.strip()}\n")
                    file.write(f"Company: {company_name.strip()}\n")                        
                    file.write(f"Experience: {experience[-9:]}\n")
                    file.write(f"Skills Required: {skills.strip()}\n")
                    file.write(f"Job Info: {job_info}")
                print(f"File saved: {index}")

if __name__ == '__main__':
    while True:
        jobs_meta_data()
        collecting_time = 5
        print(f"Waiting {collecting_time} minutes...")
        time.sleep(collecting_time * 60)