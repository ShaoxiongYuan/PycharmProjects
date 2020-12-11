######
#作者：zglg
#时间:2020-09-22
#python == 3.7
#pyecharts == 1.8.1
######

from pyecharts.globals import ThemeType
import pyecharts.options as opts
from pyecharts.charts import Radar, Timeline

vdata = [[[85, 65, 55, 90, 82]],[[50, 20, 45, 30, 75]],[[37, 80, 12, 50, 25]]]
series=['2016','2017','2018']
c = ['#00c2ff','#f9cf67','#e92b77'] 

tl = Timeline(init_opts=opts.InitOpts(theme=ThemeType.DARK)) # pyecharts 的bug ，bg_color 不起作用

for i in range(3):
    rad = (
        Radar()
        .set_global_opts(
            legend_opts=opts.LegendOpts(
                is_show=True,
                pos_bottom=45,
                item_width=14,
                item_height=14,
                textstyle_opts=opts.TextStyleOpts(
                    font_size=14,
                    color='#ade3ff'
                ) 
            )
        )
        .add_schema(
            schema=[
                opts.RadarIndicatorItem(name="灵活性", max_=100,color='#98F5FF'),
                opts.RadarIndicatorItem(name="功能性", max_=100,color='#98F5FF'),
                opts.RadarIndicatorItem(name="平稳性", max_=100,color='#98F5FF'),
                opts.RadarIndicatorItem(name="安全性", max_=100,color='#98F5FF'),
                opts.RadarIndicatorItem(name="耐用性", max_=100,color='#98F5FF'),
            ],
            center=['50%', '50%'],
            textstyle_opts=opts.TextStyleOpts(
                color='red',
            ),
            splitline_opt=opts.SplitLineOpts(
                    is_show= True,
                    linestyle_opts=opts.LineStyleOpts(
                        color='#98F5FF',
                        width=1,
                        type_='dotted'
                    )
                ),
            axisline_opt=opts.AxisLineOpts(
                    linestyle_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(
                        color='#98F5FF',
                        )
                    )
                ),
            splitarea_opt=opts.SplitAreaOpts(
                is_show=True,
                areastyle_opts=opts.AreaStyleOpts(
                    color=['#141c42', '#141c42']
                )
            )
        )
        .add(
            series_name=series[i],
            data=vdata[i],
            color=c[i],
            label_opts=opts.LabelOpts({                                               
                    "normal": {  
                    "show": True,            
                    "position": 'top',       
                    "distance": 2,            
                    "color": '#6692e2',         
                    "fontSize": 14,            
                    }  
                }
            ),  
        )
        .set_series_opts(
            linestyle_opts=opts.LineStyleOpts(
                width=2
            )
        )
    )
    tl.add(rad, "{}年".format(series[i]))

tl.render("timeline_radar.html")