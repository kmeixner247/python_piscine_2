from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter


def merge_dataframes_at_year(gdp: pd.core.frame.DataFrame,
                             lifeExpectancy: pd.core.frame.DataFrame,
                             year: int) -> pd.core.frame.DataFrame:
    """merge_dataframes_at_year(gdp: pd.core.frame.DataFrame,
                      lifeExpectancy: pd.core.frame.DataFrame,
                      year: int) -> pd.core.frame.DataFrame:

Merges the two given dataframes at a specified year

Args:
    - gdp (pd.core.frame.DataFrame): A pandas dataframe with columns for
      country and years
    - lifeExpectancy (pd.core.frame.DataFrame): A pandas dataframe with colums
      for country and years
    - year (int): The year at which the dataframes should be merged

Returns:
    pd.core.frame.DataFrame: A pandas dataframe with the merged content at the
    specified year.

Raises:
    - AssertionError: If any of the provided arguments has the wrong type.
    - KeyError: If the specified year can't be found in either dataframe.
    - TypeError: If either of the dataframes contains invalid data types.
    - Exception: If there is an unexpected error while merging the dataframes.
"""
    try:
        assert type(gdp) is pd.core.frame.DataFrame, "first argument must be\
                                                      panda dataframes"
        assert type(lifeExpectancy) is\
            pd.core.frame.DataFrame, "second argument must be panda dataframes"
        assert type(year) is int, "third argument must be integer"
        gdp = gdp[["country", str(year)]]
        lifeExpectancy = lifeExpectancy[["country", str(year)]]
        merged_df = pd.merge(gdp, lifeExpectancy, on='country')
    except AssertionError as msg:
        print("create_df_at_year: Assertion Error:", msg)
        return None
    except KeyError:
        print("create_df_at_year: KeyError: key %d does not exist in both \
                                                            dataframes" % year)
        return None
    except TypeError:
        print("create_df_at_year: TypeError: non-numeric data in one of the\
                                                                dataframes")
        return None
    except Exception as msg:
        print("create_df_at_year: Error:", msg)
        return None
    return merged_df


def set_plot_data():
    """set_plot_data()

sets the data of the current plot:
    - Makes the x-axis scale logarithmically
    - Writes ticks at 300, 100, 10000
    - Converts the 1000+ ticks to 1k and 10k
    - Labels the x- and y-axis and specifies the title

Args:
    None

Returns:
    None

Raises:
    None
"""
    ax = plt.gca()
    ax.set_xscale('log')
    ax.set_xticks([300, 1000, 10000])
    ax.xaxis.set_major_formatter(FuncFormatter(
                    lambda x, _: '{:.0f}k'.format(x/1000) if x >= 1000 else x))
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life Expectancy')
    plt.title('1900')


def create_plot(gdp, lifeExpectancy, year):
    """create_plot(gdp, lifeExpectancy, year)

Creates a scatterplot for gdp vs life expectancy in the provided year
based on the provided dataframes

Args:
    - gdp (pd.core.frame.DataFrame): A pandas dataframe with colums for country
      and years
    - lifeExpectancy (pd.core.frame.DataFrame): A pandas dataframe with colums
      for country and years
    - year (int): The year at which the scatterplot should be created

Returns:
    - None

Raises:
    - Assertion Error: If any of the arguments has the wrong type
    - Exception: If there is an unexpected error while creating the plot
"""
    try:
        assert type(gdp) is pd.core.frame.DataFrame,\
                                    "first argument must be panda dataframes"
        assert type(lifeExpectancy)\
            is pd.core.frame.DataFrame, "second argument must\
                                         be panda dataframes"
        assert type(year) is int, "third argument must be integer"
        merged_df = merge_dataframes_at_year(gdp, lifeExpectancy, year)
        merged_df.plot.scatter(x=str(year)+"_x", y=str(year)+"_y")
        set_plot_data()
    except AssertionError as msg:
        print("create_plot: Assertion Error:", msg)
    except Exception as msg:
        print("create_plot: Error:", msg)


def main():
    """Load GDP and life expectancy dataframes, and create a scatter plot for
       the year 1900.

The GDP and life expectancy dataframes are loaded using the `load` function
from the `load_csv` module. Then, a scatter plot for the year 1900 is created
using the `create_plot` function, which merges the GDP and life expectancy
dataframes at the specified year, and plots them as a scatter plot. Finally,
the plot is displayed using `plt.show()`.

    Args:
        None

    Returns:
        None

    Raises:
        see load.__doc__ and create_plot.__doc__
"""
    gdp = load("income_per_person_gdppercapita_ppp_inflaction_adjusted.csv")
    lifeExpectancy = load("life_expectancy_years.csv")
    create_plot(gdp, lifeExpectancy, 1900)
    plt.show()


if __name__ == "__main__":
    main()
