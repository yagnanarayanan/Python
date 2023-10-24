"""open two dat files and match the ISIN code from one file to the other to extract another field and create a new
file as output with the calculated field added to the original data """

# open and read the trade file to append every record line into a list
with open("trade_feed.dat", "r") as f:
    trade_content = f.readlines()
print(trade_content)
strip_content = []
for line in trade_content:
    strip_content.append(line.replace("\n", ""))
print(strip_content)
seperator = "|"
record = []
# further split the record using the seperator to identify individual fields in every record
for line in strip_content:
    record.append(line.rsplit(seperator))
print(f"trade record: {record}")
# open and read the security file and perform the same steps as for the 1st file
with open("sec_price.dat", "r") as f:
    sec_content = f.readlines()
print(sec_content)
sec_prc = []
for sec_line in sec_content:
    sec_prc.append(sec_line.replace("\n", ""))
print(sec_prc)
sec_prices = []
for prc in sec_prc:
    sec_prices.append(prc.rsplit(seperator))
print(f"sec record: {sec_prices}")
# use a common field between the two files to look up values and create a calculated field (in this case:
# price*quantity)
# open a new file and add this new calculated field to existing record with the seperator. This could be used for
# further processing downstream.
for trade in record:
    for sec in sec_prices:
        if trade[4] == sec[0]:
            with open("result.dat", "a") as f:
                f.write(trade[0] + "|" + trade[1] + "|" + trade[2] + "|" + trade[3] + "|" + trade[4] + "|" +
                        str(float(trade[3]) * float(sec[1])) + "\n")
