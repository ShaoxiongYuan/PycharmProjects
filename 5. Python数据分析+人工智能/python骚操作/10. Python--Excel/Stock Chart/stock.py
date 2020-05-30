from datetime import date
from openpyxl import Workbook

from openpyxl.chart import (
    BarChart,
    StockChart,
    Reference,
    Series,
)

from openpyxl.chart.axis import DateAxis, ChartLines
from openpyxl.chart.updown_bars import UpDownBars

wb = Workbook()
ws = wb.active

rows = [
    ['日期', '成交量', '开盘', '高', '低', '收盘'],
    ['2018-11-10', 20000, 26.20, 27.20, 23.49, 25.45, ],
    ['2018-11-11', 10000, 25.45, 25.03, 19.55, 23.05, ],
    ['2018-11-12', 15000, 23.05, 24.46, 20.03, 22.42, ],
    ['2018-11-13', 2000, 22.42, 23.97, 20.07, 21.90, ],
    ['2018-11-14', 12000, 21.9, 23.65, 19.50, 21.51, ],
]

for row in rows:
    ws.append(row)

# 高-低-收盘
c1 = StockChart()
labels = Reference(ws, min_col=1, min_row=2, max_row=6)
data = Reference(ws, min_col=4, max_col=6, min_row=1, max_row=6)
c1.add_data(data, titles_from_data=True)
c1.set_categories(labels)
for s in c1.series:
    s.graphicalProperties.line.noFill = True
    # 标记收盘
    s.marker.symbol = "dot"
    s.marker.size = 5
    c1.title = "高-低-收盘"
    c1.hiLowLines = ChartLines()

from openpyxl.chart.data_source import NumData, NumVal

pts = [NumVal(idx=i) for i in range(len(data) - 1)]
cache = NumData(pt=pts)
c1.series[-1].val.numRef.numCache = cache

ws.add_chart(c1, "A10")

# 开盘-高-低-收盘
c2 = StockChart()
data = Reference(ws, min_col=3, max_col=6, min_row=1, max_row=6)
c2.add_data(data, titles_from_data=True)
c2.set_categories(labels)
for s in c2.series:
    s.graphicalProperties.line.noFill = True
    c2.hiLowLines = ChartLines()
    c2.upDownBars = UpDownBars()
    c2.title = "开盘-高-低-收盘"

c2.series[-1].val.numRef.numCache = cache

ws.add_chart(c2, "G10")

# 创建条形图代表成交量
bar = BarChart()
data = Reference(ws, min_col=2, min_row=1, max_row=6)
bar.add_data(data, titles_from_data=True)
bar.set_categories(labels)

from copy import deepcopy

# 成交量-高-低-收盘价
b1 = deepcopy(bar)
c3 = deepcopy(c1)
c3.y_axis.majorGridlines = None
c3.y_axis.title = "价格"
b1.y_axis.axId = 20
b1.z_axis = c3.y_axis
b1.y_axis.crosses = "max"
b1 += c3

c3.title = "高低收盘成交量"

ws.add_chart(b1, "A27")

# 成交量-开盘-高-低-收盘
b2 = deepcopy(bar)
c4 = deepcopy(c2)
c4.y_axis.majorGridlines = None
c4.y_axis.title = "价格"
b2.y_axis.axId = 20
b2.z_axis = c4.y_axis
b2.y_axis.crosses = "max"
b2 += c4

ws.add_chart(b2, "G27")
wb.save("stock.xlsx")
