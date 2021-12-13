import pdb
from models.city import City
from models.pub import Pub

import repositories.city_repository as city_repository
import repositories.pub_repository as pub_repository

city_repository.delete_all()
pub_repository.delete_all()

city1 = City("Newfoundlager", "Canada", True)
city_repository.save(city1)

city2 = City("Mosdrink", "Russia", False)
city_repository.save(city2)

city3 = City("Cansberra", "Australia", True)
city_repository.save(city3)

pub1 = Pub("The Radge Moose", True, city1)
pub_repository.save(pub1)

pub2 = Pub("Bar Vodka", False, city2)
pub_repository.save(pub2)

pub3 = Pub("The Sleepy Koala", True, city3)
pub_repository.save(pub3)


