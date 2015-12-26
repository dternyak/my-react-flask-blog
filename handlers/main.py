import env_setup
env_setup.setup()
from google.appengine.api import users
import json
from webapp2 import redirect
import datetime

import logging

from env_setup import BetterHandler as RequestHandler
from models.models import BlogPost

class IsLoggedInHandler(RequestHandler):
    def get(self):
        self.request.headers['Access-Control-Allow-Origin'] = '*'
        greeting = "Success"
        final = json.dumps(greeting)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.out.write(final)

class LoginHandler(RequestHandler):
    def get(self):
        return redirect("/#/admin")

class MainHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        greeting = {}
        if user:
            print user
            greeting["status"] = "logged_in"
            greeting["user"] = user.email()
            greeting["url"] = users.create_logout_url('/#/')

        else:
            greeting["status"] = "logged_out"
            greeting["url"] = users.create_login_url('/#/')

        final = json.dumps(greeting)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(final)

class SinglePostsHandler(RequestHandler):
    def post(self):
        self.request.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        loaded_message = json.loads(self.request.body)
        data_id = int(loaded_message["id"])
        qry1 = BlogPost.get_by_id(data_id, parent=None)

        body = qry1.body
        author = qry1.author
        title = qry1.title
        time = qry1.time
        id = qry1.key.id()
        dict_to_append = {"body": body, "author": author, "title": title, "time": time, "id": id}

        final = json.dumps(dict_to_append)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(final)


class UpdatePostsHandler(RequestHandler):
    def post(self):
        self.request.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        user = users.get_current_user()

        loaded_message = json.loads(self.request.body)
        data_id = int(loaded_message["id"])
        json_body = loaded_message["body"]
        json_title = loaded_message["title"]

        qry1 = BlogPost.get_by_id(data_id, parent=None)
        author = qry1.author

        if user.email() == author:
            qry1.body = json_body
            qry1.title = json_title

            qry1.put()

            final = json.dumps("Success")

            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(final)
        else:
            final = json.dumps("Failure")
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(final)


class YourPostsHandler(RequestHandler):
    def get(self):
        self.request.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        qry1 = BlogPost.query()  # Retrieve all Account entitites
        list_to_return = []

        for item in qry1:
            body = item.body
            author = item.author
            title = item.title
            time = item.time
            item_id = item.key.id()
            dict_to_append = {"body": body, "author": author, "title": title, "time": time, "id": item_id}
            list_to_return.append(dict_to_append)

        final = json.dumps(list_to_return)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(final)

class YourPostSpecific(RequestHandler):
    def get(self):
        self.request.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        print "test"
        user = users.get_current_user()
        qry1 = BlogPost.query()  # Retrieve all Account entitites
        qry2 = qry1.filter(BlogPost.author == user.email())

        list_to_return = []

        for item in qry2:
            body = item.body
            author = item.author
            title = item.title
            time = item.time
            item_id = item.key.id()
            dict_to_append = {"body": body, "author": author, "title": title, "time": time, "id": item_id}
            list_to_return.append(dict_to_append)

        final = json.dumps(list_to_return)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(final)



class AllPostsHandler(RequestHandler):
    def get(self):
        self.request.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        qry1 = BlogPost.query()
        list_to_return = []

        for item in qry1:
            body = item.body
            author = item.author
            title = item.title
            time = item.time
            id = item.key.id()
            dict_to_append = {"body": body, "author": author, "title": title, "time": time, "id": id}
            list_to_return.append(dict_to_append)

        final = json.dumps(list_to_return)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(final)

class CreatePostsHandler(RequestHandler):
    def post(self):
        user = users.get_current_user()

        if not user:
            response = "Failure"
            final = json.dumps(response)
            self.response.headers['Content-Type'] = 'application/json'
            return self.response.out.write(final)

        loaded_message = json.loads(self.request.body)

        body = loaded_message["body"]
        title = loaded_message["title"]

        time = datetime.datetime.now()
        fixed_time = time.strftime("%B %d, %Y")
        author = user.email()

        insert_payload = BlogPost(
            time=fixed_time,
            body=body,
            title=title,
            author=author,
        )

        insert_payload.put()

        final = json.dumps("Success")
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(final)




