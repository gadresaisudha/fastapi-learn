Things learnt in API
To run fastapi application:
uvicorn app.main:app --reload

FastAPI
API testing using postman
API validation using pydantic module:
Make use of BaseModel to makesure that client sents exactly the data that is needed
def create_posts(post:Post):
when retrieving posts based on id makesure that the id parameter is int so that the pydantic module can validate that user send the integer
def get_post(id:int):
if the user sends an id which is not in database we need to handle it
if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'post with id:{id} not found')
set the status code to 201 when posts is created
@app.post('/posts',status_code=status.HTTP_201_CREATED)
use status code 204 for delete
@app.delete('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
do not send any content when you delete the data
return Response(status_code=status.HTTP_204_NO_CONTENT)
handle the request when id that needs to be deleted is not found
if index== None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'post with id:{id} not found')    
Handle the request when users send an id that needs to be updated not found
if index== None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'post with id:{id} not found')  
Make sure the for put method the data sent is as per schema requirement
def update_posts(id:int,post:Post):


FastAPI:
CRUD operations using fastAPI along with best practices
C - create - post method - data - /posts - @app.post('/posts')
R - Read   - get method - -- - /posts     - @app.get('/posts')
                             - /posts/:id - @app.get('/posts/{id}') -- the id over here is called path parameters
U - update - put method - data -/posts/:id - @app.put('/posts/{id}') -- for put method whole data needs to be sent both updated,old data fields
            -patch method - data -/posts/:id - @app.patch('/posts/{id}') - for patch only updated method of field is sent
D - Delete - delete method - data -/posts/:id - @app.delete('/posts/{id})

Best practices for api naming:
always use shorthand notation along with plural notation for class
always use same path for all httpmethods
it always checks for the first path match so be sure you structure your api with order
/posts/{id} and /posts/latest gives error for latest if this is the order

documentation for api in fastapi is automated
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
whenever you want to create a python package make sure you include a file __init__.py


Databases:
we never talk to databases directly we have DBMS that acts as a mediator between user and databases
we ask dbms to perform some operaions and it perform them on databases and returns us the results
 popular DBMS:
 Relational : MYSQL,POSTGRESQL,ORACLE, SQL SERVER
 NOSQL : MongoDB ,DYNAMODB ORACLE, SQLSERVER

SQL -> structured query language that user uses to communicate with DBMS inorder to make changes to the Databases

Table:
A table represents a subject or event in an application

Columns vs rows:
table is made of rows and columns
Each columns represents a different attribute
Each row represents a different entry in the table

primary key:
is a column or group of columns that uniquely identifies each row in a table
Table can have one and only one primary key
unique and no duplicates
Ex: Id
It does not always had to be ID column
Any column that is unique can be considered
For example for User it can be email or phone number while registering it is going to be unique

Unique constarints:
A unique constraint can be applied to any column to make sure every record has a unique value for that column

Null constraint:
when we need user to create a record where a value for particular field needs to be mandatory then we use not null on that columns so that user has to create a record with value for that field if not it throws an error

Foriegn key:
Foreign keys link data in one table to the data in another table. A foreign key column in a table points to a column with unique values in another table (often the primary key column) to create a way of cross-referencing the two tables

composite keys:
 primary key that spans multiple columns
since primary keys are unique this will ensure that they are unique
its like a composite key doesnt have issue if there are duplicates in individual columns but the combination of columns should always be a unique one
It like combination of two or more primary keys

SQL Queries:
caseinsensitive but capitalize keywords for best practices
a.To retrieve whole data from tables:
select * from table_name;

b.To retrieve specific columns data from tables:
select column_name1,column_name2 from table_name;

c.rename column
select old_column_name AS new_column_name, FROM table_name;

d. To retrieve particular record
select * from table_name WHERE column_name1= ...;
                                        > or < ..;
                                        != ...;
                                        <> same as !=;
                        WHERE column_name1 >... AND column_name2 <...;
                        WHERE column_name1 >... OR column_name2 <... OR column_name3 = ..;
                        WHERE column_name1 IN (1,2,3,....);
                        WHERE column_name1 LIKE 'TV%';                  ->start with TV
                        WHERE column_name1 LIKE '%e';->ends with e
                        WHERE column_name1 LIKE '%en%'-> en between can have characters before and after
                        WHERE column_name1 NOT LIKE 'TV%'->does not start with TV
e. order by
select * from table_name ORDER BY  column_name1 DESC
default it orders ASC     
select * from table_name ORDER BY  column_name1 DESC, 
column_name2 ,column_name3 DESC

f. LIMIT
limits the records
select * from table_name LIMIT 10;

g. OFFSET
skips number of records 
select * from table_name OFFSET 3;
skips first 3 and display others

h. insert new row:
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

insert multiple rows:
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...),(value1, value2, value3, ...),
(value1, value2, value3, ...),(value1, value2, value3, ...);

