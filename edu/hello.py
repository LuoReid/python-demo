import pandas as pd

col_school = "1你所在学校__ __ __"
col_remove = ["2您的性别", "3您的学历：", "4您的职业"]
cols = [
    "5您是否了解学校的办学理念、办学目标和学生培养目标",
    "6您是否了解学校的课程设置和对孩子的学习要求",
    "7对于学校校园环境的整洁美观程度，你感到：",
    "8您对学校提供的学生学习和活动的场地、设施等条件的配置情况感到",
    "9您对学校管理制度和管理举措的保障程度感到",
    "10您的孩子入学后，在行为习惯培养、能力发展方面的进步表现",
    "11您觉得老师对您的孩子是否公平？",
    "12在您孩子兴趣特长的培养方面，您觉得学校",
    "13学校是否对家长开展“双减”“五项管理”的政策宣传和指导",
    "14您对学校提供的学生课后服务感到",
    "15疫情期间，您有接收到学校推送或宣传的家庭教育指导类信息吗？",
    "16疫情期间，您对学校实施在线教学的组织管理和效果感到",
    "17据您了解，学校的音乐、美术、体育、劳动等课程是否有被其他课占用的情况",
    "18据您了解，每天校内体育活动（包括广播操、体育课、体育活动、课间大活动等）的情况是：",
    "19老师上课时，您的孩子对老师教学内容接受情况是",
    "20学校布置给您孩子的书面作业，每天回家后大约还需要花多少时间完成",
    "21您的孩子是否会因为学校各类作业和学习要求（含书面和非书面）影响睡眠时间？",
    "22每次期末考试后，您是否知道孩子成绩在班级中的排名",
    "23您对孩子学校教师队伍师德师风的总体印象是",
    "24您认为孩子任课老师的教育教学能力",
    "25据您了解，孩子所在班的老师对待家长送礼采用的方式是",
    "26您是否发现您孩子学校的任课教师有推荐有偿补课或进行有偿补课的现象",
    "27您觉得学校的收费情况",
    "28您觉得和孩子任课老师联系沟通是否方便",
    "29请您对孩子学校办学情况作出总体评价",
]

df = pd.read_excel("计算工具.xlsx", sheet_name="结果", names=cols, skiprows=1, nrows=4)
score = {}
for c in cols:
    idx = 0
    for k, v in df[c].fillna(0).items():
        idx += 1
        key = str(idx)
        # print("ddd-", k, v, key)
        kv = score.get(c)
        if kv:
            kv[key] = v
        else:
            score[c] = {key: v}

print(df)
print(score)
df1 = pd.read_excel("计算工具.xlsx", sheet_name="元数据")
dfcount = df1.groupby(col_school)[cols[0]].count().reset_index(name="学生数")
df1 = df1.drop(col_remove, axis=1)

num_cols = df1.select_dtypes(include=["number"]).columns
print("num cols", num_cols)
df1.applymap(str)
# df1[num_cols] = df1[num_cols].astype(str)
for nc in num_cols:
    df1[nc] = df1[nc].apply(lambda x: f"{x:.0f}")

# print('school:',df1)
print("row2 orinal:", df1.iloc[2])
for col in cols:
    if col in score:
        df1[col] = df1[col].map(score[col])
df2 = df1.groupby(col_school).sum()
df2["总分"] = df2[cols].sum(axis=1)
df3 = pd.merge(dfcount, df2, on=col_school, how="inner")
df3["平均分"] = (df3["总分"] / df3["学生数"]).round(2)
print("row2:", df1.iloc[2])
print("sum:", df2.iloc[1])
print("sum:", df3)
print("count:", dfcount)
df3.to_excel("计算工具 2024.xlsx")
