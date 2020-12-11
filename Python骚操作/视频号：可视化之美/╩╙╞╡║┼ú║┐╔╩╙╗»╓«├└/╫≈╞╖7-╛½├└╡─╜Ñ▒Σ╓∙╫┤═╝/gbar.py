######
#作者：zglg
#时间:2020-09-20
#python == 3.7
#pyecharts == 1.8.1
######


import pyecharts.options as opts
from pyecharts.charts import Bar, Line, Grid
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode

x_data = ['2012','2013','2014','2015','2016','2017','2018','2019']
y1_data = [200, 400, 300, 300, 300, 400, 400, 600, 300]
y2_data = [350, 500, 500, 500, 500, 400,200, 500, 500]
y3_data = [400, 600, 700, 700, 1000, 100, 400, 900, 700]


# 折线图对象
bar = Bar(opts.InitOpts(bg_color="#323a5e"))
# 设置图形的全局参数
(
    bar.set_global_opts(
        legend_opts=opts.LegendOpts(
            pos_top=12,
            pos_right=10,
            textstyle_opts=opts.TextStyleOpts(
                color='#fff'
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
                    color="white"
                )
            ),
            axislabel_opts=opts.LabelOpts(
            )
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            max_=1200,
            axistick_opts=opts.AxisTickOpts(
                is_show=False
            ),
            splitline_opts=opts.SplitLineOpts(
                is_show=True,
                linestyle_opts=opts.LineStyleOpts(
                    color='rgba(255,255,255,0.3)'
                ),
            ),
            axisline_opts=opts.AxisLineOpts(
                is_show=False,
                linestyle_opts=opts.LineStyleOpts(
                    color="white"
                )
            ),
            axislabel_opts=opts.LabelOpts()
        ),
        datazoom_opts=opts.DataZoomOpts(
            is_show=True,
            pos_bottom='2%',
            pos_top='94%'        
        )
    )
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="1",
        y_axis=y1_data,
        label_opts=opts.LabelOpts(
            is_show=False
        ),
        bar_width='15%',
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#fccb05'
                }, {
                    offset: 1,
                    color: '#f5804d'
                }])"""
                ),
                "barBorderRadius": 11,
            }
        }
    )
    .add_yaxis(
        series_name="2",
        y_axis=y2_data,
        label_opts=opts.LabelOpts(
            is_show=False
        ),
        bar_width='15%',
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#8bd46e'
                }, {
                    offset: 1,
                    color: '#09bcb7'
                }])"""
                ),
                "barBorderRadius": 11,
            }
        }
    )
    .add_yaxis(
        series_name="3",
        y_axis=y3_data,
        label_opts=opts.LabelOpts(
            is_show=False
        ),
        bar_width='15%',
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#248ff7'
                }, {
                    offset: 1,
                    color: '#6851f1'
                }])"""
                ),
                "barBorderRadius": 11,
            }
        }
    )

).render("gradient_bar.html")