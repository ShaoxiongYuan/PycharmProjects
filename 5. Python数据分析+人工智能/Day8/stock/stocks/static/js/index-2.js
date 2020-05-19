$(()=>{
    $.ajax({
        type:'get',
        url:$baseUrl+'/deal/bosstock',
        success:function(response){
            var data=JSON.parse(response);
            if(data.result==true){
                console.log(data.data)
                var transferAreaListHTML='';
                for(var item of data.data){
                    transferAreaListHTML+=`<div data-v-193eb34c="" data-v-46291c12="" class="list">
                        <div data-v-193eb34c="" class="td userName">${item.user}</div>
                        <div data-v-193eb34c="" class="td goodName">${item.stock}-${item.stockname}</div>
                        <div data-v-193eb34c="" class="td num">${item.amount}</div>
                        <div data-v-193eb34c="" class="td time">--</div>
                        <div data-v-193eb34c="" class="td price">${item.price}￥</div>
                        <div data-v-193eb34c="" class="td operation toBuyTransferArea">去购买</div>
                    </div>`
                }
                $(".transfer_area_list").html(transferAreaListHTML).on("click",".toBuyTransferArea",(e)=>{
                    var $tar=$(e.target);
                    var theCode=$tar.siblings(".goodName").html().split("-")[0];
                    var theName=$tar.siblings(".goodName").html().split("-")[1];
                    var theAmount=$tar.siblings(".num").html();
                    var thePrice=$tar.siblings(".price").html();
                    $(".toBuyTransferBox").show();
                    $(".toBuy_tishi").html(`当前股票为：${theCode}-${theName}，数量上限为：${theAmount}`);
                    $(".buy_ok").click(()=>{
                        var amount=$(".buy_number").val();
                        var pwd=$(".buy_password").val();
                        $.ajax({
                            type:'post',
                            url:$baseUrl+'/deal/tobuy/',
                            data:{
                                "code":theCode,
                                "amount":amount,
                                "price":thePrice,
                                "tradepwd":pwd
                            },
                            success:function(response){
                                var data=JSON.parse(response);
                                console.log(data);
                            },
                            error:function(err){
                                console.log(err)
                            }
                        })
                    })
                });
            }
            
        },
        error:function(err){
            console.log(err);
        }
    })
})