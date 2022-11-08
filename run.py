import os

import uvicorn
from starlette.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from loguru import logger

import config
from config import PORT, BIND, WORKERS, RELOAD
from api.views.index import app
from config import PORT, LOGFILE, ORIGINS, BASEDIR, LOGDIR

if __name__ == "__main__":
    uvicorn.run("api:user",
                host=BIND,
                port=int(PORT),
                reload=RELOAD,
                workers=int(WORKERS),
                )

    LOGDIR = BASEDIR + "/" + LOGDIR

    if not os.path.exists(LOGDIR):
        os.makedirs(LOGDIR)

    logger.add(LOGDIR + "/" + LOGFILE,
               rotation="10MB",
               colorize=True,
               format="<green>{time:YYYYMMDD_HH:mm:ss}</green> | {level} | <level>{message}</level>",
               level="ERROR")

    global_app = FastAPI()

    # Set all CORS enabled origins
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    global_app.include_router(app)

#     global_app.add_middleware(
#         CORSMiddleware,
#         allow_origins=[
#             "http://127.0.0.1:5200",
#             "http://0.0.0.0:5200",
#             "http://localhost:5200",
#             "http://192.168.0.213:5200",
#         ],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )
