from httpx import AsyncClient
from sqlalchemy import insert, select

from auth.models import role
from conftest import async_session_maker


async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(role).values(id=1, name='admin', permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(role)
        result = await session.execute(query)

        assert result.all() == [(1, 'admin', None)], "Роль не добавилась"


async def test_register(ac: AsyncClient):
    response = await ac.post("/auth/register", json={
        "email": "string",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string",
        "role_id": 1
    })

    assert response.status_code == 201


async def test_login(ac: AsyncClient):
    response = await ac.post('/auth/jwt/login', data={
        "username": "string",
        "password": "string",
    })

    print(response.text)

    assert response.status_code == 204

