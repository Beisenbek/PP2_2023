import re
import csv

result = [["Order","Name", "Total"]]


file = open('row.txt','r')

text = file.read()

BINPattern = r"\nБИН\s+(?P<BIN>[0-9]{12})"
KassaPattern = r"\nКасса\s+(?P<Kassa>.+)"

BINValue = re.search(BINPattern, text).group("BIN")
KassaValue = re.search(KassaPattern, text).group("Kassa")


ItemPatternText = r"\n(?P<Order>.*)\n(?P<Name>.*)\n(?P<Count>.*)x(?P<Price>.*)\n(?P<Subtotal>.*)\nСтоимость\n(?P<Total>.*)"
CompiledItemPattern = re.compile(ItemPatternText)
items = re.finditer(CompiledItemPattern, text)

for match in items:
    row = [match.group("Order"),match.group("Name"),match.group("Total")]
    result.append(row)


with open('data.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)