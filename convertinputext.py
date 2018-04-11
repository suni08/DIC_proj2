import csv

txt_file = r"out_ext.txt"
csv_file = r"out_ext.csv"

o_csv = open(csv_file, 'w')
columnTitleRow = "text,size\n"
o_csv.write(columnTitleRow)

in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'a'))

out_csv.writerows(in_txt)
