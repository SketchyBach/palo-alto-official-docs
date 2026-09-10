---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-3.x/cortex-xdr-3.x-documentation/data-management/broker-vm/manage-broker-vm/monitor-broker-vm-using-prometheus
fetched_at: 2026-09-06T09:49:56Z
source: cortex-platform
---

# Monitor Broker VM using Prometheus | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 3.x Documentation 

 Cortex XDR 3.x Documentation 

 Data management 

 Broker VM 

 Manage Broker VM 

 Cortex XDR 3.x 

 Monitor Broker VM using Prometheus 

 Learn more on monitoring the Broker VM using Prometheus. 

 You can enable local monitoring of the Broker VM to provide usage statistics in a Prometheus metrics format. You can tap in and export data by navigating to http://<broker_vm_address>:9100/metrics/ . By default, monitoring is disabled. 

 Prerequisite 

 To monitor the Broker VM using Prometheus, ensure that you enable monitoring on the Broker VM. This is performed after configuring and registering your Broker VM, when you can edit existing configurations and define additional settings in the Broker VMs page. 

 Select Settings → Configurations → Data Broker → Broker VMs . 

 In the Broker VMs table, locate your Broker VM, right-click, and select Configure . 

 Note 

 For all Broker VM nodes added to a HA cluster, you can also Configure the Broker VM nodes from the Clusters tab. 

 In the Broker VM Configurations page, select Monitoring from the left pane. 

 Clear the Use Default (Disabled) checkbox. 

 In the Montoring menu, select Enabled . 

 Click Save . 

 How to set up Prometheus and Grafana to monitor the Broker VM 

 Below is an example of how to set up Prometheus and Grafana to monitor the Broker VM. This is set up using a docker compose on an Ubuntu machine to monitor the CPU usage. 

 Perform the following procedures in the order listed below. 

 Task 1. Install Docker and Docker Compose 

 Update your Ubuntu system: 

 Ask Copy 

 sudo apt update 

 Install Docker: 

 Note 

 For more information on Docker, see the Docker website . 

 Ask Copy 

 sudo apt install docker.io 

 Start the Docker service: 

 Ask Copy 

 sudo systemctl start docker 

 Enable Docker to start on boot: 

 Ask Copy 

 sudo systemctl enable docker 

 Install Docker Compose: 

 Ask Copy 

 sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose 

 Ask Copy 

 sudo chmod +x /usr/local/bin/docker-compose 

 Task 2. Create a Docker Compose file 

 This task includes setting up Prometheus and Grafana. 

 Create a file named docker-compose.yml , and open it for editing: 

 Ask Copy 

 vim docker-compose.yml 

 Add the following content to the file: 

 Ask Copy 

 version: '3.8' 
 services: 
   prometheus: 
     image: prom/prometheus:latest 
     container_name: prometheus 
     restart: unless-stopped 
     volumes: 
      - ./prometheus.yml:/etc/prometheus/prometheus.yml 
      - prometheus_data:/prometheus 
    command: 
      - '--config.file=/etc/prometheus/prometheus.yml' 
      - '--storage.tsdb.path=/prometheus' 
      - '--web.console.libraries=/etc/prometheus/console_libraries' 
      - '--web.console.templates=/etc/prometheus/consoles' 
      - '--web.enable-lifecycle' 
      - '--log.level=debug' 
    ports: 
      - '9090:9090' 
  grafana: 
    image: grafana/grafana-enterprise 
    container_name: grafana 
    restart: unless-stopped 
    ports: 
     - '3000:3000' 
    volumes: 
      - grafana_data:/var/lib/grafana 
 volumes: 
   grafana_data: {} 
   prometheus_data: {} 

 Save and close the file. 

 Task 3. Create a Prometheus configuration file 

 You need to configure Prometheus to scrape the Broker VM metrics by creating a Prometheus configuration file. 

 Create a Prometheus configuration file named prometheus.yml in the same directory as the docker-compose.yml file that you created above. 

 Open the prometheus.yml file for editing: 

 Ask Copy 

 vim prometheus.yml 

 Add the following content to the file: 

 Ask Copy 

 global: 
   scrape_interval: 15s 
   scrape_timeout: 10s 
 scrape_configs: 
   - job_name: 'prometheus' 
     static_configs: 
       - targets: ['<your server IP address>:9090'] 
   - job_name: 'node' 
     static_configs: 
       - targets: ['<Broker VM IP address>:9100'] 

 Save and close the file. 

 Task 4. Run Docker Compose 

 In the terminal, run the following command from the project directory: 

 Verify that Prometheus is running correctly: 

 Task 5. Access Grafana and Set Up Prometheus as a Data Source 

 Open a web browser and go to http://<your server>:3000 . 

 Log in to Grafana using the default credentials. 

 Username: admin 

 Password: admin 

 Set up Prometheus as a data source: 

 In the left pane, select Administation → Data sources . 

 Click Add data source , and select Prometheus . 

 Under HTTP , set the URL to http://<your server IP address>:9090 . 

 To verify the connection, click Save & Test . 

 Task 6. Create Dashboards in Grafana 

 You can now create dashboards in Grafana to visualize the data from Prometheus. 

 In Grafana, on the left pane, click Dashboards . 

 Select New and create a new dashboard. 

 Add a panel to the dashboard and configure the dashboard to display the Prometheus metrics that you want. 

 To monitor CPU usage, use the following metric: 

 Previous Increase Broker VM storage allocated for data caching 

 Next Collect Broker VM Logs 

 Last updated 1 month ago 

 Was this helpful?
