import numpy as np
dataset_filename = "affinity_dataset.txt"
X = np.loadtxt(dataset_filename)
# 第一部分
#print(X[:5]) 打印前五行数据

# num_apple_purchases = 0
# for sample in X:
#     if sample[3] == 1:
#         num_apple_purchases +=1
# print("{0} people bought Apples".format(num_apple_purchases))

# 第二部分
from collections import defaultdict
valid_rules = defaultdict(int)#有效规则
invalid_rules = defaultdict(int)#无效规则
mum_occurances = defaultdict(int)


