pipeline {
    agent {
        docker { image 'node:14-alpine' }
    }
    stages {
        stage('build') {
            steps {
                docker build .
            }
        }
    }
}