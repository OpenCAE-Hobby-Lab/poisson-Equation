import subprocess as sp
import os
import shutil
import datetime
import random
import time
import json
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from flask import flash, Flask, render_template, request, redirect, url_for, send_file, after_this_request

app = Flask(__name__)

# ----------------------------------------------------------------------
# トップページ
# ----------------------------------------------------------------------
@app.route('/')
def index():
    return render_template(
        'index.html',
        title="Poisson equation calculator",
        X=10,
        Y=10
    )


# ----------------------------------------------------------------------
# 実行
# ----------------------------------------------------------------------
@app.route("/run", methods=['POST'])
def run():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']

        __u = []
        column = int(request.form["Y"]) # y方向

        row = int(request.form["X"]) # x方向

        # uは現在の結果､wはひとつ前の結果
        u = [[] for i in range(column)]
        w = [[] for i in range(column)]

        # u,wを初期化
        for i in range(column):
            for j in range(row):
                u[i].append(0.0)
                w[i].append(0.0)

        for i in range(1, column-1):
            u[i][row-1] = float(request.form["temperature"])

        dd = 9999 # ddI±残差
        while dd > 0.001:
            dd = 0.0
            for i in range(1, column-1):
                for j in range(1, row-1):
                    u1 = u[i+1][j] + u[i-1][j]
                    u2 = u[i][j+1] + u[i][i-1]
                    u[i][j] = (u1 + u2) / 4.0
                    dd += abs(w[i][j] - u[i][j])
                    w[i][j] = u[i][j]
                    ws.send(json.dumps([{"time": t, "y": dd}]))
                    time.sleep(1)
            # printResidual(dd)
        __u = u
    return


# ----------------------------------------------------------------------
# メインルーチン
# ----------------------------------------------------------------------
if __name__ == '__main__':
    app.debug = True
    server = pywsgi.WSGIServer(('localhost', 8000), app, handler_class=WebSocketHandler)
    server.serve_forever()