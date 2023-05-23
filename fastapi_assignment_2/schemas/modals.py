from pydantic import BaseModel


class new(BaseModel):
    student_id: int
    student_name: str
    student_course: str
    student_fees: int
