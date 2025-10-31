pipeline {
    agent any

    tools {
        // Name must match the SonarScanner installation name if you use Sonar
        // sonarQubeScanner 'SonarScanner'
    }

    environment {
        // if you added Sonar token in Jenkins credentials, set its ID here
        // SONAR_AUTH_TOKEN = credentials('sonar-token-id') 
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Code already checked out by Jenkins.'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '⚙️ Checking Python and installing packages...'
                bat '''
                    python --version
                    python -m pip --version
                    python -m pip install --upgrade pip
                    python -m pip install flask
                    python -m pip install yfinance
                    python -m pip install pytest
                '''
            }
        }

        stage('Run Tests (capture exit code)') {
            steps {
                echo '🧪 Running tests (results go to result.log)...'
                script {
                    // run pytest and capture exit code (so pipeline doesn't stop on non-zero)
                    def status = bat returnStatus: true, script: 'python -m pytest 1>result.log 2>&1'
                    // Print short summary
                    if (status == 0) {
                        echo "pytest passed (exit 0)."
                    } else {
                        echo "pytest finished with exit code ${status} — see result.log for details."
                        // Optionally mark build as UNSTABLE instead of failing:
                        currentBuild.result = 'UNSTABLE'
                    }
                }
                // show last 20 lines of test log for quick debug in console (optional)
                bat 'powershell -command "Get-Content result.log -Tail 20"'
            }
        }

        stage('SonarQube Analysis (optional)') {
            when {
                expression { return false } // set to true if you want to run Sonar locally now
            }
            steps {
                echo '🔍 Running Sonar (disabled by default in this file).'
                withSonarQubeEnv('LocalSonar') {
                    bat '''
                        sonar-scanner ^
                          -Dsonar.projectKey=Stock_Price_Viewer ^
                          -Dsonar.sources=. ^
                          -Dsonar.host.url=http://localhost:9000 ^
                          -Dsonar.login=%SONAR_AUTH_TOKEN%
                    '''
                }
            }
        }

        stage('Deploy Flask App') {
            steps {
                echo '🚀 Deploying Flask app (background)...'
                // start app in background on Windows
                bat 'start /B python app.py'
                echo '✅ Flask app started (background).'
            }
        }
    }
}
