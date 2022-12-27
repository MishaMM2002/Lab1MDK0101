create table if not exists Performance(
	id integer primary key autoincrement,
	datetime_start varchar(256) not null,
	playID integer not null,
	hallID integer no null,
	foreign key (playID) references Play(id),
	foreign key (hallID) references Hall(id)
);

create table if not exists Play(
	id integer primary key autoincrement,
	name varchar(256) not null,
	typeID integer not null,
	foreign key (typeID) references TypeOfPlay(id)
);

create table if not exists TypeOfPlay(
	id integer primary key autoincrement,
	name varchar(256) not null
);

create table if not exists Hall(
	id integer primary key autoincrement,
	number integer not null,
	capacity integer not null
);

create table if not exists User(
	id integer primary key autoincrement,
	phone varchar(12) not null unique,
    name varchar(256) not null,
    password varchar(256) not null,
    post varchar(256) not null default "User"
);

create table if not exists Ticket(
    id integer primary key autoincrement,
    performanceID integer not null,
    userID integer not null,
    foreign key (performanceID) references Performance(id),
    foreign key (userID) references User(id)
);