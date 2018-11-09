import arff, numpy as np

dataset = arff.load(open('OffComBR2.arff', 'r'))
data = np.array(dataset['data'])
print(data[1])
