# psql

# psql (Compass)
```sh
# Start/stop psql server
brew services start postgresql
brew services stop postgresql

# Connect to db
psql
# if error: db does not exist
createdb <yourusername>
```

```sql
-- Create users
CREATE ROLE vagrant LOGIN SUPERUSER PASSWORD '123';
CREATE ROLE labber LOGIN SUPERUSER PASSWORD 'labber';

\du                       -- list users
\l                        -- list of db
CREATE DATABASE <dbname>; -- Create db
\c <dbname>               -- Connect to db
\dt                       -- list tables
\d <tablename>            -- describe table
```

