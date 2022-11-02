"""Dictionary related utility functions."""

__author__ = "730562021"

# Define your functions below


from csv import DictReader
DATA_DIRECTORY = "../..data"
DATA_FILE_PATH = f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], value: str) -> list[str]:
    """Produce a list of values whose name is the second parameter."""
    resulting_values: list[str] = []
    for row in table:
        item: str = row[value]
        resulting_values.append(item)
    return resulting_values


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into a dictionary of columns."""
    result_dictionary: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result_dictionary[column] = column_values(row_table, column)
    return result_dictionary


def head(column_table: dict[str, list[str]], included_rows: int) -> dict[str, list[str]]:
    """Produce a column based table with only N number of rows for each column."""
    new_dictionary: dict[str, list[str]] = {}
    if included_rows > len(column_table):
        return column_table
    for column in column_table:
        value_list: list[str] = []
        i: int = 0
        while i < included_rows:
            value_list.append(column_table[column][i])
            i += 1
        new_dictionary[column] = value_list
    return new_dictionary       


def select(original_table: dict[str, list[str]], selection: list[str]) -> dict[str, list[str]]:
    """Create a table with only the selected columns."""
    selected_dictionary: dict[str, list[str]] = {}
    for column in selection:
        selected_dictionary[column] = original_table[column]
    return selected_dictionary


def concat(first_table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two separate column based tables into one column based table."""
    combined_dictionary: dict[str, list[str]] = {}
    for column in first_table:
        combined_dictionary[column] = first_table[column]
    for column in second_table:
        if column in combined_dictionary:
            combined_dictionary[column] += second_table[column]
        else:
            combined_dictionary[column] = second_table[column]
    return combined_dictionary


def count(chosen_values: list[str]) -> dict[str, int]:
    """Counts the number of times a certain value appears in data set."""
    count_dictionary: dict[str, int] = {}
    for item in chosen_values:
        if item in count_dictionary:
            count_dictionary[item] += 1
        else:
            count_dictionary[item] = 1
    return count_dictionary