to insert and return the inserted rows:
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...),(value1, value2, value3, ...),
(value1, value2, value3, ...),(value1, value2, value3, ...) returning *;

i. delete the row
DELETE FROM products WHERE column_name1 = value;
 
to see the deleted row along with deletion
DELETE FROM products WHERE column_name1 = value RETURNING *;

j. update the row
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

k.to see the updated row along with updation
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition returning *;

l.to delete all records of table
DELETE FROM TABLE_NAME;


m. joins
join two different tables into one based on a column
LEFT JOIN
In left join it shows instances that exists on left table but not on right table(null)
Basically in left join shows all instances from clause table "" along with matches to next one if not null
select * from table_name1(to which table will be appended) LEFT JOIN table_name2(tables that we will append)
ON table_name1.column_name = table_name2.column_name

Right Join
similarly in right join it shows instance that are present on right table but does not exist on left table(null)
In right join shows all instance of second table and matching ones from the first table(if not null)
select * from table_name1(to which table will be appended) RIGHT JOIN table_name2(tables that we will append)
ON table_name1.column_name = table_name2.column_name


POSTGRES:
It is one of relational DBMS
That means every table has a relation with other in database
each instance of postgres can be carved into multiple seperate databases
by default postgres creates a database by name postgres so that it can make connection

Datatypes in postgres:
Databases have datatypes just like any programming language
Numeric : Int,decimal,precision
Text : Varchar,text
bool : boolean
sequence : array

pgAdmin:(GUI)
We have pgAdmin using which we first setup the server with a port on which the backend databases run now create a database under this server. Generally we create one database for one application.

So under databases we have schemas option where we create tables under tables option
inside table we have option for creating columns
use serial as datatype for ID
once table is created right click to find view/edit records used to retrieve records
you can write data into table by directly adding rows
Always make sure to give default values to columns
Use NOW() function in default value for the create_at field so that postgres creates a timestamp by itself
make use of Constraints like not null, primary key

Now using above rules create a table posts with all columns in our database fastapi


psycopyg2:
In any application there are various to interact with database
One of which is to use default postgres driver(psycopyg2) used to talk to postgres database by sending sql commands


this is the package that we use inorder to connect to database 
and start querying on it
import psycopg2
from psycopg2.extras import RealDictCursor

