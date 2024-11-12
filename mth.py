import statistics

data_input = input("Enter numbers separated by spaces: ")

data = list(map(float, data_input.split()))
datas = sorted(map(int, data_input.split()))

print("Sorted Data:", *datas)

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Standard Deviation:", statistics.stdev(data))
