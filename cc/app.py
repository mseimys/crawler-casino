from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse

from cc.settings import FAVICON_PATH, MAX_DEPTH
from cc.network import get_next_nodes, get_depth

app = FastAPI()


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(FAVICON_PATH, status_code=200)


html = """
<!DOCTYPE html>
<html>
<head>
    <title>Crawler-Casino</title>
    <style>a {{ display: block }}</style>
</head>
<body>
    {body}
</body>
</html>
"""


@app.get("/{full_path:path}")
async def root(request: Request, full_path: str):
    new_links = get_next_nodes(full_path)
    depth = get_depth(full_path)

    if depth > MAX_DEPTH:
        body = (
            """<h1>Maximum depth reached!</h1><p>Sorry, you can't go any deeper.</p>"""
        )
    else:

        def render_link(link: str):
            return f'<a href="/{link}">{link}</a>'

        body = f"""
            <h1>You are {depth} levels deep!</h1>
            <p>Here are some new links to crawl, maybe you'll find something!</p>
            {" ".join([render_link(l) for l in new_links])}
        """
    return HTMLResponse(content=html.format(body=body), status_code=200)
