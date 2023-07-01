import pymongo
import numpy as np
import matplotlib.pyplot as plt
# Find the movies which have rating > 9 and have genre as Drama from 'movies' collection. Also find their total runtime.
if __name__ == '__main__':
    connection = pymongo.MongoClient('mongodb://localhost:27017')
    db = connection['movieData']
    coll = db['movies']
    f_docs = coll.find({"$and": [{'rating.average': {'$gt': 9}}, {'genres': 'Drama'}]})
    total_runtime = 0
    individual_runtime = []
    no_of_docs = 0
    movies = []
    for item in f_docs:
        total_runtime += item['runtime']
        individual_runtime.append(item['runtime'])
        no_of_docs += 1
        movies.append(item['name'])
    print(f'The total runtime is {total_runtime} minutes')
    print(f'No of movies: {no_of_docs}')
    print(f'The {no_of_docs} movies with genre as Drama and rating > 9 are as follows:')
    for i in movies:
        print(i)
    # plot above printed movies and their runtime on bar graph
    left_coordinates = np.arange(no_of_docs)
    plt.bar(left_coordinates, individual_runtime, tick_label=movies, width=0.3, color=['green', 'blue'])
    plt.title('Movies and Runtime')
    plt.xlabel('Movies')
    plt.ylabel('Runtime')
    plt.show()
