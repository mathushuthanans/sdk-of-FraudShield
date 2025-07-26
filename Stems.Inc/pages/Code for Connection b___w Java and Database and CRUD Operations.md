- `r1.next()` does 2 things - get to the next row and set a pointer.
- ```java
  package mathu;
  
  import java.sql.*;
  
  public class JDBC {
      public static void main(String[] args) throws Exception {
          // Database connection details
          String url = "jdbc:postgresql://localhost:5432/m2302"; // Database URL
          String uname = "postgres"; // Username
          String pass = "google.com12345"; // Password
  
          // Load the PostgreSQL JDBC driver
          Class.forName("org.postgresql.Driver");
  
          // Establish the connection
          Connection con = DriverManager.getConnection(url, uname, pass);
          System.out.println("Connection Passed"); // Connection successful
  
          // Create a statement for executing SQL queries
          Statement st = con.createStatement();
  
          // ----------------------------> CREATE (Insert) <-------------------------------------
          String insertQuery = "INSERT INTO \"UserData\" VALUES (7, 'Rajendra Prasad', 'google.com12345', 9)";
          st.execute(insertQuery);
          System.out.println("Data Inserted Successfully");
  
          // ----------------------------> READ (Select) <-------------------------------------
          String selectQuery = "SELECT * FROM \"UserData\"";
          ResultSet resultSet = st.executeQuery(selectQuery);
  
          System.out.println("\nReading Data from UserData Table:");
          while (resultSet.next()) {
              System.out.println("User ID: " + resultSet.getInt("userID"));
              System.out.println("Username: " + resultSet.getString("username"));
              System.out.println("Password: " + resultSet.getString("userPassword"));
              System.out.println("Points: " + resultSet.getInt("userPoints"));
              System.out.println(); // Blank line for separation
          }
  
          // ----------------------------> UPDATE <-------------------------------------
          String updateQuery = "UPDATE \"UserData\" SET \"username\" = 'Srinivasava' WHERE \"userID\" = 4";
          st.execute(updateQuery);
          System.out.println("Data Updated Successfully");
  
          // ----------------------------> DELETE <-------------------------------------
          String deleteQuery = "DELETE FROM \"UserData\" WHERE \"userID\" = 6";
          st.execute(deleteQuery);
          System.out.println("Data Deleted Successfully");
  
          // Close the connection
          con.close();
          System.out.println("\nConnection Closed"); // Connection closed
      }
  }
  ```