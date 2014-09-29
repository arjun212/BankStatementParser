import csv

print "This is a simple Bank Parser Program"

print ""

with open('statement.csv', 'rb') as f :
  reader = csv.reader(f)
  for row in reader :
    if float(row[2]) > 0 : 
      print row

