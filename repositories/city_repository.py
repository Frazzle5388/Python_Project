from db.run_sql import run_sql

from models.city import City


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
        city = City(row['name'], row['country'], row['visited'], row['id'] )
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

def update(id):
    sql = "UPDATE pubs SET (name, visited, city_id) = (%s, %s, %s) WHERE id =%s"
    values = [pub.name, pub.visited, city.id, pub.id]
    run_sql(sql, values)