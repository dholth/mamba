import libmambapy


def test_version():
    ver_str = "1.0"
    ver = libmambapy.bindings.Version.parse(ver_str)
    assert str(ver) == ver_str
