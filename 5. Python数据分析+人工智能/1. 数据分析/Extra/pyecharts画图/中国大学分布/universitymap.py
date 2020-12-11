from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType
from pyecharts.commons.utils import JsCode

data = [("江苏", 77), ("广东", 67), ("山东", 70), ("河南", 57), ("湖北", 68), ("四川", 52), ("湖南", 51), ("河北",
                                                                                             61), ("安徽", 46),
        ("辽宁", 64), ("浙江", 59), ("江西", 45), ("陕西", 57), ("北京", 68), ("福建", 39),
        ("山西", 33), ("云南", 32), ("黑龙江", 39), ("广西", 38), ("贵州", 29), ("重庆", 26), ("上海", 39), ("吉林", 37),
        ("天津", 30), ("新疆", 18), ("内蒙古", 17), ("甘肃", 22), ("海南", 8), ("宁夏", 8), ("青海", 4), ("西藏", 4)]

datac = [(it[0], it[1] * 10) for it in data]


def genGeo(data):
    c = (
        Geo(init_opts=opts.InitOpts(
            width='1800px',
            height='1000px',
            bg_color='#0F1C3C',
        ))
            .add_schema(
            maptype='china',
            itemstyle_opts=opts.ItemStyleOpts(
                border_color=JsCode(
                    """
                    new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#00F6FF'
                }, {
                    offset: 1,
                    color: '#53D9FF'
                }], false)
                    """
                ),
                color0='rgba(10,76,139,1)',
                border_width=1.0,
                opacity=0.8,
                color="#012366",
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
        )
            .add(  # 添加散点图
            "",
            data,
            symbol_size=20,
            color='#EA7552',
            label_opts=opts.LabelOpts(
                is_show=True,
                color="#0f0",
                border_width=2.,
                font_size=18,
                position="inside",
                formatter=JsCode(
                    """
                    function f(param){
                        return param.name + ','+ param.value[2]/10
                    }
                    """
                ),
            )
        )
            .set_series_opts(
            range_size=[12, 40],
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=1.0,
                border_color='#215495',
            ),
            areastyle_opts=opts.AreaStyleOpts(
                color={
                    "x": 0,
                    "y": 0,
                    "x2": 0,
                    "y2": 1,
                    "colorStops": [{
                        "offset": 0,
                        "color": '#073684'
                    }, {
                        "offset": 1,
                        "color": '#061E3D'
                    }],
                }
            )
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="全国本科院校分布图",
                pos_left='40%',
                pos_top='10%',
                title_textstyle_opts=opts.TextStyleOpts(
                    color='white',
                    font_size=20
                )
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                type_='size',
                min_=4 * 10,
                max_=80 * 10,
            ),
            legend_opts=opts.LegendOpts(
                is_show=False
            ),
            tooltip_opts=opts.TooltipOpts(
                trigger="item",
                formatter=JsCode(
                    """
                    function f(param){
                        return param.name + ','+ param.value[2]/10
                    }
                    """
                )
            )
        )
            .render("university-geo.html")
    )


genGeo(datac)
