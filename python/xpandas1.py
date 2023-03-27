import pandas as pd


data = { 'Name' : ['Jai', 'Princi', 'Gauray', 'Anuj'], 'Address' : [ 'Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 'Qualification' : [ 'Msc', 'MA', 'MCA', 'Phd'], 'Age' : [22,23,21,34]}
df = pd.DataFrame(data) 
print(df [df .columns[0:4:][::-1]]) 