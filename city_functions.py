#11-1.1

def local(city, country, population=0):
    output_string = city.title() + ", " + country.title()
    if population:
        output_string += ' - population ' + str(population)
    return output_string