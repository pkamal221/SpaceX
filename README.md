# SpaceX

**My Work for this SpaceX Challenge

1. First Created a AWS RDS Database, and Use that Instace for our Database work.

    I have created the AWS RDS Database (SQL Server) instance and access it from my desktop DB Applicaion (Microsoft SQL Server Management Studio)  
	
2. To answer the Query, first created the script to pull the data from SpaceX APIs.
   Below are the script names for APIs to pull the data from APIs and Place into the Databse Tables.
   
   Launches API   https://api.spacexdata.com/v4/launches   -  (Script Name - 1.0_SpaceX_Launches.py)
   Ships API :  https://api.spacexdata.com/v4/ships - (Script Name - 1.0_SpaceX_Ships.py)
   Rockets API : https://api.spacexdata.com/v4/rockets - (Script Name - 1.0_SpaceX_Rockets.py)
   Core Landing Result : https://api.spacexdata.com/v4/launches - (Script Name - 1.0_SpaceX_Cores_Landing_Result.py)
   Payloads API :	https://api.spacexdata.com/v4/payloads - (Script Name - 1.0_SpaceX_Payloads.py)
   GDP By Countries -  Pulling data from GDP_Countries.csv -  (Script Name - 1.0_GDP_Countries.py)
 
3. Now, Coming to the Query Part :-
 
    - For Q(3.a) Query , I have used total 4 Tables :
	          * Launches 
			  * Ships 
			  * Rockets 
			  * Core Landing Result 
			  
    - For Q(3.b) Query , I have used 1 Table.
              * Payloads 
			  
	- For Q(4) Query , I have used 3 Tables.
	          * GDP 
			  * Launches 
			  * Payloads 
			  



**How to Run the Solution - (Please note all the scripts, Query File and CSV File for GDP_Countries kept in the same Folder "SpaceX_Challenge")

1.	First of all set up the databse part -  I am still keeping my AWS RDS Database open so we can access the RDS Instance.  For Ex - You can use Microsoft SQL Server Management Studio to access the RDS Instance by putting below 	credentials.

	Server Name - database-spacex-1.cxujv5rff92r.us-east-1.rds.amazonaws.com,1433

	SQL Server Authentication:
		Username - admin
		Password - password


2. After that Run all the scripts in any Python IDE one by one (In Below Order) and populated the Database tables.

		1). 1.0_SpaceX_Launches.py
		2). 1.0_SpaceX_Ships.py
		3). 1.0_SpaceX_Rockets.py
		4). 1.0_SpaceX_Cores_Landing_Result.py
		5). 1.0_SpaceX_Payloads.py
		6). 1.0_GDP_Countries.py


3. Once Step-2 completes , all Python Script ran successfully then  Run the query file "SpaceX_Query.sql" on RDS Instance (database - SpaceX) using application (Microsoft SQL Server Management Studio) .
In the file SpaceX_Query.sql , there is total 3 queries, You can run the Query one-by-one.




                                                                            ** Thank you for reading **


	     
