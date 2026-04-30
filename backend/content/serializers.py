from rest_framework import serializers
from .models import (
    User,
    School,
    Department,
    SyllabusDepartment,
    SchoolClass,
    GradeClass,
    Subject,
    SubjectGroupe,
    Exam,
    ExamGroupe,
    StudentInfo,
    TeacherInfo,
    UserSetting,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "uuid",
            "username",
            "email",
            "name",
            "role",
            "is_staff",
            "is_superuser",
            "is_active",
            "date_joined",
        )


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ("id", "url", "name", "code")


class DepartmentSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source="school.name", read_only=True)

    class Meta:
        model = Department
        fields = ("id", "name", "school", "school_name")


class SyllabusDepartmentSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source="school.name", read_only=True)
    department_name = serializers.CharField(source="department.name", read_only=True)

    class Meta:
        model = SyllabusDepartment
        fields = (
            "id",
            "url",
            "name",
            "admission_year",
            "code",
            "school",
            "school_name",
            "department",
            "department_name",
        )


class SchoolClassSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source="department.name", read_only=True)
    syllabus_department_name = serializers.CharField(
        source="syllabus_department.name", read_only=True
    )

    class Meta:
        model = SchoolClass
        fields = (
            "id",
            "department",
            "department_name",
            "syllabus_department",
            "syllabus_department_name",
            "admission_year",
        )


class GradeClassSerializer(serializers.ModelSerializer):
    school_class_str = serializers.CharField(
        source="school_class.__str__", read_only=True
    )

    class Meta:
        model = GradeClass
        fields = (
            "id",
            "school_class",
            "school_class_str",
            "grade_str",
            "grade",
            "year",
        )


class SubjectSerializer(serializers.ModelSerializer):
    grade_class_str = serializers.CharField(
        source="grade_class.__str__", read_only=True
    )

    class Meta:
        model = Subject
        fields = (
            "id",
            "name",
            "code",
            "subject_type",
            "credits",
            "teachers_str",
            "textbooks",
            "url",
            "grade_class",
            "grade_class_str",
            "subject_groupe",
        )


class ExamGroupeSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source="subject.name", read_only=True)

    class Meta:
        model = ExamGroupe
        fields = ("id", "subject", "subject_name", "subject_groupe")


class ExamSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source="subject.name", read_only=True)

    class Meta:
        model = Exam
        fields = (
            "id",
            "url",
            "quarter",
            "week",
            "content",
            "goal",
            "subject",
            "subject_name",
            "exam_groupe",
            "file",
        )


class StudentInfoSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.name", read_only=True)
    school_class_str = serializers.CharField(
        source="school_class.__str__", read_only=True
    )

    class Meta:
        model = StudentInfo
        fields = (
            "id",
            "user",
            "user_name",
            "student_id",
            "school_class",
            "school_class_str",
        )


class TeacherInfoSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.name", read_only=True)
    department_name = serializers.CharField(source="department.name", read_only=True)

    class Meta:
        model = TeacherInfo
        fields = (
            "id",
            "user",
            "user_name",
            "department",
            "department_name",
            "department_type",
            "owner",
            "subdomain",
            "subjects",
        )


class SubjectGroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectGroupe
        fields = ("id", "name", "teachers", "subjects")


class UserSettingSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.name", read_only=True)

    class Meta:
        model = UserSetting
        fields = ("id", "user", "user_name")
