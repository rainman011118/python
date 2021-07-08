#!/usr/bin/python3.8

# CSV = a file type (Comma Separated Values)
fileopen = open("Google Stock Market Data - google_stock_data.csv.csv")
# print(fileopen)

# rd = fileopen.read()
# print(rd)

lines = [line for line in fileopen]

print(lines[0])
print(lines[1])
print(lines[0:2])

print(lines[0].strip().split(","))
print(lines[1].strip().split(","))
# .strip get's rid of the '/n'
# .split(",") makes it a bit clearer to read


fileopen.close()
