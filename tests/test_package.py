"""Initial project setup smoke tests."""


def test_package_import() -> None:
    import quant_lab

    assert quant_lab.__version__ == "0.1.0"
