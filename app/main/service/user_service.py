import requests, json
from flask import current_app, session
from . import save_image

class UserService:
    @staticmethod
    def create(data):
        return requests.post("{}/user/".format(
            current_app.config["API_DOMAIN"]),
            json = {
                "name": data.get("name_input"),
                "username": data.get("username_input"),
                "email": data.get("email_input"),
                "password": data.get("password_input")
            }
        )
    
    @staticmethod
    def edit(pid, token, data_form, data_file):
        return requests.patch("{}/user/{}".format(
            current_app.config["API_DOMAIN"],
            pid),
            headers = {
                "Authorization" : "Bearer {}".format(token)
            },
            json = {
                "name": data_form.get("name_input"),
                "username": data_form.get("username_input"),
                "email": data_form.get("email_input"),
                "password": data_form.get("password_input"),
                "photo": save_image(data_file.get("photo_input"))
            }
        )

    @staticmethod
    def get_by_token():
        return requests.get("{}/user/bytoken".format(
            current_app.config["API_DOMAIN"]),
            headers = {
                "Authorization" : "Bearer {}".format(session["booped_in"])
            }
        )
    @staticmethod
    def get_by_username(username):
        return requests.get("{}/user/username/{}".format(
            current_app.config["API_DOMAIN"], username),
            headers = {
                "Authorization" : "Bearer {}".format(session["booped_in"])
            }
        )

class AdminService:
    @staticmethod
    def create(data):
        return requests.post("{}/user/admin".format(
            current_app.config["API_DOMAIN"]),
            json = {
                "name": data.get("name_input"),
                "username": data.get("username_input"),
                "email": data.get("email_input"),
                "password": data.get("password_input")
            }
        )
    @staticmethod
    def get_by_token():
        return requests.get("{}/user/bytoken".format(
            current_app.config["API_DOMAIN"]),
            headers = {
                "Authorization" : "Bearer {}".format(session["admin_booped_in"])
            }
        )