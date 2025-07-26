- Reference: {{video https://youtu.be/K_5J4DjWBTI}}
- ---
- ### **1. Install PostgreSQL**
  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  ```
  
  ---
- ### **2. Check PostgreSQL Service Status**
  ```bash
  sudo systemctl status postgresql
  ```
- If inactive, start it:
  ```bash
  sudo systemctl start postgresql
  ```
  
  ---
- ### **3. Start the PostgreSQL Cluster**
  If the cluster is inactive, start it:
  ```bash
  sudo pg_ctlcluster <version> main start
  ```
  Replace `<version>` with your PostgreSQL version (e.g., `15`).
  
  ---
- ### **4. Enable the Cluster to Start on Boot**
  ```bash
  sudo systemctl enable postgresql@<version>-main
  ```
  
  ---
- ### **5. Reset PostgreSQL Password**
  1. Switch to the `postgres` user:
   ```bash
   sudo -i -u postgres
   ```
  
  2. Access the PostgreSQL shell:
   ```bash
   psql
   ```
  
  3. Set a new password for the `postgres` user:
   ```sql
   ALTER USER postgres WITH PASSWORD 'your-new-password';
   ```
  
  4. Exit the PostgreSQL shell:
   ```sql
   \q
   ```
  
  5. Exit the `postgres` user:
   ```bash
   exit
   ```
  
  ---
- ### **6. Install pgAdmin 4**
  ```bash
  sudo apt install pgadmin4
  ```
  
  ---
- ### **7. Access pgAdmin 4**
- Open your browser and go to:
  ```
  http://localhost/pgadmin4
  ```
  
  ---
- ### **8. Add a New Server in pgAdmin 4**
  1. Right-click **Servers** > **Register** > **Server**.
  2. Fill in the details:
	- **General Tab**:
		- Name: `Local PostgreSQL` (or any name).
	- **Connection Tab**:
		- Host: `localhost`
		- Port: `5432`
		- Username: `postgres`
		- Password: The password you set earlier.
		  3. Click **Save**.
		  
		  ---
- ### **9. Troubleshooting**
- #### **If Connection Fails:**
  1. **Check `pg_hba.conf`**:
	- Open the file:
	  ```bash
	  sudo nano /etc/postgresql/<version>/main/pg_hba.conf
	  ```
	- Change `peer` to `md5` for the `postgres` user:
	  ```
	  local   all             postgres                                md5
	  ```
	- Restart PostgreSQL:
	  ```bash
	  sudo systemctl restart postgresql
	  ```
	  
	  2. **Check Firewall**:
	- Allow port `5432`:
	  ```bash
	  sudo ufw allow 5432/tcp
	  ```
	  
	  3. **Check PostgreSQL Logs**:
	- View logs for errors:
	  ```bash
	  cat /var/log/postgresql/postgresql-<version>-main.log
	  ```
	  
	  ---
- ### **10. Retry Connection**
- Update the connection details in pgAdmin 4 and try again.
  
  ---
- ### **Key Notes:**
- Use `localhost` if PostgreSQL is on the same machine.
- Use the IP address if connecting remotely.
- Ensure the PostgreSQL service and cluster are running.
- Always verify the `pg_hba.conf` file for authentication settings.
  
  ---