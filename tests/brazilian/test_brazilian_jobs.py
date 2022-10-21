from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    assert read_brazilian_file(
       [{"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"}]
    ) == [{"title": "Maquinista", "salary": "2000", "type": "trainee"}]
