from django.http import HttpResponse

def home_page(request, *args, **kwargs):
    return HttpResponse("""
        <html>
            <head>
                <title>My Django Site</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 40px;
                        background-color: #f0f0f0;
                    }
                    .container {
                        background-color: white;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    }
                    h1 {
                        color: #333;
                    }
                    p {
                        color: #666;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Hello World</h1>
                    <marquee>Welcome to my first Django website!</marquee>
                    <ul>
                        <li>This is a simple example</li>
                        <li>Using HttpResponse</li>
                        <li>With some basic HTML and CSS</li>
                    </ul>
                </div>
            </body>
        </html>
    """)