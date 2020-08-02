from pyecharts import options as opts
from pyecharts.charts import WordCloud

words = [
    ("Python", 100),
    ("C++", 80),
    ("Java", 95),
    ("R", 50),
    ("JavaScript", 79),
    ("C", 65)
]


def wordcloud() -> WordCloud:
    c = (
        WordCloud().add("", words,
                        word_size_range=[20, 100],
                        shape='cardioid').set_global_opts(
            title_opts=opts.TitleOpts(title="WordCloud")
        )
    )
    return c


wordcloud().render('./data/wordcloud.html')
