# 读取两个文件，转化成两个kv列表，然后根据key获取对应的v，v相等，那么succ+1=>统计数据匹配成功率，匹配失败的单独拿出来
import re
import time
import json
import numpy

'''
功能: match list部分的解析，解析结果进行写入
读取文件，逐行解析，解析时间戳 和 对应list，作为kv对
返回值: kv list
'''


def parse(str):
    def norm(l):
        return l[l.index('list: ') + 6 :].strip('\n')

    in_file = open(str)
    lines = in_file.readlines()
    key_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}_\d*_\d*")
    res = []
    for line in lines:
        k = re.findall(key_pattern, line)
        if len(k) > 0:
            v = norm(line)
            res.append([k[0], v])
    in_file.close()
    res = dict(res)
    write2File(str, res)
    return res


'''
功能: 将kv list写入文件中
'''


def write2File(name, kv_list):
    out = open("result_" + name, "w")
    if type(kv_list) == list:
        for k in kv_list:
            out.write("{}\n".format(k))
    else:
        for k in kv_list:
            out.write("{} {}\n".format(k, kv_list.get(k)))
    out.close()


def parseKV(name):
    infile = open(name)
    lines = infile.readlines()
    res = []
    for line in lines:
        if len(line) > 10:
            stamp = line[: line.index('[')].strip(' ')
            if int(stamp[-10:]) > 1635984031:  # 早8点
                val_str = line[line.index('[') :].strip('\n')
                val = json.loads(val_str)
                val.sort()
                res.append([stamp, val])
    print("解析" + name + "完毕")
    return dict(res)


'''
对两个list进行比对统计
统计oldlist中的数据在下游数据中出现并且val相等的情况
分别统计出 miss_match 以及 match_list
然后各自写入到文件中
'''


def match_correct(old_list, new_list):
    miss_match = []
    match_list = []
    for k in old_list:
        if k in new_list and old_list.get(k) == new_list.get(k):
            match_list.append([k, old_list.get(k)])
        # elif k in new_list:
        else:
            miss_match.append([k, old_list.get(k)])
    miss_match = dict(miss_match)
    match_list = dict(match_list)
    conclusion1 = "上游list数量: {} 下游list数量: {}".format(len(old_list), len(new_list))
    conclusion2 = "精确匹配结果: 匹配数量{} 失配数量{} 匹配程度{} 失配程度{}".format(
        len(match_list),
        len(miss_match),
        len(match_list) / len(old_list),
        len(miss_match) / len(old_list),
    )
    print(conclusion1)
    print(conclusion2)
    return miss_match, match_list


'''
粗略匹配
'''


def match_rough(old_list, new_list):
    miss_match = []
    match_list = []
    for k in old_list:
        if k in new_list:
            match_list.append(k)
        else:
            miss_match.append(k)
    con1 = "上游list数量: {} 下游list数量: {}".format(len(old_list), len(new_list))
    con2 = "粗略匹配结果: 匹配数量{} 失配数量{} 匹配程度{} 失配程度{}".format(len(match_list), len(miss_match), len(match_list) / len(old_list), len(miss_match) / len(old_list))
    print(con1)
    print(con2)
    return miss_match, match_list


'''
key存在但是数据不同
'''


def not_match(old_list, new_list):
    miss_match = []
    for k in old_list:
        if k in new_list and old_list.get(k) != new_list.get(k):
            miss_match.append([k, [old_list.get(k), new_list.get(k)]])
    miss_match = dict(miss_match)
    print("上游list数量 {} 下游list数量 {}".format(len(old_list), len(new_list)))
    print("匹配结果: 失配数量{} 失配程度{}".format(len(miss_match), len(miss_match) / len(old_list)))
    return miss_match


'''
获取时间分布
input: unix时间戳，数组形式
'''


def get_time_distribution(time_list):
    res = []
    for k in time_list:

        pass
    for k in time_list:
        res.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(int(k) / 1000))))
        res.append(k)
    return res


def test():
    # step 1 清洗日志
    parse('clone_1115.txt')
    parse('async_1115.txt')
    clone_list = parseKV('result_clone_1115.txt')
    async_list = parseKV('result_async_1115.txt')

    # step 2 进行匹配
    miss_match, match_list = match_rough(clone_list, async_list)
    write2File('miss_match_stamp_1115.txt', miss_match)

    # step 3 统计匹配结果
    out_result = open('match_clone_async_1115.txt', 'w')
    scores = []
    for k in match_list:
        l1 = clone_list.get(k)
        l2 = async_list.get(k)
        sub_len = len(l1)
        score = 0
        for v in l1:
            if v in l2:
                score += 1
        scores.append(score / sub_len)

        out_result.write("{}\t{}\t{}\t{}\n".format(k, len(l1), len(l2), score / sub_len))
    out_result.write("数量 {}\t平均相似度 {}\n".format(len(match_list), numpy.mean(scores)))
    out_result.close()
    pass


test()
