def insertAcademies(con, academies):
    con.execute(academies.insert(), AcademyNum=10000000, AcademyName='魔法學院', OfficeAddress='魔法森林圖書館2樓',Dean='漢斯',DServing=datetime.strptime('19960905','%Y%m%d'))
    con.execute(academies.insert(), AcademyNum=20000000, AcademyName='戰士學院', OfficeAddress='勇士之村祭壇',Dean='甘道夫',DServing=datetime.strptime('19991030','%Y%m%d'))
    con.execute(academies.insert(), AcademyNum=30000000, AcademyName='弓箭學院', OfficeAddress='弓箭手村訓練中心',Dean='勒苟拉斯',DServing=datetime.strptime('19870311','%Y%m%d'))
    con.execute(academies.insert(), AcademyNum=40000000, AcademyName='忍術學院', OfficeAddress='伊賀村',Dean='哈特利',DServing=datetime.strptime('20050621','%Y%m%d'))

def insertTeachers(con, teachers):
    gandolf = read_file('./static/img/gandolf.png')
    hans = read_file('./static/img/hans.png')
    legolas = read_file('./static/img/legolas.png')
    hattori = read_file('./static/img/hattori.png')
    dbteacher = read_file('./static/img/teacher.png')
    con.execute(teachers.insert(), Ssn='A123456789', Name='甘道夫', Bdate=datetime.strptime('19100610','%Y%m%d'),
            Photo=gandolf, Address='勇士之村12號', OfficeAddress='勇士之村祭壇', Sex='男', Salary=300000, PhoneNum='0987654321', Class='教授', Expertise='劍術',AName='戰士學院')

    con.execute(teachers.insert(), Ssn='B123456789', Name='漢斯', Bdate=datetime.strptime('19010731','%Y%m%d'),
            Photo=hans, Address='魔法森林1號', OfficeAddress='魔法森林圖書館2樓', Sex='男', Salary=350000, PhoneNum='0912345678', Class='教授', Expertise='爆裂魔法',AName='魔法學院')

    con.execute(teachers.insert(), Ssn='C123456789', Name='勒苟拉斯', Bdate=datetime.strptime('18870120','%Y%m%d'),
            Photo=legolas, Address='弓箭手村5號', OfficeAddress='弓箭手村訓練中心', Sex='男', Salary=310000, PhoneNum='0945789654', Class='教授', Expertise='長弓',AName='弓箭學院')

    con.execute(teachers.insert(), Ssn='D123456789', Name='哈特利', Bdate=datetime.strptime('20100521','%Y%m%d'),
            Photo=hattori, Address='伊賀村三丁目', OfficeAddress='伊賀村', Sex='男', Salary=150000 ,PhoneNum='0932165498', Class='副教授', Expertise='你逆之術',AName='忍術學院')
    
    con.execute(teachers.insert(), Ssn='Z123456789', Name='懌芳呂', Bdate=datetime.strptime('19690121','%Y%m%d'),
            Photo=dbteacher, Address='台中市', OfficeAddress='超大智慧大樓422', Sex='男', Salary=500000, PhoneNum='0912456723', Class='教授', Expertise='帥氣與智慧',AName='魔法學院')

def insertStudents(con, students):
    wucheng = read_file('./static/img/wucheng.png')
    linwei = read_file('./static/img/linwei.png')
    boning = read_file('./static/img/boning.png')
    panhu = read_file('./static/img/panhu.png')

    con.execute(students.insert(), StudentNum=11223344, StudentName='翰承吳', BDATE=datetime.strptime('19970803','%Y%m%d'),
                Photo=wucheng, Address='台中市1號' , Sex='男',Email='11223344@whu.edu.tw', PhoneNum='0973478946', AName='忍術學院')

    con.execute(students.insert(), StudentNum=22334455, StudentName='佐威林', BDATE=datetime.strptime('19970630','%Y%m%d'),
                Photo=linwei, Address='台中市2號' , Sex='男',Email='22334455@whu.edu.tw', PhoneNum='0984572685', AName='弓箭學院')

    con.execute(students.insert(), StudentNum=33445566, StudentName='寧柏陳', BDATE=datetime.strptime('19960915','%Y%m%d'),
                Photo=boning, Address='台中市3號' , Sex='男',Email='33445566@whu.edu.tw', PhoneNum='0957649521', AName='魔法學院')

    con.execute(students.insert(), StudentNum=44556677, StudentName='虎胖', BDATE=datetime.strptime('20030410','%Y%m%d'),
                Photo=panhu, Address='台中市4號' , Sex='男',Email='44556677@whu.edu.tw', PhoneNum='0965359865', AName='戰士學院')


