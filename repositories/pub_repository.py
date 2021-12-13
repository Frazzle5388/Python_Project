from db.run_sql import run_sql

from models.pub import Pub
from models.city import City

def save(pub):
    sql = "INSERT INTO pubs (name, visited, city_id) VALUES (%s, %s, %s) RETURNING *"
    values = [pub.name, pub.visited, city.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pub.id = id
    return pub

def select_all():
    pubs = []

    sql = "SELECT * FROM pubs"
    results = run_sql(sql)

    for row in results:
        pub = Pub(row['name'], row['visited'], row['city_id'] )
        pubs.append(pub)
    return pubs

def select(id):
    pub = None
    sql = "SELECT * FROM pubs WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        pub = City(result['name'], result['visited'], result['id'])
    return pub

def delete_all():
    sql = "DELETE FROM pubs"
    run_sql(sql)



