import datetime
from decimal import Decimal

from flask import Blueprint, render_template, redirect, request, jsonify, current_app, session, url_for, g

from exts import db
import funtion as fun
bp = Blueprint("person", __name__, url_prefix="/person")


@bp.route("/person")
def person():
    # 读取全部的标签并且输出到页面上
    if session.get("name") is not None:
        s = "select * from label"
        sql = db.session.execute(s)
        sql = list(sql)
        taplist = []
        for i in sql:
            # taplist内含全部标签信息
            taplist.append(i[0])
        s = "select * from user_interest where user_name= '" + session.get("name") + "'"
        persontap = db.session.execute(s)
        persontap = list(persontap)
        # print(persontap)
        showtap = []
        for i in taplist:
            # 对该用户元祖的每个标签列逐一遍历，若发现标签列值为1，则取出该标签名
            s = "select " + i + " from user_interest where user_name = '" + session.get("name") + "'"
            # print(s)
            j = db.session.execute(s)
            j = list(j)
            j = int(j[0][0])
            if j == 1:
                showtap.append(i)
        # print(showtap)
        # 收藏
        user = session.get("name")
        s = "select * from user_collects where user= '" + user + "'"
        sql = db.session.execute(s)
        sql = list(sql)
        vid = []
        collects = []
        for i in sql:
            if i[3] == 1:
                vid.append(i[2])
        # print(vid)
        for i in vid:
            i = str(i)
            s = "select * from video_list where video_id= " + i
            sql = db.session.execute(s)
            sql = list(sql)
            sql = sql[0]
            collects.append(sql)
        # print(collects)

        ScoreMatrix = fun.getScoreMatrix()  # 此变量是已经经过余弦相似度得到的评分矩阵，甚至已经排序好了
        video_id_list = []
        for i in ScoreMatrix:
            video_id_list.append(int(i[0]))  # 把已经排序好的评分矩阵

        sql = "select video_id,video_image,video_name,video_author,video_publishedtime from video_list"
        list1 = db.session.execute(sql)
        list1 = list(list1)
        index_dict = {value: index for index, value in enumerate(video_id_list)}
        videolist = sorted(list1, key=lambda x: index_dict[x[0]])
        for i in ScoreMatrix:
            # print(i[1])
            i[1] = Decimal(str(round(i[1], 4))) * 100

        return render_template("person.html", taplist=taplist, name=session.get("name"), showtap=showtap,
                               collects=collects,score=ScoreMatrix)
    else:
        return redirect(url_for('login.login'))


@bp.route("/entertap", methods=["GET", "POST"])
def enter():
    myLabel = request.form.getlist('tap')
    # 读取到用户前端选择的标签
    allLabel = db.session.execute("select * from label")
    allLabel = list(allLabel)
    allLabel1 = []
    for i in allLabel:
        allLabel1.append(i[0])
        # 把用户所有的标签数据归零
    for i in allLabel1:
        s = "update user_interest set " + i + " = 0 where user_name ='" + session.get("name") + "'"
        db.session.execute(s);
    for i in myLabel:
        s = "update user_interest set " + i + " = 1 where user_name = '" + session.get("name") + "'"
        db.session.execute(s)
    db.session.commit()
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("checkpoint1 " + time)
    # fun.putScoreMatrixintoDatabase()
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("checkpoint2 " + time)
    return redirect(url_for('person.person'))


def iscollected(self, vid, uid):
    sql = "select * from user_collects "
    flag = db.session.execute(sql)
    flag = list(flag)
    for i in flag:
        if i[1] == uid:
            if i[2] == vid:
                return 1;
    return 0;
