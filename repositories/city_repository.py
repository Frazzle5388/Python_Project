from db.run_sql import run_sql

from models.city import City
from models.pub import Pub

import repositories.pub_repository as pub_repository


def save(city):
    sql = "INSERT INTO cities (name, country, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.country, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['name'], row['country'], row['visited'], row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = City(result['name'], result['country'], result['visited'], result['id'])
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def pubs(city):
    cities = []

    sql = "SELECT * FROM pubs WHERE pub_id = %s"
    values = [city.id]
    results = run_sql(sql, values)

    for row in results:
        pub = Pub(row['name'], row['city_id'], row['visited'], row['id'])
        pubs.append(pub)
    return pubs