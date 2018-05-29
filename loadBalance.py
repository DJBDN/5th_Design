# 计算各个服务器的权重
# 参数为字典类型
# 参数的键为服务器编号（字符串）
# 参数的值为长度为2的列表
# 列表包含了服务器的最大负载和当前负载
# 函数返回按降序排列的服务器编号列表
# 权重的计算方式为 权重 = 负载空余量 * 负载空余量所占最大负载百分比
# 即权重越大的服务器越空闲
import operator
def weightCalculation(switchInfo):
    # 初始化权重
    weight = [0] * len(switchInfo)
    # 交换机列表
    switchKeys = list(switchInfo.keys())
    # 交换机负载情况
    switchLoad = list(switchInfo.values())
    # 计算权重
    for i in range(len(switchInfo)):
        weight[i] = (switchLoad[i][0] - switchLoad[i][1]) * ((switchLoad[i][0] - switchLoad[i][1]) / switchLoad[i][0])
    # 按权重降序排列
    sortedWeight = dict()
    for i in range(len(switchInfo)):
        sortedWeight[weight[i]] = switchKeys[i]
    sortedKeys = sorted(sortedWeight.items(), key=operator.itemgetter(0), reverse=True)
    # 获取降序排列的交换机列表
    sortedWeight = list()
    for x in sortedKeys:
        sortedWeight.append(x[1])
    return sortedWeight


# 当有新连接接入
# 返回最空闲的服务器的编号
# 参数也为服务器信息
def newLinkTo(switchInfo):
    switchList = weightCalculation(switchInfo)
    return switchList[0]


# 测试
if __name__ == '__main__':
    # 服务器信息
    # 第一列为最大负载
    # 第二列为当前负载
    swInfo = dict()
    swInfo['s1'] = [1000, 100]
    swInfo['s2'] = [2000, 200]
    swInfo['s3'] = [3000, 200]
    swInfo['s4'] = [1000, 200]
    swInfo['s5'] = [10000, 9000]
    # 初始化新连接接入的服务器的编号
    nextServer = 's1'
    # 假设有2000次连接
    # 为了方便演示
    # 假设每次连接时新接入100台主机
    for i in range(20):
        # 指定服务器负载 +100
        swInfo[nextServer][1] += 100
        # 输出当前连接端口
        print('当前连接端口:'+nextServer)
        # 计算下一次接入时连接的服务器编号
        nextServer = newLinkTo(swInfo)
        # 输出各个服务器的负载信息
        print('下一连接端口:'+nextServer)
        print(swInfo)
        print('')