import numpy as np
import operator
'''
函数说明: 创建数据集
Returns:
group - 数据集
labels - 分类标签
'''
def createDataSet():
    group=np.array([[1,101],[5,89],[108,5],[115,8]]) #数据集，四组二维特征
    labels=['爱情片','爱情片','动作片','动作片'] #分类标签，四组特征的标签
    return group,labels
 
"""
函数说明:kNN算法,分类器
Parameters:
inX - 用于分类的数据(测试集)
dataSet - 用于训练的数据(训练集)
labes - 分类标签
k - kNN算法参数,选择距离最小的k个点
Returns:
sortedClassCount[0][0] - 分类结果
"""
def classify0(inX, dataSet, labels, k):
    # numpy函数shape[0]返回dataSet的行数
    dataSetSize = dataSet.shape[0]
    print(dataSetSize)
    # b = tile(a,(m,n)):即是把a数组里面的元素复制n次放进一个数组c中，然后再把数组c复制m次放进一个数组b中
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    print(diffMat)
    # 二维特征相减后平方
    sqDiffMat = diffMat ** 2
    print(sqDiffMat)
    # sum()所有元素相加，sum(0)列相加，sum(1)行相加
    sqDistances = sqDiffMat.sum(axis=1)
    print(sqDistances)
    # 开方，计算出距离
    distances = sqDistances ** 0.5
    print(distances)
    # 返回distances中元素从小到大排序后的索引值
    sortedDistIndices = distances.argsort()
    print(sortedDistIndices)
    # 定一个记录类别次数的字典
    classCount = {}
    for i in range(k):
        # 取出前k个元素的类别
        voteIlabel = labels[sortedDistIndices[i]]
        # dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
        # 计算类别次数
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # python3中用items()替换python2中的iteritems()
    # key=operator.itemgetter(1)根据字典的值进行排序
    # key=operator.itemgetter(0)根据字典的键进行排序
    # reverse降序排序字典
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # 返回次数最多的类别,即所要分类的类别
    return sortedClassCount[0][0]
 
 
if __name__ == '__main__':
    # 创建数据集
    group, labels = createDataSet()
    # 测试集
    test = [105, 20]
    # kNN分类
    test_class = classify0(test, group, labels, 3)
    # 打印分类结果
    print(test_class)