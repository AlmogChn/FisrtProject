pipeline{ 
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    environment {
        CERDS = credentials('Database')
    }
    parameters { 
        choice (name: 'TEST',
                choices: ['combined', 'frontend', 'backend'],
                description: 'Please select the environment which you want to perform the test.')
    }
    stages{
        stage('checkout') {
            steps {
                script { 
                    properties([pipelineTriggers([pollSCM('30 * * * *')])])
                }
                git 'https://github.com/AlmogChn/project_second_part.git'
                sh ' python db_connector.py ${CREDS_USR} ${CREDS_PSW} &'
            }
        }
        stage('run backend server') {
             steps {
                script{ 
                    sh ' nohup python rest_app.py &'
                }
             }
        }
        stage('run fronted server') {
            steps {
                script {
                    sh ' nohup python web_app.py &'
                }
            }
        }
        stage('backend testing') {
            when { 
                expression {params.TEST =='backend'}
            }
            steps {
                script {
                    sh 'python backend_testing.py ${CREDS_USR} ${CREDS_PSW}'
                }
            }
        }
        stage('frontend testing'){
            when {
                expression {params.TEST =='frontend'}
            }
            steps{
                script {
                    sh 'python frontend_testing.py ${CREDS_USR} ${CREDS_PSW}'
                }
            }
        }
        stage('combined testing') {
            when { 
                expression {params.TEST =='combined'}
            }
            steps {
                input message : "Are you sure you want to perform the combined testing?" , ok:'yes'
                script {
                    sh 'python combined_testing.py ${CREDS_USR} ${CREDS_PSW}'
                }
            }
        }    
        stage('clean environment') {
            steps {
                script {
                    sh 'python clean_environment.py'
                }
            }
        }
    }    
}
