import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info = {
        "name": "Meu nome",
        "email": "isaquenovo127@gmail.com",
        "evento_id": 2
    }
    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select_subscriber():
    email = "isaquenovo127@gmail.com"
    evento_id = 2

    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email, evento_id)
    print(resp.nome)

@pytest.mark.skip("Select in DB")
def test_ranking():
    evento_id = 2
    subs_repo = SubscribersRepository()
    resp = subs_repo.get_ranking(evento_id)
    print()

    for elem in resp:
        print(f"Link: {elem.link}, total de inscritos: {elem.total}")