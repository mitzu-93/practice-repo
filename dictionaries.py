countries = [
    {'Country': 'Vietnam', 
     'Foods tried': ['Banh Mi', 'Pho'],
     'Times visited': 7}
]

def add_new_country(country, foods, times_v):
    new_country = {}
    new_country['Country'] = country
    new_country['Foods tried'] = foods
    new_country['Times visited'] = times_v
    countries.append(new_country)


add_new_country('South Korea', ['Kimchi', 'Chicken'], 3)

print(countries)