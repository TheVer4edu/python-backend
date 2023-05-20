from fastapi import APIRouter

router = APIRouter(prefix='/math')


@router.get("/sum")
def sum(a: int, b: int):
    """Этот эдпоинт для сложения двух чисел"""
    return a + b


@router.get("/sub")
def sub(a: int, b: int):
    """Этот эндпоинт для разности двух чисел"""
    return a - b


@router.get("/mul")
def mul(a: int, b: int):
    """Этот эндпоинт для умножения двух чисел"""
    return a * b


@router.get("/div")
def div(a: int, b: int):
    """Этот эндпоинт для деления двух чисел"""
    return a / b
