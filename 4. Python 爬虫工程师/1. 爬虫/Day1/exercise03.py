import re

html = '''<div class="animal">
    <p class="name">
        <a title="Tiger"></a>
    </p>

    <p class="content">
        Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
        <a title="Rabbit"></a>
    </p>

    <p class="content">
        Small white rabbit white and white
    </p>
</div>'''

pattern = re.compile(r'.*?title="(.*?)".*?">(.*?)</p>.*?', re.S)

res = pattern.findall(html)

for item in res:
    print('动物名称：' + item[0])
    print('动物描述：' + item[1].strip())
    print('********************************************')
