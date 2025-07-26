- Here’s a **quick reference guide** for frequently used queries and methods when working with **JDBC (Java Database Connectivity)** and executing SQL statements in Java:
  
  ---
- ### **1. Common SQL Queries**
- #### **CREATE (Insert)**
  ```sql
  INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
  ```
  Example:
  ```sql
  INSERT INTO "UserData" ("userID", "username", "userPassword", "userPoints")
  VALUES (1, 'Mathu', 'goo', 7);
  ```
- #### **READ (Select)**
  ```sql
  SELECT column1, column2, ... FROM table_name WHERE condition;
  ```
  Example:
  ```sql
  SELECT * FROM "UserData" WHERE "userID" = 1;
  ```
- #### **UPDATE**
  ```sql
  UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
  ```
  Example:
  ```sql
  UPDATE "UserData" SET "username" = 'Srinivasava' WHERE "userID" = 4;
  ```
- #### **DELETE**
  ```sql
  DELETE FROM table_name WHERE condition;
  ```
  Example:
  ```sql
  DELETE FROM "UserData" WHERE "userID" = 6;
  ```
- Here’s an explanation and examples for **GROUP BY**, **ORDER BY**, **HAVING**, **DISTINCT**, and **COUNT** in SQL:
  
  ---
- ### **GROUP BY**
  The `GROUP BY` clause groups rows that have the same values in specified columns into summary rows. It is often used with aggregate functions like `COUNT`, `SUM`, `AVG`, etc.
  
  ```sql
  SELECT column1, aggregate_function(column2)
  FROM table_name
  GROUP BY column1;
  ```
  
  **Example:**
  ```sql
  SELECT "username", COUNT(*) AS "user_count"
  FROM "UserData"
  GROUP BY "username";
  ```
  This query groups users by their `username` and counts the number of occurrences for each username.
  
  ---
- ### **ORDER BY**
  The `ORDER BY` clause is used to sort the result set in ascending (`ASC`) or descending (`DESC`) order based on one or more columns.
  
  ```sql
  SELECT column1, column2, ...
  FROM table_name
  ORDER BY column1 ASC|DESC;
  ```
  
  **Example:**
  ```sql
  SELECT * FROM "UserData"
  ORDER BY "userPoints" DESC;
  ```
  This query retrieves all rows from the `UserData` table and sorts them in descending order of `userPoints`.
  
  ---
- ### **HAVING**
  The `HAVING` clause is used to filter groups based on a condition. It is often used with `GROUP BY` to filter aggregated results.
  
  ```sql
  SELECT column1, aggregate_function(column2)
  FROM table_name
  GROUP BY column1
  HAVING condition;
  ```
  
  **Example:**
  ```sql
  SELECT "username", COUNT(*) AS "user_count"
  FROM "UserData"
  GROUP BY "username"
  HAVING COUNT(*) > 1;
  ```
  This query groups users by `username` and returns only those usernames that appear more than once.
  
  ---
- ### **DISTINCT**
  The `DISTINCT` keyword is used to return only unique values in the result set, eliminating duplicates.
  
  ```sql
  SELECT DISTINCT column1, column2, ...
  FROM table_name;
  ```
  
  **Example:**
  ```sql
  SELECT DISTINCT "username"
  FROM "UserData";
  ```
  This query retrieves all unique usernames from the `UserData` table.
  
  ---
- ### **COUNT**
  The `COUNT` function returns the number of rows that match a specified condition.
  
  ```sql
  SELECT COUNT(column1)
  FROM table_name
  WHERE condition;
  ```
  
  **Example:**
  ```sql
  SELECT COUNT(*) AS "total_users"
  FROM "UserData";
  ```
  This query returns the total number of rows (users) in the `UserData` table.
- ### **Combining GROUP BY, HAVING, ORDER BY, and COUNT**
  You can combine these clauses to create more complex queries.
  
  **Example:**
  ```sql
  SELECT "username", COUNT(*) AS "user_count"
  FROM "UserData"
  GROUP BY "username"
  HAVING COUNT(*) > 1
  ORDER BY "user_count" DESC;
  ```
  This query:
  1. Groups users by `username`.
  2. Counts the number of occurrences for each username.
  3. Filters groups to include only those with more than one occurrence.
  4. Sorts the result in descending order of `user_count`.
