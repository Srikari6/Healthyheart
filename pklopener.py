import pickle

file_path = 'C:\Users\saina\Downloads\SWE1\SWE\SWE.pkl'


with open('C:\Users\saina\Downloads\SWE1.zip\SWE', 'rb') as file:
    data = pickle.load(file)


print(data)
