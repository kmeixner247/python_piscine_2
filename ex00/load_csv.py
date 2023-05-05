import pandas

def load(path: str) -> pandas.core.frame.DataFrame:
    """load(path: str)

Lodas and returns a csv file"""
    try:
        assert type(path) is str, "argument must be a string"
        csv = pandas.read_csv(path)
    except FileNotFoundError:
        print("load: FileNotFoundError: %s is not a valid path" % path)
        return None
    except AssertionError as msg:
        print("load: AssertionError:", msg)
        return None
    except pandas.errors.ParserError as msg:
        print("load: ParserError:", msg)
        return None
    except UnicodeDecodeError as msg:
        print("load: UnicodeDecodeError:", msg)
        return None
    except ValueError as msg:
        print("load: ValueError:", msg)
        return None
    except PermissionError as msg:
        print("load: PermissionError:", msg)
        return None
    except Exception as msg:
        print("load: Error:", msg)
        return None
    return csv
