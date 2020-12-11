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
    [("南京", 12), ("拉萨", 14), ("成都", 10), ("北京", 40), ("吉林", 20), ("乌鲁木齐", 5), ("拉萨", 6)
        , ("昆明", 10), ("遵义", 3), ("榆林", 6), ("合肥", 24), ("武汉", 35), ("上海", 50), ("沈阳", 28), ("长春", 23)],
    [("广州", 45), ("北京", 20), ("杭州", 10), ("青海", 30), ("乌鲁木齐", 12), ("拉萨", 10)],
    [("南京", 12), ("拉萨", 30), ("太原", 12), ("成都", 20), ("北京", 50), ("吉林", 20)]
]
datapair = [
    [("南京", "北京"), ("拉萨", "北京"), ("成都", "北京"), ("吉林", "北京"), ("乌鲁木齐", "北京"),
     ("拉萨", "北京"), ("昆明", "北京"), ("遵义", "北京"), ("榆林", "北京"), ("武汉", "北京")
        , ("上海", "北京"), ("沈阳", "北京"), ("长春", "北京")],
    [("北京", "广州"), ("杭州", "广州"), ("青海", "广州"), ("乌鲁木齐", "广州"), ("拉萨", "广州")],
    [("北京", "南京"), ("拉萨", "南京"), ("成都", "南京"), ("吉林", "南京"), ("太原", "南京")]
]

series = ['北京', '广州', '南京']

planepath = "path://M1705.06,1318.313v-89.254l-319.9-221.799l0.073-208.063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0.305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221.799v89.254l330.343-157.288l12.238,241.308l-134.449,92.931l0.531,42.034l175.125-42.917l175.125,42.917l0.531-42.034l-134.449-92.931l12.238-241.308L1705.06,1318.313z"

tl = (
    Timeline(
        init_opts=opts.InitOpts(
            theme=ThemeType.DARK
        )
    )
        .add_schema(
        is_auto_play=True,
        play_interval=8000,
        is_timeline_show=False,

    )
)


def genGeo(data, datapair):
    c = (
        Geo(init_opts=opts.InitOpts(
            bg_color='rgba(46, 63, 81, 127)',
        ))
            .add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(
                border_color='#445973',
                border_width=1.0,
                color="rgba(46, 63, 81, 127)",
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
            ),
            zoom=1.2,
            is_roam=False,
        )
            .add(  # 添加动态散点图
            "",
            data,
            type_=ChartType.EFFECT_SCATTER,
            # symbol_size=20,
            effect_opts=opts.EffectOpts(
                period=5,
                scale=3,
                brush_type='stroke',
                color='#0f0',
            ),
            label_opts=opts.LabelOpts(
                is_show=True,
                formatter="{b}",
                color="#0f0",
                border_width=2.,
                font_size=13,
                position="right",
            )
        )
            .add(  # 添加线段图
            "geo",
            datapair,
            type_=ChartType.LINES,
            symbol_size=10,
            effect_opts=opts.EffectOpts(
                is_show=True,
                symbol=planepath,
                symbol_size=20,
                trail_length=0.,
                color="#0f0",
            ),
            linestyle_opts=opts.LineStyleOpts(
                curve=0.3,
                width=1.0,
                opacity=0.8,
                color="#99CC99"
            ),
            label_opts=opts.LabelOpts(
                is_show=False
            )
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="十一飞机流动图"
            ),
            visualmap_opts=opts.VisualMapOpts(
                min_=0,
                max_=50,
                textstyle_opts=opts.TextStyleOpts(
                    color='#f00'
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
    tl.add(c, "{}".format(series[i]))


for i in range(3):
    genGeo(data[i], datapair[i])

tl.render("timeline_geo.html")
