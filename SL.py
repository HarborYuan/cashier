import pickle

def save(data):
    with open("cash.data","wb") as f:
        pickle.dump(data,f)

def load():
    with open("cash.data","rb") as f:
        return pickle.load(f)
