from pyecharts import options as opts
from pyecharts.charts import Graph


def graph_base() -> Graph:
    nodes = [
        {"name": "cus1", "symbolSize": 10},
        {"name": "cus2", "symbolSize": 30},
        {"name": "cus3", "symbolSize": 20}
    ]
    links = []
    for i in nodes:
        if i.get('name') == 'cus1':
            continue
        for j in nodes:
            if j.get('name') == 'cus1':
                continue
            links.append({"source": i.get("name"), "target": j.get("name")})
    c = (
        Graph().add("", nodes, links, repulsion=8000).set_global_opts(
            title_opts=opts.TitleOpts(title="customer-influence"))
    )
    return c


graph_base().render('./data/graph.html')
