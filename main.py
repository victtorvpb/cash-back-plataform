from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from resources.api_v1.api import api_router
from commons.config import settings
from schemas.common import Message

origins = [
    "http://localhost",
    "http://localhost:8080",
]


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get('/its-alive', response_model=Message)
    async def its_alive():
        return {'status': 'its_alive'}

    app.include_router(api_router, prefix=settings.API_V1_STR)
    return app


app = create_app()
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'main:app',
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG,
        reload=settings.DEBUG,
    )
