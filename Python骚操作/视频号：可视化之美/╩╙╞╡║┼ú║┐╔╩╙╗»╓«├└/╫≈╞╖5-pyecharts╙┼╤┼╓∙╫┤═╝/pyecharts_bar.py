######
#作者：zglg
#时间:2020-09-16
#python == 3.7
#pyecharts == 1.8.1
######


import pyecharts.options as opts
from pyecharts.charts import Bar, Line, Grid
from pyecharts.globals import ThemeType

x_data = [str(i)+"月份" for i in range(1, 13)]
y_data = [709, 1917, 2455, 2610, 1719, 1433,1544, 3285, 5208, 3372, 2484, 4078]
y2_data = [327, 1776, 507, 1200, 800, 482, 204, 1390, 1001, 951, 381, 220]
y3_data = [1036, 3693, 2962, 3810, 2519,1915, 1748, 4675, 6209, 4323, 2865, 4298]

# 折线图对象
bar = Bar(opts.InitOpts(bg_color="#344b58"))
# 设置图形的全局参数
(
    bar.set_global_opts(
        title_opts=opts.TitleOpts(
            title="本年银行客户人数统计",
            subtitle="BY zglg",
            title_textstyle_opts=opts.TextStyleOpts(
                color="#90979c",
                font_size="16"
            )
        ),
        legend_opts=opts.LegendOpts(
            pos_top="8%",
            textstyle_opts=opts.TextStyleOpts(
                color='#90979c'
            )
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis",
            axis_pointer_type="shadow",
            textstyle_opts=opts.TextStyleOpts(
                color="#fff"
            )
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color="#90979c"
                )
            ),
            splitline_opts=opts.SplitLineOpts(
                is_show=False
            ),
            axistick_opts=opts.AxisTickOpts(
                is_show=False
            ),
            splitarea_opts=opts.SplitAreaOpts(
                is_show=False
            ),
            axislabel_opts=opts.LabelOpts(
                interval=0
            )
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(
                is_show=False
            ),
            splitline_opts=opts.SplitLineOpts(
                is_show=False
            ),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color="#90979c"
                )
            ),
            axislabel_opts=opts.LabelOpts(
                interval=0
            ),
            splitarea_opts=opts.SplitAreaOpts(
                is_show=False
            )
        ),
        datazoom_opts=opts.DataZoomOpts(
            is_show=True,
            xaxis_index=[0],
            pos_bottom=30,
            start_value=10,
            end_value=80
        )
    )
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="女",
        y_axis=y_data,
        stack="总量",
        label_opts=opts.LabelOpts(
            is_show=True,
            color="#fff",
            position="inside"
        ),
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgba(255,144,128,1)"
        )
    )
    .add_yaxis(
        series_name="男",
        y_axis=y2_data,
        stack="总量",
        label_opts=opts.LabelOpts(
            is_show=True,
            color="#fff",
            position="inside"
        ),
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgba(0,191,183,1)"
        )
    )
)


# 折线图对象
line = Line()
# 设置图形的全局参数
(
    line.set_global_opts()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="总数",
        y_axis=y3_data,
        symbol="circle",
        symbol_size=10,
        is_symbol_show=True,
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgba(252,230,48,1)",
            border_width=0,

        ),
        label_opts=opts.LabelOpts(
            is_show=True,
            position="top"
        ),
        linestyle_opts=opts.LineStyleOpts(
            width=2,
        )
    )
)

bar.overlap(line)
(
    Grid(opts.InitOpts(bg_color="#344b58"))
    .add(
        bar,
        opts.GridOpts()
    )
).render("pyecharts_bar.html")