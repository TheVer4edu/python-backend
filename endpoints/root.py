from fastapi import APIRouter

router = APIRouter()

students = [
    'Stepan',
    'Eugene',
    'George',
    'Anatoly',
    'Alex'
]


@router.get("/")
def root_dir(mask: str):
    return [student.find(mask) for student in students]
