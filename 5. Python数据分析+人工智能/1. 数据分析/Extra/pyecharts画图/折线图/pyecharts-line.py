######
# 作者：zglg
# 时间:2020-09-12
# python == 3.7
# pyecharts==1.7.1
######

import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType

x_data = [str(i) + '日' for i in range(1, 31)]
y_data = [509, 917, 2455, 2610, 2719, 3033, 3044, 3085, 2708, 2809, 2117, 2000, 1455, 1210, 719,
          733, 944, 2285, 2208, 3372, 3936, 3693, 2962, 2810, 3519, 2455, 2610, 2719, 2484, 2078]

y2_data = [
    2136, 3693, 2962, 3810, 3519, 3484, 3915, 3823, 3455, 4310, 4019, 3433, 3544, 3885, 4208, 3372,
    3484, 3915, 3748, 3675, 4009, 4433, 3544, 3285, 4208, 3372, 3484, 3915, 3823, 4265, 4298]

(
    # 折线图对象
    Line(opts.InitOpts(
        bg_color="#1A1835",
    ))
        # 设置图形的全局参数
        .set_global_opts(

        tooltip_opts=opts.TooltipOpts(is_show=False),
        legend_opts=opts.LegendOpts(
            textstyle_opts=opts.TextStyleOpts(
                color='#90979c'
            )
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color="rgba(204,187,225,0.5)"
                )
            ),
            splitline_opts=opts.SplitLineOpts(
                is_show=False
            ),
            axistick_opts=opts.AxisTickOpts(
                is_show=False
            )
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(
                is_show=True
            ),
            splitline_opts=opts.SplitLineOpts(
                is_show=False
            ),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color="rgba(204,187,225,0.5)"
                )
            ),

        ),
        datazoom_opts=opts.DataZoomOpts(
            is_show=True,
        )
    )
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
        series_name="访问量",
        y_axis=y_data,
        symbol="circle",
        symbol_size=10,
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
        itemstyle_opts=opts.ItemStyleOpts(
            color="#6f7de3"
        ),
        markpoint_opts=opts.MarkPointOpts(
            label_opts=opts.LabelOpts(
                color='#fff'
            ),
            data=[opts.MarkPointItem(
                type_='max',
                name='最大值'
            ), opts.MarkPointItem(
                type_='min',
                name='最小值'
            )]
        )
    )
        .add_yaxis(
        series_name="订单量",
        y_axis=y2_data,
        symbol="circle",
        symbol_size=10,
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
        itemstyle_opts=opts.ItemStyleOpts(
            color="#c257F6"
        ),
        markpoint_opts=opts.MarkPointOpts(
            label_opts=opts.LabelOpts(
                color='#fff'
            ),
            data=[opts.MarkPointItem(
                type_='max',
                name='最大值'
            ), opts.MarkPointItem(
                type_='min',
                name='最小值'
            )]
        )
    )
        .render("basic_line_chart.html")
)
