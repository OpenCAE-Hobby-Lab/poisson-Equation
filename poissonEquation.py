from flask import flash, Flask, render_template, request, Blueprint

# Only single run
poissonEquation = Flask(__name__)

# To connect HobbyLab
# poissonEquation = Blueprint('poissonEquation', __name__, template_folder='templates', static_folder='./static')

# ----------------------------------------------------------------------
# トップページ
# ----------------------------------------------------------------------
@poissonEquation.route('/')
def index():
    # htmlの表示
    return render_template(
        'poissonEquation/index.html',
        title="Poisson equation calculator",
        Xnum=10,
        Ynum=10,
        dd_list=[]
    )


# ----------------------------------------------------------------------
# 計算実行と結果表示
# ----------------------------------------------------------------------
@poissonEquation.route("/run", methods=['POST'])
def run():
    # 結果を格納するリスト
    __u = []

    # 分割数の取得
    column = int(request.form["Ynum"]) # y方向
    row = int(request.form["Xnum"]) # x方向

    # uは現在の結果､wはひとつ前の結果
    u = [[] for i in range(column)]
    w = [[] for i in range(column)]

    # u,wを初期化
    for i in range(column):
        for j in range(row):
            u[i].append(0.0)
            w[i].append(0.0)

    # 温度入力辺に温度を定義
    for i in range(1, column-1):
        u[i][row-1] = float(request.form["temperature"])

    # ガウスザイデル法
    dd = 9999 # ddI±残差
    count = 0
    dd_list = []
    while dd > 0.001:
        count += 1
        dd = 0.0
        for i in range(1, column-1):
            for j in range(1, row-1):
                u1 = u[i+1][j] + u[i-1][j]
                u2 = u[i][j+1] + u[i][j-1]
                u[i][j] = (u1 + u2) / 4.0
                dd += abs(w[i][j] - u[i][j])
                w[i][j] = u[i][j]
        dd_list.append([count, dd])
    __u = u

    # 結果の表示
    return render_template(
        'poissonEquation/result.html',
        title="Poisson equation calculator",
        Xnum=10,
        Ynum=10,
        dd_list=dd_list,
        temp_data=__u
    )


# ----------------------------------------------------------------------
# メインルーチン
# ----------------------------------------------------------------------
if __name__ == '__main__':
    poissonEquation.debug = True
    poissonEquation.run(host='localhost', port=12081,
        debug=True, use_reloader=True, use_debugger=False)
