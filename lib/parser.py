def split_line(split_line):
    if split_line == '':
        raise ValueError('can not parse empty line')
    pass


def encode_line(encode_line):
    if len(encode_line) <= 2:
        raise ValueError('incomplete list')
    pass


def find_biggest_variation():
    
    pass


def load_weather_file(myfile):
    with open(myfile, 'w') as weatherfile:
        weatherdata = weatherfile.readlines()

    pass


def main():
    pass