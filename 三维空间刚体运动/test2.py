import csv
import random
import datetime

# 定义一个名字列表
names = ['李思', '江华', '姜嘉星', '李国峰', '范巍']

# 生成随机时间
def random_time(start_time, end_time):
    time_format = '%Y/%m/%d %H:%M'
    stime = datetime.datetime.strptime(start_time, time_format)
    etime = datetime.datetime.strptime(end_time, time_format)
    return (random.random() * (etime - stime) + stime).strftime(time_format)

# 生成随机名字
def random_name(names):
    return random.choice(names)

# 生成一组随机数据
def random_data(start_time, end_time, names):
    data = []
    for i in range(5):
        time = random_time(start_time, end_time)
        name = names[i]
        for i in range(random.randint(5, 15)):
            data.append([time, name])
    return data

# 生成20组随机数据
start_time = ['2023/6/1 09:00', '2023/6/1 10:00', '2023/6/1 11:00', '2023/6/1 12:00', '2023/6/1 13:00', '2023/6/1 14:00',
              '2023/6/1 15:00', '2023/6/1 16:00', '2023/6/1 17:00', '2023/6/1 18:00', '2023/6/1 19:00', '2023/6/1 20:00',]
end_time = ['2023/6/1 10:00', '2023/6/1 11:00', '2023/6/1 12:00', '2023/6/1 13:00', '2023/6/1 14:00', '2023/6/1 15:00',
            '2023/6/1 16:00', '2023/6/1 17:00', '2023/6/1 18:00', '2023/6/1 19:00', '2023/6/1 20:00', '2023/6/1 21:00']

alldata = []
for st,et in zip(start_time, end_time):
    data = random_data(st, et, names)
    alldata.extend(data)
# data = [random_data(start_time, end_time, names) for i in range(800)]

sorted_data = sorted(alldata, key=lambda x: x[0])

result = []
# 统计每个名字出现的次数
count_dict = {}
for d in sorted_data:
    name = d[1]
    if name in count_dict:
        count_dict[name] += 1
        d.append(count_dict[name])
        result.append(d)
    else:
        count_dict[name] = 1
        d.append(count_dict[name])
        result.append(d)

# 输出排序后的结果和出现次数
# for i, d in enumerate(result):
#     print(f"{i+1}\t{d[0]}\t{d[1]}\t{d[2]}")

with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['时间', '姓名', '总出现次数']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i, d in enumerate(sorted_data):
        writer.writerow({'时间': d[0], '姓名': d[1], '总出现次数': d[2]})

print('结果已保存到 output.csv 文件中')