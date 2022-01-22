#접속
mysql -u root -p

#데이터베이스 스키마 생성
create database Hackphaistus;

#스키마 선택
use Hackphaistus;

#테이블 생성
create table ratio(
id int not null auto_increment primary key ,
standard_feature varchar(100) not null,
target_feature varchar(100) not null,
standard_ratio int not null,
target_ratio float(3,1) not null,
updateDate DATETIME DEFAULT CURRENT_TIMESTAMP,
createDate DATETIME not null
);

insert into ratio(standard_feature,target_feature,standard_ratio,target_ratio,createDate) values ('eyes','cheekbones',1,3.7,'2022-01-13 15:00:00');
insert into ratio(standard_feature,target_feature,standard_ratio,target_ratio,createDate) values ('philanthropy','chin',1,2.0,'2022-01-13 15:00:00');
insert into ratio(standard_feature,target_feature,standard_ratio,target_ratio,createDate) values ('upperlip','lowerlip',1,1.5,'2022-01-13 15:00:00');
insert into ratio(standard_feature,target_feature,standard_ratio,target_ratio,createDate) values ('lips','jaw',1,2.5,'2022-01-13 15:00:00');
insert into ratio(standard_feature,target_feature,standard_ratio,target_ratio,createDate) values ('eyebrowX','eyebrowY',1,5.2,'2022-01-13 15:00:00');




# 지혜 매력 통솔력 열정 사회성 신뢰도
create table abilities(
id int not null auto_increment primary key,
ratio_id int not null,
ratio_type int, #수정
wisdom int,
charming int,
leadership int,
passion int,
socialskill int,
credit int,
updateDate DATETIME DEFAULT CURRENT_TIMESTAMP,
createDate DATETIME not null,
FOREIGN KEY (ratio_id) REFERENCES ratio(id)
);


# 미간
insert into abilities(ratio_id,ratio_type,wisdom,charming,leadership,passion,socialskill,credit,createDate) values (1,1,5,2,-6,-5,2,9,'2022-01-13 15:00:00');
insert into abilities(ratio_id,ratio_type,wisdom,charming,leadership,passion,socialskill,credit,createDate) values (1,2,6,3,1,2,2,0,'2022-01-13 15:00:00');
insert into abilities(ratio_id,ratio_type,wisdom,charming,leadership,passion,socialskill,credit,createDate) values (1,3,10,9,7,8,2,-6,'2022-01-13 15:00:00');

# 인중 턱
insert into abilities(ratio_id,ratio_type,wisdom,charming,leadership,passion,socialskill,credit,createDate) values (2,1,-5,-6,-4,10,10,-10,'2022-01-13 15:00:00');
insert into abilities(ratio_id,ratio_type,wisdom,charming,leadership,passion,socialskill,credit,createDate) values (2,2,5,10,0,0,5,3,'2022-01-13 15:00:00');
insert into abilities(ratio_id,ratio_type,wisdom,charming,leadership,passion,socialskill,credit,createDate) values (2,3,10,7,4,-8,8,10,'2022-01-13 15:00:00');

# 윗입술아랫입술
insert into abilities(ratio_id,ratio_type,wisdom,charming,leadership,passion,socialskill,credit,createDate) values (3,1,2,3,4,5,5,5,'2022-01-13 15:00:00');
insert into abilities(ratio_id,ratio_type,wisdom,charming,leadership,passion,socialskill,credit,createDate) values (3,2,6,8,-8,-2,10,10,'2022-01-13 15:00:00');

# 입술 턱
insert into abilities(ratio_id,ratio_type,wisdom,charming,leadership,passion,socialskill,credit,createDate) values (4,1,9,10,10,10,10,8,'2022-01-13 15:00:00');
insert into abilities(ratio_id,ratio_type,wisdom,charming,leadership,passion,socialskill,credit,createDate) values (4,2,6,-4,-4,5,5,6,'2022-01-13 15:00:00');

#눈썹 가로 세로
insert into abilities(ratio_id,ratio_type,wisdom,charming,leadership,passion,socialskill,credit,createDate) values (5,1,2,9,8,2,9,3,'2022-01-13 15:00:00');
insert into abilities(ratio_id,ratio_type,wisdom,charming,leadership,passion,socialskill,credit,createDate) values (5,2,8,-2,3,6,1,9,'2022-01-13 15:00:00');


# 결과값 저장
create table results(
id int not null auto_increment primary key,
task_id int not null,
wisdom int,
charming int,
leadership int,
passion int,
socialskill int,
credit int,
s3url varchar(100),
createDate DATETIME DEFAULT CURRENT_TIMESTAMP
);

# docker exec -it mysql-con bash