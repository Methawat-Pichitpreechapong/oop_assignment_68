import csv, os
from pathlib import Path

class DataLoader:
    """Handles loading CSV data files."""

    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files.
        """
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)

    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries.
        """
        filepath = self.base_path / filename
        data = []

        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))

        return data

class Table:
    """Represents a simple in-memory table backed by a list of dictionaries."""

    def __init__(self, name, rows):
        """
        Create a new Table.

        :param name: A logical name for the table (e.g., 'cities').
        :param rows: Iterable of dictionaries, each representing a row.
        """
        self.name = name
        # Copy rows into our own list so outside changes don't affect us
        self.table = list(rows)

    def filter(self, condition):
        """
        Return a new Table containing only rows that satisfy `condition`.

        :param condition: A function that takes a row (dict) and returns True/False.
        :return: A new Table instance with filtered rows.
        """
        filtered_rows = [row for row in self.table if condition(row)]
        return Table(self.name, filtered_rows)

    def aggregate(self, aggregation_function, aggregation_key):
        """
        Apply an aggregation function to a single column.

        :param aggregation_function: function(list) -> value (e.g., sum/len/max)
        :param aggregation_key: column name to aggregate (e.g., 'temperature')
        :return: result of aggregation_function(values)
        """
        values = []
        for row in self.table:
            value = row.get(aggregation_key)

            # Try converting to float so numeric strings can be aggregated
            try:
                value = float(value)
            except (TypeError, ValueError):
                # If not numeric, keep as-is
                pass

            values.append(value)

        return aggregation_function(values)

    def __len__(self):
        """Return the number of rows in the table."""
        return len(self.table)

    def __repr__(self):
        return f"Table(name={self.name!r}, rows={len(self.table)})"



loader = DataLoader()
cities = loader.load_csv('Cities.csv')
my_table1 = Table('cities', cities)

# Print the average temperature of all the cities
my_value = my_table1.aggregate(lambda x: sum(x)/len(x), 'temperature')
print(my_value)
print()

# Print all cities in Germany
my_cities = my_table1.filter(lambda x: x['country'] == 'Germany')
cities_list = [[city['city'], city['country']] for city in my_cities.table]
print("All the cities in Germany:")
for city in cities_list:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
my_cities = my_table1.filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12.0)
cities_list = [[city['city'], city['country'], city['temperature']] for city in my_cities.table]
print("All the cities in Spain with temperature above 12°C:")
for city in cities_list:
    print(city)
print()

# Count the number of unique countries
my_countries = my_table1.aggregate(lambda x: len(set(x)), 'country')
print("The number of unique countries is:")
print(my_countries)
print()

# Print the average temperature for all the cities in Germany
my_value = my_table1.filter(lambda x: x['country'] == 'Germany').aggregate(lambda x: sum(x)/len(x), 'temperature')
print("The average temperature of all the cities in Germany:")
print(my_value)
print()

# Print the max temperature for all the cities in Italy
my_value = my_table1.filter(lambda x: x['country'] == 'Italy').aggregate(lambda x: max(x), 'temperature')
print("The max temperature of all the cities in Italy:")
print(my_value)
print()