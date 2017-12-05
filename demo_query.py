

demo_query_title = {
        "demo1":"題目:查詢某位教師，例如，張三，的電話、出生年月日、性別、及照片。",
	"demo2":"題目:張三所開課的所有課程名稱、提供該課程的學院及修課人數。",
	"demo3": "題目:某一位學生，例如，李四，所屬之學院的名稱、院長之姓名、薪水等。"
}


demo_query = {
	"demo1":"SELECT Name, PhoneNum, Bdate, Sex, Photo FROM Teacher WHERE Ssn = 'Z123456789';",
	"demo2":"SELECT CourseName, Course.AName, Count(SNum) FROM Course, Take_Course WHERE TNum = 'Z123456789' AND CourseNum = CNum;",
	"demo3": "SELECT StudentName, AcademyName, Dean, Salary FROM Student, Academy, Teacher WHERE StudentNum = 33445566 AND Student.AName = AcademyName AND Dean = Teacher.Name;" 
}

