#亲和性分析
import numpy as np
dataset_filename = "affinity_dataset.txt"
X = np.loadtxt(dataset_filename)
n_samples,n_features = X.shape
features = ["面包","牛奶","奶酪","苹果","香蕉"]
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
num_occurences = defaultdict(int)#发生次数

for sample in X:
    for premise in range(n_features):#遍历
        if sample[premise] == 0:continue#如果没有继续
        num_occurences[premise] += 1#如果有发生次数加1
        for conclusion in range(n_features):#再次遍历
            if premise == conclusion:#排除自身
                continue
            if sample[conclusion] == 1:#发现又买了其他物品后
                valid_rules[(premise,conclusion)] += 1#有效规则加1
            else:
                invalid_rules[(premise,conclusion)] += 1#无效规则加1
support = valid_rules#支持情况
confidence = defaultdict(float)
for premise, conclusion in valid_rules.keys():
    confidence[(premise, conclusion)] = valid_rules[(premise, conclusion)] / num_occurences[premise]
# for premise,conclusion in confidence:
#     premise_name = features[premise]
#     conclusion_name = features[conclusion]
#     print("Rule: 如果一个人买了 {0} 他们通常还会买 {1}".format(premise_name, conclusion_name))
#     print(" - 发生几率: {0:.3f}".format(confidence[(premise, conclusion)]))
#     print(" - 发生次数: {0}".format(support[(premise, conclusion)]))
#     print("")
def print_rule(premise, conclusion, support, confidence, features):
    premise_name = features[premise]
    conclusion_name = features[conclusion]
    print("Rule: 如果一个人买了 {0} 他们通常还会买 {1}".format(premise_name, conclusion_name))
    print(" - 发生几率: {0:.3f}".format(confidence[(premise, conclusion)]))
    print(" - 发生次数: {0}".format(support[(premise, conclusion)]))
    print("")
#排序取前五
from operator import itemgetter
sorted_support = sorted(support.items(),key=itemgetter(1),reverse = True)
for index in range(5):
    print("发生几率: #{0}".format(index+1))
    (premise,conclusion) = sorted_support[index][0]
    print_rule(premise,conclusion,support,confidence,features)

sorted_confidence = sorted(confidence.items(),key=itemgetter(1),reverse =  True)
for index in range(5):
    print("支持数: #{0}".format(index+1))
    (premise,conclusion) = sorted_support[index][0]
    print_rule(premise,conclusion,support,confidence,features)


