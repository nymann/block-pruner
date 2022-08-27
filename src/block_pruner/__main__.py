import os
from pathlib import Path
import sys

from typer import Option
from typer import Typer

from block_pruner.block_pruner import BlockPruner

app = Typer()
Required = Option(...)


@app.command()
def main(
    input_files: list[Path],
    start: str = Required,
    end: str = Required,
    needle: str = Required,
):
    for input_file in input_files:
        bp = BlockPruner(
            start=start,
            end=end,
            needle=needle,
        )
        output = bp.prune_file(input_file=input_file)
        with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
            stdout.write(output)
            stdout.flush()


if __name__ == "__main__":
    app()
