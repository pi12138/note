def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


def normalize2(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


it = read_visits('./my_numbers.txt')
percentages = normalize2(it)
print(percentages)


# ***********************************


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits('./my_numbers.txt')
percentages = normalize(visits)
print(percentages)
