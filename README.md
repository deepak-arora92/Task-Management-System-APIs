Hi,
To run this project..following are the pre-Requisite

Python 2.7+ django 1.10.x + MySQL >= 5.5 needs to be installed.
a DB with name 'Happay' needs to be created.


after that 
clone this repo.
go inside it into the directory where you will find manage.py

now run the following commands sequentially.


-> python manage.py makemigrations
     it will create the table django_migrations

-> python manage.py  sqlmigrate <app_name> <migration number>
     in our case this would be:
-> python manage.py  sqlmigrate TMS 0001
-> python manage.py migrate
 It will create the Tasks and StudentsTask table in your DB.

now we need to create admin_user.
For that type the command
python manage.py createsuperuser

it will ask for username and password, give that and then our admin user will  be created.

 to start the app server:
-> python manage.py runserver


go to browser and type:
http://localhost:8000/

you should be seeing the hello world written. It means your app is running properly.

now goto:
http://localhost:8000/admin and login to the admin with super user password.

Admin can now create task and can create student users (staff users) to who he can assign tasks.
To create student users, admin needs to click on add user in admin console, it will ask for user_name & pw. 
After that user needs to be granted the staff user permission so that he can login to admin site. 

After creating the task and users.

you can use the following api to assign, view description, approve or disapprove the task.

1. just give the task id in the url and you would be able to see the task details and who all it has been assigned to.
    http://localhost:8000/task/2/

2. To asisgn give the task_id after the task and then give the Comma seprated student IDs to assign a task to  multiple students.
    http://localhost:8000/task/2/assign/?student=1,2,3,4

3.  To approve: 
    http://localhost:8000/task/2/approve/?student=2

4. To approve a task for multiple students give comma separated students IDs.
    http://localhost:8000/task/2/approve/?student=1,2,3

5. to Disappove:
    http://localhost:8000/task/2/disapprove/?student=2

6. A student user can login and change the task status with the following api.
    http://localhost:8000/task/2/update_status?status=done

Edge cases like task id/user_id  not present, task already assigned or insufficient permissions etc have been handled in api.
Please  feel free to reach me on my cell - 8147-509-884 for any clarification.
