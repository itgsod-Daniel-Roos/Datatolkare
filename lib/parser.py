import os.path

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


def find_biggest_variation(date_array):
    if not date_array:
        raise ValueError('list must not be empty')
    calc_biggest_diff = 0
    for i in date_array:
        if i['max'] - i['min'] > calc_biggest_diff:
            calc_biggest_diff = i['max'] - i['min']
            biggest_diff = i
    return biggest_diff


def load_weather_file(myfile):
    if myfile == '':
        raise ValueError('path must not be empty')
    if not os.path.isfile(myfile):
        raise IOError('file does not exist')
    with open(myfile, 'r') as weatherfile:
        weatherdata = weatherfile.readlines()
    return weatherdata[2:]


def main(inputfile):
    weather_data = load_weather_file(inputfile)
    compare_list = []
    for weather in weather_data:
        split = split_line(weather)
        compare_list.append(encode_line(split))
    biggest_variation = find_biggest_variation(compare_list)
    variation = biggest_variation['max'] - biggest_variation['min']
    return "Day ', biggest_variation['date'], ' had the biggest variation (', variation, ' degrees)."