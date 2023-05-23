from scripts.core.handlers.fast_api_handler import get, post_func, get1, upd, dd, aggregation_func
from schemas.modals import new
from fastapi import APIRouter
from scripts.constants.app_constants import Apis
from scripts.core.handlers.email_handler import send_email

app = APIRouter()


@app.get(Apis.get_constant_apis)
def func_1():
    return get()


@app.post(Apis.post_constant_apis)
def fun_2(req_json: new):
    return post_func(req_json)


@app.get(Apis.get_constant_2_apis)
def fun_3():
    return get1()


@app.put(Apis.put_cns_apis)
def fun_4(student_id: int, req_json: new):
    return upd(student_id, req_json)


@app.delete(Apis.del_cns_apis)
def fun_5(student_id: int):
    return dd(student_id)


@app.post(Apis.email_constants_apis)
def fun_6(email: str, subject: str):
    return send_email(email, subject)


@app.get(Apis.pipeline_apis)
def func_7():
    return aggregation_func()
