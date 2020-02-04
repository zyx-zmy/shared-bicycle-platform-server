# 单车行驶状态


## BicycleDriverRecord
Column|Type|Comments
:--|:--|:--
id|string|id  
bicycle_num|string|车辆编号
bicycle_status|string|车辆状态 1:停放中 2:行驶中 3:调度 中 4:被预约
update_time|string|状态更新时间
lon|int|车辆位置经度，例:“124.123456”
lat|string|车辆位置纬度， 例: “24.123123”
position|int|位置信息，例:“浑南区世纪路 2 号”
created_time|datetime|创建时间
updated_time|datetime|更新时间
