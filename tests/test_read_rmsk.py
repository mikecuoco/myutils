import pytest

from myutils.rmsk import read_rmsk


def read(file):
    df = read_rmsk(file)
    assert "length" in df.columns, "length column not found"
    assert "age" in df.columns, "age column not found"


def test_ucsc_rmsk():
    with pytest.raises(AssertionError) as e:
        df = read_rmsk("tests/rmsk.ucsc.txt")


def test_read_rmsk():
    read("tests/rmsk.out")


def test_read_rmsk_gz():
    read("tests/rmsk.out.gz")


def test_read_rmsk_astrk():
    read("tests/rmsk_astrk.out")


def test_read_rmsk_url():
    # use fruit fly as a test case
    read("https://hgdownload.soe.ucsc.edu/goldenPath/dm6/bigZips/dm6.fa.out.gz")
