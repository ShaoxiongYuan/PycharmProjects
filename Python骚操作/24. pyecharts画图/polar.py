import random
from pyecharts import options as opts
from pyecharts.charts import Polar


def polar_scatter0() -> Polar:
    data = [(alpha, random.randint(1, 100)) for alpha in range(101)]
    print(data)
    c = (
        Polar().add("", data,
                    type_="bar",
                    label_opts=opts.LabelOpts(is_show=False)).set_global_opts(
            title_opts=opts.TitleOpts(title="Polar")
        )
    )
    return c


polar_scatter0().render('./data/polar.html')
