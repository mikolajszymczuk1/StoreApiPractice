import asyncio
from pathlib import Path
import subprocess

import typer

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
        db_path: Path = Path(__file__).parent.parent / "db" / "store_api.db"
        db_path.parent.mkdir(parents=True, exist_ok=True)
        db_path.touch(exist_ok=True)

        typer.echo("Created database successfully.")
        typer.echo(f"Database path: {db_path}")

    asyncio.run(_run())


@cli.command()
def migrate() -> None:
    """
    Run all Alembic migrations to update the database schema.
    """

    subprocess.run(["alembic", "upgrade", "head"], check=True)
    typer.echo("✅ Project ready (DB migrated)")


if __name__ == "__main__":
    cli()
