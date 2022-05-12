

--Question 3.a : Which drone ships has received the most successful successive landings by falcon 9 booster? List landing drone ships in order from most successful successive landings to least.

select   S.Name as Ship_Name, count(CLR.LandingResult) As LandingCount
from Launches L
join Rockets R
on L.RocketID = R.RocketID
join Cores_Landing_Result CLR
on L.Launch_ID = CLR.LaunchID
join Ships S
on L.Launch_ID = S.Launches and L.Ships = S.Ship_ID
where R.Rocket_Name='Falcon 9' and CLR.LandingResult =1
group by S.Name
order by count(CLR.LandingResult) desc


--Question 3.b : Which payload nationality has been on the most launches? List nationalities and the count of launches that the nationality has been up on from most to least launches.

select Nationality, count(LaunchID) from Payloads
group by Nationality
order by  count(LaunchID) desc




-- Question 4. Bonus (not required): How do 2021 GDP (in USD) values compare to that country’s number of payloads for that year? Use any data source necessary in combination with the data from the SpaceX API.

select distinct year(L.Date_UTC) as YEAR, G.Country,G.GDP_In_Million_USD from Payloads P
join Launches L on P.LaunchID = L.Launch_ID
join GDP G on P.Nationality = G.Country
where year(L.Date_UTC) = '2021'
order by G.GDP_In_Million_USD

