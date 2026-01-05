import asyncio
from pathlib import Path
import subprocess

import typer

from app.core.container import Container
from app.shared.domain.services.database.i_sqlite_database_service import ISQLiteDatabaseService

cli = typer.Typer(help="CLI for managing the Store API application.")


@cli.command()
def dev() -> None:
    """
    Run the FastAPI application in development mode with auto-reload.
    """

    subprocess.run(["fastapi", "run", "app/main.py"], check=True)


@cli.command()
def start() -> None:
    """
    Start the FastAPI application using Uvicorn for production.
    """

    subprocess.run(
        [
            "uvicorn",
            "app.main:app",
            "--reload",
        ],
        check=True,
    )


@cli.command()
def prepare_db() -> None:
    """
    Initialize the database by creating all necessary tables.
    """

    async def _run() -> None:
        DATABASE_PATH: Path = Path(__file__).parent.parent / "db" / "store_api.db"
        DATABASE_URL: str = f"sqlite+aiosqlite:///{DATABASE_PATH}"

        # Initialize the dependency injection container
        container = Container()
        container.config.database.url.from_value(DATABASE_URL)
        container.config.database.echo.from_value(True)
        container.wire(packages=["app.modules"])

        db: ISQLiteDatabaseService = container.db()
        await db.init_models()
        await db.dispose()

        typer.echo("Database initialized successfully.")
        typer.echo(f"Database path: {DATABASE_PATH}")

    asyncio.run(_run())


if __name__ == "__main__":
    cli()
