from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    uniques_types_of_jobs = set()
    for job in data:
        if job["job_type"] != "":
            uniques_types_of_jobs.add(job["job_type"])
    return uniques_types_of_jobs


def filter_by_job_type(jobs, job_type):
    filtered_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_job_type.append(job)
    return filtered_job_type


def get_unique_industries(path):
    data = read(path)
    unique_industries = set()
    for industry in data:
        if industry["industry"] != "":
            unique_industries.add(industry["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    filtered_job_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_job_industry.append(job)
    return filtered_job_industry


def get_max_salary(path):
    data = read(path)
    max_salaries = set()
    for salary in data:
        if salary["max_salary"] != "":
            try:
                max_salaries.add(int(salary["max_salary"]))
            except ValueError:
                print("Valor não encontrado")
    return max(max_salaries)


def get_min_salary(path):
    data = read(path)
    min_salaries = set()
    for salary in data:
        if salary["min_salary"] != "":
            try:
                min_salaries.add(int(salary["min_salary"]))
            except ValueError:
                print("Valor não encontrado")
    return min(min_salaries)


def matches_salary_range(job, salary):
    if type(salary) != int:
        raise ValueError("This is not a numeric value")
    elif ("min_salary" or "max_salary") not in job:
        raise ValueError("There is no salary in this range")
    elif (type(job["min_salary"]) or type(job["max_salary"])) != int:
        raise ValueError("This is not a numeric value")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError(
            "The minimum value cannot be greater than the maximum"
        )
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            print('Invalid data')
    return filtered_jobs
