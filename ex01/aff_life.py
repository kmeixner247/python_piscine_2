import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def create_plot(df: pd.core.frame.DataFrame, country: str):
    """create_plot(df, country)

Creates a plot of the life expectancy projections for the given country

Args:
    - df (pandas.DataFrame): A pandas dataframe with columns for country, year,
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
        assert type(country) is str, "second parameter must be a string"
        df.set_index('country', inplace=True)
        data = df.loc[country]
        data.plot()
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.title('%s Life Expectancy Projections' % country)
    except AssertionError as msg:
        print("create_plot: AssertionError:", msg)
    except KeyError as key:
        print("create_plot: KeyError: key", key, "could not be found in the\
                                                  dataframe")
    except Exception as msg:
        print("create_plot: Error:", msg)


def main():
    """main function of aff_life.py

The life expectancy dataframe is loaded using the `load` function from the
`load_csv` module. Then, a lineplot for Germany is created using the
`create_plot` function. Finally, the plot is displayed using `plot.show()`.

Args:
    None

Returns:
    None

Raises:
    See load.__doc__ and create_plot.__doc__
"""
    lifeExpectancy = load("life_expectancy_years.csv")
    create_plot(lifeExpectancy, "Germany")
    plt.show()


if __name__ == "__main__":
    main()
