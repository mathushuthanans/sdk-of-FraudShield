- Microservices Architecture:
	- Each script is written in its own framework and runs as an independent API.
	- For example:
		- Java code runs on a **Spring Boot** server
		- Python code on a **Django** server
		- JavaScript code on its own **Node.js** server
		  
		  All of these services need to run **simultaneously**, which is why we use the **Microservices** concept.
	- Each service is wrapped in a **Docker** container.
	- Services are orchestrated and synchronized using **Kubernetes**.
	  
	  🧠 *Analogy*: Think of each service as a "bucket," and Kubernetes as the "bucket synchronizer."
	  
	  ✅ This is why **Docker**, **K8s**, and **Microservices** are used — not just buzzwords.
	  
	  ➡️ **70–80% of companies** follow this architecture.
- ProcessBuilder (Hackathon Method)
  
  Used in NIT Hackathon:
	- **Super lightweight** – doesn’t require running independent servers.
	- Can **run any language** via system processes (like spawning shell commands).
	  
	  ✅ Works well for quick execution across languages without setting up microservices.
- gRPC – Cleanest & Fastest Integration
	- The most efficient and structured way to integrate services.
	  Steps:
		- Define service methods and data types using a `.proto` file (like Java interfaces).
		- Compile the `.proto` → generates code in any target language (Java, Python, etc.).
		- Implement logic inside the generated code.
		  
		  💡 The connection between client and server is **automatically handled**.
		  
		  ✅ Used by **20–30% of companies**, especially in speed-critical or real-time systems.