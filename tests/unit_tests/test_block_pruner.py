from pathlib import Path

import pytest

from block_pruner import BlockPruner


class TestCase:
    __test__ = False

    def __init__(
        self,
        start: bytes,
        end: bytes,
        needle: bytes,
        expected_fname: str,
        input_fname: str,
    ) -> None:
        self.start = start
        self.end = end
        self.needle = needle
        self.expected_file = Path(f"tests/data/{expected_fname}")
        self.input_file = Path(f"tests/data/{input_fname}")

    def actual_matches_expected(self, compare: bytes) -> bool:
        with open(file=self.expected_file, mode="rb") as expected_fp:
            return expected_fp.read() == compare


test_cases = [
    TestCase(
        start=b"start\n",
        end=b"end\n",
        needle=b"615\n",
        expected_fname="simple-expected-output.txt",
        input_fname="simple-input.txt",
    ),
]


@pytest.mark.parametrize("test_case", test_cases)
def test_prune(test_case: TestCase) -> None:
    pruner = BlockPruner(start=test_case.start, end=test_case.end, needle=test_case.needle)
    actual: bytes = pruner.prune_file(input_file=test_case.input_file)
    assert test_case.actual_matches_expected(actual)
