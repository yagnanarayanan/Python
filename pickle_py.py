# pickle --> preserve and keep and fetch when required with binary protocol
import pickle
# storing in pickle file
cars = ["Zen", "Alto", "Esteem"]
fp = open("cars.pkl", 'wb')
pickle.dump(cars, fp)
fp.close()
# extracting from pickle file
fp = open("cars.pkl", "rb")
text = pickle.load(fp)
print(text)
print(type(text))
fp.close()
