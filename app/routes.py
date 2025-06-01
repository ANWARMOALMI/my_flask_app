from flask import Blueprint

main = Blueprint('main', _name_)

@main.route('/')
def home():
    return "Welcome to my Flask App on Render!"
