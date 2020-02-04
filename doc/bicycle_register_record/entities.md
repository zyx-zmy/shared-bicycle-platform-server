# 单车注册信息

## Bicycle
Column|Type|Comments
:--|:--|:--
bicycle_id|string|id  
bicycle_num|string|车辆编号
bicycle_type_num|string|车型编号
company_name|string|公司名称
bicycle_type_num|int|车辆类型
location_type|string|定位类型 1:gps 定位 2:基站定位 3:gps 和 基站综合定位
bluetooth_mac|int|蓝牙 mac 地址
frame_number|string|车架号
production_time|int|出厂时间(时间戳)
first_put_time|string|初次投放时间(时间戳) 
last_put_time|bool|最新投放时间(时间戳)
last_put_lon|string|最新投放位置经度，例:“124.123456”
last_put_lat|bool|最新投放位置纬度， 例: “24.123123”
last_put_position|string|最新投放位置信息，例:“浑南区世纪路 2 号”
repair_count|bool|维修次数
last_repair_time|string|最新维修时间(时间戳)
last_recovery_time|bool|最新回收时间(时间戳)
put_status|string|投放状态 1:未投放 2:已投放 3:维修中 4 已回收
created_time|datetime|创建时间
updated_time|datetime|更新时间

