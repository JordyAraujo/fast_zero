from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='test', email='teste@mail.com', password='test')
    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'teste@mail.com'))

    assert result.username == 'test'
