import pymongo
import matplotlib.pyplot as plt
import numpy as np
# Find the total quantity of each type of small pizza using aggregation pipline and plot the same on horizontal bar plot
connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['Yagna_testing']
col = db['orders']
pipeline = [{"$match": {'size': 'small'}},
            {'$group': {'_id': '$name', 'total_quantity': {'$sum': '$quantity'}}},
            {'$sort': {'_id': -1}}]
aggr_docs = col.aggregate(pipeline)
print('The total available quantity for small size pizza is as follows:')
pizza_type = []
pizza_quantity = []
doc_count = 0
for item in aggr_docs:
    doc_count += 1
    pizza_type.append(item["_id"])
    pizza_quantity.append(item["total_quantity"])
    print(f'{item["total_quantity"]} {item["_id"]} pizza available!')
fig, ax = plt.subplots()
y_pos = np.arange(doc_count)
plt.barh(y_pos, pizza_quantity, color='yellow')
plt.xlabel('quantity')
ax.set_yticks(y_pos)
ax.set_yticklabels(pizza_type)
plt.title('Small pizza type vs available quantity')
plt.show()
