- create the project and add in `pom.xml`
	- ```xml
	  <project xmlns="http://maven.apache.org/POM/4.0.0"
	           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
	                               http://maven.apache.org/xsd/maven-4.0.0.xsd">
	  
	      <modelVersion>4.0.0</modelVersion>
	  
	      <groupId>com.yourname</groupId>
	      <artifactId>my-sdk</artifactId>
	      <version>1.0.0</version>
	      <packaging>jar</packaging>
	  
	      <name>MySDK</name>
	  </project>
	  
	  ```
- Build and Install SDK to Local Maven repo - `mvn clean install` -> `.jar` (this will be created `~/.m2/repository/com/yourname/my-sdk/1.0.0/my-sdk-1.0.0.jar`)
- Use in another project:
	- ```xml
	  <dependency>
	      <groupId>com.yourname</groupId>
	      <artifactId>my-sdk</artifactId>
	      <version>1.0.0</version>
	  </dependency>
	  ```
- Publishing SDK in Remote Repository
	- Push it to GitHub and use **JitPack**
	- Or publish to a private **Nexus/Artifactory**
	- Or deploy to Maven Central (needs verification)