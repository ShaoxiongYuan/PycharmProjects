def verify_permissions(func):
    def wrapper(*args):
        print("验证权限")
        return func(*args)

    return wrapper


@verify_permissions
def enter_background(login_id, pwd):
    print(login_id, "进入后台")


@verify_permissions
def delete_order(id):
    print("删除%d订单" % id)


enter_background("zs@qq.com", "1234")
delete_order(10010)
