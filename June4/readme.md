June 4
目的：
1. 建立两个表bankaccount和subscription
2. subscription中要有bankaccount的fk （copy bankaccount的manual_id放到subscription)
3. bankaccount column m 9:40

把subscription 中的account number copy到bankaccount中去（因为是fancyadmin中去）

如果要join，可以用
fund_id_copy和investor_profile_id_raw
source和investor_name_raw，

1. 先按照Unmatched_Records中account_sub把subscription中的account_number 都修改正确，保证是从fancyadmin中的得到的
2. 把subscription 中的account number copy到bankaccount中去
3. 按照这几列把两个表一一对应，在subscription（bank_account_id）中加上bankaccount的fk （bankaccount的manual_id）
Sub
fund_id_copy	manual_id	investor_profile_id_raw
Bankaccount
manual_id	source	investor_name_raw

June 7
profile audit
确认user 和profile分别是哪个
User 谁在使用账户
profile user在给谁做投资 跟ssn   tax_id相关
associate name 不是user的另外一个名字

Dob 和 tax_id还要检查一下