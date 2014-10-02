import csv

print "This is a simple Bank Parser Program"

print ""

stat = raw_input("Please Enter the Statement Filename: ")

with open(stat, 'rb') as f :
  reader = csv.reader(f)
  for row in reader :
    if float(row[2]) <> 0 : 
      print row

