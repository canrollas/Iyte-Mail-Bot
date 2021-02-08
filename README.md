### FEATURES

- Basically,those lines of codes can send mail to person with selenium library;
- So many mails you can sent at one time with this simple idea in a short time;
- Basic idea behind this example project is find your friends and mail them in a short way;

### Explanation
- Bot program gets the data of the array what you want to write
- Bot program get names of the students with zip function which is spesific for python
- After loop program send mails by one by

### Database connection
- If someone wants to connect database for storing values and names
- It will be useful those code

```python
    import sqlite3
    
        def database_fetcher(db_name):

        con = sqlite3.connect(db_name) 

        cursor = con.cursor() 

        cursor.execute("SELECT * from 'users' ")
        
        users=cursor.fetchall()

        cursor.close()

        return users
```
## Licence & copyright

© Can Rollas , Mail Bot

Lİcensed under the [Apache License](LICENSE).
