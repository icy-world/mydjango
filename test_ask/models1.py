# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnswerDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    question_detail = models.ForeignKey('QuestionDetail', models.DO_NOTHING, blank=True, null=True)
    answer = models.ForeignKey('StudentAnswer', models.DO_NOTHING, blank=True, null=True)
    student_answers = models.TextField(blank=True, null=True)
    answer_score = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer_detail'


class AnswerDetailExt(models.Model):
    detail_id = models.AutoField(primary_key=True)
    question_detail = models.ForeignKey('QuestionDetail', models.DO_NOTHING, blank=True, null=True)
    question_detail_ext = models.ForeignKey('QuestionDetailExt', models.DO_NOTHING, blank=True, null=True)
    answer = models.ForeignKey('StudentAnswer', models.DO_NOTHING, blank=True, null=True)
    student_answers = models.CharField(max_length=256, blank=True, null=True)
    student_answers_reason = models.CharField(max_length=256, blank=True, null=True)
    answer_score = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer_detail_ext'


class BasApplyCommunity(models.Model):
    app_community_id = models.AutoField(primary_key=True)
    person_id = models.IntegerField(blank=True, null=True)
    community_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    willingly = models.IntegerField(blank=True, null=True)
    enroll = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_apply_community'


class BasApplyCourse(models.Model):
    apply_course_id = models.AutoField(primary_key=True)
    person = models.ForeignKey('BasPerson', models.DO_NOTHING)
    course = models.ForeignKey('BasCourse', models.DO_NOTHING)
    create_time = models.DateTimeField(blank=True, null=True)
    willingly = models.IntegerField(blank=True, null=True)
    enroll = models.IntegerField(blank=True, null=True)
    week_day = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_apply_course'


