from src.sorting import sort_by

JOBS_SALARY = [
    {
        "min_salary": 25000,
        "max_salary": 50000,
        "date_posted": "2022-10-21",
    },
    {
        "min_salary": 5000,
        "max_salary": 10000,
        "date_posted": "2022-10-20",
    },
]


def test_sort_by_criteria():
    sort_by(JOBS_SALARY, "min_salary")
    assert JOBS_SALARY[0]["min_salary"] == 5000

    sort_by(JOBS_SALARY, "max_salary")
    assert JOBS_SALARY[0]["max_salary"] == 50000

    sort_by(JOBS_SALARY, "date_posted")
    assert JOBS_SALARY[0]["date_posted"] == "2022-10-21"
