import os
import django

# Django設定の初期化
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from content.models import (
    User,
    StudentInfo,
    TeacherInfo,
    UserRole,
    School,
    Department,
    SchoolClass,
)
from django.db.models import Q
import pandas as pd
from datetime import datetime

users = pd.read_csv("../teams_export/users.csv")
users = users.drop("UserId", axis=1)
rename = {
    "User": "mail",
    "Name": "name",
    "Role": "teams_role",
}
users = users.rename(columns=rename)

users["role"] = "teacher"
# @inc.kisarazu.ac.jpのメールアドレスを持つユーザーを抽出
inc_mask = users["mail"].str.endswith("@inc.kisarazu.ac.jp")
users.loc[inc_mask, "student_id"] = users.loc[inc_mask, "mail"].str.replace(
    "@inc.kisarazu.ac.jp", "", regex=False
)
student_pattern = r"^[a-zA-Z]\d{5}$"
is_valid_student = users["student_id"].fillna("").str.match(student_pattern)

users.loc[inc_mask & is_valid_student, "role"] = "student"


users_ojb = []
students = []
teachers = []

school = School.objects.get(name__contains="木更津")

# STUDENTまたはTEACHERのroleを持つUserを削除
users_del = User.objects.filter(Q(role=UserRole.STUDENT) | Q(role=UserRole.TEACHER))
users_del.delete()

for index, row in users.iterrows():
    try:
        role = UserRole.STUDENT if row["role"] == "student" else UserRole.TEACHER
        user = User(
            role=role,
            name=row["name"],
            username=row["name"],
            email=row["mail"],
            is_staff=False,
        )
        users_ojb.append(user)

        if role == UserRole.STUDENT:
            department_id = row["student_id"][:1]
            if department_id == "m":
                department_str = "機械工学科"
            elif department_id == "e":
                department_str = "電気電子工学科"
            elif department_id == "d":
                department_str = "電子制御工学科"
            elif department_id == "j":
                department_str = "情報工学科"
            elif department_id == "c":
                department_str = "環境都市工学科"

            department = Department.objects.get(
                school=school,
                name=department_str,
                admission_year="20" + row["student_id"][1:3],
            )
            grade = datetime.now().year - department.admission_year + 1
            if grade <= 5:
                school_class = SchoolClass.objects.get(
                    department=department,
                    grade=grade,
                    year=datetime.now().year,
                )
                student = StudentInfo(
                    user=user,
                    student_id=row["student_id"],
                    department=department,
                    school_class=school_class,
                )
            else:
                student = StudentInfo(
                    user=user,
                    student_id=row["student_id"],
                    department=department,
                    school_class=school_class,
                )

            students.append(student)
        elif role == UserRole.TEACHER:
            teacher = TeacherInfo(
                user=user,
                school=school,
                owner=True if row["teams_role"] == "owner" else False,
            )
            teachers.append(teacher)
    except Exception as e:
        print(
            f"error {e}\n{row}\nyear: {department.admission_year} grade: {datetime.now().year - department.admission_year + 1}"
        )

print(f"{len(users_ojb)} user. {len(students) } student. {len(teachers)} teachers")
User.objects.bulk_create(users_ojb)
StudentInfo.objects.bulk_create(students)
TeacherInfo.objects.bulk_create(teachers)
