from fastapi import FastAPI

from app.bootstrap import create_app


def bootstrap() -> FastAPI:
    """
    Bootstrap the FastAPI application.
    Prepares the app instance for running.
    """

    app: FastAPI = create_app()

    return app


app: FastAPI = bootstrap()
