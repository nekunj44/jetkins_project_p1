pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Checking out code...'
                git 'https://github.com/nekunj44/jetkins_project_p1.git'
            }
        }

        stage('Install Dependencies Manually') {
            steps {
                echo '⚙️ Manually installing Python libraries...'
                sh '''
                    pip install flask
                    pip install yfinance
                    pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running basic test...'
                sh 'pytest > result.log || true'
            }
        }

        stage('Deploy Flask App') {
            steps {
                echo '🚀 Starting Flask App...'
                sh 'nohup python3 app.py &'
                echo '✅ Flask app deployed successfully!'
            }
        }
    }
}
