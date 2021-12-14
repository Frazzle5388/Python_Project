from flask import Flask, Blueprint, render_template, request, redirect

from models.pub import Pub
from models.city import City

import repositories.pub_repository as pub_repository
import repositories.city_repository as city_repository

pubs_blueprint = Blueprint("pubs", __name__)

@pubs_blueprint.route("/pubs")
def pubs():
    pubs = pub_repository.select_all()
    return render_template("pubs/index.html", all_pubs=pubs)

@pubs_blueprint.route("/pubs/new", methods=['GET'])
def new_pub():
    cities = city_repository.select_all()
    return render_template("cities/new.html", all_cities=cities)

@pubs_blueprint.route("/pubs", methods=['POST'])
def create_pub():
    name = request.form["name"]
    city = city_repository.select(request.form["city_id"])
    visited = request.form["visited"]
    pub = Pub(name, city, id, visited)
    pub_repository.save(pub)
    return redirect('/pubs')

@pubs_blueprint.route("/pubs/<id>", methods=['GET'])
def show_pub(id):
    pub = pub_repository.select(id)
    return render_template("pubs/show.html", pub = pub, all_pubs=pubs)

@pubs_blueprint.route("/pubs/<id>/edit", methods=['GET'])
def edit_pubs(id):
    pub = pub_repository.select(id)
    cities = city_repository.select_all()
    return render_template("pubs/edit.html", pub = pub, all_cities=cities)

@pubs_blueprint.route("/pubs/<id>", methods=['POST'])
def update_pub(id):
    name = request.form["name"]
    city = city_repository.select(request.form["city_id"])
    visited = request.form["visited"]
    pub = Pub(name, city, id, visited)
    pub_repository.update(pub)
    return redirect('/pubs')

@pubs_blueprint.route("/pubs/<id>/delete", methods=['POST'])
def delete_pub(id):
    pub_repository.delete(id)
    return redirect('/pubs')