class BasBuild(models.Model):
    build_id = models.AutoField(primary_key=True)
    build_name = models.CharField(max_length=220, blank=True, null=True)
    build_type = models.CharField(max_length=220, blank=True, null=True)
    campus = models.ForeignKey('BasCampus', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_build'


class BasCampus(models.Model):
    campus_id = models.AutoField(primary_key=True)
    campus_name = models.CharField(max_length=50, blank=True, null=True)
    person_id = models.IntegerField(blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_campus'


class BasClass(models.Model):
    class_id = models.AutoField(primary_key=True)
    grade = models.ForeignKey('BasGrade', models.DO_NOTHING)
    person = models.ForeignKey('BasTeacher', models.DO_NOTHING, blank=True, null=True)
    serial = models.IntegerField()
    class_name = models.CharField(max_length=32, blank=True, null=True)
    honour = models.CharField(max_length=64, blank=True, null=True)
    class_kind = models.IntegerField()
    monitor = models.IntegerField(blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)
    campus = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_class'


class BasClassDoList(models.Model):
    list_id = models.AutoField(primary_key=True)
    problem_id = models.IntegerField()
    class_id = models.IntegerField()
    subject_id = models.IntegerField()
    do_type = models.IntegerField(blank=True, null=True)
    error_persons = models.IntegerField(blank=True, null=True)
    do_persons = models.IntegerField(blank=True, null=True)
    error_students = models.CharField(max_length=512, blank=True, null=True)
    count_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bas_class_do_list'


class BasClassHistory(models.Model):
    class_id = models.IntegerField()
    grade_id = models.IntegerField()
    person_id = models.IntegerField(blank=True, null=True)
    serial = models.IntegerField()
    class_name = models.CharField(max_length=32, blank=True, null=True)
    honour = models.CharField(max_length=64, blank=True, null=True)
    class_kind = models.IntegerField()
    monitor = models.IntegerField(blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)
    semester_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_class_history'


class BasClasscourse(models.Model):
    classcourse_id = models.AutoField(primary_key=True)
    gradecourse = models.ForeignKey('BasGradecourse', models.DO_NOTHING)
    class_id = models.IntegerField(blank=True, null=True)
    person_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_classcourse'


class BasCommunity(models.Model):
    community_id = models.AutoField(primary_key=True)
    community_name = models.CharField(max_length=50, blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    teacher_name = models.CharField(max_length=30, blank=True, null=True)
    community_content = models.CharField(max_length=2048, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    file_name = models.CharField(max_length=30, blank=True, null=True)
    subject_id = models.IntegerField(blank=True, null=True)
    subject_name = models.CharField(max_length=50, blank=True, null=True)
    class_venue = models.CharField(max_length=150, blank=True, null=True)
    class_time = models.CharField(max_length=100, blank=True, null=True)
    semester_id = models.IntegerField(blank=True, null=True)
    campus = models.IntegerField(blank=True, null=True)
    audit_time = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_community'


class BasCommunityGrade(models.Model):
    community_grade_id = models.AutoField(primary_key=True)
    community_id = models.IntegerField(blank=True, null=True)
    grade_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_community_grade'


class BasCourse(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=256)
    teacher_name = models.TextField(blank=True, null=True)
    course_content = models.CharField(max_length=2048, blank=True, null=True)
    course_require = models.CharField(max_length=2048, blank=True, null=True)
    report_date = models.CharField(max_length=128, blank=True, null=True)
    require_student_type = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=256, blank=True, null=True)
    create_time = models.DateTimeField()
    serial = models.IntegerField(blank=True, null=True)
    person_id = models.IntegerField(blank=True, null=True)
    is_used = models.TextField()  # This field type is a guess.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    file_name = models.TextField(blank=True, null=True)
    subject_group = models.CharField(max_length=64, blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    limit_cnt = models.IntegerField(blank=True, null=True)
    semester_id = models.IntegerField(blank=True, null=True)
    audit_time = models.DateTimeField(blank=True, null=True)
    reason = models.CharField(max_length=1024, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    campus = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_course'


class BasCourseGrade(models.Model):
    course_grade_id = models.AutoField(primary_key=True)
    grade_no = models.IntegerField()
    course = models.ForeignKey(BasCourse, models.DO_NOTHING)
    lesson_no = models.CharField(max_length=20, blank=True, null=True)
    class_no = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_course_grade'


class BasCurrentSemester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    semester_num = models.IntegerField()
    year_startdate = models.DateTimeField()
    year_enddate = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_current_semester'


class BasDbversion(models.Model):
    version_id = models.IntegerField(primary_key=True)
    version_no = models.CharField(max_length=16, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    note = models.CharField(max_length=64, blank=True, null=True)
    versoin_no_2nd = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_dbversion'


class BasDept(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_code = models.CharField(max_length=5)
    father_id = models.CharField(max_length=5, blank=True, null=True)
    dept_name = models.CharField(max_length=20, blank=True, null=True)
    person_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_dept'


class BasDiction(models.Model):
    dict_id = models.IntegerField(primary_key=True)
    dict_type = models.IntegerField()
    type_name = models.CharField(max_length=50)
    dict_code = models.IntegerField()
    dict_name = models.CharField(max_length=50)
    easy_name = models.CharField(max_length=50, blank=True, null=True)
    used = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'bas_diction'


class BasDistrict(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=50, blank=True, null=True)
    person_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_district'


class BasEdusys(models.Model):
    level_id = models.AutoField(primary_key=True)
    level_code = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    level_name = models.CharField(max_length=20, blank=True, null=True)
    person_id = models.IntegerField(blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)
    campus = models.ForeignKey(BasCampus, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_edusys'


class BasFamily(models.Model):
    person = models.ForeignKey('BasPerson', models.DO_NOTHING, primary_key=True)
    telephone = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    if_guardian = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_family'


class BasFunction(models.Model):
    func_id = models.IntegerField(primary_key=True)
    menu = models.ForeignKey('BasMenuTree', models.DO_NOTHING)
    func_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_function'


class BasGrade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    semester = models.ForeignKey(BasCurrentSemester, models.DO_NOTHING)
    level = models.ForeignKey(BasEdusys, models.DO_NOTHING)
    grade_num = models.IntegerField(blank=True, null=True)
    grade_manager = models.IntegerField(blank=True, null=True)
    graduate_year = models.DateTimeField(blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_grade'


class BasGradeDoList(models.Model):
    list_id = models.AutoField(primary_key=True)
    grade_id = models.IntegerField()
    problem_id = models.IntegerField()
    subject_id = models.IntegerField()
    do_type = models.IntegerField(blank=True, null=True)
    error_persons = models.IntegerField(blank=True, null=True)
    do_persons = models.IntegerField(blank=True, null=True)
    count_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bas_grade_do_list'


class BasGradecourse(models.Model):
    gradecourse_id = models.AutoField(primary_key=True)
    grade = models.ForeignKey(BasGrade, models.DO_NOTHING)
    subject = models.ForeignKey('BasSubject', models.DO_NOTHING)
    person_id = models.IntegerField(blank=True, null=True)
    semester = models.ForeignKey(BasCurrentSemester, models.DO_NOTHING, blank=True, null=True)
    old_gradecourse_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_gradecourse'


class BasKnowlegePoint(models.Model):
    knowlege_id = models.AutoField(primary_key=True)
    bas_knowlege = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    knowlege_point = models.CharField(max_length=2048)
    level_no = models.IntegerField()
    subject_id = models.IntegerField()
    sorting = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_knowlege_point'


class BasLesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    unit = models.ForeignKey('BasUnit', models.DO_NOTHING)
    lesson_name = models.CharField(max_length=64, blank=True, null=True)
    sorting = models.IntegerField(blank=True, null=True)
    page_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_lesson'


class BasMenuTree(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    father_id = models.IntegerField(blank=True, null=True)
    menu_name = models.CharField(max_length=50)
    exec_filename = models.CharField(max_length=100, blank=True, null=True)
    system_name = models.CharField(max_length=32, blank=True, null=True)
    system_url_name = models.CharField(max_length=32, blank=True, null=True)
    sorting = models.IntegerField(blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)
    menu_alias = models.IntegerField(blank=True, null=True)
    menu_alias_sorting = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_menu_tree'


class BasNation(models.Model):
    nation_id = models.AutoField(primary_key=True)
    national_code = models.IntegerField(blank=True, null=True)
    national_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_nation'


class BasOperationLog(models.Model):
    operation_logid = models.AutoField(primary_key=True)
    opertion_content = models.CharField(max_length=256, blank=True, null=True)
    operation_date = models.DateTimeField()
    login_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_operation_log'


class BasParameter(models.Model):
    parameter_id = models.IntegerField(primary_key=True)
    parameter_name = models.CharField(max_length=32, blank=True, null=True)
    parameter_value = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_parameter'


class BasPerson(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    login_name = models.CharField(max_length=64, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    card_sort = models.IntegerField(blank=True, null=True)
    card_id = models.CharField(max_length=64, blank=True, null=True)
    person_type = models.IntegerField(blank=True, null=True)
    buss_scope = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_person'


class BasPersonRole(models.Model):
    person = models.ForeignKey(BasPerson, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('BasRole', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bas_person_role'
        unique_together = (('person', 'role'),)


class BasRole(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=40)
    used = models.IntegerField()
    cmis_role_id = models.IntegerField(blank=True, null=True)
    if_sync_deal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_role'


class BasRoleFunction(models.Model):
    func = models.ForeignKey(BasFunction, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey(BasRole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bas_role_function'
        unique_together = (('func', 'role'),)


class BasRoleScope(models.Model):
    scope_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(BasRole, models.DO_NOTHING, blank=True, null=True)
    subject_id = models.IntegerField(blank=True, null=True)
    grade_num = models.IntegerField(blank=True, null=True)
    class_serial = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_role_scope'


class BasRoom(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=220, blank=True, null=True)
    room_purpose = models.CharField(max_length=220, blank=True, null=True)
    room_bewrite = models.CharField(max_length=200, blank=True, null=True)
    build = models.ForeignKey(BasBuild, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_room'


class BasSchoolInfo(models.Model):
    info_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    tel = models.CharField(max_length=16, blank=True, null=True)
    fox = models.CharField(max_length=16, blank=True, null=True)
    mail_box = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    new_loc = models.CharField(max_length=32, blank=True, null=True)
    ori_loc = models.CharField(max_length=32, blank=True, null=True)
    screater = models.ForeignKey(BasPerson, models.DO_NOTHING, db_column='screater', blank=True, null=True)
    screatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_school_info'


class BasScience(models.Model):
    science_id = models.AutoField(primary_key=True)
    parent_science = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    science_point = models.CharField(max_length=2048)
    level_no = models.IntegerField()
    sorting = models.IntegerField(blank=True, null=True)
    subject_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_science'


class BasStudent(models.Model):
    person = models.ForeignKey(BasPerson, models.DO_NOTHING, primary_key=True)
    class_field = models.ForeignKey(BasClass, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    bas_person = models.ForeignKey(BasFamily, models.DO_NOTHING, blank=True, null=True)
    student_no = models.CharField(max_length=32, blank=True, null=True)
    inschool_id = models.CharField(max_length=32, blank=True, null=True)
    student_type = models.IntegerField(blank=True, null=True)
    student_addr = models.CharField(max_length=64, blank=True, null=True)
    student_pos = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    national_code = models.IntegerField(blank=True, null=True)
    exam_no = models.IntegerField(blank=True, null=True)
    national_xueji_code = models.CharField(max_length=125, blank=True, null=True)
    bj_education_id = models.CharField(max_length=125, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_student'


class BasStudentHistory(models.Model):
    person_id = models.IntegerField()
    class_id = models.IntegerField()
    bas_person_id = models.IntegerField(blank=True, null=True)
    student_no = models.CharField(max_length=32, blank=True, null=True)
    inschool_id = models.CharField(max_length=32, blank=True, null=True)
    student_type = models.IntegerField(blank=True, null=True)
    student_addr = models.CharField(max_length=64, blank=True, null=True)
    student_pos = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    semester_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_student_history'


class BasSubject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    subject_code = models.IntegerField()
    subject_name = models.CharField(max_length=128)
    sorting = models.IntegerField(blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_subject'


class BasTeacher(models.Model):
    person = models.ForeignKey(BasPerson, models.DO_NOTHING, primary_key=True)
    employee_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_teacher'


class BasTeacherDept(models.Model):
    person = models.ForeignKey(BasTeacher, models.DO_NOTHING, primary_key=True)
    dept = models.ForeignKey(BasDept, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bas_teacher_dept'
        unique_together = (('person', 'dept'),)


class BasTeachingleader(models.Model):
    person = models.ForeignKey(BasTeacher, models.DO_NOTHING, primary_key=True)
    grade = models.ForeignKey(BasGrade, models.DO_NOTHING)
    subject = models.ForeignKey(BasSubject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bas_teachingleader'
        unique_together = (('person', 'grade', 'subject'),)


class BasTextbook(models.Model):
    textbook_id = models.AutoField(primary_key=True)
    subject_id = models.IntegerField()
    grade_name = models.CharField(max_length=64, blank=True, null=True)
    publishing = models.CharField(max_length=128)
    textbooks_version = models.CharField(max_length=128, blank=True, null=True)
    note = models.CharField(max_length=256, blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_textbook'


class BasUnit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    volume = models.ForeignKey('BasVolume', models.DO_NOTHING)
    unit_name = models.CharField(max_length=128)
    sorting = models.IntegerField(blank=True, null=True)
    page_number = models.IntegerField(blank=True, null=True)
    old_unit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_unit'


class BasVolume(models.Model):
    volume_id = models.AutoField(primary_key=True)
    textbook = models.ForeignKey(BasTextbook, models.DO_NOTHING)
    grade_num = models.IntegerField()
    semester_id = models.IntegerField()
    note = models.CharField(max_length=256, blank=True, null=True)
    old_volume_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bas_volume'


class CfsHomeWork(models.Model):
    work_id = models.IntegerField(primary_key=True)
    subject_id = models.IntegerField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    deploy_time = models.DateTimeField(blank=True, null=True)
    deploy_reason = models.CharField(max_length=2000, blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    work_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cfs_home_work'


class CfsNotice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    recv_id = models.IntegerField(blank=True, null=True)
    notice_content = models.CharField(max_length=2000, blank=True, null=True)
    notice_time = models.DateTimeField(blank=True, null=True)
    notice_read = models.IntegerField(blank=True, null=True)
    notice_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cfs_notice'


class CfsReadingResource(models.Model):
    work = models.ForeignKey(CfsHomeWork, models.DO_NOTHING, blank=True, null=True)
    releation_id = models.IntegerField(blank=True, null=True)
    reading_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cfs_reading_resource'


class CfsStudyApply(models.Model):
    apply_id = models.AutoField(primary_key=True)
    subject_id = models.IntegerField(blank=True, null=True)
    record_source = models.IntegerField(blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    teacher_introduce = models.CharField(max_length=2000, blank=True, null=True)
    student_remark = models.CharField(max_length=2000, blank=True, null=True)
    is_publish = models.IntegerField(blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    response_time = models.DateTimeField(blank=True, null=True)
    is_completed = models.IntegerField(blank=True, null=True)
    room_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cfs_study_apply'


class CfsSysDict(models.Model):
    dict_id = models.AutoField(primary_key=True)
    dict_name = models.CharField(max_length=255, blank=True, null=True)
    dict_code = models.CharField(max_length=255, blank=True, null=True)
    dict_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cfs_sys_dict'


class CfsWxCourse(models.Model):
    wxc_id = models.IntegerField(primary_key=True)
    work = models.ForeignKey(CfsHomeWork, models.DO_NOTHING, blank=True, null=True)
    xx_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cfs_wx_course'


class ChoiceCourseNumber(models.Model):
    waterid = models.AutoField(primary_key=True)
    subject_group = models.CharField(max_length=126)
    grade_num = models.IntegerField()
    number_min = models.IntegerField(blank=True, null=True)
    number_max = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'choice_course_number'


class ChoiceCourseTime(models.Model):
    c_id = models.AutoField(primary_key=True)
    grade_num = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    rangse = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    weeks = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'choice_course_time'


class ElectiveTime(models.Model):
    waterid = models.AutoField(primary_key=True)
    grade_no = models.IntegerField()
    lesson_no = models.IntegerField()
    starttime = models.CharField(max_length=10, blank=True, null=True)
    endtime = models.CharField(max_length=10, blank=True, null=True)
    semester_no = models.IntegerField()
    used = models.IntegerField(blank=True, null=True)
    calltime = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elective_time'


class EvaulateActivitiesPhoto(models.Model):
    photo_id = models.AutoField(primary_key=True)
    id = models.ForeignKey('EvaulateSelectionClass', models.DO_NOTHING, db_column='id', blank=True, null=True)
    file_name = models.CharField(max_length=128, blank=True, null=True)
    file_url = models.CharField(max_length=512, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    file_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaulate_activities_photo'


class EvaulateSelectionActivities(models.Model):
    select_id = models.AutoField(primary_key=True)
    semester_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    application_endtime = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaulate_selection_activities'


class EvaulateSelectionActivitiesTemplet(models.Model):
    templet_id = models.AutoField(primary_key=True)
    templet_type = models.IntegerField(blank=True, null=True)
    templet_name = models.CharField(max_length=128, blank=True, null=True)
    templet_url = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaulate_selection_activities_templet'


class EvaulateSelectionClass(models.Model):
    select = models.ForeignKey(EvaulateSelectionActivities, models.DO_NOTHING, blank=True, null=True)
    class_id = models.IntegerField(blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaulate_selection_class'


class EvaulateStuPacesetter(models.Model):
    pacesetter_id = models.AutoField(primary_key=True)
    id = models.ForeignKey(EvaulateSelectionClass, models.DO_NOTHING, db_column='id', blank=True, null=True)
    pacesetter_type = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=128, blank=True, null=True)
    political_status = models.CharField(max_length=128, blank=True, null=True)
    study_level = models.CharField(max_length=128, blank=True, null=True)
    health_score = models.FloatField(blank=True, null=True)
    specialty = models.CharField(max_length=256, blank=True, null=True)
    volunteering = models.CharField(max_length=512, blank=True, null=True)
    practical_training = models.CharField(max_length=512, blank=True, null=True)
    awards = models.CharField(max_length=1024, blank=True, null=True)
    violation = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaulate_stu_pacesetter'


class KcwAbility(models.Model):
    abilityid = models.AutoField(db_column='AbilityId', primary_key=True)  # Field name made lowercase.
    abilityname = models.CharField(db_column='AbilityName', max_length=50)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId')  # Field name made lowercase.
    learningphaseid = models.IntegerField(db_column='LearningPhaseId')  # Field name made lowercase.
    createrid = models.IntegerField(db_column='CreaterId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updateuserid = models.IntegerField(db_column='UpdateUserId', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='IsValid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_ability'


class KcwBkexamitems(models.Model):
    examitemid = models.AutoField(db_column='ExamItemId', primary_key=True)  # Field name made lowercase.
    bkexamid = models.IntegerField(db_column='BkExamId')  # Field name made lowercase.
    bkitemid = models.IntegerField(db_column='BkItemId')  # Field name made lowercase.
    solvingprocess = models.TextField(db_column='SolvingProcess')  # Field name made lowercase. This field type is a guess.
    serialno = models.IntegerField(db_column='SerialNo')  # Field name made lowercase.
    serialtext = models.CharField(db_column='SerialText', max_length=10)  # Field name made lowercase.
    score = models.DecimalField(db_column='Score', max_digits=8, decimal_places=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_bkexamitems'


class KcwBkitemability(models.Model):
    bkitemid = models.IntegerField(db_column='BkItemId', primary_key=True)  # Field name made lowercase.
    abilityid = models.IntegerField(db_column='AbilityId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_bkitemability'
        unique_together = (('bkitemid', 'abilityid'),)


class KcwBkitemanalysevideo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    bkitemid = models.IntegerField(db_column='BkItemId')  # Field name made lowercase.
    videoname = models.CharField(db_column='VideoName', max_length=100)  # Field name made lowercase.
    videourl = models.CharField(db_column='VideoUrl', max_length=100)  # Field name made lowercase.
    intro = models.CharField(db_column='Intro', max_length=500, blank=True, null=True)  # Field name made lowercase.
    clickrate = models.IntegerField(db_column='ClickRate')  # Field name made lowercase.
    score = models.FloatField(db_column='Score')  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_bkitemanalysevideo'


class KcwBkitembank(models.Model):
    bkitemid = models.AutoField(db_column='BkItemId', primary_key=True)  # Field name made lowercase.
    originalitemid = models.IntegerField(db_column='OriginalItemId')  # Field name made lowercase.
    itemtypeid = models.IntegerField(db_column='ItemTypeId')  # Field name made lowercase.
    parentitemid = models.IntegerField(db_column='ParentItemId')  # Field name made lowercase.
    itemcontent = models.TextField(db_column='ItemContent', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    answer = models.TextField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.
    answerdes = models.TextField(db_column='AnswerDes', blank=True, null=True)  # Field name made lowercase.
    difficulty = models.FloatField(db_column='Difficulty', blank=True, null=True)  # Field name made lowercase.
    differentiation = models.FloatField(db_column='Differentiation', blank=True, null=True)  # Field name made lowercase.
    childitemindex = models.IntegerField(db_column='ChildItemIndex')  # Field name made lowercase.
    complete = models.IntegerField(db_column='Complete', blank=True, null=True)  # Field name made lowercase.
    resolve = models.TextField(db_column='Resolve', blank=True, null=True)  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId')  # Field name made lowercase.
    learningphaseid = models.IntegerField(db_column='LearningPhaseId')  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeId')  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId')  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId')  # Field name made lowercase.
    zucount = models.IntegerField(db_column='ZuCount')  # Field name made lowercase.
    usephase = models.IntegerField(db_column='UsePhase', blank=True, null=True)  # Field name made lowercase.
    reslevel = models.IntegerField(db_column='ResLevel', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    scoringrate = models.IntegerField(db_column='ScoringRate', blank=True, null=True)  # Field name made lowercase.
    testnumber = models.IntegerField(db_column='TestNumber', blank=True, null=True)  # Field name made lowercase.
    isdel = models.IntegerField(db_column='IsDel')  # Field name made lowercase.
    createrid = models.IntegerField(db_column='CreaterId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updateuserid = models.IntegerField(db_column='UpdateUserId', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_bkitembank'


class KcwBkitemchapter(models.Model):
    chapterid = models.IntegerField(db_column='ChapterId', primary_key=True)  # Field name made lowercase.
    bkitemid = models.IntegerField(db_column='BkItemId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_bkitemchapter'
        unique_together = (('chapterid', 'bkitemid'),)


class KcwBkitemcognitive(models.Model):
    bkitemid = models.IntegerField(db_column='BkItemId')  # Field name made lowercase.
    cognitiveid = models.IntegerField(db_column='CognitiveId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_bkitemcognitive'
        unique_together = (('cognitiveid', 'bkitemid'),)


class KcwBkitemknowledgepoint(models.Model):
    bkitemid = models.IntegerField(db_column='BkItemId', primary_key=True)  # Field name made lowercase.
    knid = models.IntegerField(db_column='KnId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_bkitemknowledgepoint'
        unique_together = (('bkitemid', 'knid'),)


class KcwBkitemoptions(models.Model):
    optionid = models.AutoField(db_column='OptionId', primary_key=True)  # Field name made lowercase.
    bkitemid = models.IntegerField(db_column='BkItemId')  # Field name made lowercase.
    itemoption = models.CharField(db_column='ItemOption', max_length=4)  # Field name made lowercase.
    optioncontent = models.TextField(db_column='OptionContent')  # Field name made lowercase.
    isright = models.TextField(db_column='IsRight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createrid = models.BigIntegerField(db_column='CreaterId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updateuserid = models.BigIntegerField(db_column='UpdateUserId', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_bkitemoptions'


class KcwBkresource(models.Model):
    bkresourceid = models.AutoField(db_column='BkResourceId', primary_key=True)  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId')  # Field name made lowercase.
    unitid = models.IntegerField(db_column='UnitId')  # Field name made lowercase.
    chapterid = models.IntegerField(db_column='ChapterId')  # Field name made lowercase.
    resourceid = models.IntegerField(db_column='ResourceId')  # Field name made lowercase.
    displayinhome = models.TextField(db_column='DisplayInHome', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createuserid = models.IntegerField(db_column='CreateUserId', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    browsenum = models.IntegerField(db_column='BrowseNum', blank=True, null=True)  # Field name made lowercase.
    commentnum = models.IntegerField(db_column='CommentNum', blank=True, null=True)  # Field name made lowercase.
    resourcename = models.CharField(db_column='ResourceName', max_length=100)  # Field name made lowercase.
    faceurl = models.CharField(db_column='FaceUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId')  # Field name made lowercase.
    semesterid = models.IntegerField(db_column='SemesterId', blank=True, null=True)  # Field name made lowercase.
    releasestatus = models.IntegerField(db_column='ReleaseStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_bkresource'


class KcwBkresourceexam(models.Model):
    bkresourceid = models.IntegerField(db_column='BkResourceId', primary_key=True)  # Field name made lowercase.
    bkexamid = models.IntegerField(db_column='BkExamId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_bkresourceexam'
        unique_together = (('bkresourceid', 'bkexamid'),)


class KcwChapter(models.Model):
    chapterid = models.AutoField(db_column='ChapterId', primary_key=True)  # Field name made lowercase.
    textbookid = models.IntegerField(db_column='TextbookId')  # Field name made lowercase.
    chaptername = models.CharField(db_column='ChapterName', max_length=50)  # Field name made lowercase.
    chaptertype = models.IntegerField(db_column='ChapterType')  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId')  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.TextField(db_column='IsValid')  # Field name made lowercase. This field type is a guess.
    createrid = models.IntegerField(db_column='CreaterId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updateuserid = models.IntegerField(db_column='UpdateUserId', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_chapter'


class KcwChapterknowledge(models.Model):
    chapterid = models.IntegerField(db_column='ChapterId', primary_key=True)  # Field name made lowercase.
    knowledgeid = models.IntegerField(db_column='KnowledgeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_chapterknowledge'
        unique_together = (('chapterid', 'knowledgeid'),)


class KcwCognitivelevel(models.Model):
    cognitiveid = models.AutoField(db_column='CognitiveId', primary_key=True)  # Field name made lowercase.
    cognitivename = models.CharField(db_column='CognitiveName', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId')  # Field name made lowercase.
    learningphaseid = models.IntegerField(db_column='LearningPhaseId')  # Field name made lowercase.
    createrid = models.IntegerField(db_column='CreaterId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updateuserid = models.IntegerField(db_column='UpdateUserId', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='IsValid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_cognitivelevel'


class KcwExam(models.Model):
    bkexamid = models.AutoField(db_column='BkExamId', primary_key=True)  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId')  # Field name made lowercase.
    unitid = models.IntegerField(db_column='UnitId')  # Field name made lowercase.
    chapterid = models.IntegerField(db_column='ChapterId')  # Field name made lowercase.
    examname = models.CharField(db_column='ExamName', max_length=100)  # Field name made lowercase.
    instruction = models.TextField(db_column='Instruction', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration')  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    modifieduserid = models.IntegerField(db_column='ModifiedUserid', blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    teachingstage = models.IntegerField(db_column='TeachingStage', blank=True, null=True)  # Field name made lowercase.
    checkingtype = models.IntegerField(db_column='CheckingType', blank=True, null=True)  # Field name made lowercase.
    videoresid = models.IntegerField(db_column='VideoResId', blank=True, null=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId')  # Field name made lowercase.
    semester_id = models.IntegerField(db_column='Semester_id', blank=True, null=True)  # Field name made lowercase.
    releasestatus = models.IntegerField(db_column='ReleaseStatus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_exam'


class KcwExamanswer(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    examresultid = models.IntegerField(db_column='ExamResultId')  # Field name made lowercase.
    bkexamid = models.IntegerField(db_column='bkExamId')  # Field name made lowercase.
    bkitemid = models.IntegerField(db_column='BkItemId')  # Field name made lowercase.
    answer = models.TextField(db_column='Answer')  # Field name made lowercase.
    score = models.DecimalField(db_column='Score', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    teacherid = models.IntegerField(db_column='TeacherId', blank=True, null=True)  # Field name made lowercase.
    readingtime = models.DateTimeField(db_column='ReadingTime', blank=True, null=True)  # Field name made lowercase.
    answerresult = models.IntegerField(db_column='AnswerResult', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    replytype = models.IntegerField(db_column='ReplyType', blank=True, null=True)  # Field name made lowercase.
    usedtime = models.IntegerField(db_column='UsedTime', blank=True, null=True)  # Field name made lowercase.
    teacherscore = models.FloatField(db_column='TeacherScore', blank=True, null=True)  # Field name made lowercase.
    appraise = models.TextField(db_column='Appraise', blank=True, null=True)  # Field name made lowercase.
    appraisetype = models.IntegerField(db_column='AppraiseType', blank=True, null=True)  # Field name made lowercase.
    fullscore = models.DecimalField(db_column='FullScore', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    submittime = models.DateTimeField(db_column='SubmitTime', blank=True, null=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentId', blank=True, null=True)  # Field name made lowercase.
    processattach = models.CharField(db_column='ProcessAttach', max_length=200, blank=True, null=True)  # Field name made lowercase.
    markedanswerimgurl = models.CharField(db_column='MarkedAnswerImgUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_examanswer'


class KcwExamitems(models.Model):
    examitemid = models.AutoField(db_column='ExamItemId', primary_key=True)  # Field name made lowercase.
    bkexamid = models.IntegerField(db_column='BkExamId')  # Field name made lowercase.
    bkitemid = models.IntegerField(db_column='BkItemId')  # Field name made lowercase.
    solvingprocess = models.TextField(db_column='SolvingProcess')  # Field name made lowercase. This field type is a guess.
    serialno = models.IntegerField(db_column='SerialNo')  # Field name made lowercase.
    serialtext = models.CharField(db_column='SerialText', max_length=10)  # Field name made lowercase.
    score = models.DecimalField(db_column='Score', max_digits=8, decimal_places=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_examitems'


class KcwExamresult(models.Model):
    examresultid = models.AutoField(db_column='ExamResultId', primary_key=True)  # Field name made lowercase.
    bkexamid = models.IntegerField(db_column='BkExamId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    submittime = models.DateTimeField(db_column='SubmitTime', blank=True, null=True)  # Field name made lowercase.
    score = models.DecimalField(db_column='Score', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    readingpeopleid = models.BigIntegerField(db_column='ReadingPeopleId', blank=True, null=True)  # Field name made lowercase.
    readingtime = models.DateTimeField(db_column='ReadingTime', blank=True, null=True)  # Field name made lowercase.
    elapsedtime = models.IntegerField(db_column='ElapsedTime', blank=True, null=True)  # Field name made lowercase.
    zgtscore = models.FloatField(db_column='ZGTScore', blank=True, null=True)  # Field name made lowercase.
    kgtscore = models.FloatField(db_column='KGTScore', blank=True, null=True)  # Field name made lowercase.
    classid = models.BigIntegerField(db_column='ClassId', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    teacherscore = models.FloatField(db_column='TeacherScore', blank=True, null=True)  # Field name made lowercase.
    degradedscore = models.FloatField(db_column='DegradedScore', blank=True, null=True)  # Field name made lowercase.
    checkstudentid = models.IntegerField(db_column='CheckStudentId', blank=True, null=True)  # Field name made lowercase.
    markedanswerimgurl = models.CharField(db_column='MarkedAnswerImgUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_examresult'


class KcwItemability(models.Model):
    itemid = models.IntegerField(db_column='ItemId', primary_key=True)  # Field name made lowercase.
    abilityid = models.IntegerField(db_column='AbilityId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_itemability'
        unique_together = (('itemid', 'abilityid'),)


class KcwItemanalysevideo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemId')  # Field name made lowercase.
    videoname = models.CharField(db_column='VideoName', max_length=100)  # Field name made lowercase.
    videourl = models.CharField(db_column='VideoUrl', max_length=100)  # Field name made lowercase.
    intro = models.CharField(db_column='Intro', max_length=500, blank=True, null=True)  # Field name made lowercase.
    clickrate = models.IntegerField(db_column='ClickRate')  # Field name made lowercase.
    score = models.FloatField(db_column='Score')  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_itemanalysevideo'


class KcwItembank(models.Model):
    itemid = models.AutoField(db_column='ItemId', primary_key=True)  # Field name made lowercase.
    itemtypeid = models.IntegerField(db_column='ItemTypeId')  # Field name made lowercase.
    parentitemid = models.IntegerField(db_column='ParentItemId')  # Field name made lowercase.
    itemcontent = models.TextField(db_column='ItemContent', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    answer = models.TextField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.
    answerdes = models.TextField(db_column='AnswerDes', blank=True, null=True)  # Field name made lowercase.
    difficulty = models.FloatField(db_column='Difficulty', blank=True, null=True)  # Field name made lowercase.
    differentiation = models.FloatField(db_column='Differentiation', blank=True, null=True)  # Field name made lowercase.
    childitemindex = models.IntegerField(db_column='ChildItemIndex')  # Field name made lowercase.
    complete = models.IntegerField(db_column='Complete', blank=True, null=True)  # Field name made lowercase.
    resolve = models.TextField(db_column='Resolve', blank=True, null=True)  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId')  # Field name made lowercase.
    learningphaseid = models.IntegerField(db_column='LearningPhaseId')  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeId')  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId')  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId')  # Field name made lowercase.
    zucount = models.IntegerField(db_column='ZuCount')  # Field name made lowercase.
    usephase = models.IntegerField(db_column='UsePhase', blank=True, null=True)  # Field name made lowercase.
    reslevel = models.IntegerField(db_column='ResLevel', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    scoringrate = models.IntegerField(db_column='ScoringRate', blank=True, null=True)  # Field name made lowercase.
    testnumber = models.IntegerField(db_column='TestNumber', blank=True, null=True)  # Field name made lowercase.
    isdel = models.IntegerField(db_column='IsDel')  # Field name made lowercase.
    createrid = models.IntegerField(db_column='CreaterId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updateuserid = models.IntegerField(db_column='UpdateUserId', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_itembank'


class KcwItemchapter(models.Model):
    chapterid = models.IntegerField(db_column='ChapterId', primary_key=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_itemchapter'
        unique_together = (('chapterid', 'itemid'),)


class KcwItemcognitive(models.Model):
    itemid = models.IntegerField(db_column='ItemId')  # Field name made lowercase.
    cognitiveid = models.IntegerField(db_column='CognitiveId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_itemcognitive'
        unique_together = (('cognitiveid', 'itemid'),)


class KcwItemknowledgepoint(models.Model):
    itemid = models.IntegerField(db_column='ItemId', primary_key=True)  # Field name made lowercase.
    knid = models.IntegerField(db_column='KnId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_itemknowledgepoint'
        unique_together = (('itemid', 'knid'),)


class KcwItemoptions(models.Model):
    optionid = models.AutoField(db_column='OptionId', primary_key=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemId')  # Field name made lowercase.
    itemoption = models.CharField(db_column='ItemOption', max_length=4)  # Field name made lowercase.
    optioncontent = models.TextField(db_column='OptionContent')  # Field name made lowercase.
    isright = models.TextField(db_column='IsRight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createrid = models.BigIntegerField(db_column='CreaterId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updateuserid = models.BigIntegerField(db_column='UpdateUserId', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_itemoptions'


class KcwItemtype(models.Model):
    itemtypeid = models.AutoField(db_column='ItemTypeId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500)  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder', blank=True, null=True)  # Field name made lowercase.
    createrid = models.IntegerField(db_column='CreaterId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updateuserid = models.IntegerField(db_column='UpdateUserId', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    basicitemtype = models.IntegerField(db_column='BasicItemType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_itemtype'


class KcwKnowledge(models.Model):
    knowledgeid = models.AutoField(db_column='knowledgeId', primary_key=True)  # Field name made lowercase.
    knowledgename = models.CharField(db_column='KnowledgeName', max_length=100)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId')  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId')  # Field name made lowercase.
    learningphaseid = models.IntegerField(db_column='LearningPhaseId')  # Field name made lowercase.
    coursestandardid = models.IntegerField(db_column='CourseStandardId')  # Field name made lowercase.
    knowledgelevel = models.IntegerField(db_column='KnowledgeLevel')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder')  # Field name made lowercase.
    createrid = models.IntegerField(db_column='CreaterId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updateuserid = models.IntegerField(db_column='UpdateUserId', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='IsValid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_knowledge'


class KcwKsexamtask(models.Model):
    examtaskid = models.IntegerField(primary_key=True)
    schoolitemid = models.IntegerField()
    orgid = models.IntegerField()
    schoolyearid = models.IntegerField()
    gradeid = models.IntegerField()
    subjectid = models.IntegerField(blank=True, null=True)
    termid = models.IntegerField()
    examtype = models.IntegerField(blank=True, null=True)
    exammodel = models.IntegerField(blank=True, null=True)
    examcategory = models.IntegerField(blank=True, null=True)
    examdate = models.CharField(max_length=100)
    progress = models.IntegerField()
    state = models.IntegerField()
    isopen = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.CharField(max_length=100)
    create_userid = models.IntegerField(db_column='create_userId')  # Field name made lowercase.
    create_time = models.DateTimeField()
    modified_userid = models.IntegerField(blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kcw_ksexamtask'


class KcwMistakeitems(models.Model):
    mistakeid = models.AutoField(db_column='MistakeId', primary_key=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemId')  # Field name made lowercase.
    examid = models.IntegerField(db_column='ExamId', blank=True, null=True)  # Field name made lowercase.
    examresultid = models.IntegerField(db_column='ExamResultId', blank=True, null=True)  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    redodate = models.DateTimeField(db_column='RedoDate', blank=True, null=True)  # Field name made lowercase.
    iscorrect = models.TextField(db_column='IsCorrect', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isredo = models.TextField(db_column='IsRedo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    nodisplay = models.TextField(db_column='NoDisplay')  # Field name made lowercase. This field type is a guess.
    answer = models.TextField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.
    markteacherid = models.IntegerField(db_column='MarkTeacherId', blank=True, null=True)  # Field name made lowercase.
    markdate = models.DateTimeField(db_column='MarkDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_mistakeitems'


class KcwPaperbank(models.Model):
    paperid = models.AutoField(db_column='PaperId', primary_key=True)  # Field name made lowercase.
    papername = models.CharField(db_column='PaperName', max_length=100)  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId')  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # Field name made lowercase.
    rreliability = models.FloatField(db_column='Rreliability', blank=True, null=True)  # Field name made lowercase.
    validity = models.FloatField(db_column='Validity', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    itemtotal = models.IntegerField(db_column='ItemTotal', blank=True, null=True)  # Field name made lowercase.
    paperscore = models.IntegerField(db_column='PaperScore', blank=True, null=True)  # Field name made lowercase.
    cardformat = models.TextField(db_column='CardFormat', blank=True, null=True)  # Field name made lowercase.
    paperfilepath = models.CharField(db_column='PaperFilePath', max_length=100, blank=True, null=True)  # Field name made lowercase.
    finishtotal = models.IntegerField(db_column='FinishTotal', blank=True, null=True)  # Field name made lowercase.
    audittotal = models.IntegerField(db_column='AuditTotal', blank=True, null=True)  # Field name made lowercase.
    passtotal = models.IntegerField(db_column='PassTotal', blank=True, null=True)  # Field name made lowercase.
    audituserid = models.IntegerField(db_column='AuditUserId', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    modifieduserid = models.IntegerField(db_column='ModifiedUserid', blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    papertype = models.IntegerField(db_column='PaperType', blank=True, null=True)  # Field name made lowercase.
    usephase = models.IntegerField(db_column='UsePhase', blank=True, null=True)  # Field name made lowercase.
    reslevel = models.IntegerField(db_column='ResLevel', blank=True, null=True)  # Field name made lowercase.
    apaperid = models.IntegerField(db_column='APaperId')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_paperbank'


class KcwPaperchapter(models.Model):
    chapterid = models.IntegerField(db_column='ChapterId', primary_key=True)  # Field name made lowercase.
    paperid = models.IntegerField(db_column='PaperId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_paperchapter'
        unique_together = (('chapterid', 'paperid'),)


class KcwPaperitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    paperid = models.IntegerField(db_column='PaperId')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemId')  # Field name made lowercase.
    serialno = models.IntegerField(db_column='SerialNo')  # Field name made lowercase.
    itemnumber = models.CharField(db_column='ItemNumber', max_length=10)  # Field name made lowercase.
    score = models.FloatField(db_column='Score')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_paperitems'


class KcwPersonalexam(models.Model):
    personalexamid = models.AutoField(db_column='PersonalExamId', primary_key=True)  # Field name made lowercase.
    personalexamname = models.CharField(db_column='PersonalExamName', max_length=100)  # Field name made lowercase.
    examid = models.IntegerField(db_column='ExamId')  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentId')  # Field name made lowercase.
    releasedate = models.DateTimeField(db_column='ReleaseDate')  # Field name made lowercase.
    finishdate = models.DateTimeField(db_column='FinishDate', blank=True, null=True)  # Field name made lowercase.
    studentname = models.CharField(db_column='StudentName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coursename = models.CharField(db_column='CourseName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId', blank=True, null=True)  # Field name made lowercase.
    teacherid = models.IntegerField(db_column='TeacherId', blank=True, null=True)  # Field name made lowercase.
    teachername = models.CharField(db_column='TeacherName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    itemcount = models.IntegerField(db_column='ItemCount', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField()
    usephase = models.IntegerField(db_column='UsePhase')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_personalexam'


class KcwPersonalexamdetail(models.Model):
    detailid = models.AutoField(db_column='DetailId', primary_key=True)  # Field name made lowercase.
    personalexamid = models.IntegerField(db_column='PersonalExamId')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemId')  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId', blank=True, null=True)  # Field name made lowercase.
    sourceitemid = models.IntegerField(db_column='SourceItemId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    answerdate = models.DateTimeField(db_column='AnswerDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    iscorrect = models.IntegerField(db_column='IsCorrect', blank=True, null=True)  # Field name made lowercase.
    answer = models.TextField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    processattach = models.CharField(db_column='ProcessAttach', max_length=200, blank=True, null=True)  # Field name made lowercase.
    markedanswerimgurl = models.CharField(db_column='MarkedAnswerImgUrl', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_personalexamdetail'


class KcwPersonalexamrecord(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    examid = models.IntegerField(db_column='ExamId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    teacherid = models.IntegerField(db_column='TeacherId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_personalexamrecord'


class KcwQuestionnaireanswer(models.Model):
    answerid = models.AutoField(db_column='AnswerId', primary_key=True)  # Field name made lowercase.
    questionnaireresultid = models.IntegerField(db_column='QuestionnaireResultId')  # Field name made lowercase.
    questionnaireid = models.IntegerField(db_column='QuestionnaireId')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemId')  # Field name made lowercase.
    answer = models.TextField(db_column='Answer')  # Field name made lowercase.
    score = models.DecimalField(db_column='Score', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_questionnaireanswer'


class KcwQuestionnairecategory(models.Model):
    questionnairecategoryid = models.AutoField(db_column='QuestionnaireCategoryId', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=100)  # Field name made lowercase.
    categorytype = models.IntegerField(db_column='CategoryType', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId')  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder', blank=True, null=True)  # Field name made lowercase.
    createrid = models.IntegerField(db_column='CreaterId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    lastupdateuserid = models.IntegerField(db_column='LastUpdateUserId', blank=True, null=True)  # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='LastUpdateDate', blank=True, null=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_questionnairecategory'


class KcwQuestionnaireitembank(models.Model):
    itemid = models.AutoField(db_column='ItemId', primary_key=True)  # Field name made lowercase.
    questiontypeid = models.IntegerField(db_column='QuestionTypeId')  # Field name made lowercase.
    parentitemid = models.IntegerField(db_column='ParentItemId', blank=True, null=True)  # Field name made lowercase.
    itemcontent = models.TextField(db_column='ItemContent', blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=2, decimal_places=0)  # Field name made lowercase.
    mark = models.DecimalField(db_column='Mark', max_digits=2, decimal_places=0)  # Field name made lowercase.
    childitemindex = models.IntegerField(db_column='ChildItemIndex')  # Field name made lowercase.
    createrid = models.IntegerField(db_column='CreaterId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    lastupdateuserid = models.IntegerField(db_column='LastUpdateUserId', blank=True, null=True)  # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='LastUpdateDate', blank=True, null=True)  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId')  # Field name made lowercase.
    papercount = models.IntegerField(db_column='PaperCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_questionnaireitembank'


class KcwQuestionnaireitemoptions(models.Model):
    optionid = models.AutoField(db_column='OptionId', primary_key=True)  # Field name made lowercase.
    itemid = models.BigIntegerField(db_column='ItemId')  # Field name made lowercase.
    itemoption = models.CharField(db_column='ItemOption', max_length=4)  # Field name made lowercase.
    optioncontent = models.CharField(db_column='OptionContent', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=8, decimal_places=1)  # Field name made lowercase.
    createrid = models.BigIntegerField(db_column='CreaterId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updateuserid = models.BigIntegerField(db_column='UpdateUserId', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_questionnaireitemoptions'


class KcwQuestionnaireitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    questionnaireid = models.IntegerField(db_column='QuestionnaireId')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemId')  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=3, decimal_places=2)  # Field name made lowercase.
    mark = models.DecimalField(db_column='Mark', max_digits=3, decimal_places=2)  # Field name made lowercase.
    tempid = models.IntegerField(db_column='TempId')  # Field name made lowercase.
    serialno = models.IntegerField(db_column='SerialNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_questionnaireitems'


class KcwQuestionnairereleasenotes(models.Model):
    releaseid = models.AutoField(db_column='ReleaseId', primary_key=True)  # Field name made lowercase.
    questionnaireid = models.IntegerField(db_column='QuestionnaireId')  # Field name made lowercase.
    publisherid = models.IntegerField(db_column='PublisherId')  # Field name made lowercase.
    publishdate = models.DateTimeField(db_column='PublishDate')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_questionnairereleasenotes'


class KcwQuestionnaireresult(models.Model):
    resultid = models.AutoField(db_column='ResultId', primary_key=True)  # Field name made lowercase.
    releaseid = models.IntegerField(db_column='ReleaseId')  # Field name made lowercase.
    questionnaireid = models.IntegerField(db_column='QuestionnaireId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    submittime = models.DateTimeField(db_column='SubmitTime', blank=True, null=True)  # Field name made lowercase.
    elapsedtime = models.IntegerField(db_column='ElapsedTime', blank=True, null=True)  # Field name made lowercase.
    score = models.DecimalField(db_column='Score', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    userroleid = models.IntegerField(db_column='UserRoleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_questionnaireresult'


class KcwQuestionnaires(models.Model):
    questionnaireid = models.AutoField(db_column='QuestionnaireId', primary_key=True)  # Field name made lowercase.
    questionnairename = models.CharField(db_column='QuestionnaireName', max_length=100)  # Field name made lowercase.
    usertype = models.IntegerField(db_column='UserType')  # Field name made lowercase.
    agerange = models.IntegerField(db_column='AgeRange')  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolId')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    itemcount = models.IntegerField(db_column='ItemCount', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.TextField(db_column='IsDelete', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    usenum = models.IntegerField(db_column='UseNum')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_questionnaires'


class KcwQuestionnairetemplate(models.Model):
    tempid = models.AutoField(db_column='TempId', primary_key=True)  # Field name made lowercase.
    questionnaireid = models.IntegerField(db_column='QuestionnaireId')  # Field name made lowercase.
    serialno = models.IntegerField(db_column='SerialNo', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    parenttempid = models.IntegerField(db_column='ParentTempId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_questionnairetemplate'


class KcwReceiveclass(models.Model):
    bkresourceid = models.IntegerField(db_column='BkResourceId', primary_key=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId')  # Field name made lowercase.
    rescategory = models.IntegerField(db_column='ResCategory')  # Field name made lowercase.
    begindate = models.DateTimeField(db_column='BeginDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_receiveclass'
        unique_together = (('bkresourceid', 'classid', 'rescategory'),)


class KcwResknowledgepoint(models.Model):
    resid = models.IntegerField(db_column='ResId', primary_key=True)  # Field name made lowercase.
    knid = models.IntegerField(db_column='KnId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_resknowledgepoint'
        unique_together = (('resid', 'knid'),)


class KcwResource(models.Model):
    resid = models.AutoField(db_column='ResId', primary_key=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId')  # Field name made lowercase.
    textbookid = models.IntegerField(db_column='TextbookId', blank=True, null=True)  # Field name made lowercase.
    resname = models.CharField(db_column='ResName', max_length=100)  # Field name made lowercase.
    rescontent = models.TextField(db_column='ResContent', blank=True, null=True)  # Field name made lowercase.
    extname = models.CharField(db_column='ExtName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    restype = models.IntegerField(db_column='ResType')  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    trialseeding = models.IntegerField(db_column='Trialseeding', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    browsenum = models.IntegerField(db_column='BrowseNum', blank=True, null=True)  # Field name made lowercase.
    commentnum = models.IntegerField(db_column='CommentNum', blank=True, null=True)  # Field name made lowercase.
    faceurl = models.CharField(db_column='FaceUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reslevel = models.IntegerField(db_column='ResLevel', blank=True, null=True)  # Field name made lowercase.
    attasize = models.FloatField(db_column='AttaSize')  # Field name made lowercase.
    schoolid = models.BigIntegerField(db_column='SchoolId')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    timecited = models.IntegerField(db_column='TimeCited', blank=True, null=True)  # Field name made lowercase.
    score = models.DecimalField(db_column='Score', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rescategory = models.IntegerField(db_column='ResCategory')  # Field name made lowercase.
    isexcellent = models.TextField(db_column='IsExcellent')  # Field name made lowercase. This field type is a guess.
    istop = models.TextField(db_column='IsTop')  # Field name made lowercase. This field type is a guess.
    toptime = models.DateTimeField(db_column='TopTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_resource'


class KcwResourceability(models.Model):
    resid = models.IntegerField(db_column='ResId', primary_key=True)  # Field name made lowercase.
    abilityid = models.IntegerField(db_column='AbilityId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_resourceability'
        unique_together = (('resid', 'abilityid'),)


class KcwResourcechapter(models.Model):
    resid = models.IntegerField(db_column='ResId')  # Field name made lowercase.
    chapterid = models.IntegerField(db_column='ChapterId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_resourcechapter'
        unique_together = (('chapterid', 'resid'),)


class KcwResourcecognitive(models.Model):
    resid = models.IntegerField(db_column='ResId')  # Field name made lowercase.
    cognitiveid = models.IntegerField(db_column='CognitiveId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_resourcecognitive'
        unique_together = (('cognitiveid', 'resid'),)


class KcwResourcerecord(models.Model):
    resrecid = models.AutoField(db_column='ResRecId', primary_key=True)  # Field name made lowercase.
    bkresid = models.IntegerField(db_column='BkResId')  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_resourcerecord'


class KcwResourcerecorddetailed(models.Model):
    resrecdetid = models.AutoField(db_column='ResRecDetId', primary_key=True)  # Field name made lowercase.
    bkresid = models.IntegerField(db_column='BkResId')  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId')  # Field name made lowercase.
    point = models.IntegerField(db_column='Point')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_resourcerecorddetailed'


class KcwResourcereply(models.Model):
    replyid = models.AutoField(db_column='ReplyId', primary_key=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId')  # Field name made lowercase.
    resourceid = models.IntegerField(db_column='ResourceId')  # Field name made lowercase.
    bkresourceid = models.IntegerField(db_column='BkResourceId', blank=True, null=True)  # Field name made lowercase.
    replycategory = models.IntegerField(db_column='ReplyCategory', blank=True, null=True)  # Field name made lowercase.
    replycontent = models.CharField(db_column='ReplyContent', max_length=500)  # Field name made lowercase.
    replydate = models.DateTimeField(db_column='ReplyDate')  # Field name made lowercase.
    replyuserid = models.IntegerField(db_column='ReplyUserId')  # Field name made lowercase.
    replyrealname = models.CharField(db_column='ReplyRealName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    score = models.DecimalField(db_column='Score', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_resourcereply'


class KcwSubjectitemtype(models.Model):
    subjectid = models.IntegerField(db_column='SubjectId', primary_key=True)  # Field name made lowercase.
    itemtypeid = models.IntegerField(db_column='ItemTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_subjectitemtype'
        unique_together = (('subjectid', 'itemtypeid'),)


class KcwTextbooks(models.Model):
    textbookid = models.AutoField(db_column='TextbookId', primary_key=True)  # Field name made lowercase.
    levelid = models.IntegerField(db_column='LevelId')  # Field name made lowercase.
    textbookname = models.CharField(db_column='TextbookName', max_length=100)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId')  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId')  # Field name made lowercase.
    learningphaseid = models.IntegerField(db_column='LearningPhaseId')  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeId', blank=True, null=True)  # Field name made lowercase.
    publishingcompanyid = models.IntegerField(db_column='PublishingCompanyId')  # Field name made lowercase.
    volumeid = models.IntegerField(db_column='VolumeId')  # Field name made lowercase.
    coverurl = models.CharField(db_column='CoverUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isvalid = models.TextField(db_column='IsValid')  # Field name made lowercase. This field type is a guess.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    schoolid = models.BigIntegerField(db_column='SchoolId')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    summary = models.CharField(db_column='Summary', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createrid = models.IntegerField(db_column='CreaterId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updateuserid = models.IntegerField(db_column='UpdateUserId', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_textbooks'


class KcwWxopenuserid(models.Model):
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    openid = models.CharField(db_column='openId', max_length=32)  # Field name made lowercase.
    loginname = models.CharField(db_column='loginName', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kcw_wxopenuserid'


class KsCandidate(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentId')  # Field name made lowercase.
    candidateid = models.CharField(db_column='CandidateId', max_length=50)  # Field name made lowercase.
    examtaskid = models.IntegerField(db_column='ExamTaskId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ks_candidate'


class KsExamanswerrecord(models.Model):
    examanswerrecordid = models.AutoField(db_column='ExamAnswerRecordId', primary_key=True)  # Field name made lowercase.
    examrecordid = models.ForeignKey('KsExamrecord', models.DO_NOTHING, db_column='ExamRecordId')  # Field name made lowercase.
    examplanid = models.IntegerField(db_column='ExamPlanId')  # Field name made lowercase.
    questionnum = models.CharField(db_column='QuestionNum', max_length=30)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    parentnum = models.CharField(db_column='ParentNum', max_length=20)  # Field name made lowercase.
    answer = models.CharField(db_column='Answer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    answerurl = models.CharField(db_column='AnswerUrl', max_length=500, blank=True, null=True)  # Field name made lowercase.
    score = models.DecimalField(db_column='Score', max_digits=8, decimal_places=2)  # Field name made lowercase.
    layer = models.IntegerField(db_column='Layer', blank=True, null=True)  # Field name made lowercase.
    errormark = models.CharField(db_column='ErrorMark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    errors = models.CharField(db_column='Errors', max_length=50, blank=True, null=True)  # Field name made lowercase.
    srid = models.IntegerField(db_column='Srid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ks_examanswerrecord'


class KsExamclass(models.Model):
    examclassid = models.AutoField(db_column='ExamClassId', primary_key=True)  # Field name made lowercase.
    examplanid = models.ForeignKey('KsExamplan', models.DO_NOTHING, db_column='ExamPlanId')  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId')  # Field name made lowercase.
    classname = models.CharField(db_column='ClassName', max_length=50)  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ks_examclass'


class KsExampaper(models.Model):
    exampaperid = models.AutoField(db_column='ExamPaperId', primary_key=True)  # Field name made lowercase.
    examplanid = models.ForeignKey('KsExamplan', models.DO_NOTHING, db_column='ExamPlanId', blank=True, null=True)  # Field name made lowercase.
    questionnum = models.CharField(db_column='QuestionNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    examtype = models.IntegerField(db_column='ExamType', blank=True, null=True)  # Field name made lowercase.
    itempoolid = models.IntegerField(db_column='ItemPoolId')  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    parentpoolid = models.IntegerField(db_column='ParentPoolId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ks_exampaper'


class KsExamplan(models.Model):
    examplanid = models.AutoField(db_column='ExamplanId', primary_key=True)  # Field name made lowercase.
    examtaskid = models.ForeignKey('KsExamtask', models.DO_NOTHING, db_column='ExamtaskId')  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId')  # Field name made lowercase.
    moduleid = models.IntegerField(db_column='ModuleId', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    bookversionid = models.IntegerField(db_column='BookVersionId', blank=True, null=True)  # Field name made lowercase.
    teachmark = models.CharField(db_column='TeachMark', max_length=500, blank=True, null=True)  # Field name made lowercase.
    subreq = models.CharField(db_column='SubReq', max_length=500, blank=True, null=True)  # Field name made lowercase.
    audituserid = models.IntegerField(db_column='AudituserId', blank=True, null=True)  # Field name made lowercase.
    cardfile = models.CharField(db_column='CardFile', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cardformat = models.CharField(db_column='CardFormat', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    teachuserid = models.IntegerField(db_column='TeachUserId', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    modifieduserid = models.IntegerField(db_column='ModifiedUserId', blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ks_examplan'


class KsExamrecord(models.Model):
    examrecordid = models.IntegerField(db_column='ExamRecordId', primary_key=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentId')  # Field name made lowercase.
    candidatenum = models.CharField(db_column='CandidateNum', max_length=50)  # Field name made lowercase.
    examplanid = models.IntegerField(db_column='ExamPlanId')  # Field name made lowercase.
    schoolitemid = models.IntegerField(db_column='SchoolItemId', blank=True, null=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeId')  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId')  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId')  # Field name made lowercase.
    moduleid = models.IntegerField(db_column='ModuleId', blank=True, null=True)  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId')  # Field name made lowercase.
    classid = models.IntegerField(db_column='ClassId')  # Field name made lowercase.
    schoolyearid = models.IntegerField(db_column='SchoolYearId')  # Field name made lowercase.
    examtype = models.CharField(db_column='ExamType', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    totalscore = models.DecimalField(db_column='TotalScore', max_digits=8, decimal_places=1)  # Field name made lowercase.
    layer = models.IntegerField(db_column='Layer', blank=True, null=True)  # Field name made lowercase.
    importdate = models.DateTimeField(db_column='ImportDate', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=500, blank=True, null=True)
    srid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ks_examrecord'


class KsExamstandardinfo(models.Model):
    examstandardid = models.AutoField(db_column='ExamStandardId', primary_key=True)  # Field name made lowercase.
    examplanid = models.ForeignKey(KsExamplan, models.DO_NOTHING, db_column='ExamPlanId')  # Field name made lowercase.
    questionnum = models.CharField(db_column='QuestionNum', max_length=50)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    parentnum = models.CharField(db_column='ParentNum', max_length=50)  # Field name made lowercase.
    examtype = models.IntegerField(db_column='ExamType', blank=True, null=True)  # Field name made lowercase.
    questiontype = models.IntegerField(db_column='QuestionType', blank=True, null=True)  # Field name made lowercase.
    score = models.DecimalField(db_column='Score', max_digits=8, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    answer = models.CharField(db_column='Answer', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    scoreset = models.CharField(db_column='ScoreSet', max_length=500, blank=True, null=True)  # Field name made lowercase.
    options = models.CharField(db_column='Options', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    modifieduserid = models.IntegerField(db_column='ModifiedUserId', blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ks_examstandardinfo'


class KsExamtask(models.Model):
    examtaskid = models.AutoField(db_column='ExamTaskId', primary_key=True)  # Field name made lowercase.
    schoolitemid = models.IntegerField(db_column='SchoolItemId', blank=True, null=True)  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    schoolyearid = models.IntegerField(db_column='SchoolYearId', blank=True, null=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeId')  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId')  # Field name made lowercase.
    termid = models.IntegerField(db_column='TermId', blank=True, null=True)  # Field name made lowercase.
    examtype = models.IntegerField(db_column='ExamType', blank=True, null=True)  # Field name made lowercase.
    exammodel = models.IntegerField(db_column='ExamModel', blank=True, null=True)  # Field name made lowercase.
    examcategory = models.IntegerField(db_column='ExamCategory', blank=True, null=True)  # Field name made lowercase.
    examdate = models.TextField(db_column='ExamDate', blank=True, null=True)  # Field name made lowercase.
    progress = models.IntegerField(db_column='Progress', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    isopen = models.TextField(db_column='IsOpen', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    modifieduserid = models.IntegerField(db_column='ModifiedUserId', blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ks_examtask'


class KsExamtaskrecord(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    examtaskid = models.IntegerField(db_column='ExamTaskId', blank=True, null=True)  # Field name made lowercase.
    examplanid = models.IntegerField(db_column='ExamplanId', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ks_examtaskrecord'


class KsReportheaders(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    headerid = models.IntegerField(db_column='HeaderId')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    cols = models.TextField(db_column='Cols')  # Field name made lowercase.
    total = models.IntegerField(db_column='Total')  # Field name made lowercase.
    colnames = models.TextField(db_column='Colnames')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ks_reportheaders'


class KsRoleLimit(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    limitid = models.IntegerField(db_column='LimitId')  # Field name made lowercase.
    limitname = models.CharField(db_column='LimitName', max_length=100)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleId')  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ks_role_limit'


class KsStudentlevel(models.Model):
    studentlevelid = models.AutoField(db_column='StudentLevelId', primary_key=True)  # Field name made lowercase.
    examplanid = models.IntegerField(db_column='ExamPlanId', blank=True, null=True)  # Field name made lowercase.
    examtaskid = models.IntegerField(db_column='ExamTaskId', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    upperlimit = models.DecimalField(db_column='UpperLimit', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lowerlimit = models.DecimalField(db_column='LowerLimit', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    modifieduserid = models.IntegerField(db_column='ModifiedUserId', blank=True, null=True)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ks_studentlevel'


class KsTableExplain(models.Model):
    id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=50, blank=True, null=True)
    field_name = models.CharField(max_length=50, blank=True, null=True)
    field_value = models.CharField(max_length=50, blank=True, null=True)
    explain = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ks_table_explain'


class OUserpassword(models.Model):
    p_id = models.IntegerField(primary_key=True)
    loginname = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    backupa = models.IntegerField(blank=True, null=True)
    backupb = models.IntegerField(blank=True, null=True)
    backupc = models.CharField(max_length=20, blank=True, null=True)
    backupd = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'o_userpassword'


class OaTeacher(models.Model):
    person_id = models.IntegerField(primary_key=True)
    learn_code = models.CharField(max_length=32, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    degree_code = models.IntegerField(blank=True, null=True)
    polity_code = models.IntegerField(blank=True, null=True)
    marry_state = models.IntegerField(blank=True, null=True)
    graduate_college = models.CharField(max_length=256, blank=True, null=True)
    work_date = models.DateTimeField(blank=True, null=True)
    position = models.CharField(max_length=64, blank=True, null=True)
    professional = models.IntegerField(blank=True, null=True)
    mobile_tel = models.CharField(max_length=32, blank=True, null=True)
    home_tel = models.CharField(max_length=32, blank=True, null=True)
    e_mail = models.CharField(max_length=32, blank=True, null=True)
    home_address = models.CharField(max_length=256, blank=True, null=True)
    link_address = models.CharField(max_length=256, blank=True, null=True)
    introduce = models.CharField(max_length=256, blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    if_leader = models.IntegerField(blank=True, null=True)
    campus_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oa_teacher'


class OaTeam(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oa_team'


class OptionalCourse(models.Model):
    optional_id = models.AutoField(primary_key=True)
    grade_no = models.IntegerField(blank=True, null=True)
    class_no = models.IntegerField(blank=True, null=True)
    week_no = models.IntegerField(blank=True, null=True)
    lesson_no = models.IntegerField(blank=True, null=True)
    lesson_name = models.CharField(max_length=500, blank=True, null=True)
    semester_no = models.IntegerField(blank=True, null=True)
    uploader = models.IntegerField(blank=True, null=True)
    up_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'optional_course'


class PeAddStandard(models.Model):
    a_id = models.AutoField(primary_key=True)
    pe_id = models.IntegerField(blank=True, null=True)
    note = models.CharField(db_column='NOTE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    add_score = models.IntegerField(blank=True, null=True)
    grade_1_down = models.CharField(max_length=20, blank=True, null=True)
    grade_2_down = models.CharField(max_length=20, blank=True, null=True)
    grade_3_down = models.CharField(max_length=20, blank=True, null=True)
    grade_4_down = models.CharField(max_length=20, blank=True, null=True)
    grade_5_down = models.CharField(max_length=20, blank=True, null=True)
    grade_6_down = models.CharField(max_length=20, blank=True, null=True)
    pe_sex = models.CharField(max_length=2, blank=True, null=True)
    grade_1_up = models.CharField(max_length=20, blank=True, null=True)
    grade_2_up = models.CharField(max_length=20, blank=True, null=True)
    grade_3_up = models.CharField(max_length=20, blank=True, null=True)
    grade_4_up = models.CharField(max_length=20, blank=True, null=True)
    grade_5_up = models.CharField(max_length=20, blank=True, null=True)
    grade_6_up = models.CharField(max_length=20, blank=True, null=True)
    chu_1_down = models.CharField(max_length=50, blank=True, null=True)
    chu_2_down = models.CharField(max_length=50, blank=True, null=True)
    chu_3_down = models.CharField(max_length=50, blank=True, null=True)
    gao_1_down = models.CharField(max_length=50, blank=True, null=True)
    gao_2_down = models.CharField(max_length=50, blank=True, null=True)
    gao_3_down = models.CharField(max_length=50, blank=True, null=True)
    chu_1_up = models.CharField(max_length=50, blank=True, null=True)
    chu_2_up = models.CharField(max_length=50, blank=True, null=True)
    chu_3_up = models.CharField(max_length=50, blank=True, null=True)
    gao_1_up = models.CharField(max_length=50, blank=True, null=True)
    gao_2_up = models.CharField(max_length=50, blank=True, null=True)
    gao_3_up = models.CharField(max_length=50, blank=True, null=True)
    gao_4_up = models.CharField(max_length=50, blank=True, null=True)
    gao_4_down = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_add_standard'


class PeBaseinfo(models.Model):
    pe_id = models.AutoField(primary_key=True)
    pe_unit = models.CharField(max_length=10, blank=True, null=True)
    pe_note = models.CharField(max_length=500, blank=True, null=True)
    pe_type = models.CharField(max_length=2, blank=True, null=True)
    pe_name = models.CharField(max_length=100, blank=True, null=True)
    pe_ztype = models.IntegerField(blank=True, null=True)
    pe_precision = models.CharField(max_length=10, blank=True, null=True)
    objective = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_baseinfo'


class PeBaseinfoGraderela(models.Model):
    pe_id = models.IntegerField(primary_key=True)
    pe_grade_code = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'pe_baseinfo_graderela'
        unique_together = (('pe_id', 'pe_grade_code'),)


class PeBaseinfoLevelrela(models.Model):
    pe_id = models.IntegerField()
    pe_level_code = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'pe_baseinfo_levelrela'
        unique_together = (('pe_level_code', 'pe_id'),)


class PeBaseinfoSexrela(models.Model):
    pe_id = models.IntegerField()
    pe_sex = models.CharField(primary_key=True, max_length=2)

    class Meta:
        managed = False
        db_table = 'pe_baseinfo_sexrela'
        unique_together = (('pe_sex', 'pe_id'),)


class PeExaPlan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    exam_name = models.CharField(max_length=32, blank=True, null=True)
    exam_type = models.IntegerField(blank=True, null=True)
    semester_id = models.IntegerField()
    semester_name = models.CharField(max_length=20, blank=True, null=True)
    semester_num = models.IntegerField(blank=True, null=True)
    exam_area = models.IntegerField(blank=True, null=True)
    exam_teacher = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pe_exa_plan'


class PeExaPlanGraderela(models.Model):
    plan_id = models.IntegerField()
    g_id = models.IntegerField()
    r_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pe_exa_plan_graderela'


class PeExaPlanPerela(models.Model):
    plan_id = models.IntegerField()
    r_id = models.IntegerField()
    pe_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pe_exa_plan_perela'


class PeExcObject(models.Model):
    pe_grade_code = models.CharField(max_length=2)
    pe_grade_name = models.CharField(max_length=20)
    grade_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pe_exc_object'


class PeFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=100, blank=True, null=True)
    filepath = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_file'


class PeGrade(models.Model):
    g_id = models.AutoField(primary_key=True)
    g_name = models.CharField(max_length=50, blank=True, null=True)
    g_note = models.CharField(max_length=500, blank=True, null=True)
    semester_id = models.IntegerField(blank=True, null=True)
    semester_name = models.CharField(max_length=20, blank=True, null=True)
    semester_num = models.IntegerField(blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    teacher_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_grade'


class PeGradeDictionary(models.Model):
    grade_num = models.IntegerField(blank=True, null=True)
    grade_name = models.CharField(max_length=10, blank=True, null=True)
    grade_levle = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_grade_dictionary'


class PeGradeStuRela(models.Model):
    g_id = models.IntegerField(primary_key=True)
    stu_id = models.IntegerField()
    grade_num = models.IntegerField(blank=True, null=True)
    grade_id = models.IntegerField(blank=True, null=True)
    serial = models.IntegerField(blank=True, null=True)
    class_num = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    student_no = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_grade_stu_rela'
        unique_together = (('g_id', 'stu_id'),)


class PeLevel(models.Model):
    pe_level_name = models.CharField(max_length=10)
    pe_level_code = models.CharField(primary_key=True, max_length=10)
    pe_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'pe_level'


class PeRecipe(models.Model):
    r_id = models.AutoField(primary_key=True)
    pe_level_code = models.CharField(max_length=2, blank=True, null=True)
    r_cnt = models.CharField(db_column='R_cnt', max_length=500, blank=True, null=True)  # Field name made lowercase.
    filerelaid = models.IntegerField(blank=True, null=True)
    pe_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_recipe'


class PeRecipeFileRela(models.Model):
    relafileid = models.IntegerField(primary_key=True)
    fileid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pe_recipe_file_rela'
        unique_together = (('relafileid', 'fileid'),)


class PeRetdataImp(models.Model):
    d_id = models.AutoField(primary_key=True)
    g_year = models.CharField(max_length=20, blank=True, null=True)
    pe_id = models.IntegerField(blank=True, null=True)
    r_name = models.CharField(max_length=50, blank=True, null=True)
    g_id = models.CharField(max_length=12, blank=True, null=True)
    g_sn = models.CharField(max_length=5, blank=True, null=True)
    pe_sex_code = models.CharField(max_length=2, blank=True, null=True)
    r_final = models.CharField(max_length=2, blank=True, null=True)
    plan_id = models.PositiveIntegerField(blank=True, null=True)
    file_id = models.IntegerField(blank=True, null=True)
    insert_time = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_retdata_imp'


class PeRetdataImpFileRela(models.Model):
    file_id = models.IntegerField(primary_key=True)
    filerelaid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pe_retdata_imp_file_rela'
        unique_together = (('file_id', 'filerelaid'),)


class PeScore(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_score = models.IntegerField(blank=True, null=True)
    pe_level_code = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_score'


class PeScoreStandard(models.Model):
    pe_id = models.IntegerField()
    score = models.DecimalField(max_digits=4, decimal_places=1)
    one_score_downlimit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    one_score_uplimit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    two_score_downlimit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    two_score_uplimit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    three_score_downlimit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    three_score_uplimit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    four_score_downlimit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    four_score_uplimit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    five_score_downlimit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    five_score_uplimit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    six_score_downlimit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    six_score_uplimit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    pe_sex = models.CharField(max_length=2, blank=True, null=True)
    pe_level_code = models.CharField(max_length=20, blank=True, null=True)
    one_score_downlimit_chu = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    one_score_uplimit_chu = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    two_score_downlimit_chu = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    two_score_uplimit_chu = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    three_score_downlimit_chu = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    three_score_uplimit_chu = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    one_score_downlimit_gao = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    one_score_uplimit_gao = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    two_score_downlimit_gao = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    two_score_uplimit_gao = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    three_score_downlimit_gao = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    three_score_uplimit_gao = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    four_score_downlimit_gao = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    four_score_uplimit_gao = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_score_standard'


class PeScoreWeight(models.Model):
    weight_id = models.AutoField(primary_key=True)
    pe_id = models.IntegerField()
    score_weight = models.FloatField(blank=True, null=True)
    pe_grade_code = models.CharField(max_length=11, blank=True, null=True)
    six_score_weight = models.CharField(max_length=50, blank=True, null=True)
    five_score_weight = models.CharField(max_length=50, blank=True, null=True)
    four_score_weight = models.CharField(max_length=50, blank=True, null=True)
    three_score_weight = models.CharField(max_length=50, blank=True, null=True)
    two_score_weight = models.CharField(max_length=50, blank=True, null=True)
    one_score_weight = models.CharField(max_length=50, blank=True, null=True)
    one_score_weight_chu = models.CharField(max_length=50, blank=True, null=True)
    two_score_weight_chu = models.CharField(max_length=50, blank=True, null=True)
    three_score_weight_chu = models.CharField(max_length=50, blank=True, null=True)
    one_score_weight_gao = models.CharField(max_length=50, blank=True, null=True)
    two_score_weight_gao = models.CharField(max_length=50, blank=True, null=True)
    three_score_weight_gao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_score_weight'


class PeSex(models.Model):
    pe_sex = models.CharField(primary_key=True, max_length=2)
    pe_sex_name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_sex'


class PeSexAdd(models.Model):
    pe_sex = models.CharField(max_length=255, blank=True, null=True)
    pe_sex_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_sex_add'


class PeStuFileData(models.Model):
    file_id = models.IntegerField(blank=True, null=True)
    school_name = models.CharField(max_length=50, blank=True, null=True)
    ishead = models.CharField(max_length=2, blank=True, null=True)
    grade = models.CharField(max_length=20, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=10, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.CharField(max_length=20, blank=True, null=True)
    stu_id = models.CharField(max_length=20, blank=True, null=True)
    exam_name = models.CharField(max_length=50, blank=True, null=True)
    mt = models.CharField(max_length=30, blank=True, null=True)
    check_date = models.CharField(max_length=20, blank=True, null=True)
    result1 = models.CharField(max_length=10, blank=True, null=True)
    result2 = models.CharField(max_length=10, blank=True, null=True)
    result3 = models.CharField(max_length=10, blank=True, null=True)
    result4 = models.CharField(max_length=10, blank=True, null=True)
    result5 = models.CharField(max_length=10, blank=True, null=True)
    result6 = models.CharField(max_length=10, blank=True, null=True)
    result7 = models.CharField(max_length=10, blank=True, null=True)
    result8 = models.CharField(max_length=10, blank=True, null=True)
    result9 = models.CharField(max_length=10, blank=True, null=True)
    result10 = models.CharField(max_length=10, blank=True, null=True)
    result11 = models.CharField(max_length=10, blank=True, null=True)
    result12 = models.CharField(max_length=10, blank=True, null=True)
    result13 = models.CharField(max_length=10, blank=True, null=True)
    result14 = models.CharField(max_length=10, blank=True, null=True)
    x_id = models.AutoField(primary_key=True)
    g_id = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_stu_file_data'


class PeStuResult(models.Model):
    r_id = models.AutoField(primary_key=True)
    pe_id = models.IntegerField(blank=True, null=True)
    g_id = models.IntegerField(blank=True, null=True)
    r_result = models.CharField(max_length=200, blank=True, null=True)
    r_score = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    pe_level_code = models.CharField(max_length=2, blank=True, null=True)
    stu_id = models.IntegerField(blank=True, null=True)
    weightscore = models.FloatField(blank=True, null=True)
    d_id = models.IntegerField(blank=True, null=True)
    stacore = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    addscore = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    plan_id = models.IntegerField()
    remark = models.CharField(max_length=200, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_stu_result'


class PeStudent(models.Model):
    s_id = models.IntegerField(primary_key=True)
    s_stu_id = models.CharField(max_length=30)
    g_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe_student'


class PeUnit(models.Model):
    pe_unit = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'pe_unit'


class QuestionDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    papers = models.ForeignKey('QuestionPapers', models.DO_NOTHING)
    detail_order = models.IntegerField(blank=True, null=True)
    question_type = models.IntegerField(blank=True, null=True)
    question_content = models.TextField(blank=True, null=True)
    need_score = models.IntegerField(blank=True, null=True)
    need_answer = models.IntegerField(blank=True, null=True)
    low_answer = models.IntegerField(blank=True, null=True)
    high_answer = models.IntegerField(blank=True, null=True)
    old_detail_id = models.IntegerField(blank=True, null=True)
    isfu = models.IntegerField(blank=True, null=True)
    fu_id = models.IntegerField(blank=True, null=True)
    fu_options_id = models.IntegerField(blank=True, null=True)
    haszi = models.IntegerField(blank=True, null=True)
    page_id = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'question_detail'


class QuestionDetailExt(models.Model):
    ext_id = models.AutoField(primary_key=True)
    detail = models.ForeignKey(QuestionDetail, models.DO_NOTHING)
    grade_num = models.IntegerField()
    subject_name = models.CharField(max_length=256, blank=True, null=True)
    course_name = models.CharField(max_length=256, blank=True, null=True)
    teacher_name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'question_detail_ext'


class QuestionDetailOptions(models.Model):
    options_id = models.AutoField(primary_key=True)
    detail = models.ForeignKey(QuestionDetail, models.DO_NOTHING)
    options_order = models.IntegerField()
    options_content = models.CharField(max_length=256, blank=True, null=True)
    options_score = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    is_custom = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_detail_options'


class QuestionHistory(models.Model):
    h_id = models.AutoField(primary_key=True)
    question_id = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField()
    content = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_history'


class QuestionPapers(models.Model):
    papers_id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(blank=True, null=True)
    dept_id = models.IntegerField(blank=True, null=True)
    edit_user = models.ForeignKey(BasPerson, models.DO_NOTHING, blank=True, null=True)
    question_name = models.CharField(max_length=256, blank=True, null=True)
    question_num = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('QuestionType', models.DO_NOTHING, blank=True, null=True)
    apply_status = models.IntegerField(blank=True, null=True)
    publish_user = models.ForeignKey(BasPerson, models.DO_NOTHING, blank=True, null=True)
    publish_status = models.IntegerField(blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    allow_anonymity = models.IntegerField(blank=True, null=True)
    answer_object = models.IntegerField(blank=True, null=True)
    question_desc = models.CharField(max_length=256, blank=True, null=True)
    commit_content = models.CharField(max_length=256, blank=True, null=True)
    allow_same_ip = models.IntegerField(blank=True, null=True)
    allow_same_username = models.IntegerField(blank=True, null=True)
    allow_view = models.IntegerField(blank=True, null=True)
    have_time_limit = models.IntegerField(blank=True, null=True)
    teacher_dept = models.IntegerField(blank=True, null=True)
    teacher_everyone = models.IntegerField(blank=True, null=True)
    student_inschool_time = models.IntegerField(blank=True, null=True)
    inschool_time = models.CharField(max_length=64, blank=True, null=True)
    student_level = models.IntegerField(blank=True, null=True)
    student_specialty_name = models.IntegerField(blank=True, null=True)
    student_course = models.IntegerField(blank=True, null=True)
    student_organization = models.IntegerField(blank=True, null=True)
    question_remark = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_papers'


class QuestionType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_type'


class StudentAnswer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question_type = models.IntegerField(blank=True, null=True)
    batch_type = models.IntegerField(blank=True, null=True)
    question_paper_id = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=64, blank=True, null=True)
    total_score = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    answer_time = models.DateTimeField(blank=True, null=True)
    is_commit = models.IntegerField(blank=True, null=True)
    user_ip_name = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    personal_type = models.IntegerField()
    login_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_answer'


class SuitGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    papers = models.ForeignKey(QuestionPapers, models.DO_NOTHING, blank=True, null=True)
    group_type = models.IntegerField(blank=True, null=True)
    content = models.IntegerField(blank=True, null=True)
    person_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'suit_group'


class TComment(models.Model):
    commentid = models.AutoField(db_column='commentId', primary_key=True)  # Field name made lowercase.
    newsid = models.IntegerField(db_column='newsId', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=200, blank=True, null=True)
    userip = models.CharField(db_column='userIP', max_length=40, blank=True, null=True)  # Field name made lowercase.
    commentdate = models.DateTimeField(db_column='commentDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_comment'


class TLink(models.Model):
    linkid = models.AutoField(db_column='linkId', primary_key=True)  # Field name made lowercase.
    linkname = models.CharField(db_column='linkName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    linkurl = models.CharField(db_column='linkUrl', max_length=40, blank=True, null=True)  # Field name made lowercase.
    linkemail = models.CharField(db_column='linkEmail', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='orderNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_link'


class TNews(models.Model):
    newsid = models.AutoField(db_column='newsId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=40, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    publishdate = models.DateTimeField(db_column='publishDate', blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(max_length=20, blank=True, null=True)
    typeid = models.IntegerField(db_column='typeId', blank=True, null=True)  # Field name made lowercase.
    click = models.IntegerField(blank=True, null=True)
    ishead = models.IntegerField(db_column='isHead', blank=True, null=True)  # Field name made lowercase.
    isimage = models.IntegerField(db_column='isImage', blank=True, null=True)  # Field name made lowercase.
    imagename = models.CharField(db_column='imageName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ishot = models.IntegerField(db_column='isHot', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_news'


class TNewsMenu(models.Model):
    pid = models.IntegerField(db_column='pId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_news_menu'


class TNewstype(models.Model):
    newstypeid = models.AutoField(db_column='newsTypeId', primary_key=True)  # Field name made lowercase.
    typename = models.CharField(db_column='typeName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_newstype'


class TUser(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'


class TimeLimit(models.Model):
    waterid = models.AutoField(primary_key=True)
    willingly = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    semester_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_limit'


class WinAnswer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    stu_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    option_value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'win_answer'


class WinQuestion(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_lib_id = models.IntegerField()
    question_content = models.CharField(max_length=255, blank=True, null=True)
    question_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'win_question'


class WinQuestionLib(models.Model):
    lib_id = models.AutoField(primary_key=True)
    lib_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'win_question_lib'
