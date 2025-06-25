pipeline {
    agent any

    environment {
        // Directory where Sphinx builds the HTML output.
        DOCS_BUILD_DIR = 'docs/_build/html'
        // The branch used for GitHub Pages.
        GH_PAGES_BRANCH = 'gh-pages'
        // Jenkins credentials ID for accessing GitHub.
        // Make sure this ID is correctly configured in Jenkins with access to your repository.
        GIT_CREDENTIALS_ID = 'github-credentials'
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
                // Add the Python bin directory to PATH and build the Sphinx documentation.
                sh 'export PATH=$PATH:/Users/andrew/Library/Python/3.9/bin && sphinx-build -b html docs/ ${DOCS_BUILD_DIR}'
            }
        }

        stage('Deploy to GitHub Pages') {
            steps {
                // Uses Jenkins credentials to interact with GitHub.
                // The credentials should be of type 'Username with password' or 'Secret text'.
                withCredentials([usernamePassword(credentialsId: env.GIT_CREDENTIALS_ID, usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                    // Sets up Git user information for commits.
                    sh 'git config --global user.email "jenkins@localhost"'
                    sh 'git config --global user.name "Jenkins"'

                    // Clones the gh-pages branch into a temporary directory.
                    // Using a full URL with credentials directly in the clone command for robust access.
                    sh "git clone --single-branch --branch ${GH_PAGES_BRANCH} https://${GIT_USER}:${GIT_PASS}@${REPO_URL} gh-pages-temp"

                    dir('gh-pages-temp') {
                        // Cleans the existing content in gh-pages to prepare for new documentation.
                        sh 'git rm -rf .'
                        // Copies the newly built documentation into the gh-pages directory.
                        sh "cp -r ../${DOCS_BUILD_DIR}/* ."
                        // Adds all changes, commits, and pushes to the gh-pages branch.
                        // The '|| true' prevents the pipeline from failing if there are no changes to commit.
                        sh 'git add .'
                        sh 'git commit -m "Update docs from Jenkins build ${BUILD_NUMBER}" || true'
                        sh 'git push origin HEAD' // Pushes current branch (gh-pages)
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