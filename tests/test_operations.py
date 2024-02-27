from httpx import AsyncClient


async def test_get_operations(ac: AsyncClient):
    response = await ac.post("/operations", json={
        "id": 1,
        "quantity": "25.5",
        "figi": "figi_CODE",
        "instrument_type": "bond",
        "date": "2023-02-01T00:00:01",
        "type": "Выплата купонов",
    })

    assert response.status_code == 200

    response = await ac.post("/operations", json={
        "id": 2,
        "quantity": "25.5",
        "figi": "figi_CODE",
        "instrument_type": "bond",
        "date": "2023-02-01T00:00:02",
        "type": "Выплата купонов",
    })

    assert response.status_code == 200

    response = await ac.post("/operations", json={
        "id": 3,
        "quantity": "25.5",
        "figi": "figi_CODE",
        "instrument_type": "bond",
        "date": "2023-02-01T00:00:03",
        "type": "Выплата купонов",
    })

    assert response.status_code == 200

    finally_response = await ac.get('/operations', params={'operation_type': "Выплата купонов"})

    assert finally_response.status_code == 200
    assert len(finally_response.json()["data"]) == 3


async def test_add_specific_operations(ac: AsyncClient):
    response = await ac.post("/operations", json={
        "id": 4,
        "quantity": "25.5",
        "figi": "figi_CODE",
        "instrument_type": "bond",
        "date": "2023-02-01T00:00:00",
        "type": "Выплата купонов",
    })

    assert response.status_code == 200


