# `MySQL查询`

## 多表查询

- 现在有三个表，`guardians_guardian, guardians_guardianstudent, students_student`
- 表`guardians_guardianstudent`中有其他两个表的外键。

```mysql
SELECT guardians_guardian.id, guardians_guardian.name, guardians_guardian.avatar, students_student.id, students_student.fullname, guardians_guardianstudent.relation
FROM guardians_guardianstudent, guardians_guardian, students_student
WHERE guardians_guardianstudent.student_id = students_student.id and guardians_guardianstudent.guardian_id = guardians_guardian.id and guardians_guardian.id = 652; 
```

## 查询最新的几条数据

- 先查询表中的数据总数

  ```mysql
  select count(*) from table_name;
  ```

- 然后借助limit关键字查询

  ```mysql
  select * from table_name limit count-5, 5;
  ```

## 查询不同的数据

- 当需要查询一列的数据有多少不同的时

  ```mysql
  select distinct col_name from table_name;
  ```

## 查询一列中的最值

- 借助order by先排序，然后使用limit

  ```mysql
  select col_name 
  from table_name 
  order by col_name
  limit 1;
  ```

  