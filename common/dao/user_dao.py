from ..models.users import Users
from ..utils.db_helper import get_session

class UserDao():

    def __init__(self):
        self._session = get_session()
        pass
    
    def insert_one(self, user: Users) -> None:
        try:
            self._session.add(user)
        except Exception as e:
            self._session.rollback()
            raise e
        self._session.commit()

    def update_one_by_id(self, user_id: int, user: Users) -> None:
        try:
            self._session.query(Users).filter_by(id=user_id).update(user)
        except Exception as e:
            self._session.rollback()
            raise e
        self._session.commit()
    
    def delete_one_by_id(self, user_id: int) -> None:
        try:
            self._session.query(Users).filter_by(id=user_id).delete()
        except Exception as e:
            self._session.rollback()
            raise e
        self._session.commit()

    def query_all_users(self, condition: dict) -> dict:
        try:
            self._session.query(Users).filter_by(condition).all()
        except Exception as e:
            self._session.rollback()
            raise e
        self._session.commit()
