import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import util


current_login_user = ""


def read_file_atm():
    return util.day4_utils.read_file("atm")


def write_file_atm(dicts):
    util.day4_utils.write_file("atm", dicts)


def read_file_person_flow():
    return util.day4_utils.read_file("personflow")


def write_file_person_flow(dicts):
    return util.day4_utils.write_file("personflow", dicts)


def read_file_atm_flow():
    return util.day4_utils.read_file("atmflow")


def write_file_atm_flow(name, desp):
    atm_flow = util.day4_utils.read_file("atmflow")
    element = []
    if atm_flow.__contains__(name):
        element = atm_flow[name]
    element.append(desp)
    atm_flow[name] = element
    util.day4_utils.write_file("atmflow", atm_flow)


# 用户权限检查
def check_admin(func):
    def wrapper(*args, **kwargs):
        username = args[0]
        user_info = read_file_atm()
        if user_info.__contains__(username):
            user = user_info[username]
            if user["isadmin"]:
                func(*args, **kwargs)
            else:
                print("不是管理员不能执行此项操作")
                back()

    return wrapper


# 检查用户账户是否被冻结
def check_close(func):
    def wrapper(*args, **kwargs):
        username = args[0]
        user_info = read_file_atm()
        if user_info.__contains__(username):
            user = user_info[username]
            if not user["state"]:
                func(*args, **kwargs)
            else:
                print("账户不存在或已经被冻结")
                back()
    return wrapper


# 创建新card用户，默认额度15000或者自定义
def create_user(isadmin):
    name = input("请输入用户名：")
    password = input("请输入密码：")
    credit_lines = input("请输入额度：")
    user_info = read_file_atm()
    # 判断用户是否存在，不存在则进行初始化创建
    if user_info.__contains__(name):
        print(name + "用户已存在")
        return
    else:
        # 初始化用户信息 用户名、密码、信用额度、余额、管理员权限、账户冻结
        temp_user = {"name": name, "password": password, "credit_lines": int(credit_lines), "remaining_sum": 0,
                     "isadmin": isadmin, "state": False}
        user_info[name] = temp_user
        print(name + "创建成功")
    write_file_atm(user_info)

    write_file_atm_flow(name, "创建账户" + name)


# 管理员创建入口
def create_admin():
    create_user(True)
    back()


# 普通用户创建入口
@check_admin
def create_normal(username):
    create_user(False)
    back()


# 登录
def login():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    user_info = read_file_atm()
    if user_info.__contains__(username):
        user = user_info[username]
        if user["name"] == username and user["password"] == password:
            global current_login_user
            print("登录成功")
            current_login_user = username
            main_menu()
            return
    print("登录失败")


# 功能主菜单
def main_menu():
    choice = int(input("请选择你所需的服务：\n1.查询\n2.付款\n3.提现\n4.还款\n5.转账\n6.流水查询\n7.添加用户\n8.冻结用户\n9.调整额度\n"))
    if choice == 1:
        query(current_login_user)
    elif choice == 2:
        pay(current_login_user)
    elif choice == 3:
        withdraw(current_login_user)
    elif choice == 4:
        repayment(current_login_user)
    elif choice == 5:
        transfer_accounts(current_login_user)
    elif choice == 6:
        read_atm_flow(current_login_user)
    elif choice == 7:
        create_normal(current_login_user)
    elif choice == 8:
        close_user(current_login_user)
    elif choice == 9:
        change_credit_lines(current_login_user)


# 查询菜单
@check_close
def query(username):
    user_info = read_file_atm()
    if user_info.__contains__(username):
        user = user_info[username]
        temp = "已" if user["state"] else "未"
        print("可用额度为：" + str(user["credit_lines"]) + "\n剩余资金：" + str(user["remaining_sum"]) + "\n账户" + temp + "冻结")
    back()


