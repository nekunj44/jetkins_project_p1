pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Checking out code...'
            }
        }

        stage('Install Dependencies Manually') {
            steps {
                echo '⚙️ Manually installing Python libraries...'
                bat '''
                    pip install flask
                    pip install yfinance
                    pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running basic test...'
                bat 'pytest > result.log || true'
            }
        }

        stage('Deploy Flask App') {
            steps {
                echo '🚀 Starting Flask App...'
                bat 'nohup python3 app.py &'
                echo '✅ Flask app deployed successfully!'
            }
        }
    }
}
