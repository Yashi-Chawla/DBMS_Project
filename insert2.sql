\c shopping
insert into customer values (1, 'Hermine Jacmar', 'Z9gtubmni', 'hjacmar0@ucla.edu', '4265173388', '2003-11-03');
insert into customer values (2, 'Verna Hadgraft', 'JfZG6a5', 'vhadgraft1@huffingtonpost.com', '1178089989', '2004-12-09');
insert into customer values (3, 'Linell Wederell', 'gcNFlaqOe', 'lwederell2@cornell.edu', '4782533085', '1998-02-3');
insert into customer values (4, 'Catlin Filchagin', '2zyyz4G', 'cfilchagin3@twitpic.com', '7692341640', '2004-05-06');
insert into customer values (5, 'Richie Mangeot', 'z1cZAQEV', 'rmangeot4@google.pl', '3971658219', '1998-10-7');
insert into customer values (6, 'Vickie Hellis', 'XaOkEg7OhLR', 'vhellis5@pen.io', '6474674901', '1996-10-25');
insert into customer values (7, 'Rafael Janecki', 'bcbRcv7yKzRy', 'rjanecki6@cdbaby.com', '5266682866', '1996-09-02');
insert into customer values (8, 'Sinclare Morena', 'SdzO5khw5', 'smorena7@miitbeian.gov.cn', '7218601087', '2001-08-29');
insert into customer values (9, 'Ragnar Abrahamian', 'lQoLB9x', 'rabrahamian8@ox.ac.uk', '4413363314', '2002-08-17');
insert into customer values (10, 'Mohandas O'' Byrne', 'MRZyqfNELA', 'mo9@ehow.com', '3818990634', '2003-11-17');



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
insert into product values (2, 'Elora Petriello', 'Cras in purus eu magna vulputate luctus.', 3267, 2);
insert into product values (3, 'Adler Spurway', 'Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.', 1538, 3);
insert into product values (4, 'Nissie Ongin', 'Proin risus. Praesent lectus.', 4170, 4);
insert into product values (5, 'Rickard Hassey', 'Sed vel enim sit amet nunc viverra dapibus.', 3631, 5);
insert into product values (6, 'Ariel Ebertz', 'Maecenas tincidunt lacus at velit.', 2200, 6);
insert into product values (7, 'Valeda Donson', 'Integer ac neque.', 1568, 7);
insert into product values (8, 'Patricia Alyutin', 'Morbi porttitor lorem id ligula.', 3906, 8);
insert into product values (9, 'Luelle Danilin', 'Aenean fermentum. Donec ut mauris eget massa tempor convallis.', 1056, 9);
insert into product values (10, 'Cullan Hardwidge', 'Nam nulla.', 4604, 10);

insert into cart values (1, 0, '56485 Corben Plaza', '91 Logan Park', '2021-08-03',0,10);
insert into cart values (2, 0, '995 Loomis Road', '3 Welch Point', '2021-09-22',0,9);
insert into cart values (3, 0, '702 Schiller Center', '633 Red Cloud Hill', '2021-01-21',0,8);
insert into cart values (4, 0, '31 Jenna Lane', '13 Ronald Regan Plaza', '2021-03-21',0,7);
insert into cart values (5, 0, '55487 Blaine Drive', '34355 Golf Parkway', '2021-09-24',0,6);
insert into cart values (6, 0, '34 Ronald Regan Trail', '88831 Commercial Trail', '2021-06-28',0,5);
insert into cart values (7, 0, '3 Prairieview Point', '5719 American Drive', '2021-01-23',0,4);
insert into cart values (8, 0, '76058 Di Loreto Terrace', '5 Monterey Circle', '2021-09-12',0,3);
insert into cart values (9, 0, '0 Gulseth Center', '3 Knutson Court', '2021-10-18',0,2);
insert into cart values (10,0, '41515 Lighthouse Bay Street', '0534 Lawn Trail', '2021-05-29',0,1);

insert into customer_order values (1, 8);
insert into customer_order values (1, 6);
insert into customer_order values (1, 10);
insert into customer_order values (1, 5);
insert into customer_order values (1, 10);

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

insert into review values ('2021-06-28', 3, 'Duis aliquam convallis nunc.', 1, 10);
insert into review values ('2020-12-21', 2, 'Fusce consequat. Nulla nisl.', 2,9);
insert into review values ('2021-04-30', 1, 'Sed vel enim sit amet nunc viverra dapibus.', 3, 8);
insert into review values ('2021-02-19', 2, 'Morbi quis tortor id nulla ultrices aliquet.', 4, 7);
insert into review values ('2021-03-26', 5, 'Cras pellentesque volutpat dui.', 5, 6);
insert into review values ('2021-4-12', 2, 'In est risus, auctor sed, tristique in, tempus sit amet, sem. Fusce consequat.', 6, 5);
insert into review values ('2021-01-25', 5, 'Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.', 7, 4);
insert into review values ('2021-06-10', 5, 'Vivamus vestibulum sagittis sapien.', 8, 3);
insert into review values ('2020-05-16', 4, 'Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue.', 9, 2);
insert into review values ('2021-05-27', 5, 'Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.', 10, 1);

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

select * from cart;