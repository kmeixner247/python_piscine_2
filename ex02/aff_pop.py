import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from matplotlib.ticker import FuncFormatter


def millions_formatter(x: float, pos: int) -> str:
    """millions_formatter(x, pos)

Convert axis tick value to millions and format as string with "M" suffix

Args:
    - x (float): Axis tick value.
    - pos (int): Tick position.

Returns:
    - str: The formatted tick value with a "M" suffix.
"""
    return f"{x/1e6:.0f}M"


def thousands_formatter(x: float, pos: int) -> str:
    """thousands_formatter(x, pos)

Convert axis tick value to millions and format as string with "M" suffix

Args:
    - x (float): Axis tick value.
    - pos (int): Tick position.

Returns:
    - str: The formatted tick value with a "k" suffix.
"""
    return f"{x/1e3:.0f}k"


def create_plot(df, countries):
    """create_plot(df, country)

Creates a plot of the life expectancy projections for the given country

Args:
    - df (pd.DataFrame): A pandas dataframe with columns for country, year,
                         and life expectancy
    - country (str): The name of the country to plot data for

Returns:
    None

Raises:
    - AssertionError: If either of the provided arguments has the wrong type.
    - KeyError: If the provided country doesn't exist as a key in the
                dataframe.
    - Exception: If there is an unexpected error while creating the plot
"""
    try:
        assert type(df) is pd.core.frame.DataFrame, "first argument must be a\
                                                     pandas dataframe"
        assert type(countries) is list, "second argument must be a list"
        for country in countries:
            assert type(country) is str, "every element of the second argument\
                                          must be a string"
        df.set_index('country', inplace=True)
        fig, ax = plt.subplots()
        for country in countries:
            data = df.loc[country]
            data = data.apply(lambda x: float(x[:-1]) * 1000000 if 'M' in x
                              else float(x[:-1]) * 1000)
            data.plot()
        if data.values.max() > 2000000:
            ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
        else:
            ax.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title('%s Population Projections')
        plt.legend(loc="lower right")
    except AssertionError as msg:
        print("create_plot: AssertionError:", msg)
    except KeyError as key:
        print("create_plot: KeyError: key", key, "could not be found\
                                                  in the dataframe")
    except Exception as msg:
        print("create_plot: Error:", msg)


def main():
    """main function of aff_pop.py

The population dataframe is loaded using the `load` function from the
`load_csv` module. Then, a lineplot for Germany vs Netherlands is created using
the `create_plot` function. Finally, the plot is displayed using `plot.show()`.

Args:
    None

Returns:
    None

Raises:
    see load.__doc__ and create_plot.__doc__
"""
    population = load("population_total.csv")
    create_plot(population, ["Germany", "Netherlands"])
    plt.show()


if __name__ == "__main__":
    main()
