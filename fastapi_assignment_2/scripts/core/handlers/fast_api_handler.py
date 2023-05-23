from scripts.utils.mongo_util import student_Q
from schemas.modals import new


def get():
    return {"welcome to fastapi Project"}


def post_func(req_json: new):
    try:
        student_Q.insert_one(req_json.dict())
        return {" assigned successfully"}
    except Exception as e:
        return {"error": str(e)}


def get1():
    course = (student_Q.find())
    new_course = []
    for student in course:
        del student['_id']
        new_course.append(student)
    return new_course


def upd(student_id: int, stu: new):
    student_Q.update_one({'student_id': student_id}, {'$set': stu.dict()})
    return {' upd successful'}


def dd(student_id: int):
    student_Q.delete_one({"student_id": student_id})
    return {'delete function is done'}


def aggregation_func():
    pipeline = [
        {
            '$group': {
                '_id': None,
                'total': {
                    '$sum': '$student_fees'
                }
            }
        }, {
            '$project': {
                '_id': 0
            }
        }
    ]
    data = student_Q.aggregate(pipeline)
    data = list(data)
    print(data)
    return{'total fees': data[0]['total']}
