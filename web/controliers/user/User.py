from flask import Blueprint,render_template
router_user = Blueprint('user_page',__name__)
@router_user.route('/login')
def login():
    return render_template('user/login.html')
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
