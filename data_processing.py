import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

for city in cities:
    if city['country'] == 'Germany':
        print(city)
print()

# Print all cities in Spain with a temperature above 12°C

for city in cities:
    if city['country'] == 'Spain' and float(city['temperature']) > 12:
        print(city)
print()

# Count the number of unique countries

countries = set()
for city in cities:
    countries.add(city['country'])
print("Number of unique countries:", len(countries))
print()

# Print the average temperature for all the cities in Germany

germany_temps = [float(city['temperature']) for city in cities if city['country'] == 'Germany']
if germany_temps:
    print("Average temperature in Germany:", sum(germany_temps) / len(germany_temps))
else:
    print("No data for Germany")
print()

# Print the max temperature for all the cities in Italy

italy_temps = [float(city['temperature']) for city in cities if city['country'] == 'Italy']
if italy_temps:
    print("Max temperature in Italy:", max(italy_temps))
else:
    print("No data for Italy")
print()
