from fastapi import APIRouter
from schemas.user import User
from fastapi import HTTPException, status

router = APIRouter(prefix='/democrud')


@router.post('/')
def create_user(user: User):
    with open('users.csv', 'a+') as file:
        file.write(str(user))



@router.get('/')
def get_all_users():
    pass


@router.put('/')
def edit_user():
    pass


@router.delete('/')
def remove_user():
    if True:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='You have no access to perform this action'
        )
