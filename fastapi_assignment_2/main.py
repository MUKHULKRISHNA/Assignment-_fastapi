"""registering students in a course"""

import uvicorn
from fastapi import FastAPI
from scripts.core.services.fast_api_services import app as crud_router
from scripts.constants.app_configuration import host, port

app = FastAPI()

app.include_router(crud_router)
if __name__ == "__main__":
    uvicorn.run('main:app', host=host, port=int(port))
