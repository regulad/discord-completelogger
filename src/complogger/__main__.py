"""CLI for CompleteLogger - Log deleted messages.

Copyright (C) 2024  Parker Wahle

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""  # noqa: E501, B950

from __future__ import annotations

import json
from base64 import b64decode
from binascii import Error
from logging import INFO
from logging import Formatter
from logging import getLogger
from logging.handlers import QueueHandler, QueueListener
from logging.handlers import RotatingFileHandler
from os import environ
from pathlib import Path
from queue import Queue

import typer
from discord import Status
from dotenv import load_dotenv
from rich.logging import RichHandler

from ._assets import RESOURCES
from .client import SocialLoggerClient


cli = typer.Typer()


def try_force_decode_jwt(jwt_segment: str) -> str:
    try:
        return b64decode(jwt_segment).decode("utf-8")
    except Error:
        # don't eat the recursion error, look for it
        return try_force_decode_jwt(jwt_segment + "=")

@cli.command()
def main() -> None:
    load_dotenv()

    logs_dir = Path("logs")

    if not logs_dir.exists():
        logs_dir.mkdir()

    root_logger = getLogger()
    root_logger.setLevel(INFO)

    rich_handler = RichHandler()
    file_handler = RotatingFileHandler(
        logs_dir / "complogger.log", maxBytes=1000000, backupCount=5, encoding="utf-8"
    )
    timestamp_formatter = Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(timestamp_formatter)

    queue = Queue()
    queue_listener = QueueListener(queue, rich_handler, file_handler)

    queue_listener.start()
    root_logger.addHandler(QueueHandler(queue))  # avoid blocking the main thread w/ the asyncio loop

    tokens = environ["DISCORD_TOKEN"]
    for token in tokens.split(","):  # currently unused, have to do the async code for each
        user_id = try_force_decode_jwt(token.split(".")[0])

        client_logger = getLogger(user_id)
        client = SocialLoggerClient(client_logger, status=Status.offline)

        try:
            client.run(token, log_handler=None)
        finally:
            queue_listener.stop()


if __name__ == "__main__":  # pragma: no cover
    cli()

__all__ = ("cli",)
