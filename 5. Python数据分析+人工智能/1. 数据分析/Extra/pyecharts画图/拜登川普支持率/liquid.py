"""
@作者：zglg
@时间:2020-10-4
@python == 3.7
pip install pyecharts == 1.8.1
"""

from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode

import pyecharts

print(pyecharts.__version__)


def buildLiquid(name, data, center):
    l1 = (
        Liquid()
            .add(
            name,
            data,
            center=center,
            label_opts=opts.LabelOpts(
                position="inside",
                color="white",
            ),
            background_color={
                "type": 'linear',
                "x": 1,
                "y": 0,
                "x2": 0.5,
                "y2": 1,
                "colorStops": [{
                    "offset": 1,
                    "color": 'rgba(68, 145, 253, 0)'
                }, {
                    "offset": 0.5,
                    "color": 'rgba(68, 145, 253, .25)'
                }, {
                    "offset": 0,
                    "color": 'rgba(68, 145, 253, 1)'
                }],
                "globalCoord": False
            },
            color=[{
                "type": 'linear',
                "x": 0,
                "y": 0,
                "x2": 0,
                "y2": 1,
                "colorStops": [{
                    "offset": 1,
                    "color": 'rgba(58, 71, 212, 0)'
                }, {
                    "offset": 0.5,
                    "color": 'rgba(31, 222, 225, .2)'
                }, {
                    "offset": 0,
                    "color": 'rgba(31, 222, 225, 1)'
                }],
                "globalCoord": False
            }],
            outline_border_distance=0.,
            outline_itemstyle_opts=opts.ItemStyleOpts(
                border_width=20,
                border_color={
                    "type": 'linear',
                    "x": 0,
                    "y": 0,
                    "x2": 0,
                    "y2": 1,
                    "colorStops": [{
                        "offset": 0,
                        "color": 'rgba(69, 73, 240, 0)'
                    }, {
                        "offset": 0.5,
                        "color": 'rgba(69, 73, 240, .25)'
                    }, {
                        "offset": 1,
                        "color": 'rgba(69, 73, 240, 1)'
                    }],
                    "globalCoord": False
                }
            )
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="拜登和川普最新支持率",
                title_link="https://new.qq.com/omn/20201004/20201004A0098Z00.html",
                pos_left="32%",
                pos_top="15%",
                title_textstyle_opts=opts.TextStyleOpts(
                    color="white",
                    font_size=30,
                )
            )
        )
    )
    return l1


l1 = buildLiquid("拜登", [0.65], ["30%", "50%"])
l2 = buildLiquid("川普", [0.35], ["70%", "50%"])

grid = (
    Grid(init_opts=opts.InitOpts(
        bg_color=JsCode(
            """
            new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
            offset: 0,
            color: '#431ab8'
            }, {
            offset: 1,
            color: '#471bba'
            }])
            """
        )
    ))
        .add(
        l1,
        grid_opts=opts.GridOpts()
    )
        .add(
        l2,
        grid_opts=opts.GridOpts()
    )
)

grid.render("multiple_liquid.html")
