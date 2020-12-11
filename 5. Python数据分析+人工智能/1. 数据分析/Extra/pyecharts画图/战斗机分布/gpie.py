# 作者：zglg
# 时间:2020-09-23
# python == 3.7
# pyecharts == 1.8.1

from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
from pyecharts.globals import JsCode

datalist = [[['H-6K轰炸机', 80], ['J-10歼机', 155], ['JH-7飞豹', 30], ['Q-5强机', 90]],
            [['H-6K轰炸机', 100], ['J-10歼机', 180], ['JH-7飞豹', 50], ['Q-5强机', 101]],
            [['H-6K轰炸机', 120], ['J-10歼机', 235], ['JH-7飞豹', 70], ['Q-5强机', 118]]
            ]
years = [2016, 2017, 2018]

rich = {
    "yellow": {
        "color": "#ffc72b",
        "fontSize": 30,
        "padding": [5, 4],
        "align": 'center'
    },
    "total": {
        "color": "#ffc72b",
        "fontSize": 40,
        "align": 'center'
    },
    "white": {
        "color": "#fff",
        "align": 'center',
        "fontSize": 14,
        "padding": [21, 0]
    },
    "blue": {
        "color": '#49dff0',
        "fontSize": 16,
        "align": 'center'
    },
    "hr": {
        "borderColor": '#0b5263',
        "width": '100%',
        "borderWidth": 1,
        "height": 0,
    }
}

tl = (
    Timeline(init_opts=opts.InitOpts(
        theme=ThemeType.DARK
    )
    )
        .add_schema(
        is_auto_play=True,
        play_interval=1500)
)

for i in range(3):
    p = (
        Pie(init_opts=opts.InitOpts(
            bg_color='#031f2d',
        ))
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="%d年\n\n不同空军机型统计" % (years[i],),
                pos_left='center',
                pos_top='40%',
                padding=[24, 0],
                title_textstyle_opts=opts.TextStyleOpts(
                    color='#fff',
                    font_size=18,
                    align='center'
                )
            ),
            legend_opts=opts.LegendOpts(
                type_="scroll",
                pos_left="80%",
                orient="vertical",
                textstyle_opts=opts.TextStyleOpts(
                    color='#fff',
                    font_size=16,
                    rich=rich
                ),
            )
        )
            .add(
            "xilie1",
            datalist[i],
            radius=['42%', '50%'],
            label_opts=opts.LabelOpts(
                position="outside",
                rich=rich,
                formatter="{white|{b}} \n{hr|}\n{yellow|{c}}\n{blue|{d}%}"
                # 参数说明：{a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）
            )
        )
    )
    tl.add(p, "{}年".format(years[i]))

tl.render("timeline_pie.html")
