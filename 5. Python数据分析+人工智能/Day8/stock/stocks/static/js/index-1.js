$(() => {
    //K线图
    var upColor = '#00da3c';
    var downColor = '#ec0000';
    var myChart = echarts.init(document.getElementById("chart-panel"));

    function splitData(rawData) {
        var categoryData = [];
        var values = [];
        var volumes = [];
        for (var i = 0; i < rawData.length; i++) {
            categoryData.push(rawData[i].splice(0, 1)[0]);
            values.push(rawData[i]);
            volumes.push([i, rawData[i][4], rawData[i][0] > rawData[i][1] ? 1 : -1]);
        }

        return {
            categoryData: categoryData,
            values: values,
            volumes: volumes
        };
    }

    function calculateMA(dayCount, data) {
        var result = [];
        for (var i = 0, len = data.values.length; i < len; i++) {
            if (i < dayCount) {
                result.push('-');
                continue;
            }
            var sum = 0;
            for (var j = 0; j < dayCount; j++) {
                sum += data.values[i - j][1];
            }
            result.push(+(sum / dayCount).toFixed(3));
        }
        return result;
    }

    function k(code) {
        //K线图
        $.ajax({
            type: "get",
            url: $baseUrl + '/stock/kdata',
            data: {
                code: code
            },
            success: function (rawData) {
                var indexData = JSON.parse(rawData);
                // console.log(JSON.parse(rawData));
                //深度图
                var deepData = indexData.data.stockdeep;
                if (deepData != "") {
                    var deepHTML = `<tr data-v-642d2254="">
                        <th data-v-642d2254="" class="type">类型</th>
                        <th data-v-642d2254="" class="price">价格</th>
                        <th data-v-642d2254="" class="quantity">数量</th>
                        <th data-v-642d2254="" class="total pc">交易时间</th>
                        <th data-v-642d2254="" class="room"></th>
                    </tr>`;
                    for (var item of deepData) {
                        deepHTML += `<tr data-v-642d2254="">
                            <td data-v-642d2254="" class="type" width="150px;">${item.role}</td>
                            <td data-v-642d2254="" class="price">${item.price}</td>
                            <td data-v-642d2254="" class="quantity">${item.amount}</td>
                            <td data-v-642d2254="" class="total pc">${item.datetime}</td>
                            <div data-v-642d2254="" class="background redbg" style="width: 20%;"></div>
                        </tr>`;
                    }
                    $(".tableDeep").html(deepHTML);
                } else {
                    $(".tableDeep").html("暂无数据！");
                }

                //输出预测结果：
                prediction = indexData.prediction
                console.log('11111111111111111111'+JSON.stringify(prediction))
                var deepHTML = `<tr data-v-642d2254="">
                    <th data-v-642d2254="" class="type">指标</th>
                    <th data-v-642d2254="" class="price">建议</th>
                </tr>`;
                for (item in prediction) {
                    console.log(prediction[item])
                    deepHTML += `<tr data-v-642d2254="">
                        <td data-v-642d2254="" class="type" width="150px;">${item}</td>
                        <td data-v-642d2254="" class="price">`+prediction[item]+`</td>
                        <div data-v-642d2254="" class="background redbg" style="width: 20%;"></div>
                    </tr>`;
                }
                $(".tableDeep").html(deepHTML);


                var kTitleData = indexData.data.stockdata;
                // console.log(kTitleData);
                var titleHTML = `<div data-v-0fea8eec="" class="title">
                        <div data-v-0fea8eec="" class="title">${kTitleData.name}</div>
                    </div>
                    <div data-v-0fea8eec="" class="newprice">
                        <div data-v-0fea8eec="" class="title">当前价格</div>
                        <div data-v-0fea8eec="" class="value">${kTitleData.price}</div>
                    </div>
                    <div data-v-0fea8eec="" class="lowprice pc">
                        <div data-v-0fea8eec="" class="title">开盘价</div>
                        <div data-v-0fea8eec="" class="value">${kTitleData.open_price}</div>
                    </div>
                    <div data-v-0fea8eec="" class="higprice pc">
                        <div data-v-0fea8eec="" class="title">收盘价</div>
                        <div data-v-0fea8eec="" class="value">${kTitleData.pre_close}</div>
                    </div>
                    <div data-v-0fea8eec="" class="twentyfourhourstradingvolume">
                        <div data-v-0fea8eec="" class="title">最高价</div>
                        <div data-v-0fea8eec="" class="value">${kTitleData.high}</div>
                    </div>
                    <div data-v-0fea8eec="" class="buyone pc">
                        <div data-v-0fea8eec="" class="title">最低价</div>
                        <div data-v-0fea8eec="" class="value">${kTitleData.low}</div>
                    </div>
                    <div data-v-0fea8eec="" class="sellone pc">
                        <div data-v-0fea8eec="" class="title">成交量</div>
                        <div data-v-0fea8eec="" class="value">${kTitleData.volume}</div>
                    </div>
                    <div data-v-0fea8eec="" class="change">
                        <div data-v-0fea8eec="" class="title">成交金额</div>
                        <div data-v-0fea8eec="" class="value">${kTitleData.amount}</div>
                </div>`;
                $(".ktitleData").html(titleHTML)

                var rawData = JSON.parse(rawData).data.datastr;
                var data = splitData(rawData);
                myChart.setOption(option = {
                    backgroundColor: 'rgb(235,238,240)',
                    animation: false,
                    legend: {
                        bottom: 10,
                        left: 'center',
                        data: ['Dow-Jones index', 'MA5', 'MA10', 'MA20', 'MA30']
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross'
                        },
                        backgroundColor: 'rgba(245, 245, 245, 0.8)',
                        borderWidth: 1,
                        borderColor: '#ccc',
                        padding: 10,
                        textStyle: {
                            color: '#000'
                        },
                        position: function (pos, params, el, elRect, size) {
                            var obj = {
                                top: 10
                            };
                            obj[['left', 'right'][+(pos[0] < size.viewSize[0] / 2)]] = 30;
                            return obj;
                        }
                        // extraCssText: 'width: 170px'
                    },
                    axisPointer: {
                        link: {
                            xAxisIndex: 'all'
                        },
                        label: {
                            backgroundColor: '#777'
                        }
                    },
                    toolbox: {
                        feature: {
                            dataZoom: {
                                yAxisIndex: false
                            },
                            brush: {
                                type: ['lineX', 'clear']
                            }
                        }
                    },
                    brush: {
                        xAxisIndex: 'all',
                        brushLink: 'all',
                        outOfBrush: {
                            colorAlpha: 0.1
                        }
                    },
                    visualMap: {
                        show: false,
                        seriesIndex: 5,
                        dimension: 2,
                        pieces: [{
                            value: 1,
                            color: downColor
                        }, {
                            value: -1,
                            color: upColor
                        }]
                    },
                    grid: [{
                            left: '10%',
                            right: '8%',
                            height: '50%'
                        },
                        {
                            left: '10%',
                            right: '8%',
                            top: '63%',
                            height: '16%'
                        }
                    ],
                    xAxis: [{
                            type: 'category',
                            data: data.categoryData,
                            scale: true,
                            boundaryGap: false,
                            axisLine: {
                                onZero: false
                            },
                            splitLine: {
                                show: false
                            },
                            splitNumber: 20,
                            min: 'dataMin',
                            max: 'dataMax',
                            axisPointer: {
                                z: 100
                            }
                        },
                        {
                            type: 'category',
                            gridIndex: 1,
                            data: data.categoryData,
                            scale: true,
                            boundaryGap: false,
                            axisLine: {
                                onZero: false
                            },
                            axisTick: {
                                show: false
                            },
                            splitLine: {
                                show: false
                            },
                            axisLabel: {
                                show: false
                            },
                            splitNumber: 20,
                            min: 'dataMin',
                            max: 'dataMax'
                            // axisPointer: {
                            //     label: {
                            //         formatter: function (params) {
                            //             var seriesValue = (params.seriesData[0] || {}).value;
                            //             return params.value
                            //             + (seriesValue != null
                            //                 ? '\n' + echarts.format.addCommas(seriesValue)
                            //                 : ''
                            //             );
                            //         }
                            //     }
                            // }
                        }
                    ],
                    yAxis: [{
                            scale: true,
                            splitArea: {
                                show: true
                            }
                        },
                        {
                            scale: true,
                            gridIndex: 1,
                            splitNumber: 2,
                            axisLabel: {
                                show: false
                            },
                            axisLine: {
                                show: false
                            },
                            axisTick: {
                                show: false
                            },
                            splitLine: {
                                show: false
                            }
                        }
                    ],
                    dataZoom: [{
                            type: 'inside',
                            xAxisIndex: [0, 1],
                            start: 98,
                            end: 100
                        },
                        {
                            show: true,
                            xAxisIndex: [0, 1],
                            type: 'slider',
                            top: '85%',
                            start: 98,
                            end: 100
                        }
                    ],
                    series: [{
                            name: 'Dow-Jones index',
                            type: 'candlestick',
                            data: data.values,
                            itemStyle: {
                                normal: {
                                    color: upColor,
                                    color0: downColor,
                                    borderColor: null,
                                    borderColor0: null,
                                }
                            },
                            tooltip: {
                                formatter: function (param) {
                                    param = param[0];
                                    return [
                                        'Date: ' + param.name +
                                        '<hr size=1 style="margin: 3px 0">',
                                        'Open: ' + param.data[0] + '<br/>',
                                        'Close: ' + param.data[1] + '<br/>',
                                        'Lowest: ' + param.data[2] + '<br/>',
                                        'Highest: ' + param.data[3] + '<br/>'
                                    ].join('');
                                }
                            }
                        },
                        {
                            name: 'MA5',
                            type: 'line',
                            data: calculateMA(5, data),
                            smooth: true,
                            lineStyle: {
                                normal: {
                                    opacity: 0.5
                                }
                            }
                        },
                        {
                            name: 'MA10',
                            type: 'line',
                            data: calculateMA(10, data),
                            smooth: true,
                            lineStyle: {
                                normal: {
                                    opacity: 0.5
                                }
                            }
                        },
                        {
                            name: 'MA20',
                            type: 'line',
                            data: calculateMA(20, data),
                            smooth: true,
                            lineStyle: {
                                normal: {
                                    opacity: 0.5
                                }
                            }
                        },
                        {
                            name: 'MA30',
                            type: 'line',
                            data: calculateMA(30, data),
                            smooth: true,
                            lineStyle: {
                                normal: {
                                    opacity: 0.5
                                }
                            }
                        },
                        {
                            name: 'Volume',
                            type: 'bar',
                            xAxisIndex: 1,
                            yAxisIndex: 1,
                            data: data.volumes
                        }
                    ]
                }, true);

                // myChart.on('brushSelected', renderBrushed);

                // function renderBrushed(params) {
                //     var sum = 0;
                //     var min = Infinity;
                //     var max = -Infinity;
                //     var countBySeries = [];
                //     var brushComponent = params.brushComponents[0];

                //     var rawIndices = brushComponent.series[0].rawIndices;
                //     for (var i = 0; i < rawIndices.length; i++) {
                //         var val = data.values[rawIndices[i]][1];
                //         sum += val;
                //         min = Math.min(val, min);
                //         max = Math.max(val, max);
                //     }

                //     panel.innerHTML = [
                //         '<h3>STATISTICS:</h3>',
                //         'SUM of open: ' + (sum / rawIndices.length).toFixed(4) + '<br>',
                //         'MIN of open: ' + min.toFixed(4) + '<br>',
                //         'MAX of open: ' + max.toFixed(4) + '<br>'
                //     ].join(' ');
                // }

                myChart.dispatchAction({
                    type: 'brush',
                    areas: [{
                        brushType: 'lineX',
                        coordRange: ['2016-06-02', '2016-06-20'],
                        xAxisIndex: 0
                    }]
                });
            },
            error: function (error) {
                console.log(error)
            }
        })
        //展示当前股票的委托记录
        var user=getCookie("user");
        if(user!=null){
            $.ajax({
                type:'post',
                url:$baseUrl+'/deal/trade',
                data:{"code":code},
                success:function(response){
                    var data=JSON.parse(response);
                    // console.log("委托列表",data);
                    var commissionHTML='';
                    for(var item of data.data.bosstocklist){
                        commissionHTML+=`<tr>
                            <td data-v-11252f49="" class="id pc">${item.stock}-${item.stockname}</td>
                            <td data-v-11252f49="" class="time pc">${item.get_datetime}</td>
                            <td data-v-11252f49="" class="type">${item.role}</td>
                            <td data-v-11252f49="" class="price">${item.price}</td>
                            <td data-v-11252f49="" class="quantity">${item.amount}</td>
                            <td data-v-11252f49="" class="dealdone">已成交</td>
                            <td data-v-11252f49="" class="total pc">${item.price*item.amount}</td>
                        </tr>`
                    };
                    $(".tableCommission").html(commissionHTML);
                },
                error:function(err){console.log(err)}
            })
        }
            
    }


    //首页数据展示

    //1.首页列表

    $.ajax({
        type: "get",
        url: $baseUrl + "/stock/index",
        success: function (response) {
            var $data = JSON.parse(response);
            // console.log($data);
            var $indexList = $data.data.stocklist;
            firstCode=$indexList[0].code;
            k(firstCode);
            $myCode=firstCode;
            var html = '';
            for (var item of $indexList) {
                html += `<div data-v-fee9bace="" id="${item.code}" class="indexListItem">
                    <div data-v-7ad1a312="" data-v-fee9bace="" class="marketitem">
                    <div data-v-7ad1a312="" class="content">
                        <div data-v-7ad1a312="" class="left">
                        <div data-v-7ad1a312="" class="icon">
                            <img data-v-7ad1a312="" src="${item.img}">
                        </div>
                        </div>
                        <div data-v-7ad1a312="" class="center">
                        <div data-v-7ad1a312="" class="top">
                            <div data-v-7ad1a312="" class="tradeName">
                            ${item.name}
                            </div>

                        </div>
                        <div data-v-7ad1a312="" class="bottom">
                            <div data-v-7ad1a312="" class="price">
                            <div data-v-7ad1a312="" class="value">${item.code}</div>
                            </div>
                            <div data-v-7ad1a312="" title="市盈率" class="changeWidth">${item.pe}</div>
                        </div>
                        </div>
                    </div>
                    </div>
                </div>`;
            }
            $(".indexList").html(html).children(":first").find(".content").addClass("active");
            //点击股票列表
            $(".indexList").on("click", "div.indexListItem", (e) => {
                var $tar = $(e.target).parents(".indexListItem");
                var codeId = $tar.attr("id");
                k(codeId);
                $myCode=codeId;
                $tar.find(".content").addClass("active");
                $tar.siblings().find(".content").removeClass("active");
            });


            //成交记录
            var dealdata = $data.data.dealstocks;
            // console.log("成交记录",dealdata);
            var dealHTML = "";
            for (var item of dealdata) {
                dealHTML += `<tr>
                    <td data-v-0520926c="" class="time pc">${item.datetime}</td>
                    <td data-v-0520926c="" class="type red">${JSON.parse(item.stock).stonumber}</td>
                    <td data-v-0520926c="" class="price">${item.price}</td>
                    <td data-v-0520926c="" class="quantity">${item.amount}</td>
                    <td data-v-0520926c="" class="total pc">${item.price*item.amount}</td>
                </tr>`;
            }
            $(".tableDeal>tbody").html(dealHTML);
        },
        error: function (error) {
            console.log(error)
        }
    })

    // 点击买入
    $(".btn_buy").click(()=>{
        var buy_price=$(".buy_price").val();
        var buy_number=$(".buy_number").val();
        // var buy_total=buy_number*buy_price;
        var buy_paypassword=$(".buy_paypassword").val();
        // console.log(
        //     "买入价格：",buy_price,
        //     "---买入数量：",buy_number,
        //     "---支付密码：",buy_paypassword,
        //     "---code码",$myCode
        // );
        if(buy_price==''||buy_number==''||buy_paypassword==''){
            Ply.dialog("alert", "请输入正确数据！");
        }else{
            $.ajax({
                type:'post',
                url:$baseUrl+'/deal/tobuy/',
                data:{
                    "code":$myCode,
                    "amount":buy_number,
                    "price":buy_price,
                    "tradepwd":buy_paypassword
                },
                success:function(response){
                    var data=JSON.parse(response);
                    console.log(data);
                    if(data.result==true){
                        Ply.dialog("alert",data.data);
                        balance();
                    }else{
                        Ply.dialog("alert", data.data);
                    }
                },
                error:function(err){
                    console.log(err)
                }
            })
        }
        
    })

    //点击卖出 (我的挂单)
    $(".btn_sell").click(()=>{
        var sell_price=$(".sell_price").val();
        var sell_number=$(".sell_number").val();
        // var sell_total=sell_number*sell_price;
        var sell_paypassword=$(".sell_paypassword").val();
        if(sell_number==''||sell_paypassword==''||sell_price==''){
            Ply.dialog("alert", "请输入正确数据！");
        }else{
            $.ajax({
                type:'post',
                url:$baseUrl+'/deal/tosell/',
                data:{
                    "code":$myCode,
                    "amount":sell_number,
                    "price":sell_price,
                    "tradepwd":sell_paypassword
                },
                success:function(response){
                    var data=JSON.parse(response);
                    console.log(data)
                },
                error:function(err){
                    console.log(err)
                }
            })
        }
    })

    //失去焦点时计算总额
    $(".buy_number,.buy_price").blur(()=>{
        buyTotal();
    })
    function buyTotal(){
        var buy_price=$(".buy_price").val();
        var buy_number=$(".buy_number").val();
        $(".buy_total").html(buy_number*buy_price)
    }
    $(".sell_number,.sell_price").blur(()=>{
        sellTotal();
    })
    function sellTotal(){
        var sell_price=$(".sell_price").val();
        var sell_number=$(".sell_number").val();
        $(".sell_total").html(sell_number*sell_price)
    }



    //是否在线接口

    // $.ajax({
    //     type:'get',
    //     url:$baseUrl+'/user/islogin',
    //     success:function(response){
    //         console.log("是否在线",JSON.parse(response))
    //     },
    //     error:function(err){
    //         console.log(err);
    //     }
    // })


    // 用户余额
    function balance(){
        var user=getCookie("user");
        if(user!=null){
            $.ajax({
                type:'get',
                url:$baseUrl+'/user/info',
                success:function(response){
                    var data=JSON.parse(response);
                    console.log(data,"资金刷新！");
                    $(".available_money").html(data.data.money);
                    $(".frozenmoney").html(data.data.frozenmoney);
                    $(".samount").html(data.data.samount);
                    $(".sfrozen").html(data.data.sfrozen);
                },
                error:function(err){console.log(err)}
            })
        }
    }
    balance();

})