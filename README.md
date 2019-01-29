

# session

## #0 Blog

```
https://blog.csdn.net/Coxhuang/article/details/86694441
```


## #1 环境

```
Python3.6
Django==2.0.7
```

## #2 开始

### #2.1 数据库迁移

因为session是一个存在数据库得一张表,所以需要初始化数据库

```
python3 manage.py makemigrations 
python3 manage.py migrate 
```

### #2.2 设置session


```
class set_session(APIView):

    def post(self, request):

        request.session['email'] = 'cox@cox.com'

        return Response("设置session")
```

#### #2.2.1 设置

```
request.session['email'] = 'cox@cox.com' # 普通设置

request.session.setdefault('email',"cox@cox.com") # 存在则不设置

request.session.set_expiry(value)

# 默认的过期时间是两周，如果自己设置了过期时间，这样自己设定的优先级就会高于默认的

# 如果value是个整数，session会在些秒数后失效。

# 如果value是个datatime或timedelta，session就会在这个时间后失效。

# 如果value是0,用户关闭浏览器session就会失效。

# 如果value是None,session会依赖全局session失效策略。

```
#### #2.2.2 获取

```
request.session["email"] # 如果email不存在则会报错

request.session.get["email"] # 如果email不存在则会报错

request.session.get["email",None] # 如果email不存在则返回None

```

#### #2.2.3 删除

```
del request.session["email"] # 删除

request.session.clear() # 删除

request.session.clear_expired() # 清除小鱼当前时间的session

request.session.delete("session_key") # 删除当前用户的所有Session数据



```

#### #2.2.4 查看session


```
request.session.keys()

request.session.values()

request.session.items()

```

