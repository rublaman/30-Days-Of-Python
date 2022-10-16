'''
Python has the module called statistics and we can use this module to do all the statistical calculations. 
However, to learn how to make function and reuse function let us try to develop a program, which calculates 
the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance,
standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency 
distribution of the sample. You can create a class called Statistics and create all the functions that do 
statistical calculations as methods for the Statistics class. Check the output below.
'''


class Statistics:

    import math

    def __init__(self, list_number) -> None:
        self.list_number = list_number

    def mean(self) -> float:
        return sum(self.list_number) / len(self.list_number)

    def median(self) -> float:
        sorted_items = sorted(self.list_number)
        return sorted_items[(len(sorted_items)) // 2]

    def mode(self) -> float:
        return max(set(self.list_number), key=self.list_number.count)

    def range(self) -> float:
        return max(self.list_number) - min(self.list_number)

    def variance(self) -> float:
        mean = self.mean()
        return sum((x-mean)**2 for x in self.list_number) / \
            len(self.list_number)

    def std_deviation(self) -> float:
        return self.math.sqrt(self.variance())

    def min(self) -> float:
        return min(self.list_number)

    def max(self) -> float:
        return max(self.list_number)

    def count(self) -> float:
        return len(self.list_number)

    def frequency(self) -> float:
        res = {}
        for i in self.list_number:
            if res.get(i):
                res[i] += 1
            else:
                res[i] = 1

        return res


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24,
        32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
print(data.mean())
print(data.median())
print(data.mode())
print(data.frequency())
print(data.max())
print(data.min())
print(data.range())
print(data.variance())
print(data.std_deviation())

'''
OUTPUT

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
'''
