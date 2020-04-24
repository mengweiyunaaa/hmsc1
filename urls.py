from web.controliers.user.User import router_user
from application import app
from web.controliers.static import route_static
app.register_blueprint(router_user,url_prefix='/user')

app.register_blueprint(route_static,url_prefix="/static")
@app.route('/')
def index():
    return '路由是/user/...'