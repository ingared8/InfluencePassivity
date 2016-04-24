import numpy as np

class Yelp(object):

    def __init__(self, restaurants, ratings):
        self.restaurants = restaurants
        self.ratings = ratings

    def find(self, coordinates, radius, dining_hour=None, sort_by_rating=False):
        # Returns list of Restaurant within radius.
        #
        #  coordinates: (latitude, longitude)
        #  radius: kilometer in integer
        #  dining_hour: If None, find any restaurant in radius.
        #               Otherwise return list of open restaurants at specified hour.
        #  sort_by_rating: If True, sort result in descending order,
        #                  highest rated first.

        try:
            latitude = coordinates[0]
            longitude = coordinates[1]
            results = []
            ratings= []
            for i in range(len(self.restaurants)):
                restaurant = self.restaurants[i]
                rating = self.ratings[i]
                if (restaurant.longitude != coordinates[1] & restaurant.latitude != coordinates[0]):
                    if self.find_distance(coordinates[0],coordinates[1],restaurant.latitude,restaurant.longitude) <= radius:
                        if self.is_open(restaurant,dining_hour):
                            results.append(restaurant)
                    else:
                        pass
                else:
                    results.append(restaurant)
                    results.append(rating)

            return results.sort(key=lambda x : x.Rating.rating)
        except:
            raise RuntimeError("Error in finding ")

    def find_distance(self, lat1,lon1, lat2, lon2):
        pi = 22/7.0
        rad = 6378.137 # radius of earth (in kms)
        dLat = (lat2 - lat1) * pi / 180
        dLon = (lon2 - lon1) * pi / 180
        a = np.math.sin(dLat/2) * np.math.sin(dLat/2) + np.math.cos(lat1 * pi / 180) * np.math.cos(lat2 * pi / 180) * np.math.sin(dLon/2) * np.math.sin(dLon/2)
        c = 2 * np.math.atan2(np.sqrt(a), np.sqrt(1-a))
        d = rad*c
        return d # Kms

    def is_open(self, restaurant, dining_hour):

        # Assuming a twnety four scale time frame
        return (dining_hour >= restaurant.open_hour & dining_hour < restaurant.close_hour)


class Restaurant(object):
    # where open_hour and close_hour is in [0-23]
    def __init__(self, id, name, latitude, longitude, open_hour, close_hour):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.open_hour = open_hour
        self.close_hour = close_hour

class Rating(object):

    # rating is in [1-5]

    def __init(self, restaurant_id, rating):
        self.restaurant_id = restaurant_id
        self.rating = rating

def function1():
    print "Calling main1"
    for i in range(1,101):
        res = ""
        if ((i%3)==0):
            res += "On"
        elif (i%7 == 0):
            res += "Base"
        else:
            res += str(i)
        print res

def check_prime():

    # Since sqrt(100) = 10, lets look at factors till  10

    print(2)
    for i in range(3,101):
        for j in range(2,min(i,10)):
            if (i%j == 0 & i!=j):
                print(i)
                break
            else:
                pass



if __name__ == '__main__':

    #restaurants = [Restaurant(0, "Domino's Pizza", 37.7577, -122.4376, 7, 23)]
    #ratings = [Rating(0, 3)]

    #y = Yelp(restaurants, ratings)
    #y.find((37.7, -122.6), 5, None, False)

    function1()
    check_prime()
