//封装cookie
function setCookie(name, value, iDay) {
    var oDate = new Date();
    oDate.setDate(oDate.getDate() + iDay);
    document.cookie = name + '=' + value + ';expires=' + oDate;
};
/*使用方法：setCookie('user', 'simon', 11);*/
/*获取cookie*/
function getCookie(name) {
    var arr = document.cookie.split('; '); //多个cookie值是以; 分隔的，用split把cookie分割开并赋值给数组
    //历遍数组
    // for (var i = 0; i < arr[i].length; i++) 
    // {
    //     //原来割好的数组是：user=simon，再用split('=')分割成：user simon 这样可以通过arr2[0] arr2[1]来分别获取user和simon 
    //     console.log(arr[i])
    //     var arr2 = arr[i].split('='); 
    //     // console.log(arr2);
    //     if (arr2[0] == name) //如果数组的属性名等于传进来的name
    //     {
    //         return arr2[1]; //就返回属性名对应的值
    //     }
    //     return ''; //没找到就返回空
    // }
    for(var i=0;i<arr.length;i++){
        var cookieName=arr[i].split("=")[0];
        var cookieValue=arr[i].split("=")[1];
        if(cookieName==name){
            return cookieValue;
        }
    }
};
/*使用方法：getCookie('user')*/
/*删除cookie*/
function removeCookie(name) {
    setCookie(name, 1, -1); //-1就是告诉系统已经过期，系统就会立刻去删除cookie
};
/*使用方法：removeCookie('user')*/

$myCode='';
$baseUrl = "http://localhost:8004";
$available_money=0;
$frozenmoney=0;

//加载头部

$.get("header", (data) => {
    var $headerHTML=$(data);
    var user=getCookie("user");
    if(user!=null){
        $headerHTML.find(".username").html("欢迎登录，"+user);
        $headerHTML.find(".click_login,.click_register").hide();
        $headerHTML.find(".click_logout").show();
        $(".islogin").removeClass("lognmark");
        $("#header").html($headerHTML);
    }else{
        $("#header").html(data);
    }
})

// $.ajax({
//     type:'get',
//     url:'header.html',
//     success:function(data){
//         var $headerHTML=$(data);
//         var user=getCookie("user");
//         if(user!=null){
//             $headerHTML.find(".username").html("欢迎登录，"+user);
//             $headerHTML.find(".click_login,.click_register").hide();
//             $headerHTML.find(".click_logout").show();
//             $(".islogin").removeClass("lognmark");
//             $("#header").html($headerHTML);
//         }else{
//             $("#header").html(data);
//         }
//     },
//     error:function(err){console.log(err)}
// })




$(() => {
    $(".transfer_list").click((e) => {
        var $tar = $(e.target);
        if ($tar.hasClass("transfer_index")) {
            $(location).attr("href", "index-1")
        } else if ($tar.hasClass("transfer_area")) {
            $(location).attr("href", "index-2")
        } else if ($tar.hasClass("my_transfer")) {
            $(location).attr("href", "index-3")
        } else if ($tar.hasClass("my_sale")) {
            $(location).attr("href", "index-4")
        }
    })

    // 点击注册事件
    $(".click_register").click(() => {
        $(".stock_register").show();
        $(".stock_login").hide();
    })
    // 点击登录事件
    $(".click_login").click(() => {
        $(".stock_login").show();
        $(".stock_register").hide();
    })
    // 关闭登录和注册框
    $(".close").click(() => {
        // $(".stock_login").hide();
        // $(".stock_register").hide();
        $(".mdialog").hide();
    })
    //登录之后点击退出
    $(".click_logout").click(()=>{
        $.ajax({
            type:"get",
            url:$baseUrl+'/user/logout',
            success:function(response){
                // console.log(response);
                if(JSON.parse(response).result==true){
                    console.log("222")
                    removeCookie("user");
                    window.history.go(0);  
                }
            },
            error:function(err){
                console.log(err)
            }
        })
    })
    //点击确定注册
    $(".stock_submitRegister").click((e) => {
        e.preventDefault();
        var $registerName = $(".stock_registerName").children().val();
        var $registerPwd = $(".stock_registerPwd").children().val();
        var $registerAgain = $(".stock_registerAgain").children().val();
        // console.log($registerName, $registerPwd, $registerAgain,$payPassword);
        $.ajax({ 
            type: "post",
            url: $baseUrl + '/user/register',
            data: {
                username: $registerName,
                pwd: $registerPwd,
                cpwd: $registerAgain,
                // payPassword:$payPassword
            },
            success: function (response) {
                // console.log(response)
                var data=JSON.parse(response);
                // console.log(data);
                if(data.result==true){
                    $(".mdialog").hide();
                    Ply.dialog("alert", "注册成功！");
                }else{
                    Ply.dialog("alert", data.error);
                }
            },
            error: function (error) {
                console.log(error)
            }
        })

    })
    //点击确定登录
    $(".stock_submitLogin").click((e) => {
        e.preventDefault();
        var $loginPwd = $(".stock_loginPwd").children().val();
        var $loginName = $(".stock_loginName").children().val();
        console.log($loginName, $loginPwd)
        $.ajax({
            type: "post",
            url: $baseUrl + '/user/login',
            data: {
                username: $loginName,
                password: $loginPwd
            },
            success: function (response) {
                var data=JSON.parse(response);
                console.log(data);
                if(data.result==true){
                    var username =data.data.username;
                    console.log(username);
                    setCookie("user", username, 0.1);
                    $(".stock_login").hide();
                    console.log($(".islogin"));
                    window.history.go(0);
                    $available_money=data.data.money;
                    $frozenmoney=data.data.frozenmoney;
                }else{
                    Ply.dialog("alert", data.error);
                }
            },
            error: function (error) {
                console.log(error)
            }
        })
    })

    //轮播
    var duration = 4000;

    function task() {
        var show = document.querySelector(".banner .banner-show");
        show.className = "";
        if (show.nextElementSibling != null) {
            show.nextElementSibling.className = "banner-show";
        } else {
            show.parentNode.children[0].className = "banner-show";
        }
    }
    var timer = setInterval(task, duration);
    var banner = document.querySelector(".banner");
    banner.onmouseover = function () {
        clearInterval(timer);
        this.timer = null;
    }
    banner.onmouseout = function () {
        timer = setInterval(task, duration);
    }




})