- ---
-
- ### **2. JDBC Methods for Executing Queries**
- #### **`Statement` Methods**
- **`execute(String sql)`**:
	- Executes any SQL statement (e.g., `INSERT`, `UPDATE`, `DELETE`).
	- Returns `true` if the result is a `ResultSet`, otherwise `false`.
	  ```java
	  boolean result = st.execute(sql);
	  ```
- **`executeQuery(String sql)`**:
	- Executes a `SELECT` query and returns a `ResultSet`.
	  ```java
	  ResultSet rs = st.executeQuery(sql);
	  ```
- **`executeUpdate(String sql)`**:
	- Executes `INSERT`, `UPDATE`, or `DELETE` queries.
	- Returns the number of rows affected.
	  ```java
	  int rowsAffected = st.executeUpdate(sql);
	  ```
- #### **`ResultSet` Methods**
- **`next()`**:
	- Moves the cursor to the next row.
	- Returns `true` if there is a next row, otherwise `false`.
	  ```java
	  while (rs.next()) {
	    // Process the current row
	  }
	  ```
- **`getInt(String columnName)`**:
	- Retrieves the value of the specified column as an `int`.
	  ```java
	  int userID = rs.getInt("userID");
	  ```
- **`getString(String columnName)`**:
	- Retrieves the value of the specified column as a `String`.
	  ```java
	  String username = rs.getString("username");
	  ```
- **`getBoolean(String columnName)`**:
	- Retrieves the value of the specified column as a `boolean`.
	  ```java
	  boolean isActive = rs.getBoolean("isActive");
	  ```
	  
	  ---
- ### **3. PreparedStatement (Dynamic Queries)**
- **Create a `PreparedStatement`**:
  ```java
  String sql = "INSERT INTO \"UserData\" (\"userID\", \"username\", \"userPassword\", \"userPoints\") VALUES (?, ?, ?, ?)";
  PreparedStatement pst = con.prepareStatement(sql);
  ```
- **Set Parameters**:
  ```java
  pst.setInt(1, 1); // Set userID
  pst.setString(2, "Mathu"); // Set username
  pst.setString(3, "goo"); // Set userPassword
  pst.setInt(4, 7); // Set userPoints
  ```
- **Execute**:
  ```java
  pst.executeUpdate(); // For INSERT, UPDATE, DELETE
  ```
  
  ---
- ### **4. Connection Management**
- **Establish Connection**:
  ```java
  Connection con = DriverManager.getConnection(url, uname, pass);
  ```
- **Close Connection**:
  ```java
  con.close();
  ```
- **Auto-Close with Try-With-Resources**:
  ```java
  try (Connection con = DriverManager.getConnection(url, uname, pass);
       Statement st = con.createStatement()) {
      // Execute queries
  } catch (SQLException e) {
      e.printStackTrace();
  }
  ```
  
  ---
- ### **5. Common Exceptions**
- **`SQLException`**:
	- Thrown when there is an issue with the database connection or query execution.
	- Always handle this exception in your code.
- **`ClassNotFoundException`**:
	- Thrown when the JDBC driver class is not found.
	- Ensure the driver JAR is in the classpath.
	  
	  ---
- ### **6. Example Workflow**
  ```java
  import java.sql.*;
  
  public class JDBCExample {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/m2302";
        String uname = "postgres";
        String pass = "google.com12345";
  
        try (Connection con = DriverManager.getConnection(url, uname, pass);
             Statement st = con.createStatement()) {
  
            // CREATE
            String insertQuery = "INSERT INTO \"UserData\" VALUES (7, 'Rajendra Prasad', 'google.com12345', 9)";
            st.execute(insertQuery);
            System.out.println("Data Inserted");
  
            // READ
            String selectQuery = "SELECT * FROM \"UserData\"";
            ResultSet rs = st.executeQuery(selectQuery);
            while (rs.next()) {
                System.out.println("User ID: " + rs.getInt("userID"));
                System.out.println("Username: " + rs.getString("username"));
                System.out.println("Password: " + rs.getString("userPassword"));
                System.out.println("Points: " + rs.getInt("userPoints"));
                System.out.println();
            }
  
            // UPDATE
            String updateQuery = "UPDATE \"UserData\" SET \"username\" = 'Srinivasava' WHERE \"userID\" = 4";
            st.executeUpdate(updateQuery);
            System.out.println("Data Updated");
  
            // DELETE
            String deleteQuery = "DELETE FROM \"UserData\" WHERE \"userID\" = 6";
            st.executeUpdate(deleteQuery);
            System.out.println("Data Deleted");
  
        } catch (SQLException e) {
            System.err.println("SQL Error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
  }
  ```
-