def insertCourses(con, courses):
    con.execute(courses.insert(), CourseNum=1234, CourseName='魔法傳教' , AcademicYear='105學年度',Semester='第二學期', AName='魔法學院')
    con.execute(courses.insert(), CourseNum=1324, CourseName='JAVA魔法應用' , AcademicYear='104學年度',Semester='第二學期', AName='魔法學院')
    con.execute(courses.insert(), CourseNum=1454, CourseName='資料庫' , AcademicYear='105學年度',Semester='第一學期', AName='魔法學院')

    con.execute(courses.insert(), CourseNum=2234, CourseName='勞作教育' , AcademicYear='104學年度',Semester='第一學期', AName='戰士學院')
    con.execute(courses.insert(), CourseNum=2424, CourseName='揍人基礎' , AcademicYear='104學年度',Semester='第一學期', AName='戰士學院')
    con.execute(courses.insert(), CourseNum=2745, CourseName='進階劍術' , AcademicYear='105學年度',Semester='第二學期', AName='戰士學院')

    con.execute(courses.insert(), CourseNum=3354, CourseName='弓箭基礎' , AcademicYear='104學年度',Semester='第二學期', AName='弓箭學院')
    con.execute(courses.insert(), CourseNum=3124, CourseName='弓箭進階' , AcademicYear='105學年度',Semester='第一學期', AName='弓箭學院')

    con.execute(courses.insert(), CourseNum=4244, CourseName='你逆之術基礎' , AcademicYear='104學年度',Semester='第一學期', AName='忍術學院')
    con.execute(courses.insert(), CourseNum=4824, CourseName='你逆之術進階' , AcademicYear='105學年度',Semester='第二學期', AName='忍術學院')

def insertTCourse(con, tkcourse):
    con.execute(tcourse.insert(), SNum=33445566,CNum=1234, TNum='B123456789' ,Score=87, AName='魔法學院')
    con.execute(tcourse.insert(), SNum=33445566,CNum=1324, TNum='B123456789' ,Score=59, AName='魔法學院')
    con.execute(tcourse.insert(), SNum=33445566,CNum=2234, TNum='A123456789' ,Score=59, AName='戰士學院')
    con.execute(tcourse.insert(), SNum=33445566,CNum=1454, TNum='Z123456789' ,Score=95, AName='魔法學院')


    con.execute(tcourse.insert(), SNum=11223344,CNum=1454, TNum='Z123456789' ,Score=95, AName='魔法學院')
    con.execute(tcourse.insert(), SNum=11223344,CNum=4244, TNum='D123456789' ,Score=89, AName='忍術學院')
    con.execute(tcourse.insert(), SNum=11223344,CNum=4824, TNum='D123456789' ,Score=90, AName='忍術學院')
    con.execute(tcourse.insert(), SNum=11223344,CNum=2234, TNum='A123456789' ,Score=75, AName='戰士學院')


    con.execute(tcourse.insert(), SNum=22334455,CNum=1454, TNum='Z123456789' ,Score=95, AName='魔法學院')
    con.execute(tcourse.insert(), SNum=22334455,CNum=3354, TNum='C123456789' ,Score=87, AName='弓箭學院')
    con.execute(tcourse.insert(), SNum=22334455,CNum=3124, TNum='C123456789' ,Score=87, AName='弓箭學院')
    con.execute(tcourse.insert(), SNum=22334455,CNum=2234, TNum='A123456789' ,Score=69, AName='戰士學院')

    con.execute(tcourse.insert(), SNum=44556677,CNum=2424, TNum='A123456789' ,Score=99, AName='戰士學院')
    con.execute(tcourse.insert(), SNum=44556677,CNum=2234, TNum='A123456789' ,Score=64, AName='戰士學院')