# 付款
@check_close
def pay(username):
    user_info = read_file_atm()
    if user_info.__contains__(username):
        money = int(input("请填写支付款数量："))
        user = user_info[username]
        # 当前剩余金额
        store_money = user["remaining_sum"]
        # 判断当前额度是否足够
        if store_money - money < -user["credit_lines"]:
            print("余额不足")
        else:
            user["remaining_sum"] = int(store_money - money)
            write_file_atm(user_info)
            print("支付完成，余额" + str(store_money - money))

            add_atm_flow(username, "支付完成，余额" + str(store_money - money))
    back()


# 提现
@check_close
def withdraw(username):
    user_info = read_file_atm()
    if user_info.__contains__(username):
        money = int(input("请填写提现款数量："))
        user = user_info[username]
        # 当前剩余金额
        store_money = user["remaining_sum"]
        if store_money - money * (1 + 0.05) < -user["credit_lines"]:
            print("余额不足")
        else:
            user["remaining_sum"] = int(store_money - money * (1 + 0.05))
            write_file_atm(user_info)
            print("提现完成，余额" + str(store_money - money * (1 + 0.05)))

            add_atm_flow(username, "提现完成，余额" + str(store_money - money * (1 + 0.05)))
    back()


# 转账
@check_close
def transfer_accounts(username):
    user_info = read_file_atm()
    to_user = input("请输入收款人姓名：")
    money = int(input("请输入转账额度："))
    if user_info.__contains__(username) and user_info.__contains__(to_user) and username != to_user \
            and user_info[username]["remaining_sum"] > money:
        # 可以转账
        user_info[username]["remaining_sum"] = user_info[username]["remaining_sum"] - money
        user_info[to_user]["remaining_sum"] = user_info[to_user]["remaining_sum"] + money
        write_file_atm(user_info)
        print("转账完成，余额"+str(user_info[username]["remaining_sum"]))

        add_atm_flow(username, "转账完成，余额"+str(user_info[username]["remaining_sum"]))
    else:
        print("转账失败")
    back()


# 还款
@check_close
def repayment(username):
    user_info = read_file_atm()
    if user_info.__contains__(username):
        money = int(input("请填写还款数量："))
        user = user_info[username]
        # 当前剩余金额
        store_money = user["remaining_sum"]
        user["remaining_sum"] = int(store_money + money)
        write_file_atm(user_info)
        print("还款完成，余额" + str(store_money + money))

        add_atm_flow(username, "还款完成，余额" + str(store_money + money))
    else:
        print("还款失败")

    back()


# 添加流水
def add_atm_flow(name, desp):
    flow_info = read_file_person_flow()
    flow_list_info = []
    # 存在元素直接获取流水列表信息
    if flow_info.__contains__(name):
        flow_list_info = flow_info[name]
    # 流水直接添加到最后
    flow_list_info.append(time.strftime("%Y-%m-%d %H:%M:%S") + desp)
    flow_info[name] = flow_list_info
    write_file_person_flow(flow_info)


# 打印流水
@check_close
def read_atm_flow(username):
    flow_info = read_file_person_flow()
    # 存在元素直接获取流水列表信息
    if flow_info.__contains__(username):
        flow_list_info = flow_info[username]
        for i in range(flow_list_info.__len__()):
            print(flow_list_info[i])
    else:
        print("查无此人")


# 返回上一级菜单
def back():
    print("\n")
    main_menu()


# 冻结用户
@check_admin
def close_user(username):
    closename = input("请输入欲冻结账户姓名：")
    isclose = int(input("是否冻结用户：1.冻结 2.激活"))
    user_info = read_file_atm()
    if user_info.__contains__(closename):
        user = user_info[closename]
        user["state"] = True if isclose == 1 else False
        write_file_atm(user_info)
        print(closename + "已被冻结")
    back()


# 调整信用额度
@check_admin
def change_credit_lines(username):
    toname = input("请输入欲调节的账户姓名：")
    money = int(input("请填写调整的额度："))
    user_info = read_file_atm()
    if user_info.__contains__(toname):
        user = user_info[toname]
        user["credit_lines"] = money
        write_file_atm(user_info)
        print(toname + "额度为" + str(user["credit_lines"]))
    back()


login()
