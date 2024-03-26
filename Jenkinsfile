pipeline {
    agent any
    stages {
        stage('version'){
            steps {
                sh 'push --version'
            }
        }
        stage('hello'){
            steps {
                sh 'push hello.ps1'
            }
        }
    }
}