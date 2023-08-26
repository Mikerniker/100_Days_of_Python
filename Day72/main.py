from bs4 import BeautifulSoup
import requests
import csv

start_url = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"


def get_majors(soup):
    all_majors = []
    salary_table = soup.find("table", attrs={"class": "data-table"})
    salary_table_data = salary_table.tbody.find_all("tr")
    for item in salary_table_data:
        all_data = item.find_all("td")
        new_list = [a.getText().split(":") for a in all_data]
        majors = {major[0]: major[1] for major in new_list}
        all_majors.append(majors)
    return all_majors

final_majors = []
for page in range(1, 35):
    link = f'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page}'
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    final_majors.append(get_majors(soup))


headers = ["Rank", "Major", "Degree Type", "Early Career Pay", "Mid-Career Pay", "% High Meaning"]

with open("salaries2023.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    for major in final_majors:
        writer.writerows(major)
