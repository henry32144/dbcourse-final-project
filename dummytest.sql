INSERT INTO Academy(AcademyNum, AcademyName, OfficeAddress)
VALUES (11111111, "魔法學院", "魔法森林"),
		(22222222, "戰士學院", "勇士之村");
		(33333333, "弓箭學院", "弓箭手村");

INSERT INTO Teacher(Ssn, Name, Bdate, Photo, Address, OfficeAddress, 
					Sex, Salary, PhoneNum, Class, Expertise, AName)
VALUES ("A123456789", "漢斯", "1111-11-11", "1535136616168616", "魔法森林21號", "大圖書館",
		"男", 100000, 12356789, "導師", "時間魔法", "魔法學院");
		("B14864284", "赫麗娜", "0911-05-21", "1535136616168616", "弓箭手村01號", "訓練中心",
		"女", 90000, 21346789, "導師", "長弓", "弓箭手村");

UPDATE Academy SET Dean="漢斯", DServing="1219-04-01" WHERE AcademyNum=11111111;