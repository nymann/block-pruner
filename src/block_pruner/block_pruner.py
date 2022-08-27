from pathlib import Path


class BlockPruner:
    def __init__(self, start: str, end: str, needle: str) -> None:
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
                self._feed_line(raw_line=line)
        return b"".join(self._save)

    def _feed_line(self, raw_line: bytes) -> None:
        line = utf8_or_empty(raw_line).strip("\n")
        if line == self.start:
            self._inside_block = True
        if self._inside_block:
            self._temp.append(raw_line)
            if line == self.needle:
                self._keep_block = False
        else:
            self._save.append(raw_line)

        if line == self.end:
            self._keep_or_disregard_block()

    def _keep_or_disregard_block(self) -> None:
        if self._keep_block:
            self._save.extend(self._temp)
        self._temp = []
        self._keep_block = True
        self._inside_block = False


def utf8_or_empty(line: bytes) -> str:
    try:
        return line.decode()
    except UnicodeDecodeError:
        return ""
