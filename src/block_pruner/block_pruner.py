from pathlib import Path


class BlockPruner:
    def __init__(self, start: bytes, end: bytes, needle: bytes) -> None:
        self.start = start
        self.end = end
        self.needle = needle

        self._temp: list[bytes] = []
        self._save: list[bytes] = []

        self._keep_block = True
        self._inside_block = False

    def prune_file(self, input_file: Path) -> bytes:
        with open(input_file, "rb") as input_fp:
            for line in input_fp:
                self._feed_line(line=line)
        return b"".join(self._save)

    def _feed_line(self, line: bytes) -> None:
        if line == self.start:
            self._inside_block = True
        if self._inside_block:
            self._temp.append(line)
            if line == self.needle:
                self._keep_block = False
        else:
            self._save.append(line)

        if line == self.end:
            self._keep_or_disregard_block()

    def _keep_or_disregard_block(self) -> None:
        if self._keep_block:
            self._save.extend(self._temp)
        self._temp = []
        self._keep_block = True
        self._inside_block = False
