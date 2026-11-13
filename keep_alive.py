"""keep_alive.py — Lightweight HTTP server so Render keeps the bot alive."""

from aiohttp import web

async def handle(request):
    return web.Response(text="Bot is alive!")

async def start_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
    print("✅ Keep-alive server running on port 8080")
