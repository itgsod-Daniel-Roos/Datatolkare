def split_line(split_line):
    if split_line == '':
        raise ValueError('can not parse empty line')
    words = split_line.split()
    return words


def encode_line(encode_line):
    hashresult = {}
    if len(encode_line) <= 2:
        raise ValueError('incomplete list')
    hashresult['date'] = int(encode_line[0])
    hashresult['max'] = int(encode_line[1])
    hashresult['min'] = int(encode_line[2])
    return hashresult


def find_biggest_variation(find_biggest_variation):
    #if len(find_biggest_variation([])) == 0:
    if not find_biggest_variation:
        raise ValueError('list must not be empty')
    
    pass


def load_weather_file(myfile):
    with open(myfile, 'w') as weatherfile:
        weatherdata = weatherfile.readlines()

    pass


def main():
    pass