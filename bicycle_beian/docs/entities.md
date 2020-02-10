# 单车备案

## BicycleBeian
Column|Type|Comments
:--|:--|:--
beian_bicycle_id|string|id  
bicycle_model_code|string|车辆型号编码
company_id|string|企业id
bicycle_model_name|string|车辆型号名称
bicycle_type|int|单车类型 1普通单车 2助力车
bicycle_model_describe|string|车辆型号描述
access_num|int|准入数量
bicycle_model_image|string|车辆型号图片
has_bicycle_number|bool|是否含有车辆编号
created_time|datetime|创建时间
updated_time|datetime|更新时间


## BicycleNumber
Column|Type|Comments
:--|:--|:--
id|string|id  
bicycle_number|string|车辆编号
beian_bicycle_id|string|备案车辆
company_id|string|备案企业
created_time|datetime|创建时间
updated_time|datetime|更新时间