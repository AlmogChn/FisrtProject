pipeline{ 
    agent any
    parameters { 
        choice (name: 'TEST',
                choices: ['combined', 'frontend', 'backend'],
                description: 'Please select the environment which you want to perform the test.')
    }
    stages{
        stage('run backend server') {
            steps {
                script {
                    sh 'python start /min rest_app.py'
                }
            }
        }
        stage('run fronted server') {
            steps {
                script {
                    bat 'python start /min web_app.py'
                }
            }
        }
        stage('backend testing') {
            when { 
                expression {params.TEST =='backend'}
            }
            steps {
                script {
                    bat 'python backend_testing.py'
                }
            }
        }
        stage('frontend testing'){
            when {
                expression {params.TEST =='frontend'}
            }
            steps{
                script {
                    bat 'python frontend_testing.py'
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
                    bat 'python combined_testing.py'
                }
            }
        }    
        stage('clean environment') {
            steps {
                script {
                bat 'python lean_environment.py'
                }
            }
        }
        
    }    
}
