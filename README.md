## Devops Capstone Project
### Project Details
    Capstone project utilizing popular devops tools to deploying a flask application within a Kubernetes cluster and a docker container. Docker application was forwarded to local port (localhost:5050) for monitoring purposes. Elastick stack configuration monitors active system resources for docker containers, flask application and kubernetes clusters as well as an overview of system resources.
   
   * presentation link:https://docs.google.com/presentation/d/15cgdRMHgh51yS0TzwsKxQAorttKgNCq0dIaLRRTbJ6E/edit?usp=sharing
### Requirements
* jenkins
* docker
* microk8s
* kubectl
* ansible
* metricbeat

### Configuration Steps
* Running Jenkins pipeline
  * jenkins start
  *  from the dashboard page click new item
  *  enter a name for the pipeline, select the pipeline option click ok.
  *   under source code management enter the link for this repository. Select Ok
  *   click build now to run the pipeline.
* Running Metricbeat
  *  within this repo  
     * `metricbeat modules docker kubernetes http system`   
     * `metricbeat -f metricbeat.yml`

* Running ELK Stack
  * `cd docker-elk`
  * `docker-compose up`
