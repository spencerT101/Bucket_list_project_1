from flask import Blueprint, Flask, render_template, redirect, request

import repositories.bucket_list_repository as bucket_list_repository
import repositories.country_repository as country_repository
import repositories.destination_repository as destination_repository

from models.bucket_list import BucketList
from models.destination import Destination
from models.country import Country

city_destinations_blueprint = Blueprint("city_destinations", __name__)

@city_destinations_blueprint.route("/city")
def cities():
    cities = destination_repository.select_all()
    return render_template("city/index.html", all_cities = cities)

@city_destinations_blueprint.route("/city/new", methods = ['GET'])
def new_country():
    country = country_repository.select_all()
    return render_template("city/new.html", all_countries = country)

@city_destinations_blueprint.route("/city", methods = ['POST'])
def create_city():
    city_name = request.form["city_name"]
    country_id = request.form["country"]
    visited = request.form["visited"]
    country = country_repository.select(country_id)
    city = Destination(city_name, country, visited)
    destination_repository.save(city)
    return redirect('/city')



@city_destinations_blueprint.route("/city/<id>/edit", methods = ['GET'])
def edit_visited(id):
    city = destination_repository.select(id)
    # destination = destination_repository.select_all()
    country = country_repository.select_all()
    return render_template("city/edit.html", city = city, country = country)

@city_destinations_blueprint.route("/city/<id>", methods = ['POST'])
def update_visited(id):
    city = destination_repository.select(id)
    visit = request.form["visited"]
    # country_id = country_repository.select(id)
    destination_visit = Destination(city.city_name,city.country,visit, city.id)
    destination_repository.update(destination_visit)
    return redirect('/destinations')