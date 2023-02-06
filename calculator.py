# -*- coding: utf-8 -*-
import xlwings as xw

from pace.paceloader import init, size, load
from pace.pacecolor import Color
from plots.graph import Graph


"""
(base) C:\pace\docs>pip install xlwings
Requirement already satisfied: xlwings in c:\appdata\local\continuum\anaconda3\lib\site-packages (0.11.5)
Requirement already satisfied: comtypes in c:\appdata\local\continuum\anaconda3\lib\site-packages (from xlwings) (1.1.4)

(base) C:\pace\docs>xlwings addin install
Successfully installed the xlwings add-in! Please restart Excel.
"""

blue = Color("#25557e")
red = Color("#841439")
light_blue = Color("#25557e")
light_red = Color("#841439")
light_blue.luminance = 0.5
light_red.luminance = 0.5

colors = [blue, red, light_blue, light_red]


@xw.func
def loadValue(table, name, x, n=None):
    init(table=table)
    if n:
        return load(name, x=int(x), n=int(n))
    else:
        return load(name, x=int(x))


@xw.func
@xw.ret(expand='table')
def loadTable(table, names, xMin=-1, xMax=-1, step=1):
    names = to_array(names)

    init(table=table)

    if xMin == -1 or xMax == -1:
        xMin = 0
        xMax = size()

    data = [["Alter"]]
    for name in names:
        data[0].append(name)

    for x in range(int(xMin), int(xMax+1), int(step)):
        line = [x]
        for name in names:
            value = load(name, x=int(x))
            line.append(value)
        data.append(line)
    return data


@xw.func
@xw.arg('xl_app', vba='Application')
def plot(xl_app, title, tables, labels, name, xMin=-1, xMax=-1):
    tables = to_array(tables)
    labels = to_array(labels)
    xMin = int(xMin)
    xMax = int(xMax)

    g = Graph()
    if xMin != -1:
        g.xMin = xMin
    if xMax != -1:
        g.xMax = xMax
    for i, table in enumerate(tables):
        g.add_plot(name, table=table, color=colors[i], label=labels[i])

    wb = xw.Book.caller()
    sht = wb.sheets[xl_app.Caller.Worksheet.Name]
    sht.pictures.add(g.create(), name=title, update=True)

    return title


@xw.func
@xw.arg('xl_app', vba='Application')
def plot_n(xl_app, title, tables, labels, colors_i, name, xMin=-1, xMax=-1, step=10):
    tables = to_array(tables)
    labels = to_array(labels)
    colors_i = to_array(colors_i)
    xMin = int(xMin)
    xMax = int(xMax)
    step = int(step)

    g = Graph()
    if xMin != -1:
        g.xMax = xMin
    if xMax != -1:
        g.xMax = xMax

    for i, table in enumerate(tables):
        g.add_plot_n(name, table=table, label=labels[i], step=step, color=colors[int(colors_i[i])])

    wb = xw.Book.caller()
    sht = wb.sheets[xl_app.Caller.Worksheet.Name]
    sht.pictures.add(g.create(), name=title, update=True)

    return title


def to_array(array):
    if type(array) == str:
        return [array]
    return array


"""
@xw.func
def plot3D_n(title, tables, labels, colors, name, xMin=-1, xMax=-1, step=10):
    tables = checkArray(tables)
    labels = checkArray(labels)
    colors = checkArray(colors)
    
    wb = xw.Book.caller()
    sht = wb.sheets[1]
    directory = path.getParent(wb.fullname) + "\\" + path.getFileName(wb.name)
    fig = plots.plot3D_n(directory, title, tables, labels, colors, name, int(xMin), int(xMax), int(step))
    sht.pictures.add(fig, name="table_" + title, update=True)
    return "Create Diagram " + title
"""

