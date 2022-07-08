pipeline{ 
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    environment {
        CREDS = credentials('project0')   /* ..please add to your jenkins new credentials = username: AEfWGNA9zC + password: g0PRYTjC6R, id: project0  .. */
    }
    parameters { 
        choice (name: 'TEST',
                choices: ['combined', 'frontend', 'backend'],
                description: 'Please select the environment which you want to perform the test.')
    }
    stages{
        stage('checkout') {
            steps {
                git branch: 'bonus', url: 'https://github.com/AlmogChn/project_second_part.git'
            }
        }
        stage('run backend server') {
            steps{
                script{
                    try {
                        sh ' nohup python rest_app.py $CREDS_USR $CREDS_PSW &'
                    }
                    catch(NoRouteToHostException e){
                        echo 'non-existing route'
                    }
                }
            }
        }
        stage('run fronted server') {
            steps {
                script {
                    try{
                        sh ' nohup python web_app.py $CREDS_USR $CREDS_PSW &'
                    }
                    catch(NoRouteToHostException e){
                        echo 'non-existing route'
                    }
                }
            }
        }
        stage('backend testing') {
            when { 
                expression {params.TEST =='backend'}
            }
            steps {
                script {
                    sh 'python backend_testing.py $CREDS_USR $CREDS_PSW'
                }
            }
        }
        stage('frontend testing'){
            when {
                expression {params.TEST =='frontend'}
            }
            steps{
                script {
                    sh 'python frontend_testing.py $CREDS_USR $CREDS_PSW'
                }
            }
        }
        stage('combined testing') {
            when { 
                expression {params.TEST =='combined'}
            }
            steps {
                script {
                    sh 'python combined_testing.py $CREDS_USR $CREDS_PSW'
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
    post {
    failure {
        mail to: 'almogchn100@gmail.com',
             subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
             body: "Something is wrong"
        }
    }
}
