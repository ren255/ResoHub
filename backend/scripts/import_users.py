import os
import django

# Django設定の初期化
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from content.models import User, StudentInfo, TeacherInfo, UserRole
from django.db.models import Q
import pandas as pd

# CSVファイルの読み込みと整形
users = pd.read_csv("../teams_export/users.csv")
users = users.drop("UserId", axis=1)
rename = {
    "User": "mail",
    "Name": "name",
    "Role": "teams_role",
}
users = users.rename(columns=rename)

# ロールの判定
users["role"] = "teacher"
inc_mask = users["mail"].str.endswith("@inc.kisarazu.ac.jp")
users.loc[inc_mask, "student_id"] = users.loc[inc_mask, "mail"].str.replace(
    "@inc.kisarazu.ac.jp", "", regex=False
)
student_pattern = r"^[a-zA-Z]\d{5}$"
is_valid_student = users["student_id"].fillna("").str.match(student_pattern)
users.loc[inc_mask & is_valid_student, "role"] = "student"

# 既存のSTUDENTまたはTEACHERのroleを持つUserを削除
users_del = User.objects.filter(Q(role=UserRole.STUDENT) | Q(role=UserRole.TEACHER))
users_del.delete()

# Userオブジェクトの作成
users_obj = []
students = []
teachers = []

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
        users_obj.append(user)

        if role == UserRole.STUDENT:
            student = StudentInfo(
                user=user,
                student_id=row["student_id"],
            )
            students.append(student)
        elif role == UserRole.TEACHER:
            teacher = TeacherInfo(
                user=user,
                owner=True if row["teams_role"] == "owner" else False,
            )
            teachers.append(teacher)
    except Exception as e:
        print(f"Error creating user: {e}\n{row}")

print(f"{len(users_obj)} users. {len(students)} students. {len(teachers)} teachers")

# 一括作成
User.objects.bulk_create(users_obj)
StudentInfo.objects.bulk_create(students)
TeacherInfo.objects.bulk_create(teachers)

print("Initial user creation completed!")
