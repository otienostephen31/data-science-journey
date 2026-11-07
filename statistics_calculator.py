
import statistics

print("MY STATISTICAL CALCULATOR")

numbers = input("Enter numbers separated by commas: ")

data = [float(x.strip()) for x in numbers.split(",")]

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.multimode(data)

print("\n--- RESULTS ---")
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

