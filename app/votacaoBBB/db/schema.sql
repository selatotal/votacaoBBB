drop table if exists participants;

create table participants (
	id integer primary key,
	name text not null,
	votes integer
);

drop table if exists votings;

create table votings (
	id integer primary key,
	participant1_id integer not null,
	participant2_id integer not null,
	finish_date text not null,
	foreign key(participant1_id) references participants(id),
	foreign key(participant2_id) references participants(id)
);

drop table if exists hour_votings;

create table hour_votings (
    id integer primary key autoincrement,
    date_hour text not null,
    participant1_votes integer not null,
    participant2_votes integer not null
);

insert into participants values (1, 'Participante 1', 0);
insert into participants values (2, 'Participante 2', 0);

insert into votings values (1, 1, 2, '20150530101000');
