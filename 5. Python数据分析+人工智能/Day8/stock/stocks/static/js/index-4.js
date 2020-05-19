$(() => {
    //点击修改密码弹框事件
    $(".change_pwd").click(() => {
        var user = getCookie("user");
        console.log(user)
        if (user == null) {
            Ply.dialog("alert", "请先登录账号！");
        } else {
            $(".stock_changePwd").show();
            $(".changePwd_ok").click(() => {
                var oldpassword = $(".pwd_old").val();
                var newpassword = $(".pwd_new").val();
                var conpassword = $(".pwd_newAgain").val();
                $.ajax({
                    type: 'post',
                    url: $baseUrl + '/user/changepwd',
                    data: {
                        "oldpassword": oldpassword,
                        "newpassword": newpassword,
                        "conpassword": conpassword
                    },
                    success: function (response) {
                        var data = JSON.parse(response);
                        console.log(data);
                        if (data.result == true) {
                            removeCookie("user");
                            Ply.dialog("alert", "密码修改成功，下次请用新密码登录！");
                            $(".mdialog").hide();
                            setTimeout(()=>{
                                window.history.go(0);
                            },1500)
                        }
                    },
                    error: function (err) {
                        console.log(err);
                    }
                })
            })
        }

    });

    //点击用户充值弹框事件
    $(".recharge").click(() => {
        $(".stock_recharge").show();
    })
    //确认充值的按钮事件
    $(".recharge_ok").click(() => {

        var recharge_number = $(".recharge_number").val();
        var transaction_password = $(".transaction_password").val();
        // console.log(recharge_number,transaction_password);
        if(recharge_number=='' || transaction_password==''){
            Ply.dialog("alert", "请输入数据！");
        }else{
            // console.log(recharge_number, transaction_password);
            $.ajax({
                type:'post',
                url:$baseUrl+'/user/charge',
                data:{
                    "money":recharge_number,
                    "charpwd":transaction_password
                },
                success:function(response){
                    var data = JSON.parse(response);
                    console.log(data);
                    if(data.result==true){
                        Ply.dialog("alert", "充值成功！");
                        $(".mdialog").hide();
                    }else{
                        Ply.dialog("alert", data.error);
                    }
                },
                error:function(err){
                    console.log(err)
                }
            })
        }
        
    })
    //点击绑定弹框
    $(".binding").click(() => {
        var user = getCookie("user");
        if (user == null) {
            Ply.dialog("alert", "请先登录账号！");
        } else {
            $(".stock_binding").show();
        }
    })
    //确定绑定
    $(".binding_ok").click(() => {
        var bank = $("select[name=notremember]").val();
        var username = $(".card_master").val();
        var bankno = $(".card_num").val();
        var paypwd = $(".pay_password").val();
        if (bankno.length == 16) {
            $.ajax({
                type: 'post',
                url: $baseUrl + '/user/bankbg',
                data: {
                    "bank": bank,
                    "username": username,
                    "bankno": bankno,
                    "paypwd": paypwd
                },
                success: function (response) {
                    var data=JSON.parse(response);
                    if(data.result==true){
                        Ply.dialog("alert", "绑定成功！");
                        $(".mdialog").hide();
                    }else{
                        Ply.dialog("alert", data.error);
                    }
                },
                error: function (err) {
                    console.log(err);
                }
            })
        } else {
            Ply.dialog("alert", "银行卡号格式错误，请输入16位数字！");
        }


    })
})