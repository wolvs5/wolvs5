Exercises 2: single table queries

question no 1:
select * from goal;
![Screenshot 2024-09-29 220149](https://github.com/user-attachments/assets/67cbe15d-f4e6-41d6-ae05-702cfbee6115)



Question 2:

select name from airport where iso_country ='FI';
![Screenshot 2024-09-29 220213](https://github.com/user-attachments/assets/7742ea5d-037f-4863-8fed-23c61a5e36dc)

Question 3:

select name from airport where iso_country ='FI' group by name;
![Screenshot 2024-09-29 220238](https://github.com/user-attachments/assets/21e306c0-5c24-451b-bf9f-1277f5475f2a)

Question 4:

select name, type from airport where iso_country ='FI' group by type, name;
![Screenshot 2024-09-29 220303](https://github.com/user-attachments/assets/c59cf608-691a-4ee7-b3e5-9cc26659e5ad)

Question 5:

select name from country where name like 'f%';
![Screenshot 2024-09-29 220324](https://github.com/user-attachments/assets/75f9cf0d-ee26-4d25-b276-001f010316d7)

Question 6:

Select name as name from country where name like '%f%';
![image](https://github.com/user-attachments/assets/3ba16910-2122-401b-9d3b-98081f098987)


Question 7:

select location from game where screen_name = "Vesa";
![Screenshot 2024-09-29 220353](https://github.com/user-attachments/assets/cf90c9ec-c3a8-4983-a037-38c7f204c65d)

Question 8:

select co2_consumed from game where screen_name = "Ilkka";
![Screenshot 2024-09-29 220408](https://github.com/user-attachments/assets/b1808660-2d40-488f-8e93-38af914dc690)

Question 9:

select distinct game.co2_budget from game;
![Screenshot 2024-09-29 220425](https://github.com/user-attachments/assets/3e96a838-c06b-417b-85ad-353d051bb321)

Question 10:

select screen_name, co2_budget, co2_consumed, @co2_left:=co2_budget-co2_consumed as co2_left from game
where screen_name = 'Ilkka';
![Screenshot 2024-09-29 220709](https://github.com/user-attachments/assets/b1d44b5e-b209-4d90-b3f1-c10dc30e44bd)

Exercises 3: Multiple Table Queries
Question 1:

select country.name as "country name", airport.name as "airport name" from airport, country where airport.iso_country = country.iso_country and country.name = "Iceland";
![Screenshot 2024-09-29 220753](https://github.com/user-attachments/assets/c4e3ae40-8bbc-4012-85c2-b196a007a630)

Question 2:

select airport.name as "airport name" from airport where airport.type = 'large_airport' and iso_country = 'FR';
![Screenshot 2024-09-29 220941](https://github.com/user-attachments/assets/d4d17068-b9fc-4c51-a272-fc1a5b6ed33d)

Question 3:

select country.name as 'country_name', airport.name as 'airport name' from airport, country where airport.iso_country = country.iso_country and country.continent = 'AN';
![Screenshot 2024-09-29 221017](https://github.com/user-attachments/assets/7b800d62-d2eb-42f6-903d-1441bfb08770)

Question 4:

select airport.elevation_ft from airport, game where game.location = airport.ident and game.screen_name = 'Heini';
![Screenshot 2024-09-29 221054](https://github.com/user-attachments/assets/cf34b8e1-9484-40ca-8621-4cfcec4849ed)

Question 5:

select airport.elevation_ft * 0.3048 as 'elevation_m' from airport, game where game.location = airport.ident and game.screen_name = 'Heini';
![Screenshot 2024-09-29 221133](https://github.com/user-attachments/assets/17dedee6-bf5f-4a17-8ac1-1339c079086f)

Question 6:

select name from game, airport where airport.ident = game.location and game.screen_name = 'Ilkka';
![Screenshot 2024-09-29 221208](https://github.com/user-attachments/assets/0def2367-3982-4ac3-83b9-c03292105b3a)


Question 7:

select country.name from airport, game, country where game.screen_name = 'Ilkka' and game.location = airport.ident and airport.iso_country = country.iso_country;
![Screenshot 2024-09-29 221242](https://github.com/user-attachments/assets/41fecc06-9792-4ec6-8539-b0e30c9a521a)

Question 8:

select goal.name from goal, goal_reached, game where game.screen_name = 'Heini' and game.id = goal_reached.game_id and goal_reached.goal_id = goal.id;
![image](https://github.com/user-attachments/assets/8e4970ba-d808-421a-99cc-42790bd1dab0)

Question 9:

select airport.name from goal, airport, game, goal_reached where game.screen_name = 'Ilkka' and game.location = airport.ident and game.id = goal_reached.game_id and goal_reached.goal_id = goal.id and goal.name = 'CLOUDS';
![image](https://github.com/user-attachments/assets/1af96d3a-b37a-448b-9854-f0a607f43da9)

Question 10

select country.name from goal, airport, game, goal_reached, country where country.iso_country = airport.iso_country and game.screen_name = 'Ilkka' and game.location = airport.ident and game.id = goal_reached.game_id and goal_reached.goal_id = goal.id and goal.name = 'CLOUDS';
![image](https://github.com/user-attachments/assets/2f9f01a8-152d-4572-ac3a-bfc53ce84d71)


Exercises 4: Join
Question 1:
select country.name as 'country name', airport.name as 'airport.name' from country join airport on country.iso_country = airport.iso_country where country.iso_country = 'FI' and airport.scheduled_service = 'yes';
![Screenshot 2024-09-29 222339](https://github.com/user-attachments/assets/df64831a-5997-4d7a-a30a-87b17ae34252)


Question 2:

select game.screen_name, airport.name from game join airport on game.location = airport.ident;
![Screenshot 2024-09-29 222405](https://github.com/user-attachments/assets/64ac72d2-fe0d-46d1-98ae-7f47294f6245)


Question 3:

select game.screen_name, country.name from game join airport on game.location = airport.ident join country on airport.iso_country = country.iso_country;
![Screenshot 2024-09-29 222446](https://github.com/user-attachments/assets/62c97658-af7f-4f85-b9ac-12ee6e2cffe6)


Question 4:

select airport.name, game.screen_name from airport left join game on airport.ident = game.location where airport.name like '%Hels%';
![Screenshot 2024-09-29 222533](https://github.com/user-attachments/assets/919afc8e-e00a-4817-b45c-58b2d1b63cc3)



Question 5:

select goal.name, game.screen_name from goal left join goal_reached on goal.id = goal_reached.goal_id left join game on goal_reached.game_id = game.id;
![Screenshot 2024-09-29 222612](https://github.com/user-attachments/assets/cbdbccee-2285-4ecb-a198-aa01fbae2273)


Exercises 5: Subqueries
Question 1:

select country.name from country where country.iso_country in ( select airport.iso_country from airport where airport.name like 'Satsuma%' );
![Screenshot 2024-09-29 222750](https://github.com/user-attachments/assets/646025e5-2a6c-49f4-95c7-baf1781abf6a)

Question 2:

select airport.name from airport where airport.iso_country in ( select country.iso_country from country where country.name = 'Monaco' );
![image](https://github.com/user-attachments/assets/cc726665-7b00-46b0-b468-496ca993b676)



Question 3:

select game.screen_name from game where game.id in ( select goal_reached.game_id from goal_reached where goal_reached.goal_id in ( select goal.id from goal where goal.name = 'CLOUDS' ) );
![image](https://github.com/user-attachments/assets/29c4b09b-9853-4fda-9fd8-93822aeb01eb)



Question 4:

select country.name from country where country.iso_country not in ( select airport.iso_country from airport );

![Screenshot 2024-09-29 230915](https://github.com/user-attachments/assets/1a0ea99f-912e-41ff-88e7-5188a8ef663e)

Question 5:

select goal.name from goal where goal.id not in ( select goal_reached.goal_id from goal_reached where goal_reached.game_id in ( select game.id from game where game.screen_name = 'Heini' ) );
![image](https://github.com/user-attachments/assets/52f130e7-1c51-45fb-b94b-ceb32ede032e)


Exercises 6: Aggregate Queries
Question 1:

select max(elevation_ft) from airport;
![Screenshot 2024-09-29 230737](https://github.com/user-attachments/assets/bb6bdf44-605f-45fb-9346-9d55debdf1ae)
![Screenshot 2024-09-29 231253](https://github.com/user-attachments/assets/ef04e606-9eff-4970-95fa-79ad8f291394)

Question 2:

select continent, count(*) from country group by continent;
![Screenshot 2024-09-29 231328](https://github.com/user-attachments/assets/5787b490-96d8-406f-bf2b-bab94a08d90d)

Question 3:

select game.screen_name, count(*) from game right join goal_reached on game.id = goal_reached.game_id group by screen_name;
![Screenshot 2024-09-29 231424](https://github.com/user-attachments/assets/0afa29e7-7cc1-459e-a107-deb44e48ddbf)

Question 4:

select game.screen_name from game where game.co2_consumed in ( select min(game.co2_consumed) from game );
![Screenshot 2024-09-29 232138](https://github.com/user-attachments/assets/ae12ad9c-b3cb-4412-abf9-ea9f5e242f30)
Question 5:

select country.name, count() from airport left join country on airport.iso_country = country.iso_country group by country.iso_country order by count() desc limit 50;
![Screenshot 2024-09-29 232138](https://github.com/user-attachments/assets/171658cb-e027-4b54-bd90-a5f41e7cbc36)














