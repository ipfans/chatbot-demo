from fastapi import FastAPI

import src.frontend as frontend

app = FastAPI()

frontend.init(app)
