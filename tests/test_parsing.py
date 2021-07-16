"""Testing parsing utilities."""

from pylsmod import parsing


LSMOD_EMPTY = """\
Module                  Size  Used by
"""


def test_parse_lsmod_nomodules():
    """Should return empty graph on empty input."""
    assert parsing.parse_lsmod(LSMOD_EMPTY) == {}


LSMOD_SAMPLE = """\
Module                  Size  Used by
aaaaaa                  1000  0
bbbbbb                  2000  1 aaaaaa
cccccc                  2500  2 bbbbbb,aaaaaa
dddddd                  5000  1 eeeeee
eeeeee                  1500  0
"""


def test_parse_lsmod_sample():
    """Should return valid directed graph."""
    assert parsing.parse_lsmod(LSMOD_SAMPLE) == {
        "aaaaaa": {"cccccc", "bbbbbb"},
        "bbbbbb": {"cccccc"},
        "cccccc": set(),
        "dddddd": set(),
        "eeeeee": {"dddddd"},
    }


def test_parse_proc_modules_nomodules():
    """Should return empty graph on empty input."""
    assert parsing.parse_proc_modules("") == {}


PROC_MODULES_SAMPLE = """\
aaaaaa 1000 0 - Live 0x0000000000000000
bbbbbb 2000 1 aaaaaa, Live 0x0000000000000000
cccccc 2500 2 bbbbbb,aaaaaa, Live 0x0000000000000000
dddddd 5000 1 eeeeee, Live 0x0000000000000000
eeeeee 1500 0 - Live 0x0000000000000000
"""


def test_parse_proc_modules_sample():
    """Should return valid directed graph."""
    assert parsing.parse_proc_modules(PROC_MODULES_SAMPLE) == {
        "aaaaaa": {"cccccc", "bbbbbb"},
        "bbbbbb": {"cccccc"},
        "cccccc": set(),
        "dddddd": set(),
        "eeeeee": {"dddddd"},
    }


PROC_MODULES_TRAILING = """\
aaaaaa 1000 0 - Live 0x0000000000000000
bbbbbb 2000 1 aaaaaa, Live 0x0000000000000000 (OE)
cccccc 2500 2 bbbbbb,aaaaaa, Live 0x0000000000000000 (POE)
dddddd 5000 1 eeeeee, Live 0x0000000000000000
eeeeee 1500 0 - Live 0x0000000000000000
"""


def test_parse_proc_modules_sample_trailing():
    """Should ignore /proc/modules trailing flags."""
    assert parsing.parse_proc_modules(PROC_MODULES_TRAILING) == {
        "aaaaaa": {"cccccc", "bbbbbb"},
        "bbbbbb": {"cccccc"},
        "cccccc": set(),
        "dddddd": set(),
        "eeeeee": {"dddddd"},
    }
