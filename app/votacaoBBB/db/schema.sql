drop table if exists participants;

create table participants (
	id integer primary key,
	name text not null,
	votes integer
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
