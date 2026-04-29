# ResoHub オブジェクト構成

## User 関連

```
User
├── UserSetting (1:1)
├── StudentInfo (1:1) ──> SchoolClass
└── TeacherInfo (1:1) ──> Department
    └── Subject (M:N)
```

## Organization 関連

```
School
└── Department
    ├── SyllabusDepartment
    │
    └── SchoolClass ──> SyllabusDepartment
        └── GradeClass
            └── Subject ──> SubjectGroupe
```

## Subject / Exam 関連

```
SubjectGroupe
└── Subject ──> GradeClass
    ├── ExamGroupe ──> SubjectGroupe
    │   └── Exam ──> TextFileStorage
    │
    └── TeacherInfo (M:N)
```

## モデル一覧

| モデル名 | 説明 |
|---------|------|
| User | カスタムユーザー（メール認証） |
| UserSetting | ユーザー設定 |
| StudentInfo | 生徒情報（学籍番号、クラス） |
| TeacherInfo | 教師情報（学部、担当教科） |
| School | 学校 |
| Department | 学部 |
| SyllabusDepartment | シラバスに紐づく学部（学科*入学年度付き） |
| SchoolClass | クラス（学科×入学年） |
| GradeClass | 学年クラス（クラス(学科×入学年)×学年） |
| Subject | 教科 |
| SubjectGroupe | 教科グループ |
| ExamGroupe | 試験グループ |
| Exam | 試験 |
| TextFileStorage | ファイルストレージ |
