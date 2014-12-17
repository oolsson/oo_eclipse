#!/usr/bin/env python

from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle
import pandas as pd

doc = SimpleDocTemplate("df_table.pdf", pagesize=letter)
parts = []

data = [
    ['Item', 'Cost', 'Quantity'],
    ['Widget', 3.99, 26],
    ['Whatsit', 2.25, 26],
    ['Hooplah', 10.00, 26]]

df=pd.DataFrame([[1,1,1],[2,2,2],[3,3,3]],index=['a','s','l'],columns=['A','K','P'])
def dfTable(df):
    df2 = df.reset_index() # reset the index so row labels show up in the reportlab table
    n = df2.columns.nlevels # number of table header rows to repeat
    if n > 1:
        labels = map(list, zip(*df2.columns.values))
    else:
        labels = [df2.columns[:,].values.astype(str).tolist()]
    values = df2.values.tolist()
    datalist = labels + values
#     print datalist
    return datalist

data=dfTable(df)

# table = Table(data, [3 * inch, 1.5 * inch, inch])
table_with_style = Table(data, [1 * inch, 1.5 * inch, inch])

s2 = TableStyle(
[('LINEABOVE', (1,0), (-1,1), 2, colors.green),                 #first 0=starting from column, sec0nd=?, -1= goes to last column
# ('LINEABOVE', (0,-1), (-1,-1), 0.25, colors.black),
('INNERGRID', (0, 1), (-1, -1), 0.25, colors.black),
('LINEBELOW', (0,-1), (-1,-1), 1, colors.blue),
('BOX', (0, 1), (-1, -1), 0.25, colors.black),
('ALIGN', (0,0), (0,-1), 'LEFT'),
('ALIGN', (1,0), (-1,-1), 'CENTRE'),
('BACKGROUND', (1,0), (-1,0), colors.Color(0,0,0)),
('TEXTCOLOR',(0,0),(0,0),colors.white),
('TEXTCOLOR',(1,0),(-1,0),colors.yellow)])

table_with_style.setStyle(s2)


# table_with_style.setStyle(TableStyle([
#     ('FONT', (0, 0), (-1, -1), 'Helvetica'),
#     ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
#     ('FONTSIZE', (0, 0), (-1, -1), 8),
#     ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#     ('BOX', (0, 0), (-1, 0), 0.25, colors.green),
#     ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
# ]))

# parts.append(table)
# parts.append(Spacer(1, 0.5 * inch))
parts.append(table_with_style)
parts.append(table_with_style)
print parts
doc.build(parts)