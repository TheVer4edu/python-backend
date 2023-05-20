import uvicorn
from fastapi import FastAPI
from endpoints.root import router as root_router
from endpoints.math import router as math_router
from endpoints.test_crud import router as crud_router

app = FastAPI()
app.include_router(root_router, tags=['Main page'])
app.include_router(math_router, tags=['Mathematics'])
app.include_router(crud_router, tags=['Demo Crud'])


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=False
    )