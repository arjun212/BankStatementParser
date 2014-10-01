import csv

print "This is a simple conversion Program"

print ""

with open('statement2.csv', 'rb') as f :
  reader = csv.reader(f)
  for row in reader :
    if (row[5] == "") :
      print row[0]+",", row[4]+",", float(row[6])
    else :
      print row[0]+",", row[4]+",", -float(row[5])
      
