
pipeline {
    agent any
    triggers{pollSCM('') 
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
                sh 'git clone https://github.com/kbelle-max/Devops-Bootcamp-Capstone-Project.gi'
                sh 'cd Devops-Bootcamp-Capstone-Project'
                //  Building new image from repo
                sh 'docker image build -t $DOCKER_HUB_REPO .'
                sh 'docker image tag $DOCKER_HUB_REPO $DOCKER_HUB_REPO'


            }
        }
        }
        stage('Deploy') {
            steps {
                script{
                    // Deploy application
                    sh 'docker stop $CONTAINER_NAME:latest || docker rm $CONTAINER_NAME:latest || docker run -d -p 5050:5050 $DOCKER_HUB_REPO:latest'
                    // Run playbook 
                    sh 'ansible-playbook playbook.yml'
                       }
                    }
                         }

}