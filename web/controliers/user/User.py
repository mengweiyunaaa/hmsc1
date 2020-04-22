from flask import Blueprint,render_template,request,jsonify
import json
router_user = Blueprint('user_page',__name__)


@router_user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("user/login.html")

    resp = {
        'code': 200,
        'msg': '登录成功',
        'data': {}
    }
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if login_name is None or len(login_name) < 1:
        resp['code'] = 0
        resp['msg'] = '请输入正确的用户名'
        return jsonify(resp)

    if login_pwd is None or len(login_name) < 1:
        resp['code'] = 0
        resp['msg'] = '请输入正确的密码'
        return jsonify(resp)

    return jsonify(resp)
@router_user.route('/logout')
def logout():
    return 'dengchu'
@router_user.route('/edit')
def edit():
    return 'bianji'
@router_user.route('/reset_pas')
def reset():
    return 'gaimima'
@router_user.route('/create')
def create():
    return 'zengjia'
@router_user.route('/delete')
def delete():
    return 'shanchu'
