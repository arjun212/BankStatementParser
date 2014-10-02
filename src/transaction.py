import csv
import time

class Transaction:
  def __init__(self, date, description, amount, category):
    self.date = time.strptime(date, "%Y-%m-%d")

    self.desc = description
    self.amount = float(amount)
    self.category = category

class Category:
  def __init__(self, name, descString):
    self.name = name
    self.descString = descString

stat = "statement.csv"
#raw_input("Please Enter the Statement Filename: ")

transList = []
catList = []

with open(stat, 'rb') as f :
  reader = csv.reader(f)
  for row in reader :
    if float(row[2]) <> 0 :
      transList.append(Transaction(row[0], row[1], row[2], None))
      while catFound
      print transactionList[-1].desc


