\c shopping

insert into customer values (0,'Test','test','test@test.com','8082495533','1994-07-11','81308 Grayhawk Avenue', '52 Kropf Road');
insert into customer values (1, 'Taddeo Aldersea', 'YhxiNqYCs', 'taldersea0@noaa.gov', '6007773273', '1994-07-11', '81308 Grayhawk Avenue', '52 Kropf Road');
insert into customer values (2, 'Carleton Sekulla', 'jVlFJuBErZ', 'csekulla1@phpbb.com', '8082495533', '1996-10-09', '791 Farmco Terrace', '88 Oakridge Parkway');
insert into customer values (3, 'Correy McConville', 'fvy8LF', 'cmcconville2@nature.com', '5246283383', '1998-01-05', '54 Di Loreto Plaza', '270 Bartillon Way');
insert into customer values (4, 'Flss Dongate', '1C500k7Of5j', 'fdongate3@china.com.cn', '5054492575', '1996-07-16', '02819 Heffernan Court', '79 Twin Pines Place');
insert into customer values (5, 'Broderick Preston', 'M7oUQw7O6eMb', 'bpreston4@rambler.ru', '4819256685', '1997-10-15', '447 Dennis Alley', '7 Westridge Plaza');
insert into customer values (6, 'Vina Hammer', 'T4cgPDs', 'vhammer5@utexas.edu', '5169715969', '2001-07-22', '91111 Pleasure Point', '28 Amoth Avenue');
insert into customer values (7, 'Catha Natwick', 'ylWekF9uMcW', 'cnatwick6@nationalgeographic.com', '3167215176', '2003-04-13', '34 Waubesa Parkway', '71397 Morningstar Road');
insert into customer values (8, 'Miguelita Aspling', 'shl9bOz74', 'maspling7@house.gov', '2373430425', '1997-09-24', '925 Chive Road', '418 Victoria Center');
insert into customer values (9, 'Gwenette Rove', 'xZ5T6WD', 'grove8@privacy.gov.au', '8833436581', '1997-09-24', '12 Dakota Lane', '96877 Scofield Center');
insert into customer values (10, 'Randell McArley', 'ruwr6R', 'rmcarley9@java.com', '9652444117', '1997-05-25', '9 Hollow Ridge Crossing', '0 Prentice Hill');

insert into transaction values ('89-295-3455', 0, 'credit card', 1);
insert into transaction values ('50-800-7145', 0, 'cash', 2);
insert into transaction values ('99-354-0299', 0, 'debit card', 3);
insert into transaction values ('67-186-4509', 0, 'cash', 4);
insert into transaction values ('09-406-4340', 0, 'credit card', 5);
insert into transaction values ('95-700-8392', 0, 'cash', 6);
insert into transaction values ('19-413-6789', 0, 'debit card', 7);
insert into transaction values ('69-512-9040', 0, 'cash', 8);
insert into transaction values ('92-769-6257', 0, 'debit card', 9);
insert into transaction values ('77-326-9947', 0, 'credit card', 10);

insert into brand values (1, 'Darbee Kunkel', 'http://sphinn.com');
insert into brand values (2, 'Katina Cordero', 'http://icio.us');
insert into brand values (3, 'Cass McNickle', 'https://europa.eu');
insert into brand values (4, 'Carrol Brill', 'http://msn.com');
insert into brand values (5, 'Levi Bursnell', 'https://china.com.cn');
insert into brand values (6, 'Malvina Grishunin', 'https://blogspot.com');
insert into brand values (7, 'Davon Klainer', 'http://parallels.com');
insert into brand values (8, 'Estella Arnhold', 'http://ft.com');
insert into brand values (9, 'Bryn Antoinet', 'https://fda.gov');
insert into brand values (10, 'Perren Arends', 'http://indiatimes.com');

insert into product values (1, 'Marmaduke Eagland', 'Nulla tempus.', 2243, 1);
insert into product values (2, 'Elora Petriello', 'Cras in purus eu ', 3267, 2);
insert into product values (3, 'Adler Spurway', 'mattis nibh ligula nec sem.', 1538, 3);
insert into product values (4, 'Nissie Ongin', 'Proin risus. Praesent lectus.', 4170, 4);
insert into product values (5, 'Rickard Hassey', 'Sed vel enim sit ', 3631, 5);
insert into product values (6, 'Ariel Ebertz', 'Maecenas tincidunt.', 2200, 6);
insert into product values (7, 'Valeda Donson', 'Integer ac neque.', 1568, 7);
insert into product values (8, 'Patricia Alyutin', 'Morbi porttitor lorem id ligula.', 3906, 8);
insert into product values (9, 'Luelle Danilin', 'Donec ut mauris eget ', 1056, 9);
insert into product values (10, 'Cullan Hardwidge', 'Nam nulla.', 4604, 10);

