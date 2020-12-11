from pyecharts import options as opts
from pyecharts.charts import HeatMap

xdata = ["橘子", "苹果", "梨", "桃子", "杏", "栗子", "葡萄", "西瓜", "哈密瓜", "西红柿"]
ydata = ["1月", "2月", "3月", "4月", "5月", "6月"]

data = [
    [0, 0, 1],
    [1, 0, 80],
    [2, 0, 1],
    [3, 0, 40],
    [4, 0, 150],
    [5, 0, 80],
    [6, 0, 40],
    [7, 0, 80],
    [8, 0, 140],
    [9, 0, 90],
    [0, 1, 80],
    [1, 1, 10],
    [2, 1, 80],
    [3, 1, 150],
    [4, 1, 60],
    [5, 1, 2],
    [6, 1, 60],
    [7, 1, 80],
    [8, 1, 50],
    [9, 1, 45],
    [0, 2, 158],
    [1, 2, 91],
    [2, 2, 120],
    [3, 2, 30],
    [4, 2, 70],
    [5, 2, 140],
    [6, 2, 80],
    [7, 2, 2],
    [8, 2, 3],
    [9, 2, 1],
    [0, 3, 47],
    [1, 3, 32],
    [2, 3, 20],
    [3, 3, 145],
    [4, 3, 60],
    [5, 3, 70],
    [6, 3, 80],
    [7, 3, 90],
    [8, 3, 50],
    [9, 3, 40],
    [0, 4, 91],
    [1, 4, 38],
    [2, 4, 2],
    [3, 4, 5],
    [4, 4, 66],
    [5, 4, 21],
    [6, 4, 60],
    [7, 4, 10],
    [8, 4, 140],
    [9, 4, 28],
    [0, 5, 22],
    [1, 5, 41],
    [2, 5, 110],
    [3, 5, 39],
    [4, 5, 40],
    [5, 5, 90],
    [6, 5, 50],
    [7, 5, 60],
    [8, 5, 146],
    [9, 5, 15],
]

axisOpts = opts.AxisOpts(
    type_="category",
    axisline_opts=opts.AxisLineOpts(
        is_show=False
    ),
    axislabel_opts=opts.LabelOpts(
        color='#A3C7E7',
        font_size=10,
    ),
    axistick_opts=opts.AxisTickOpts(
        is_show=False
    ),
    splitline_opts=opts.SplitLineOpts(
        is_show=True,
        linestyle_opts=opts.LineStyleOpts(
            is_show=True,
            color='black',
            width=10,
        )
    ),
)

c = (
    HeatMap(init_opts=opts.InitOpts(
        bg_color='black',
    ))
        .add_xaxis(xdata)
        .add_yaxis(
        "月份",
        ydata,
        data,
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(),
        legend_opts=opts.LegendOpts(
            is_show=False,
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=1,
            max_=158,
            is_calculable=True,
            orient='horizontal',
            pos_left='center',
            pos_bottom='-1%',
            range_color=['#C0F1F4', '#60BDCB', '#316870', '#EA7552'],
            textstyle_opts=opts.TextStyleOpts(
                color='#A3C7E7'
            )
        ),
        tooltip_opts=opts.TooltipOpts(
            position='top'
        ),
        xaxis_opts=axisOpts,
        yaxis_opts=axisOpts,
    )
        .set_series_opts(
        zlevel=-1  # 这是一个重要属性，设置图层
    )
        .render("sale-heatmap.html")
)
