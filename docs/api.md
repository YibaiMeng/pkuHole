# PKU Hole API 文档

## 数据结构

树洞的是由许许多多的洞（post）组成的。每个洞有一段由“洞主”写的文字，可以附加一张图片或一段音频。登录用户可以选择关注某个洞，不过这对洞的呈现没有作用，无论关注人数如何，洞都是按照发布的时间顺序呈现的。每个洞附属一些评论（comment）。评论只能发布文字，每个评论者将被赋予一个化名，可以回复洞主以及本评论下的人。任何消息一经发布就不能更改，但可以向管理员举报，管理员可以删除。

### 洞（post）

每个洞有以下几个参数：

| 参数名称      | 参数类型      | 参数描述                           |
| ------------- | ------------- | ---------------------------------- |
| pid           | `int`         | 洞的身份标识，唯一不重复。按照洞发布的时间顺序依次赋值 |
| text          | `str`         | 文字内容。Unicode编码，要预处理一下 |
| type          | `str`         | 洞的类型。可以取text，image，audio三个值 |
| url           | `str`         | 如果type是image或audio，表示该洞的附属图片音频的URL。该URL显然是某个哈希，但我不知道是什么 |
| reply         | `int`         | 评论的数量 |
| likenum       | `int`         | 喜欢的数量 |
| time          | `int`         | 洞发布时间，以POSIX时间戳的形式储存，应该是服务器的时间 |
| extra         | `int`         | 如果type是image或auio，表示洞的附属图片音频文件的大小。单位是字节 |


### 评论（comment）

每个评论有以下参数：

| 参数名称      | 参数类型      | 参数描述                           |
| ------------- | ------------- | ---------------------------------- |
| cid           | `int`         | 评论的身份标识，唯一不重复。按照洞发布的时间顺序依次赋值。注意，同一个洞的评论的cid不一定连续！ |
| pid           | `int`         | 评论属于的洞的pid |
| text          | `str`         | 文字内容。Unicode编码，要预处理一下。开头会有回复者的化名。向谁回复也是在文字内容中体现的 |
| name          | `str`         | 回复者化名 |
| islz          | `bool`        | 回复者是否是洞主 |
| hidden        | ?             | 不明，一般是0 |
| anonymous     | ?             | 不明，一般是1 |
| time          | `int`         | 评论发布时间，以POSIX时间戳的形式储存，应该是服务器的时间 |

## API列表

树洞提供获取洞和评论信息的功能，以及发布评论和树洞的功能。一切操作都是通过HTTP RESTful API的方式进行的。信息的获取不需要身份的验证，不过发帖和评论的过程是需要验证的。系统还提供按关键词检索的功能。

具体的功能列表如下：
- 一页一页地获取洞的信息。每页为30个洞。获取的信息不含评论。
- 获取某个洞的所有评论
- 搜索含有特定关键词的洞

所有的操作，基本信息都一致：

- 请求类型：HTTP

- 请求地址：http://www.pkuhelper.com/services/pkuhole/api.php

- 请求方式：`GET`

- 数据类型：`application/x-www-form-urlencoded`

- 响应类型：`application/json`

User-Agent目前服务器没有校验，不过客户端用的是`Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36`。

### 获取洞

请求参数如下表所示：

| 参数名称  | 数据类型 | 描述                |  是否必须  | 默认值/固定值  |
| ---       | ---      | ---                 |   ---      | --             | 
| action    | `str`    | 操作的行为描述      | 是         | getlist        |
| p         | `int`    | 第几页的洞，从0开始 | 否         | 0              |

例子：获得目前第3页的洞
```bash
curl http://www.pkuhelper.com/services/pkuhole/api.php?action=getlist&p=3
```
这获得的是按照发布时间顺序排列，最新的第91个到第120个洞的信息。

返回值例子如下
```json
{
   "code":0,
   "data":[ 
      {
         "pid":"464012",
         "text":"\u6709\u5b66\u957f\u59d0\u7b7e\u8fc7\u660e\u5fb7\u7acb\u4eba\u8fd9\u5bb6\u7559\u5b66\u4e2d\u4ecb\u673a\u6784\u5417\uff1f\u6c42\u6d4b\u8bc4\uff01",
         "type":"text",
         "timestamp":"1533021971",
         "reply":"0",
         "likenum":"1",
         "extra":"0",
         "url":"",
         "hot":"1533021971"
      },
      ...... 还有29个
   ],
   "timestamp" : 1533022261
}
```

### 获取评论

请求参数如下表所示：

| 参数名称  | 数据类型 | 描述               |  是否必须  | 默认值/固定值 |
| ---       | ---      | ---                |   ---      | ------------- | 
| action    | `str`    | 操作的行为描述     | 是         | getcomment    |
| pid       | `int`    | 评论对应的洞的pid  | 是         | ---           |

例子：获得234567号洞的评论
```bash
curl http://www.pkuhelper.com/services/pkuhole/api.php?action=getcomment&pid=234567
```

返回值例子如下
```json
{ 
   "code":0,
   "data":[  
      {  
         "cid":"10329",
         "pid":"39000",
         "text":"[Alice]  hello world!",
         "timestamp":"1445178275",
         "hidden":"0",
         "anonymous":"1",
         "islz":0,
         "name":"Alice"
      },
      ......
   ],
   "attention":0
}
```

### 检索

请求参数如下表所示：

| 参数名称  | 数据类型 | 描述               |  是否必须  | 默认值/固定值 |
| ---       | ---      | ---                |   ---      | ------------- | 
| action    | `str`    | 操作的行为描述     | 是         | search        |
| keywords  | `str`    | 关键词             | 否         | ---           |
| type      | `str`    | 检索的洞的类型，为text，audio，image中的一个，不填为全部  | 否         | ---           |
| pagesize  | `int`    | 最多返回的洞的数量 | 否         | 100           |

例子：查找有关键词“元培”的树洞，只要前20个结果。
```bash
curl http://www.pkuhelper.com/services/pkuhole/api.php?action=search&keywords=元培&pagesize=20
```

如果keywords不填的话，将会按照时间顺序返回值。比如我想要最近10000条洞：
```bash
curl http://www.pkuhelper.com/services/pkuhole/api.php?action=search&pagesize=10000
```
pagesize没有人为上限，不过一般超过100000那边服务器会崩。

返回结果和获取洞时的结果，除了没有整体的timestamp参数，其他都一样。

### 零碎说明

获得最近的30个洞有另一个方法：
```
http://www.pkuhelper.com/services/pkuhole/api.php?action=refreshlist
```
和`getlist`貌似没有什么区别。

图片的URL是
```
http://www.pkuhelper.com/services/pkuhole/images/
```
音频的URL是
```
http://www.pkuhelper.com/services/pkuhole/audios/ 
```
