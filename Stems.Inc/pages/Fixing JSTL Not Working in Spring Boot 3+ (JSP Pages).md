-
- ### **Problem:**
- JSTL expressions (`${prod}`) were **not working** in JSP pages.
- The page was **loading correctly** but **JSTL tags were not evaluated**.
- ### **Solution:**
- **Remove old JSTL dependency (`javax.servlet:jstl`)**
- **Use the correct JSTL dependencies for Spring Boot 3+ (Jakarta EE)**:
  
  ```
  <dependency>
    <groupId>jakarta.servlet.jsp.jstl</groupId>
    <artifactId>jakarta.servlet.jsp.jstl-api</artifactId>
    <version>3.0.0</version>
  </dependency>
  <dependency>
    <groupId>org.glassfish.web</groupId>
    <artifactId>jakarta.servlet.jsp.jstl</artifactId>
    <version>3.0.0</version>
  </dependency>
  ```
- **Ensure JSP Compilation Support by adding:**
  
  ```
  <dependency>
    <groupId>org.apache.tomcat.embed</groupId>
    <artifactId>tomcat-embed-jasper</artifactId>
  </dependency>
  ```
- **Explicitly add Tomcat dependency for JSP support:**
  
  ```
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-tomcat</artifactId>
    <scope>provided</scope>
  </dependency>
  ```
- **Recompile & Restart Application:**
  
  ```
  mvn clean package
  ```
- ### **Test If JSTL Works**
  
  In `final.jsp`, add:
  
  ```
  <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
  <c:set var="testVar" value="JSTL is working!" />
  <p>Test: <c:out value="${testVar}" /></p>
  ```
  
  If it prints `Test: JSTL is working!`, JSTL is now correctly configured. 🚀