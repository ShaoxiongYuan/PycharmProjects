"""
@作者：zglg
@时间:2020-10-1
@python == 3.7
@pyecharts == 1.8.1
@ref: https://pyecharts.org/#/zh-cn/geography_charts?id=geo%ef%bc%9a%e5%9c%b0%e7%90%86%e5%9d%90%e6%a0%87%e7%b3%bb
"""

from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Geo, Timeline
from pyecharts.globals import ChartType, SymbolType
from pyecharts.commons.utils import JsCode

data = [
    [("广州", 455), ("北京", 260), ("杭州", 1000),
     ("青海", 800), ("乌鲁木齐", 125), ("西藏", 100)],
    [("南京", 120), ("西藏", 260), ("成都", 1000), ("北京", 800), ("吉林", 650)],
    [("南京", 120), ("西藏", 260), ("太原", 420),
     ("成都", 1000), ("北京", 800), ("吉林", 650)]
]
datapair = [
    [("广州", "北京"), ("广州", "杭州"), ("广州", "青海"), ("广州", "乌鲁木齐"), ("广州", "西藏")],
    [("北京", "南京"), ("北京", "西藏"), ("北京", "成都"), ("北京", "吉林")],
    [("南京", "北京"), ("南京", "西藏"), ("南京", "成都"), ("南京", "吉林"), ("南京", "太原")]
]
series = ['2017', '2018', '2019']

tl = (
    Timeline(
        init_opts=opts.InitOpts(
            theme=ThemeType.DARK
        )
    )
        .add_schema(
        is_auto_play=True,
        play_interval=6000
    )
)


def genGeo(data, datapair):
    c = (
        Geo(init_opts=opts.InitOpts(
            bg_color='#344b58',
        ))
            .add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(
                border_color='#344b58',
                border_width=2.0,
                area_color='rgba(0,0,0,0)',
                color="#eeeeee",
            ),
            label_opts=opts.LabelOpts(
                is_show=False,
                color='rgba(255,144,128,1)',
            ),
            emphasis_itemstyle_opts=opts.ItemStyleOpts(
                area_color='rgba(0,0,0,0)'
            ),
            emphasis_label_opts=opts.LabelOpts(
                is_show=False
            ))
            .add(  # 添加动态散点图
            "",
            data,
            type_=ChartType.EFFECT_SCATTER,
            # symbol_size=20,
            effect_opts=opts.EffectOpts(
                period=5,
                scale=5,
                brush_type='fill'
            ),
            label_opts=opts.LabelOpts(
                is_show=True,
                formatter="{b}",
                color="rgba(255,144,128,1)",
                border_width=2.,
                font_size=18,
            )
        )
            .add(  # 添加线段图
            "geo",
            datapair,
            type_=ChartType.LINES,
            symbol_size=7,
            effect_opts=opts.EffectOpts(
                symbol="circle",
                symbol_size=8,
                trail_length=0.08,
                color="rgba(255,144,128,1)"
            ),
            linestyle_opts=opts.LineStyleOpts(
                curve=0.5,
                width=2.5,
                opacity=0.8,
                color=JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: '#00acea'
                    }, {
                        offset: 1,
                        color: '#FF8C00'
                    }])"""
                )
            ),
            label_opts=opts.LabelOpts(
                is_show=False
            )
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="十一人口流动图"
            ),
            visualmap_opts=opts.VisualMapOpts(
                min_=0,
                max_=1000,
                textstyle_opts=opts.TextStyleOpts(
                    color='white'
                )
            ),
            legend_opts=opts.LegendOpts(
                is_show=False
            ),
            tooltip_opts=opts.TooltipOpts(
                trigger="item",
                formatter='{b}'
            ),
        )
    )
    tl.add(c, "{}年".format(series[i]))


for i in range(3):
    genGeo(data[i], datapair[i])

tl.render("timeline_geo.html")
