from typing import Optional

from fastapi import FastAPI

import uvicorn

app = FastAPI()

if __name__ == "main":
    print('hi')
    uvicorn.run(app, host="0.0.0.0", port=8000)
