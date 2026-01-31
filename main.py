from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ProductVector - Coming Soon</title>
        <style>
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                margin: 0;
                background: linear-gradient(135deg, #f7b42c 0%, #fc575e 100%);
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .header-bar {
                width: 100vw;
                background: linear-gradient(90deg, #fc575e 0%, #f7b42c 100%);
                padding: 0;
                margin: 0;
                box-shadow: 0 2px 8px rgba(252,87,94,0.13);
                display: flex;
                align-items: center;
                justify-content: space-between;
                min-height: 64px;
                position: fixed;
                top: 0;
                left: 0;
                z-index: 1000;
            }
            .header-title {
                color: #fff;
                font-size: 2.2em;
                font-weight: bold;
                letter-spacing: 2px;
                font-family: 'Segoe UI', Arial, sans-serif;
                margin-left: 32px;
            }
            .header-buttons {
                margin-right: 32px;
            }
            .header-btn {
                background: linear-gradient(90deg, #f7b42c 0%, #fc575e 100%);
                color: #fff;
                border: none;
                border-radius: 8px;
                font-size: 1.08em;
                font-weight: bold;
                padding: 10px 24px;
                margin-left: 12px;
                cursor: pointer;
                box-shadow: 0 2px 8px rgba(252,87,94,0.13);
                transition: background 0.2s, transform 0.2s;
            }
            .header-btn:hover {
                background: linear-gradient(90deg, #fc575e 0%, #f7b42c 100%);
                transform: scale(1.04);
            }
            .container {
                background: #fff;
                border-radius: 18px;
                box-shadow: 0 2px 16px rgba(0,0,0,0.08);
                padding: 36px 32px;
                max-width: 540px;
                margin: 96px auto 48px auto;
                width: 100%;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            h1 {
                color: #fc575e;
                font-size: 2.3em;
                margin-bottom: 18px;
                letter-spacing: 1.5px;
                text-shadow: 1px 2px 0 #fff6e0, 0 4px 12px #fc575e33;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-weight: bold;
                text-align: center;
            }
            p {
                color: #b95c00;
                font-size: 1.15em;
                text-align: center;
            }
            ul {
                margin-top: 16px;
                padding-left: 20px;
                color: #b95c00;
                font-size: 1.1em;
            }
            li {
                margin-bottom: 8px;
            }
        </style>
    </head>
    <body>
        <div class="header-bar">
            <span class="header-title">ProductVector</span>
            <div class="header-buttons">
                <button class="header-btn" onclick="window.location.href='/contact'">Contact Us</button>
            </div>
        </div>
        <div class="container">
            <h1>Coming Soon</h1>
            <p><strong>ProductVector</strong> by Construct Dynamics LLC</p>
            <p>ProductVector is an API-first automation engine that transforms structured product data into deployable marketing and commerce assets.</p>
            <p>The platform provides:</p>
            <ul>
                <li>A single endpoint for converting product data into complete funnel structures</li>
                <li>Automated generation of landing content, email sequences, and templates</li>
                <li>Programmatic tools for affiliate e-commerce and lead generation workflows</li>
                <li>Lightweight, scalable backend infrastructure for developers and businesses</li>
            </ul>
            <p><strong>API Status:</strong> Online soon</p>
            <p><strong>Contact:</strong> <a href="mailto:support@constructdynamics.com">support@constructdynamics.com</a></p>
            <p>© 2026 Construct Dynamics LLC. All rights reserved.</p>
        </div>
    </body>
    </html>
    """

@app.get("/contact", response_class=HTMLResponse)
async def contact():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Us - ProductVector</title>
        <style>
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                margin: 0;
                background: linear-gradient(135deg, #f7b42c 0%, #fc575e 100%);
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .header-bar {
                width: 100vw;
                background: linear-gradient(90deg, #fc575e 0%, #f7b42c 100%);
                padding: 0;
                margin: 0;
                box-shadow: 0 2px 8px rgba(252,87,94,0.13);
                display: flex;
                align-items: center;
                justify-content: space-between;
                min-height: 64px;
                position: fixed;
                top: 0;
                left: 0;
                z-index: 1000;
            }
            .header-title {
                color: #fff;
                font-size: 2.2em;
                font-weight: bold;
                letter-spacing: 2px;
                font-family: 'Segoe UI', Arial, sans-serif;
                margin-left: 32px;
            }
            .header-buttons {
                margin-right: 32px;
            }
            .header-btn {
                background: linear-gradient(90deg, #f7b42c 0%, #fc575e 100%);
                color: #fff;
                border: none;
                border-radius: 8px;
                font-size: 1.08em;
                font-weight: bold;
                padding: 10px 24px;
                margin-left: 12px;
                cursor: pointer;
                box-shadow: 0 2px 8px rgba(252,87,94,0.13);
                transition: background 0.2s, transform 0.2s;
            }
            .header-btn:hover {
                background: linear-gradient(90deg, #fc575e 0%, #f7b42c 100%);
                transform: scale(1.04);
            }
            .container {
                background: #fff;
                border-radius: 18px;
                box-shadow: 0 2px 16px rgba(0,0,0,0.08);
                padding: 36px 32px;
                max-width: 540px;
                margin: 96px auto 48px auto;
                width: 100%;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            h1 {
                color: #fc575e;
                font-size: 2.3em;
                margin-bottom: 18px;
                letter-spacing: 1.5px;
                text-shadow: 1px 2px 0 #fff6e0, 0 4px 12px #fc575e33;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-weight: bold;
                text-align: center;
            }
            p {
                color: #b95c00;
                font-size: 1.15em;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="header-bar">
            <span class="header-title">ProductVector</span>
            <div class="header-buttons">
                <button class="header-btn" onclick="window.location.href='/'">Home</button>
            </div>
        </div>
        <div class="container">
            <h1>Contact Us</h1>
            <p>If you have any questions or need support, feel free to reach out to us:</p>
            <p><strong>Email:</strong> <a href="mailto:support@constructdynamics.com">support@constructdynamics.com</a></p>
            <p>We look forward to hearing from you!</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)