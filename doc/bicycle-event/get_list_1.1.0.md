#### 地址
```
GET /bicycle_events
```

#### 请求参数
|字段|类型|是否必传|说明|
|---|---|---|
|company_name|string|否|企业名称|
|event_type|int|否|事件类型1违规停车 2超时用车 3超范围骑行|
|bicycle_number|string|否|车辆编号|
|user_id|string|否|用户编号|
|page_num|int|否|第几页 默认1|
|page_size|int|否|每页大小 默认15|

#### 返回状态

##### status 200 成功返回 [BicycleEvent] 列表
##### status 403 权限错误
##### status 422 参数错误
```
{
    '':'',
    'errors': [
    {'field': company_name, 'error': 'invalid'},
    {'field': user_id, 'error': 'invalid'},
    {'field': event_type, 'error': 'invalid'},
    {'field': bicycle_number, 'error': 'invalid'},
    {'field': page_num, 'error': 'invalid'},
    {'field': page_size, 'error': 'invalid'},
    ]
}
```
[BicycleEvent]:entities.md#BicycleEvent