insert into customer_order values (1, 8);
insert into customer_order values (1, 6);
insert into customer_order values (1, 10);
insert into customer_order values (1, 5);

insert into customer_order values (2, 3);

insert into customer_order values (3, 4);

insert into customer_order values (4, 4);
insert into customer_order values (4, 3);
insert into customer_order values (4, 2);

insert into customer_order values (5, 7);

insert into customer_order values (6, 5);
insert into customer_order values (6, 8);
insert into customer_order values (6, 2);

insert into customer_order values (7, 8);
insert into customer_order values (7, 2);
insert into customer_order values (7, 7);
insert into customer_order values (7, 3);

insert into customer_order values (8, 3);
insert into customer_order values (8, 2);
insert into customer_order values (8, 8);

insert into customer_order values (9, 4);

insert into customer_order values (10, 1);
insert into customer_order values (10, 8);
insert into customer_order values (10, 10);

insert into review values ('2021-06-28', 3, 'test14', 1, 10);
insert into review values ('2020-12-21', 2, 'test13', 2,9);
insert into review values ('2021-04-30', 1, 'test12', 3, 8);
insert into review values ('2021-02-19', 2, 'test11', 4, 7);
insert into review values ('2021-03-26', 5, 'test10', 5, 6);
insert into review values ('2021-4-12', 2, 'test9', 6, 5);
insert into review values ('2021-01-25', 5, 'test8', 7, 4);
insert into review values ('2021-06-10', 5, 'test7', 8, 3);
insert into review values ('2020-05-16', 4, 'test6', 9, 2);
insert into review values ('2021-05-27', 5, 'test5.', 10, 1);
insert into review values ('2021-05-28', 4, 'test1', 1, 1);
insert into review values ('2021-05-29', 4, 'test2', 9, 1);
insert into review values ('2021-05-30', 2, 'test3', 7, 1);
insert into review values ('2021-05-01', 3, 'test4', 4, 1);

insert into supplier values (1, 'Charles Pople', 'http://mit.edu', '6976573751', 'cpople0@europa.eu');
insert into supplier values (2, 'Tadeas McIver', 'https://archive.org', '9088550777', 'tmciver1@ted.com');
insert into supplier values (3, 'Merissa Rasmus', 'https://vkontakte.ru', '1088374509', 'mrasmus2@ezinearticles.com');
insert into supplier values (4, 'Karl Baitson', 'http://sogou.com', '2026649720', 'kbaitson3@time.com');
insert into supplier values (5, 'Thurstan Narramore', 'https://surveymonkey.com', '7575055757', 'tnarramore4@booking.com');
insert into supplier values (6, 'Morton Guenther', 'http://angelfire.com', '3147869904', 'mguenther5@comsenz.com');
insert into supplier values (7, 'Jobina Sabin', 'http://last.fm', '2795367503', 'jsabin6@wix.com');
insert into supplier values (8, 'Leoine Capeloff', 'http://livejournal.com', '4874502804', 'lcapeloff7@blogspot.com');
insert into supplier values (9, 'Hinda Deamer', 'https://flickr.com', '4733528041', 'hdeamer8@youku.com');
insert into supplier values (10, 'Mohandis Yakuntsov', 'http://addthis.com', '8726583260', 'myakuntsov9@flickr.com');

insert into sold_by (brand_id, s_id) values (1, 10);
insert into sold_by (brand_id, s_id) values (2, 9);
insert into sold_by (brand_id, s_id) values (3, 8);
insert into sold_by (brand_id, s_id) values (4, 7);
insert into sold_by (brand_id, s_id) values (5, 6);
insert into sold_by (brand_id, s_id) values (6, 5);
insert into sold_by (brand_id, s_id) values (7, 4);
insert into sold_by (brand_id, s_id) values (8, 3);
insert into sold_by (brand_id, s_id) values (9, 2);
insert into sold_by (brand_id, s_id) values (10, 1);
