from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

doc = SimpleDocTemplate("2table.pdf", pagesize=letter)
elements = []

data1 = [['00', '01', '02', '03', '04', '10', '11', '12', '13', '14'],
        ['10', '11', '12', '13', '14', '10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24', '10', '11', '12', '13', '14'],
        ['30', '31', '32', '33', '34', '10', '11', '12', '13', '14']]

t1 = Table(data1, 5 * [0.3 * inch], 4 * [0.2 * inch])
t1.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (4, 0), colors.gray),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
]))


data2 = [['100', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]

t2 = Table(data2, 5 * [0.4 * inch], 4 * [0.2 * inch])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (4, 0), colors.gray),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
]))

data = [[t1, t2]]
# adjust the length of tables
t1_w = 3 * inch
t2_w = 3 * inch
shell_table = Table(data, colWidths=[t1_w, t2_w])
elements.append(shell_table)
doc.build(elements)