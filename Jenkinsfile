pipeline {
    agent any

    // Define constants here so they are easy to change later
    environment {
        EC2_IP = '65.1.134.171'         // <--- CHANGE THIS
        EC2_USER = 'ubuntu'
        REPO_URL = 'git@github.com:tejasgund02/DevOps-Project-Two-Tier-Flask-App-using-AWS-main.git' // <--- CHANGE THIS
        SSH_CRED_ID = 'ec2-instance-key'
        PROJECT_DIR = '/home/ubuntu/student-app'
    }

    stages {
        stage('Check Connectivity') {
            steps {
                sshagent([SSH_CRED_ID]) {
                    // Simple ping to make sure EC2 is alive before we try anything heavy
                    sh "ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} 'echo Connection Successful! Server is ready.'"
                }
            }
        }

        stage('Update Code on Server') {
            steps {
                sshagent([SSH_CRED_ID]) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} '
                            # 1. Create directory if it doesn not exist
                            mkdir -p ${PROJECT_DIR}
                            cd ${PROJECT_DIR}

                            # 2. Check if git is already initialized
                            if [ -d ".git" ]; then
                                echo "Repository exists. Pulling latest changes..."
                                git reset --hard  # Force discard local changes to avoid conflicts
                                git pull origin main
                            else
                                echo "First time deployment. Cloning repository..."
                                # We clone into the current directory (.)
                                git clone ${REPO_URL} .
                            fi
                        '
                    """
                }
            }
        }

        stage('Build & Deploy') {
            steps {
                sshagent([SSH_CRED_ID]) {
                    sshagent([SSH_CRED_ID]) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} '
                            cd ${PROJECT_DIR}
                            
                            echo " stopping old containers to avoid conflicts..."
                            # The "|| true" part means "if this fails (because no containers exist), just keep going"
                            sudo docker-compose down || true
                            
                            echo "Building and Starting New Containers..."
                            sudo docker-compose up -d --build --remove-orphans
                        '
                    """
                    }
                }
            }
        }

        stage('Cleanup (Free Tier Saver)') {
            steps {
                sshagent([SSH_CRED_ID]) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} '
                            echo "Cleaning up old images to save disk space..."
                            # This removes all dangling images (layers not used by running containers)
                            sudo docker system prune -f
                        '
                    """
                }
            }
        }
    }
}
