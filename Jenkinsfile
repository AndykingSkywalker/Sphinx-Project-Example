pipeline {
    agent any

    environment {
        // Directory where Sphinx builds the HTML output.
        DOCS_BUILD_DIR = 'docs/_build/html'
        // The branch used for GitHub Pages.
        GH_PAGES_BRANCH = 'gh-pages'
        // Jenkins credentials ID for accessing GitHub.
        // Make sure this ID is correctly configured in Jenkins with access to your repository.
        GIT_CREDENTIALS_ID = 'webhook'
        // The URL of your GitHub repository.
        // Ensure this uses the HTTPS format.
        REPO_URL = 'github.com/AndykingSkywalker/Sphinx-Project-Example.git'
    }

    triggers {
        // Polls the SCM every 5 minutes for changes.
        pollSCM('H/5 * * * *')
    }

    stages {
        stage('Install Dependencies') {
            steps {
                // Ensure Python and pip are available.
                sh 'python3 --version || exit 1'
                sh 'python3 -m pip --version || exit 1'

                // Install dependencies using pip.
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Build Sphinx HTML') {
            steps {
                // Clean previous build artifacts
                sh 'rm -rf ${DOCS_BUILD_DIR}'
                // Add the Python bin directory to PATH and build the Sphinx documentation.
                // Add project root to PYTHONPATH so autodoc can import modules.
                sh 'export PATH=$PATH:/Users/andrew/Library/Python/3.9/bin && PYTHONPATH=$(pwd) sphinx-build -b html docs/ ${DOCS_BUILD_DIR}'
            }
        }

        stage('Deploy to GitHub Pages') {
            steps {
                withCredentials([string(credentialsId: env.GIT_CREDENTIALS_ID, variable: 'GIT_TOKEN')]) {
                    sh 'git config --global user.email "jenkins@localhost"'
                    sh 'git config --global user.name "Jenkins"'

                    sh 'git clone --single-branch --branch ${GH_PAGES_BRANCH} https://${GIT_TOKEN}@${REPO_URL} gh-pages-temp'

                    dir('gh-pages-temp') {
                        sh 'git rm -rf * || true'
                        sh "cp -r ../${DOCS_BUILD_DIR}/* ."
                        sh 'git add .'
                        sh 'git commit -m "Update docs from Jenkins build ${BUILD_NUMBER}" || true'
                        sh 'git push origin HEAD'
                    }
                }
            }
        }

    }

    post {
        // Always cleans the workspace after the pipeline completes, regardless of success or failure.
        always {
            cleanWs()
        }
    }
}