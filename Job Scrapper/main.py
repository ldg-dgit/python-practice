from extractors.we_work_remotely import extract_jobs_wwr
from extractors.indeed import extract_jobs_indeed

keyword = input("What do you want to search for?")

indeed = extract_jobs_indeed(keyword)
wwr = extract_jobs_wwr(keyword)

jobs = indeed + wwr

for job in jobs:
    print(job)
    print("////////////////////")
