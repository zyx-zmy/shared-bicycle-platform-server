#### 地址
```
GET /users
```

#### 请求参数
|字段|类型|是否必传|说明|
|---|---|---|
|company_id|string|否|企业id|
|user_id|string|否|用户编号|
|page_num|int|否|第几页 默认1|
|page_size|int|否|每页大小 默认15|

#### 返回状态

##### status 200 成功返回 [User] 列表
##### status 403 权限错误
##### status 422 参数错误
```
{
    '':'',
    'errors': [
    {'field': company_name, 'error': 'invalid'},
    {'field': user_id, 'error': 'invalid'},
    {'field': page_num, 'error': 'invalid'},
    {'field': page_size, 'error': 'invalid'},
    ]
}
```

[User]:entities.md#User
