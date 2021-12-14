from db.run_sql import run_sql

from models.pub import Pub
from models.city import City

import repositories.city_repository as city_repository

def save(pub):
    sql = "INSERT INTO pubs (name, city_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [pub.name, pub.city.id, pub.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    pub.id = id
    return pub

def select_all():
    pubs = []

    sql = "SELECT * FROM pubs"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        pub = Pub(row['name'], city, row['visited'])
        pubs.append(pub)
    return pubs

def select(id):
    pub = None
    sql = "SELECT * FROM pubs WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = city_repository.select(row['city_id'])
        pub = Pub(result['name'], city, result['visited'], result['id'])
    return pub

def delete_all():
    sql = "DELETE FROM pubs"
    run_sql(sql)

def update(pub):
    sql = "UPDATE pubs SET (name, city_id, visited) = (%s, %s, %s) WHERE id = %s"
    values = [pub.name, pub.city.id, pub.visited, pub.id]
    print(values)
    run_sql(sql, values)



