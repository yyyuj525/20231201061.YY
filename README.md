# Hello World Django应用

这是一个简单的Django Hello World应用程序。

## 功能特性

- 首页欢迎页面
- Hello World页面
- 个性化问候页面（支持传入姓名参数）
- 响应式设计

## 安装和运行

1. 确保已安装Python 3.8+
2. 激活虚拟环境（如果使用）：
   ```bash
   .venv\Scripts\activate
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 运行数据库迁移：
   ```bash
   python manage.py migrate
   ```

5. 启动开发服务器：
   ```bash
   python manage.py runserver
   ```

6. 在浏览器中访问：http://127.0.0.1:8000

## 可用路由

- `/` - 首页
- `/hello/` - Hello World页面
- `/hello/<name>/` - 个性化问候页面（将`<name>`替换为任意姓名）

## 示例

- http://127.0.0.1:8000/hello/ - 显示"Hello, World!"
- http://127.0.0.1:8000/hello/张三/ - 显示"Hello, 张三!"
- http://127.0.0.1:8000/hello/李四/ - 显示"Hello, 李四!"

## 项目结构

```
mysite/
├── __init__.py
├── settings.py
├── urls.py
└── wsgi.py
hello/
├── __init__.py
├── views.py
└── urls.py
manage.py
requirements.txt
```