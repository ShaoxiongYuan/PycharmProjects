import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode

ds = [('河南', 57), ('陕西', 57), ('浙江', 59), ('河北', 61), ('辽宁', 64), ('广东', 67), ('湖北', 68), ('北京', 68), ('山东', 70),
      ('江苏', 77)]

x_data = [it[0] for it in ds]
y1_data = [it[1] for it in ds]

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
            max_=90,
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
        series_name="本科院校",
        y_axis=y1_data,
        label_opts=opts.LabelOpts(
            is_show=False
        ),
        bar_width='25%',
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
).render("university-top.html")
