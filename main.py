
from dotenv import load_dotenv


load_dotenv()

import os
from fastapi import FastAPI, Form, Response
import uvicorn

from service.github_service import add_github_permission


app = FastAPI()

# @app.get("/add/{email}")
# async def add_test(email: str):
#    return await add_github_permission(email, "")


@app.post("/sale/")
async def post_sale(product_id: str = Form(...), email: str = Form(...)):
   try:
    return await add_github_permission(email, product_id)
   except Exception as error:
      print(error)
      return Response(status_code=500, content=str(error))


if __name__ == '__main__':
    if (os.environ["ENV"] == 'prod'):
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8001,
                    reload=True,
                    ssl_keyfile="privkey.pem",
                    ssl_certfile="fullchain.pem"
                    )
    else:
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8001,
                    reload=True
                    )