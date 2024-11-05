from sqlalchemy import select

from fm_fastapi.models import User


def test_create_user(session):
    user = User(username='Felipe', email='felipe@teste.com', password='pass')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'felipe@teste.com'))

    assert result.username == 'Felipe'
