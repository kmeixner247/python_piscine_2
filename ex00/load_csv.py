import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    """load(path: str)

Lodas and returns a csv file

Args:
    - path (str): the path of the file to be read

Returns:
    pd.core.frame.DataFrame: A pandas dataframe with the contents of the csv
    file.

Raises:
    - FileNotFoundError: If the provided path does not exist.
    - AssertionError: If the provided argument is not a string.
    - pd.errors.ParserError: If there is an error while parsing the csv file.
    - UnicodeDecodeError: If there is an error while decoding the csv file.
    - ValueError: If there is a problem with the provided argument or csv file.
    - PermissionError: If there is a problem with permissions for accessing the
                       csv file.
    - Exception: If there is an unexpected error while loading the csv file.
"""
    try:
        assert type(path) is str, "argument must be a string"
        csv = pd.read_csv(path)
    except FileNotFoundError:
        print("load: FileNotFoundError: %s is not a valid path" % path)
        return None
    except AssertionError as msg:
        print("load: AssertionError:", msg)
        return None
    except pd.errors.ParserError as msg:
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
