- 1. Create a Server container.
- 2. Map the servlet by creating a Context (the servlet object and the tag that refers in the server)
- 3. Connect the context and servlet object to the Tomcat. Start and Awaits the server.
- ```xml
      <dependency>
        <groupId>jakarta.servlet</groupId>
        <artifactId>jakarta.servlet-api</artifactId>
        <version>4.0.4</version>
        <scope>provided</scope>
      </dependency>
  
      <dependency>
        <groupId>org.apache.tomcat.embed</groupId>
        <artifactId>tomcat-embed-core</artifactId>
        <version>8.5.96</version>
      </dependency>
  ```
- ```java
  package com.servlet;
  
  
  
  import org.apache.catalina.LifecycleException;
  import org.apache.catalina.startup.Tomcat;
  import org.apache.catalina.Context;
  
  /**
   * Hello world!
   *
   */
  public class App 
  {
      public static void main(String[] args) throws LifecycleException
      {
          Tomcat tomcat = new Tomcat();
          tomcat.setPort(9090);
          
  
          Context context=tomcat.addContext("", null);
          Tomcat.addServlet(context,"HelloServlet",new HelloServlet());
          context.addServletMappingDecoded("/hello", "HelloServlet");
          
          tomcat.start(); 
          tomcat.getServer().await();
          /*
  
          1. Create a Server container. 
          2. Map the servlet by creating a Context (the servlet object and the tag that refers in the server)
          3. Connect the context and servlet object to the Tomcat. 
  
           */
  
      }
  }
  
  ```
- ```java
  // Servlet
  package com.servlet;
  
  import javax.servlet.http.HttpServlet;
  import javax.servlet.http.HttpServletRequest;
  import javax.servlet.http.HttpServletResponse;
  
  public class HelloServlet extends HttpServlet{
      
      public void service(HttpServletRequest req, HttpServletResponse res){
          System.out.println("In Service");
      }
      
  }
  
  ```