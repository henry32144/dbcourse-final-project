CREATE TABLE Academy (
	AcademyNum 		INTEGER(8) PRIMARY KEY NOT NULL,
	AcademyName 	NVARCHAR(50) NOT NULL UNIQUE,
	OfficeAddress 	NVARCHAR(255) ,
	Dean			NVARCHAR(50) ,
	DServing 		DATE,
	CONSTRAINT Dean_SUPER_ForiegnKey 
		FOREIGN KEY (Dean) REFERENCES Teacher(Name)
);


CREATE TABLE Teacher (
	Ssn 			CHAR(20) PRIMARY KEY NOT NULL,
	Name 			NVARCHAR(50) NOT NULL,
	Bdate 			DATE NOT NULL,
	Photo 			BLOB NOT NULL,
	Address 		NVARCHAR(255),
	OfficeAddress 	NVARCHAR(255),
	Sex 			NCHAR,
	Salary			INTEGER(10),
	PhoneNum 		CHAR(16),
	Class 			NVARCHAR(8),
	Expertise 		NVARCHAR(50),
	AName 			NVARCHAR(50),
	CONSTRAINT T_AcademyName_SUPER_ForiegnKey
		FOREIGN KEY (AName) REFERENCES Academy(AcademyName)
);

CREATE TABLE Course (
	CourseNum 		INTEGER(4) PRIMARY KEY NOT NULL,
	CourseName		NVARCHAR(50) NOT NULL UNIQUE,
	AcademicYear 	NVARCHAR(8),
	Semester 		NVARCHAR(4),
	AName  			NVARCHAR(50),
	CONSTRAINT C_AcademyName_SUPER_ForiegnKey
		FOREIGN KEY (AName) REFERENCES Academy(AcademyName)
);

CREATE TABLE Student (
	StudentNum  	INTEGER(8) PRIMARY KEY NOT NULL,
	StudentName 	NVARCHAR(50) NOT NULL,
	BDATE  			DATE NOT NULL,
	Sex  			NCHAR,
	Photo 			BLOB,
	Email  			VARCHAR(100),
	PhoneNum 		CHAR(16),
	Address  		NVARCHAR(255),
	AName 			NVARCHAR(50),
	CONSTRAINT S_AcademyName_SUPER_ForiegnKey
		FOREIGN KEY (AName) REFERENCES Academy(AcademyName)
);

CREATE TABLE Take_Course (
	SNum 			INTEGER(8) NOT NULL,
	CNum 			INTEGER(4)	NOT NULL,
	TNum 			CHAR(20) ,
	AName 			NVARCHAR(50),
	Score  			DECIMAL(3,2),
	PRIMARY KEY (SNum, CNum),
	FOREIGN KEY (SNum) REFERENCES Student(StudentNum),
	FOREIGN KEY (CNum) REFERENCES Course(CourseNum),
	FOREIGN KEY (TNum) REFERENCES Teacher(Ssn),
	FOREIGN KEY (AName) REFERENCES Academy(AcademyName)
);


