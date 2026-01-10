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

users["subdomain"] = users["mail"].str.extract(r"[\.@]([^\.@]+?)\.kisarazu")
mask = users["mail"].str.contains("@inc.kisarazu.ac.jp", na=False)
users.loc[mask, "student_id"] = users.loc[mask, "mail"].str.replace(
    "@inc.kisarazu.ac.jp", "", regex=False
)
users["role"] = "teacher"
users.loc[users["subdomain"] == "a", "role"] = "other"
users.loc[users["subdomain"] == "inc", "role"] = "student"

# 既存のSTUDENTまたはTEACHERのroleを持つUserを削除
users_del = User.objects.filter(
    Q(role=UserRole.STUDENT)
    | Q(role=UserRole.TEACHER)
    | Q(role=UserRole.STUDENT_AFFAIRS)
)
users_del.delete()

# Userオブジェクトの作成
users_obj = []
students = []
teachers = []

for index, row in users.iterrows():
    try:
        if row["role"] == "student":
            role = UserRole.STUDENT
        elif row["role"] == "teacher":
            role = UserRole.TEACHER
        else:
            role = UserRole.STUDENT_AFFAIRS

        user = User(
            role=role,
            name=row["name"],
            username=row["name"],
            email=row["mail"],
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
                subdomain=row["subdomain"],
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
