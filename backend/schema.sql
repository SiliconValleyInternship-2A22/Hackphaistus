#접속
mysql -u root -p

#데이터베이스 스키마 생성
create database Hackphaistus;

#스키마 선택
use Hackphaistus;

#테이블 생성

create table ratio(
idx int not null auto_increment primary key ,
feature1 varchar(30) not null,
feature2 varchar(30) not null,
ratio1 int,
ratio2 float(3,1) not null
);

insert into ratio(feature1,feature2,ratio1,ratio2) values ('eyes','cheekbones',1,3.7);
insert into ratio(feature1,feature2,ratio1,ratio2) values ('philanthropy','chin',1,2.0);
insert into ratio(feature1,feature2,ratio1,ratio2) values ('upperlip','lowerlip',1,1.5);
insert into ratio(feature1,feature2,ratio1,ratio2) values ('lips','jaw',1,2.5);
insert into ratio(feature1,feature2,ratio1,ratio2) values ('eyebrowX','eyebrowY',1,5.2);

# 지혜 매력 통솔력 열정 사회성 신뢰도

create table abilities(
idx int not null auto_increment primary key,
ratio_id int not null,
ver int,
wisdom int,
charming int,
leadership int,
passion int,
socialskill int,
credit int,
FOREIGN KEY (ratio_id) REFERENCES ratio(idx)
);


# 미간
insert into abilities(ratio_id,ver,wisdom,charming,leadership,passion,socialskill,credit) values (1,1,5,2,-6,-5,2,9);
insert into abilities(ratio_id,ver,wisdom,charming,leadership,passion,socialskill,credit) values (1,2,6,3,1,2,2,0);
insert into abilities(ratio_id,ver,wisdom,charming,leadership,passion,socialskill,credit) values (1,3,10,9,7,8,2,-6);

# 인중 턱
insert into abilities(ratio_id,ver,wisdom,charming,leadership,passion,socialskill,credit) values (2,1,-5,-6,-4,10,10,-10);
insert into abilities(ratio_id,ver,wisdom,charming,leadership,passion,socialskill,credit) values (2,2,5,10,0,0,5,3);
insert into abilities(ratio_id,ver,wisdom,charming,leadership,passion,socialskill,credit) values (2,3,10,7,4,-8,8,10);

# 윗입술아랫입술
insert into abilities(ratio_id,ver,wisdom,charming,leadership,passion,socialskill,credit) values (3,1,2,3,4,5,5,5);
insert into abilities(ratio_id,ver,wisdom,charming,leadership,passion,socialskill,credit) values (3,2,6,8,-8,-2,10,10);

# 입술 턱
insert into abilities(ratio_id,ver,wisdom,charming,leadership,passion,socialskill,credit) values (4,1,9,10,10,10,10,8);
insert into abilities(ratio_id,ver,wisdom,charming,leadership,passion,socialskill,credit) values (4,2,6,-4,-4,5,5,6);

#눈썹 가로 세로
insert into abilities(ratio_id,ver,wisdom,charming,leadership,passion,socialskill,credit) values (5,1,2,9,8,2,9,3);
insert into abilities(ratio_id,ver,wisdom,charming,leadership,passion,socialskill,credit) values (5,1,8,-2,3,6,1,9);
