from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/set-lang", response_class=HTMLResponse)
async def set_lang(response: Response):
    response.set_cookie(key="lang", value="de",
                        httponly=True, samesite="Lax")
    return "Sprache gesetzt!"

@app.get("/get-lang", response_class=HTMLResponse)
async def get_lang(request: Request):
    lang = request.cookies.get("lang", "nicht gesetzt")
    return f"Sprache: {lang}"

@app.get("/delete-lang", response_class=HTMLResponse)
async def delete_lang(response: Response):
    response.delete_cookie("lang")
    return "Sprache gelöscht!"
