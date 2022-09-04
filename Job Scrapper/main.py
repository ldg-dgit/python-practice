from extractors.we_work_remotely import extract_jobs_wwr
from extractors.indeed import extract_jobs_indeed

keyword = input("What do you want to search for?")

wwr = extract_jobs_wwr(keyword)
indeed = extract_jobs_indeed(keyword)

jobs = indeed + wwr

file = open(f"Job Scrapper/export_data/{keyword}_job_scrap.csv", "w")

file.write('Position,Company,Location,URL\n')

for job in jobs:
    file.write(
        f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()
