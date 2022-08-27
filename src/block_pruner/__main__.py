import os
from pathlib import Path
import sys

from block_pruner.block_pruner import BlockPruner


def main():
    for arg in sys.argv[1:]:
        bp = BlockPruner(
            start=b"start\n",
            end=b"end\n",
            needle=b"615\n",
        )
        output = bp.prune_file(Path(arg))
        with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
            stdout.write(output)
            stdout.flush()


if __name__ == "__main__":
    main()
