June 19
用到的表
individualInvestorProfile
Group by user
https://docs.google.com/spreadsheets/d/15iMdNgAfp60K3bvtaJJcOUeEP9jaOq1AlLBwFRGOVlQ/edit?gid=582667491#gid=582667491

User
https://docs.google.com/spreadsheets/d/1F-vg0Q0IV_q9EOHgQHpUOD7DRJVQ1s3htYMgYGm7UfY/edit?gid=1056298877#gid=1056298877

Sheet1 - Only have group 1 data(get it from investor list)
去重过了

Name email dob

目的：
所有从investor list中来的user，我们应该把它整理成一个unique的表

把这两张表按照user group之后对一下
1. 确保对应得上
2. 给每一个profile 加上一个fk： user_id （final goal）

问题:
user还没整理完，无法产生一个手动自增的unique user_id

方法：
可以先反过来
1. 先给profile建一个unique的pk: manual_id start from 1
2. 再在user中建一个fk: profile_id 填写对应的manual_id in profile值

但是！user跟profile是one-many的关系
每一个profile应该有一个unique user_id
每个user可能有多个profile

所以：这里的问题是！每个user可能有多个profile，profile_id不唯一
所以在user中可能遇到这种状况
profile_id	user_id
1,2,3,4	1
9,10	2

先手动整理成上述这样，然后用pandas
把这两列转换生成另一张表，第一行user_id 是1，第十行user_id 是2,
做这种reverse mapping
然后再把reverse mapping添加到individualInvestorProfile中作为新的一列

另一个小任务
User建完后需要对每一列进行normalize
phone number
email （python包）
address 在bankaccount表中已经normalize了，替代掉user中的地址
问题：怎么对应上
办法：source and investor_name_raw in bankaccount join fund_id and investor_name_raw in individualInvestorProfile
investor_name_raw in bankaccount join original_investor_profile_id in User


结果：
1. 填充了individualInvestorProfile unique pk: profile_id start from 1
2. 在User 中为每个user填充了对应的profile_id
3. 填充了User unique pk: user_id start from 1
4. 翻过来在individualInvestorProfile中为每个profile填充了user_id
5. 在User中，normalize phonenumber， email，address（在bankaccount表中没找到对应的标黄了）
