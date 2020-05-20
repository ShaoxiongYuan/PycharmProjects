from django.db import models
import json
from json.encoder import JSONEncoder
# Create your models here.

class Stock(models.Model):
    stonumber = models.CharField(max_length=20,null=False,verbose_name='股票编码')
    company_name = models.CharField(max_length=64, verbose_name='公司名称')
    industry = models.CharField(blank=True, null=True, max_length=200, verbose_name='细分行业')
    area = models.CharField(max_length=30, blank=True, null=True, verbose_name='地区')
    pe = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='市盈率')
    outstanding = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='流通股本(亿)')
    totals = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='总股本(亿)')
    totalAssets = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='总资产(万)')
    liquidAssets = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='流动资产')
    fixedAssets = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='固定资产')
    reserved = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='公积金')
    reservedPerShare = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='每股公积金')
    esp = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='每股收益')
    bvps = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='每股净资')
    pb = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='市净率')
    timeToMarket = models.DateField(verbose_name='上市日期')


    def __str__(self):
        return str(self.stonumber)


    def model_to_dict(self):
        stockde = {}
        stockde['stonumber'] = self.stonumber
        stockde['company_name'] = self.company_name
        stockde['industry'] = self.industry
        stockde['area'] = self.area
        stockde['pe'] = str(self.pe)
        stockde['outstanding'] = str(self.outstanding)
        stockde['totals'] = str(self.totals)
        stockde['totalAssets'] = str(self.totalAssets)
        stockde['liquidAssets'] = str(self.liquidAssets)
        stockde['fixedAssets'] = str(self.fixedAssets)
        stockde['reserved'] = str(self.reserved)
        stockde['reservedPerShare'] = str(self.reservedPerShare)
        stockde['esp'] = str(self.esp)
        stockde['bvps'] = str(self.bvps)
        stockde['pb'] = str(self.pb)
        stockde['timeToMarket'] = self.timeToMarket.strftime('%Y-%m-%d %H:%M:%S')
        return stockde


    class Meta:
        db_table = 'Stock'
        verbose_name = '股票信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']


class Link(models.Model):
    title = models.CharField(max_length=50,blank=True, null=True, verbose_name='标题')
    callback_url = models.URLField(blank=True, null=True, verbose_name='url地址')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.title



class StockPredictionModel(object):
    ''' 股价预测模型
    当前类根据传入的某支股票K线数据进行量化分析，从股价趋势线、布林带、OBV、
    5日移动均线、10日移动均线等指标分析后得出分析结果，最终给出建议：买入、卖出、持有

    Attributes:
        kdata:  存储当前股票每天的k线数据，结构如下：
                |date|opening_price|highest_price|lowest_price|closing_price|volume|
                date: 交易日期
                opening_price: 开盘价
                highest_price: 最高价
                lowest_price:  最低价
                closing_price: 收盘价
                volume:        当日交易量
    '''
    def __init__(self, kdata):
        '''
        kdata 当前股票数据
        '''
        self.kdata = kdata

    def analysis():
        '''分析当前股票的kdata，得出不同指标下的结论，返回分析结果。
            dic: 
        '''
        dic = {}


        return dic

    # 最小二乘多项式拟合
    def linearregression(self, date, valdata):
        # 讲日期类型转为int
        days = date.astype(int)
        p = np.polyfit(days, valdata, 4)
        # 预测未来一天数据
        date_fea = np.zeros((1, ))
        num = days[0] + 1
        date_fea[0, ] = num
        return np.polyval(p, date_fea)
    
    # 布林带
    '''
    中规往往是一条中期均线
    上轨和下轨分别是中轨加上或减去同期收盘价的标准差固定的倍数，标准版为2倍
    '''
    def boll(self, date, ma5, closing_price):
        # 求标准差
        stds = np.zeros(ma5.size - 5)
        for i in range(0, stds.size):
            # print(stds.shape)
            stds[i] = closing_price[i:i + 5,].std()
        stds *= 2
        lower = ma5[:stds.size,] - stds
        upper = ma5[:stds.size,] + stds
        return self.linearregression(date, lower), self.linearregression(date, upper), lower, upper

    # OBV
    def obv(self, diff, volume):
        return diff * volume
        
    # 多项式线性拟合
    def line(self, x, y, t):
        #调用线性规划包
        model = LinearRegression()
        #线性回归训练
        model.fit(x, y)
        #截距
        a = model.intercept_
        #回归系数
        b = model.coef_
        print("拟合参数:截距",a,",回归系数：",b)
        Y_pred = model.predict(t)
        print('今日收盘价',y[0, 0], '预测明日收盘价',Y_pred[0, 0])
        plt.plot(y)
        plt.plot(Y_pred, c='red')
        plt.show()
        if y[0, 0] > Y_pred[0, 0]:
            return '建议卖出'
        elif y[0, 0] <= Y_pred[0, 0]:
            return '建议买入'
        

    def main(self):
        date, opening_price, closing_price, volume, diff, ma5 = \
            self.date, self.opening_price, self.closing_price, self.volume, self.diff, self.ma5
        # 预测后一天的开盘价，ma5,布林下线，布林上线，obv
        preopen = self.linearregression(date, opening_price)
        prema5 = self.linearregression(date, ma5)
        prelower, preupper, lower, upper = self.boll(date[:-5], ma5, closing_price)
        obvs = self.obv(diff, volume)
        preobv = self.linearregression(date, obvs)
        x = np.array([opening_price[:-5], ma5[:-5], lower, upper, obvs[:-5]]).T
        y = np.array([closing_price[:-5]],).T
        t = np.array([preopen, prema5, prelower, preupper, preobv]).T
        return self.line(x, y, t)
