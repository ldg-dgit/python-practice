from flask import Flask

app = Flask("Job_Scrapper")


@app.route("/")
def home():
    return 'hey there!'


app.run()


# from extractors.we_work_remotely import extract_jobs_wwr
# from extractors.indeed import extract_jobs_indeed
# from file import save_to_file

# keyword = input("What do you want to search for?")
# wwr = extract_jobs_wwr(keyword)
# indeed = extract_jobs_indeed(keyword)
# jobs = indeed + wwr

# save_to_file(keyword, jobs)
