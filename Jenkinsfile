pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                // Execute a PowerShell command to get the version
                powershell 'Get-Host | Select-Object Version'
            }
        }
        stage('run python script') {
            steps {
                // Run the Python script using python command
                bat 'python your_script.py'
            }
        }
    }
}
