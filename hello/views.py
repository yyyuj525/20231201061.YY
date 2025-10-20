from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    """简单的Hello World视图"""
    return HttpResponse("""
    <html>
    <head>
        <title>Hello World</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f0f0f0; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; }
            .info { background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 20px 0; }
            .links { margin-top: 20px; }
            .links a { display: inline-block; margin-right: 15px; padding: 10px 15px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; }
            .links a:hover { background: #0056b3; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, World!</h1>
            <p>欢迎来到我的第一个Django应用！</p>
            <div class="info">
                <p><strong>开发者信息：</strong></p>
                <p>姓名：杨坤</p>
                <p>学号：20231201061</p>
            </div>
            <div class="links">
                <a href="/">返回首页</a>
                <a href="/hello/杨坤/">Hello 杨坤</a>
            </div>
        </div>
    </body>
    </html>
    """)

def hello_name(request, name):
    """带参数的Hello视图"""
    return HttpResponse(f"""
    <html>
    <head>
        <title>Hello {name}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f0f0f0; }}
            .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #333; }}
            .info {{ background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 20px 0; }}
            .links {{ margin-top: 20px; }}
            .links a {{ display: inline-block; margin-right: 15px; padding: 10px 15px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; }}
            .links a:hover {{ background: #0056b3; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, {name}!</h1>
            <p>很高兴见到你！</p>
            <div class="info">
                <p><strong>开发者信息：</strong></p>
                <p>姓名：杨坤</p>
                <p>学号：20231201061</p>
            </div>
            <div class="links">
                <a href="/">返回首页</a>
                <a href="/hello/">Hello World</a>
            </div>
        </div>
    </body>
    </html>
    """)

def index(request):
    """首页视图"""
    return HttpResponse("""
    <html>
    <head>
        <title>Hello World App</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f0f0f0; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; }
            .info { background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 20px 0; }
            .links { margin-top: 20px; }
            .links a { display: inline-block; margin-right: 15px; padding: 10px 15px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; }
            .links a:hover { background: #0056b3; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>欢迎来到Hello World应用！</h1>
            <p>这是一个简单的Django Hello World应用程序。</p>
            <div class="info">
                <p><strong>开发者信息：</strong></p>
                <p>姓名：杨坤</p>
                <p>学号：20231201061</p>
            </div>
            <div class="links">
                <a href="/hello/">Hello World</a>
                <a href="/hello/杨坤/">Hello 杨坤</a>
                <a href="/hello/张三/">Hello 张三</a>
                <a href="/hello/李四/">Hello 李四</a>
            </div>
        </div>
    </body>
    </html>
    """)