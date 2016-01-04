from flask import request, jsonify, Blueprint, redirect, url_for, g
import datetime
from models import BlogPost
from google.appengine.api import users

api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/get_single_post', methods=['POST'])
def get_single_post():
    loaded_message = request.get_json()
    data_id = int(loaded_message["id"])
    qry1 = BlogPost.get_by_id(data_id, parent=None)
    body = qry1.body
    author = qry1.author
    title = qry1.title
    the_time = qry1.time
    id = qry1.key.id()
    dict_to_append = {"body": body, "author": author, "title": title, "time": the_time, "id": id}
    return jsonify(data=dict_to_append)


@api.route('/your_posts', methods=['GET'])
def your_posts():
    qry1 = BlogPost.query()  # Retrieve all Account entitites
    list_to_return = []

    for item in qry1:
        body = item.body
        author = item.author
        title = item.title
        the_time = item.time
        item_id = item.key.id()
        dict_to_append = {"body": body, "author": author, "title": title, "time": the_time, "id": item_id}
        list_to_return.append(dict_to_append)

    return jsonify(data=list_to_return)


@api.route('/create_post', methods=["POST", "GET"])
def make_post():
    loaded_message = request.get_json()

    body = loaded_message["body"]
    title = loaded_message["title"]

    the_time = datetime.datetime.now()
    fixed_time = the_time.strftime("%B %d, %Y")
    author = "DTernyak@gmail.com"

    insert_payload = BlogPost(
            time=fixed_time,
            body=body,
            title=title,
            author=author,
    )

    insert_payload.put()
    return jsonify(success=True)


@api.route('/login')
def login():
    login_url = users.create_login_url('/#/editor')
    return redirect(login_url)


@api.route('/is_admin')
def is_admin():
    return jsonify(result=True)