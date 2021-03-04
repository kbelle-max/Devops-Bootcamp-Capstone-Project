
pipeline {
    agent any
    triggers{
        cron('H/5 * * * *')
    }
    environment {
        DOCKER_HUB_REPO = "kbelle/case_study1"
        CONTAINER_NAME = "kbelle/case_study1"
        STUB_VALUE = "200"
    }
    stages {
        
        stage('Build') {
            steps {
                // Download and change directory into repo
                sh 'rm -rf Devops-Bootcamp-Capstone-Project'
                sh 'git clone https://github.com/kbelle-max/Devops-Bootcamp-Capstone-Project.git'
                sh 'cd Devops-Bootcamp-Capstone-Project'
            



            }
        }
        
        stage('Deploy') {
            steps {
                script{
                    // Deploy independant application
                    sh 'docker stop $CONTAINER_NAME:latest || docker rm $CONTAINER_NAME:latest || docker run -d -p 5050:5050 $DOCKER_HUB_REPO:latest'
                    // Run playbook 
                    sh 'ansible-playbook playbook.yml'
                       }
                    }
                         }
    }

}