code to connection our application with a database:
while True:
    try:
        conn = psycopg2.connect(host='localhost',database='fastapi', user= 'postgres',password='Sumalatha8*',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Databse connection was successful')
        break
    except Exception as error:
        print('Error',error)
        time.sleep(2)

First using password, user and database we connect to database
and use RealDictCursor as it converts retrieved results into dict

CRUD operations using psycopg2:
now using the cursor declared above which is an instance of database connection we use methods to pass sql queries to get data
for retrieve all data:
@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    print(posts)
    return {"data": posts}
first statement retrieves all records of table
second statement fetches all records of table into our application

For retieve bases on id:

cursor.execute("""SELECT * FROM posts WHERE id=%s""",(str(id)))
post = cursor.fetchone()

first statement retrieves one record of table
second statement fetches one record of table into our application
use %s as variable and pass id data to avaoid sqlinjection
make sure to convert id into string as it executes a str stament
but for validation in method parameters it should be id

for create records in table:
cursor.execute("""INSERT INTO posts(title,content,published) VALUES(%s,%s,%s)""",(post.title,post.content,post.published))

we use %s because there may be wierd sql commands in parameterds that leads to sql injections so we use %s to prevent this.
here %s is varaible and values are passed in second parameters of execute method

To see created record
new_post = cursor.fetchone()

uptill now we have only created it but not saved to our table
to save created record to table use
conn.commit()

Similarly for the update and delete use the following code
for delete:
 cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
delete with that id retrieve the post and save the model in database

For update
 cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id=%s RETURNING *""",
                   (post.title,post.content,post.published,str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
update with that id retrieve that post and save that model in database


Another approach to talk to our database is to use ORM(object relational mapper)
Instead of using sql directly in this we no longer use sql but the taditional python codde.
ORM acts as layer of abstraction that sits between database and us
we use alternate python methods and functions that finally turn into sql and apply to databses
ORM
application -----(use python)-----ORM---(use psycopg2+sql)---databases

what ORM do:
Intead of manually defining tables in postgres, we can define our tables as python model
queries can be made exclusively through python code. NO SQL is necessary
Then can call methods to a dbquery to generate final sql command

SQLALCHEMY:
One of popular ORM is SQLALCHEMY
It is a standalone library and can be associated with any webframeworks and webapplications 
here the sqlalchemy does not know how to talk to databses
it just python code for sql so we would definetly need a database driver to talk to database in this case definetly need a psycopyg2

create a database.py file that handles all database connections
Now iniside this file first we need a connection string that is used for sqlalchemy to connect to a database
then we need a engine that is responsible for connecting sqlalchemy to connect to database
QL_ALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<databse_name>'
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
It is a bad practice to give your password and all basically hardcore your sqlalchemy url we need to store it some where
now if you want to talk to the sql databse we need to create a session. (basically acts like our cursor)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
we have to define a baseclass as all the models that we use to create a table are extending from this baseclass
Base = declarative_base()

models.py
Now as we are using ORM we no longer need to create table in pgadmin we can create them as python models in new file models.py
all tables are declared in model.py
First we need to import our Base model
make use of column() method to create columns and then extend the base class
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published= Column(Boolean,default=True)

This is a dependency method inside databse.py
Create a method which is used to initiate the SessionLocal varible that is used to talk to database and finally close
so everytime an api request is made we call this function stating the SessionLocal variable to query the databse and finally close
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

make sure you call this method as parmeter on every api request
that how you establish connection with database and run commands
def test(db: Session = Depends(get_db)):

Inorder to query every single record from a particular table
post = db.query(models.Post).all()
Basically its an abstract to sql command to select all records
when you remove all() method it gives you the sql query to select all records

Limitation of sqlalchemy is that it doesnt modify the table basically its columns and all
it run the first line in main.py and creates the tables present in models if its already created wont touch it
so any time there is a change in table columns and all we need to drop table and create one
now as we are using orm no longer need to make sql statements directly make use of python methods to run sql command on databases

CRUD operations using sqlalchemy ORM

get all records 
Inorder to query every single record from a particular table
post = db.query(models.Post).all()
Basically its an abstract to sql command to select all records
when you remove all() method it gives you the sql query to select all records

Create a record
new_post = models.Post(title=post.title,content=post.content,published=post.published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data" : new_post}
line 1:create a record based on models post
line 2: add it to database
line 3: commit to databse
line 4: return the newly created record and save it in variable

Limitation suppose we have 50 fields for our class in that case during creation you need to initiate the whole 50 fields which is not best practice

so we use post.dict()--->this return the dict of post request data
now using **post.dict() unpacks the dict hence it assigns all the fields present in post model with post request data

to get one record use following query:
post = db.query(models.Post).filter(models.Post.id == id).first()
use first() method inorder to get first match record

to delete particular record with id
 deleted_post = db.query(models.Post).filter(models.Post.id == id)
deleted_post.delete()
db.commit()
first line is the query to  gets the record with id
second line chains another query to existing one to delete retireved record
third line actually saves the datamodel

to update a particular post
update_post_query = db.query(models.Post).filter(models.Post.id == id)
update_post_query.update(post.model_dump(),synchronize_session=False)
db.commit()
return {"data" : update_post_query.first()}
first line is the query to  gets the record with id
Before this check whether a record with that id exists using first() method then 
second line chains another query to existing one to update retireved record
third line actually saves the datamodel
final line is to return the first updated record

It may be a little confusing at here but you may notice that there are two classes are defined Post
one is defined in main.py file and another is defined in the model.py file

Schema/pydantic models
one defined in main.py file is Schema or Pydantic model
this model is used for Api request or response validation
This model is used in parameters in methods under http methods
schema/pydantic models define the structure of request and response
This ensures when a user wants to create a record in database it should have all the 
fields defined in our schema/pydantic model
mainly used for validation
chrome ---->request --->schema/pydantic model -----> Fastapi
     <------- schema/pydantic model <------ response<----
move your schemas to new file
from . import schemas
also update method parameters with schema.posts
def update_posts(id:int,post:schemas.Post,db:Session = Depends(get_db)):

we need to create different schema models for each of request 
as there may be possibility where we allow user to create some fields
only during creation then during updation we dont want user to 
update all fields but only few fields
class CreatePost(BaseModel):
    title: str
    content: str
    published: bool = True

class UpdatePost(BaseModel):
    published: bool = True

so instead of creating new class every request 
we can just create a base class and then extend this class
extending class gives us the flexibility
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
class PostCreate(PostBase):
    pass
class PostUpdate(PostBase):
    published: bool
Similarly we define schema/pydantic models for response 
to make sure that we restrict response by sending only few fields
or else follow the schema in response
In the class for response make sure to include
class Config:
    orm_mode = True
This is because by default pydantic model reads the data only if it 
is a dict so when you create post you return a sqlalchemy model 
but here we are defining pydantic model for response so that pydantic model 
gets confused when it see a sqlalchemy model which is not dict
hence the above code in pydantic Repsonse class states that to convert the data 
to dict and read the data 
make sure to add below line in our create posts to return ReponseSchema model
@app.post('/posts',status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
make use of List[schemas.PostResponse] when you are retrieving list of records
@app.get("/posts",response_model=List[schemas.PostResponse])

SQLalchemy models:(ORM models)
Responsible for creating columns in table within postgres
used to define all attributes in our table
mostly used to perform queries in our databse
which inturn used to create,update,delete entries within database
sqlalchemy model ---> create table in postgres
using this model ---->query table and CRUD on table


User Functionality:
From here we are going to handle user like table,CRUD operation and authentication and auhorization
storing passwords in database securely
As of now we are using SQLAlchemy orm to create table and handle CRUD opertation
so start creating a class with table name and all required attributes with default values in models.py
now in schemas define a pydantic model class User for validation of request make use of EmailStr for email validation
write create_user method when we get post request include validation request model we can see that there is no proper 
validation for response so create a response validation pydantic model for user

As of now we have been storing user password in database in the form of string which is not a bestpractice
as there is a possibility that the users password may be exposed when someone hacks the database
Hence we use a technique called hashing. we generally hash the password and then store it in database
reverse engineering that hash into string password is almost impossible
for this we need passlib library with bcrypt alogirthm hence 
pip install passlib[bcrypt]
pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")
this line will let the passlib know to use bcrypt algorithm
Now before creating the user we hash the password and then add to table
hash the password and set the hashed password as user password
hashed_password = pwd_context.hash(user.password)
user.password = hashed_password

store all these utility functions into utils.py
and now create a get_user mwthod to retrieve individual record
@app.get('/users/{id}',response_model=schemas.UserResponse)
def get_user(id:int,db:Session=Depends(get_db)):

first line the things you pass are called decorators
and in second line you pass functional parameters
split the main.py into two files specific to user and another with post
inside routers folder

make use of APIRouter method:
we can replace the keyword app with router
router= APIRouter()
and use router for http methods decorator
and in main.py 
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)
make use of include_router() method

instead of using same url path make use of prefix
router = APIRouter(
    prefix= '/users'
)

Inorder to give a tag to particular file paths
make use of tags you can see the documentation on localhost/docs.
Improve readability of our documentation

Authentication:
The process in which we verify users identity
(Login)
Two ways to tackle authentication:
1.Session based authentication:
In this we store something in our backend to track whether a user logged in.
So theres some piece of info which we store in database or memory to keeps track whether user is loggedin or loggedout

2. JWT token authentication:
Its stateless that means we wont store any info on database or memory(Api) which keeps track of user login activity.
we have a token which will be stored on frontend and the clients keep track if the user is logged in or not
Flow for JWT token:

client -------(/login(username+password))-----Api(backend) --(check for credentials and sends back sign JWT token)
      -----------   {token} --------------

now whenever the users requires to access  the data or application that requires authentication we send the Jwt token
as part of header from client in request then the backend or api validates or verify if token is valida and sends
back the data

client -----/posts +{token}-------Api(check for validitity)
  ---------- send {data} if valid------------

JWT Deep dive:
The jwt token looks like its encrypted but its not.
it comprises of 3 parts:
1. Header : It consist of metadata about taken
we are going to sign the token that means hash the token so we need to specify 
the algorithm that we use for hashing token (ex: HS256)
2 . payload: Any piece of info which is not that important as it is not encrypted
mostly we send the name and id of the user and role of user
we use this id to verify the token for this User
3. Signature : combination of header+payload+secret(key that we keep in api)
now we  use hashing algorithm to generate a Signature
secret only present in api server no one has access
this signture is very important to determine if token is valid
no encryption is there 

purpose of signature:
suppose a user send his credentials then api creates a token and sends back to user

Token structure:
Header     |
payload    |
Secret Key | hash algo--------- Signature |
                                 Header   |--------- Token
                                 payload  |

suppose a hacker wants to mess with application suppose he tries to change
user access in payload from normal user to admin and then send it as usual token
then in that case it wont valid as the signature that we have created for that user 
is  based on payload for initial role access and secret and header hence he has to create 
a new signature but he cannot as it hashing of payload and secret key that no one has access to

Api validation for signature:
suppose somehow the user has send the token bu generating signature based on only payload and header
then on the backend the api will have header payload and secret and it creates a test signature and compares it with the signature
coming from frontend and thus stops the hacker as it wont match
jwt token is not encrypted anybody can change data of token and see data of token but they cannot generate signature as they wont have secret key

Logging in user:
client ----------/login[email,password]--------Api-------Find user by email---->Databases
                                                 <------get user hashed password-----
                                                APi --->password from client
                                                        |
                                                        |hash it
                                                 Api-----compare client hashed password 
                                                        and databse stored hashed password
         <-------------  {token}     <---------- Api -----if they match   

create a new auth.py file:
In the new auth file we are going to verify the credentials and generate token for user
use Apirouter for route make use of post for /login path and in method invoke get_db and make
use of UserBase Schema model for request data validation.
Now filter databse based on request data email and get user
write a util function that  verifies client provided password and hashed password stores in database
and call this from auth.py file

Now install librabry that handles the signing and verifying of token
pip install python-jose[cryptography]

For authentication aand JWT use a different file Oauth2.py
import JWTError and jwt
inorder to generate token we need secret key, algo hashing and access token expiration
create a function to create token
get the payload data and update it with expiration time
now call jwt.encode() method with these parameters to create token
encoded_jwt= jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

Now you call the above function to create token from 
utils file under /login path
 access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token":access_token,
            "token_type": "bearer"}
to generate token for the authenticated user
you can validate the token in jwt debugger and check for payload data and expiration date

now instead of passign user credentials in login method we 
are going to use oauth2passwordrequesterform
we are going to use dependencies
this dependency will store user credentials coming from frontend
make sure you change crosschecking with email to username as oauth2passwordrequesterform will store details only as username and password
now using this inbuilt functionality we make sure that 
from frontend only form data is sent and as username and password. while testing in postman use username and password and also as form data

now once the user get the token he sends that as header for each api request then we use this token to validate the token and see its not tampered and not expired
First we are going to define the schema model for 
request data for Token (update schemas.py)
write a function to verify the token in oauth2.py
and get the decoded token using decode method
def verify_access_token(token:str, credentials_exception):
    payload = jwt.decode(token,SECRET_KEY,ALGORITHM)
now from the token you get payload which has user id
check whether user id exists
id:str = payload.get("users_id")

    if id is None:
        raise credentials_exception

Also verify that the user id matches the schema for TokenData
token_data = schemas.TokenData(id=id)

now create a dependency function that is going to take the token from request automatically and extract the id for us
and check for token validity
token is again depends on oauth2passwordbearer for schema
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f'Could not validate credentials',
                                          headers={"WWW-Authenticate":"Bearer"})

    return verify_access_token(token,credentials_exception)

Now for each request the users makes where they need to be logged in to get the data or create
we call upon this dependency function which automaticlly picks the token and verifies if it is valid
so include this dependency function inside as parameter for all http request(for ex:/post)
@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def create_posts(post:schemas.PostCreate, db:Session = Depends(get_db),get_current_user:int = Depends(oauth2.get_current_user)):

similary call this method user_id:int = Depends(oauth2.get_current_user) in all http request
Now in the oauth2 file call for db function to get the user object based on token id (which is userid) here
def get_current_user(token:str = Depends(oauth2_scheme),db:Session = Depends(get_db)):
    token = verify_access_token(token,credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user

postman environments:
For different prod and dev environments we need different localhost and different port 
and we change them constantly for testing
so instead of that in posstman we create environment inorder to test them without any issues
Inside the environment we create a environment variables and set them and use these
instead of hardcoded urls
create a variable and assign values
now set the environment to dev
and use the value in url as follows:
{{URL}}posts/2

now we dont want to alwaysmanually add the token for each request
so in postman after login request there is an option to run scripts in that 
pm.environment.set("JWT", pm.response.json().access_token);
basically we are setting an environment variable 
JWT with value of token that we get from that login request
now go and set this variable in all authorization for each http request
{{JWT}} set this at authorization on all request


Relationships:
For now we can create as many users as possible login with users and also create posts
or modify them but there is no association between the user and post like who created the post
that where Relational databases shine now we create a relation between user and post
here comes the concept of foriegn key we create a column in post that links to another column in user
in this case we create a foriegn key in post table this key is coming from user table from id column of user table
we store it as user_id in the users table

users               posts
id, ....            id, user_id(foriegn key)
|------------------------->|

Here it a one-to-many relationship its like one user can create many posts but the post is associated with only one user
Now go to pgadmin and delete exisitng posts and add the column user_id as foriegn key and makesure datatype is same as one in it original table
in pgadmin create a columnunder posts table set its datatype and not null true
now under constraints we have foriegn key option now set the posts columns, reference column and table
set actions for delete and update

select * from posts where user_id = 7;
gets posts createdby users
This how you create a foriegn key using postgres pgadmin
now lets delete this and see how to create it using sqlalchemy through code
sqlalchemy check for that tablename if it is not prsent it creates it there is no updation of columns option
so delete table from postgres pgadmin and add
owner_id = Column(Integer,ForeignKey("users.id",ondelete='CASCADE'),nullable=False)
where it says owner_id column under post table is a foriegn key
and it references to "users.id"-> table.columnname
and action ondelete of user.id CaASCADE ---> it means delete this record on deletion of this id from user
now rerun application to create a new table of post with owner_id as columns

now that we have updated the models we need to update the schema of post
now for postreposne schema model make sure to add it so we get owner_id in repsonse
class PostResponse(PostBase):
    id:int
    created_at : datetime
    owner_id : int
    class Config:
        orm_mode = True

this will get us post along with user_id
but during creation of posts we need  owner_id as it is mandatory column in post model
but we are not going to send the owner_id as data request in our postcreate schema 
instead we are going to handle it using the token , extract user_id from token (authentication status)and 
then add it during creation of post in method directly

def create_posts(post:schemas.PostCreate, db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
new_post = models.Post(owner_id=current_user.id,**post.model_dump())

we already get user object after checking for token authentication so we use that to get userid and pass into crreation of record
test in postman where you can see that the based on our previous datarequest we were able to create post and get owner_id in response
only after login with particular user

Rightnow in delete posts method a user can delete anyones post if he is loggedin
we have makesure that user deletes only his post
if deleted_post.owner_id!=current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN,detail=f'Cannot delete post with id:{id}')
make the similar changes in update as well to makesure user only updated his post

now if we want the whole object details of user instead of just id add below statement to Post model
owner = relationship("User")
make use of this to create a relationship between the objects
now set the schema for postresponse schema to return owner details
class PostResponse(PostBase):
    id:int
    created_at : datetime
    owner_id : int
    owner : UserResponse


query parameters:
http://.....search?.....
anything to right of ? is the query parameter 
they are optional key-value pairs used to filter out the request
It is used in pagination or filter based on receent ....

When we want to limit number of posts and skip post
 {{URL}}posts?limit=5&skip=1
 just add limit to url and change method parameters and add limit() and offset method
 @router.get("/",response_model=List[schemas.PostResponse])
def get_posts(db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user),limit:int = 10,skip:int = 0):
    #post = cursor.fetchone()
    posts = db.query(models.Post).limit(limit).offset(skip)
    return posts

Inorder to add serch functionality like filter posts based on string in url
 {{URL}}posts?limit=5&skip=1&search=great
 make use of contains method and just add parameter to method
def get_posts(db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user),limit:int = 10,skip:int = 0,search:Optional[str]=""):
    #post = cursor.fetchone()
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
 
 for space on search functionality make use of %20 in url
  {{URL}}posts?limit=5&skip=1&search=great%20wall

  Environment variables:
  our database url is exposed so anyone can get in with username and password and also the url maybe different on dev and prod
  and will be prod server for database might be running on completely different system
  and also auth secret key is exposed to solve all these issues we use environment variables
  All Os support this we tell OS to intialize all environmental variables before calling method in application
 on our OS if we go to search -> edit environmental variables
 there you can see we have
 1.system variables -> accessed all over system
 2. user specific variables -> only accesible to particular user
 In that we have Path key and also values associated with it
  commande line for environamental variable path
  ------ echo %path%
  In python we can get
  import os
  path = os.getenv("path")
  we dont need to create env variables and use them in application its mostly slow
  we need to make sure that all env variables are intialized and also validate them that they are
  in right datatype as env variables always send us a string
  we make use of pydantic models to validate that our env variables are of right datatype
  create a new file config.py where we set validation for our env variables
  create a class with all env variables
  and there expected datatype , pydantic models validate them and throws an error
  when there is a missmatch
  create an instance of that class
  and use that instance in main.py
  In dev environment generally you create a file .env and atore all your keys
  In prod we set our env variables on the machine
  pydantic is caseinsensitive
  
  Now as for dev environement we create a new file .env
  that contains the all values for our env variables.
  No defaults values are provided in config file
  Now we have to tell pydantic to import the values from .env file
  for that we create a class and then provide 
  env_file = ".env" ---> filename where variables are present
  create .env file at root level under fastpi folder and call this file 
  from config class
  make sure that this .env file never gets into git
  so keep this file in gitignore along with pycache and venv

  once you are sure the .env file variables are intialized go to databse.py file
  and rewrite sql_url using the .env variables
  also similary change the values in oauth2.py file get the values from config file
  SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
now when we move to production we just need to change the config.py file and reference them to file
where our envirornment variables values are stored

voting/likes System requirements:
1.users should be able to like a post
2. should only be able to like a post once
3. retreieving post should also fetch 
number of likes
Vote model:
create a table for Vote
columns that refrenece postid
column referencing user who liked post
a user should be able to like a post only once that means we need to ensure every entry post_id/user_id is a unique combination

simplest solution to last one is composite keys:
1. primary key that spans multiple columns
since primary keys are unique this will ensure that no user can like post twice
its like a composite key doesnt have issue if there are duplicates in individual columns but the combination of columns should always be a unique one

Implementation of vote model:
now you can go a explore creating vote table
using pgadmin and explore creating columns for vote table.
both our columns post that user liked
and user who liked the post. both columns are primary keys and also foriegn keys referncing the user and post tables
set the constriants
Drop the table if created and start implementation of table creation using sqlalchemy
step 1: 
Go to model.py file and create vote model
with appropriate columns which are primary keys and also foriegn keys refrencing to two
different tables

Step 2:
update schema file with the expected datatype for the data request
no need of user_id as we will be getting it from jwt token
just the postid and dir of vote should be enough

step 3:
create a new file vote.py that handles all
/vote urls
for this url we get user_id from jwt token
and data request from frontend we will send the post_id and also direction of vote if it postive or negative
import models and schemas and databses
call dependency function from method parameter for get_db(handles databse session) and oauth2.get_current_user for jwt token
and finally add new_vote to db based on data and commit db and refresh and return message

first write query to find the vote record based on post_id and user_id
a. if vote dir is pos(1):
    then if there is already existing vote raise exception cannot vote twice or else just add vote to databse
b. if vote dir is negative(0):
    then if there is no already existing vote write exception
    that vote 404 not found
    or else if found just delete it
once done wire up this route to main.py file
Test these on postman

up untill now in database postgres in posts table we only have owner_id who created the post now if we want the user details we need to query user table based on owner_id
 which is not efficient to query mutliple times. so in database we create join
 basicallyjoin 2 tables based on a column
left join (create in pgadmin)
selct * from posts LEFT JOIN users ON
posts.owner_id = users.id
specific table all column
selct posts.* from posts LEFT JOIN users ON
posts.owner_id = users.id
selct posts.id,users.id from posts LEFT JOIN users ON
posts.owner_id = users.id

In left join it shows instances that exists on left table but not on right table(null)
Basically in left join shows all instances from clause table "" along with matches to next one if not null
similarly in right join it shows instance that are present on right table but does not exist on left table(null)
In right join shows all instance of second table and matching ones from the first table(if not null)

select users.id, Count(posts.id) from posts RIGHT JOIN users ON
posts.owner_id = users.id Group By users.id;
This query gives all users and number of posts by user
first we are doing a right join that means all user instances and connected post instance then group them by user and give count of post instance
for each user

write query for total number of votes on each post
select Count(votes.user_id) from votes RIGHT JOIN posts ON
votes.post_id = posts.id Group By posts.id;
This is will right join so consider all posts we are going to group by posts id and now from votes tables count number of user_id for each post_id
anytime you use count eventhough it null count as 1
select posts.id,Count(votes.post_id) from posts LEFT JOIN votes ON
votes.post_id = posts.id Group By posts.id;
the above one will also work

Now implement this using sqlalchemy:
now in getposts method from post.py we want to get total votes for that post and send them back
db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id== models.Post.id,isouter=True).group_by(models.Post.id)

models.Post,-> from posts
func.count(models.Vote.post_id).label("votes") -> count(vote.post_id) as votes
join(models.Vote,models.Vote.post_id== models.Post.id,isouter=True) -> left join with votes bases on columns and left outer join
group_by(models.Post.id)-> group by post.id
default sqlalchemy will use left inner join -> make required changes as per this
response_model=List[schemas.PostResponse]
now since our response is changed make changes to our schema resposnse
class PostVoteResponse(BaseModel):
    Post: PostResponse
    votes: int
    class Config:
        orm_mode = True
call this response model from get_posts method
also update get_post by id with new response model and new db query


Limitation of sqlalchemy:
cant update our columns and cant update constraints like primary key and all once its created
does not allow modification on the table
it bcoz sqlalchemy checks for tablename in code if it is not present it just creates a new one 
if its existing doesnt touch it
so any modification made to table later are not considered

Database migration tool:
Developers can track changes to code and rollback code easily with Git. why cant we do the same for databse models/tables
databse migrations allow us to incrementally track changes to database schemma and rollback changes at any point in time
we will use a tool called alembic to make changes to our databse
alembic can automatically pull database models from sqlalchemy and generate the proper tables

ALembic ->> tool for the above issue
Basically this tool allows us to modify our database schema, track the changes of database
allows us to automatically update the colmns and constraints in database
it is a database migration tool
allows us to make incremntal changes to our databases

To install alembic
pip install alembic
now delete the  existing tables as we are going to create using alembic
intialize alembic in new folder
alembic init alembic
now in alembic folder you can see env.py file thats the major file that we edit
As alembic works with sqlalchemy and models we need to import our basemodel here in env.py file
set the connection string to postgres database and set the base metadata for target_metadata
config.set_main_option("sqlalchemy.url", SQL_ALCHEMY_DATABASE_URL)
target_metadata = Base.metadata
here grab the Base from app.models instead of database as it would read all models

when we want to make changes to our database the command is 
alembic revision
we also have optinal parameters (always msg double quotes)
alembic revision -m "create posts table"
so under alembic folder under versions we have a file with above message that is where we are going to create, modify or rollback our table
we have upgrade() method where we create and modify and downgrade() method that rollbacks our table
now in upgrade method write statements to create columns in table
def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('title',sa.String(),nullable= False))
def downgrade() -> None:
    op.drop_table('posts')
    pass
run the command
alembic current
--displays current revision for a database
There is a revision number in alembic->versions-> create post file
run the following command to actually call the upgrade method
alembic upgrade eeb18f3337b7
In pgadmin you can see that a posts table is created and also an alembic_version table is created it keeps track of all the versions as we are updating
now we want to add another column
so we create new revision file and call add_column method into our upgrade method

now alembic current -> this command provides where we are in database (revision)
and alembic heads -> this command provides where  we are at source code(revision)
alembic upgrade heads -> runs the heads revision

now if we want to delete the table
just give
alembic downgrade rev_num(revision number)
alembic downgrade -1(previous)

creation of users table:
create a revision file
update upgrade and downgrade method with creation of column and drop of table
def upgrade():
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))


def downgrade():
    op.drop_table('users')

now check your current and heads and according implemnt respective revision files
alembic history 
---for history of revisions
alembic upgrade heads 
--creates user table
add back the content column

now relationship between posts and user table : add foriegn key
create a revision file
and add column and set it as foriegn key
def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk','posts',"users",
                          ["owner_id"],["id"],ondelete='CASCADE')


def downgrade():
    op.drop_constraint('posts_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
now call upgrade of revision file
alembic upgrade heads

Also add last few columns of the posts table:
same proces create revision file, update methods call the upgrade on revision file

Similary create votes table with foriegn keys and all but this time we use autogenerate feeature that looks into our models code ang generate the required code
alembic revision --autogenerate -m "add vote"
create a file with all code for vote table creation
alembic upgrade heads
at any point of time you can just update your models and run alembic autogenerate command to modify your database schema and constraints

comment this line as this says sqlalchemy to create tables based on metadata from models file
models.Base.metadata.create_all(bind=engine)
we are commenting this because we are going to let alembic to send message to sqlalchemy to create tables


Basically once you have developed your application upuntill now we have tested only sending requests from postman that is we are sending request from our own system.
Once moved to prod your application receives requests from different machines and also from different web browser.
we need to handle the part when we get request from webbrowser

so go to google.com -> inspect->console
from here you can send the request from 
webbrowser level
fetch('http://localhost:8000/').then(res=>res.json()).then(console.log)

this will send request to our root url
and return the response
There you can see we will get the CORS issue it like we get data from postman but not getting data when request is made from webbrowser

CORS:
cross orign resource sharing(CORS) allows you to make requests from a webserver on one domain to a server on a different domain.
By default our api will only allow web browsers running on same domain as our server to make requests to it
Basically http://localhost:8000/
it gives us reply from this domain name in browser but when we call this url or domain from different website(ebay.com) from different domain name it raises CORS issue.
CORS is the solution for this allowing communication between different domains
in main.py file
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
add these inorder for our app to reply to 
app hosted with different domain
CORSMiddleware -> function that runs before each request
allow_origins = origins , origins here is the list of all domains that are allowed to talk to our api
allow_methods=["*"] , we can also restrict 
the http methods which are allowed and not allowed
allow_headers=["*"] -> also have control on headers
now if you put google url in list now 
you can receive response from our api when request is made from google.com
if your api is public api
then origins = ['*]
if its private then just set the origin to that private domain that send the request to our api

Git:
first create .gitignore file and add 
__pycache__ , venv/, .env as they are private have passwords and all our installation libraries and letting them out would be dangerous

But we would want our team members to know what all libraries have been installed
for that give command:
pip freeze
gives all the libraries/packages installed along with version
take output and store it in requirement.txt
pip freeze > requirements.txt
now anyone can go to git clone our repository and run 
pip install -r requirements.txt
this should install all dependency libraries/packages
download git if not installed previously
git --version 
(to check if installed)
we are going to setup a remote repository 
on github to store our code
go to github an create repository
now comeback to vscode
---- git init
(intialize your git)
you wont see this but when you uncheck a  hidden files in files explorer you will find .git file
----- git add --all
(add all files in our directory to git
i.e stages the files)
----- git commit -m "initial commit"
(commits the files)
if username and password not configured do it
git branch -M main
first create a branch on which your code will reside
git remote add origin https://github.com/your-username/your-repository.git
now set the remote github url that you have created on github account
git push -u origin main
push your local changes onto remote repository on the main branch
Thus all code is stored on main branch on your remote repository

Deploy application on heroku platform:
signup online and install heroku CLI on machine
and also git on machine 
now follow the commands:
check if heroku installed on machine
heroku --version
For login:
heroku login
once logged in
heroku create
this will create folder same as origin like remote repository
if git remote
you can see two folders heroku and origin
now push local changes to heroku remote repository
git push heroku main
now our code is in heroku remote repository
but it does not know what to do so it throws error
it just knows that its a  python application
so now we create a file from root by name Procfile and give the command
web: uvicorn app.main:app --host= 0.0.0.0 --port=${PORT: -5000}

run the application and it accepts any hostnumber and any port number provided by heroku
