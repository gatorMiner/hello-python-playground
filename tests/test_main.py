from playground.main import hello


def test_hello_default():
    assert hello() == "Hello, World!"


def test_hello_name():
    assert hello("Alice") == "Hello, Alice!"


def test_empty_name_returns_world():
    assert hello("") == "Hello, World!"
