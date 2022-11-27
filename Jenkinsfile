/*
 * Jenkins File
 * Jenkins python, docker plugin install
 * python 3.9 기준 빌드이므로 docker image 는 python 3.9 로 설정
 * Jenkins 빌드 기준 설정 필요 (GitHub Pull Request Builder)
 * Stage 는 파라미터에 python 파일 실행하는 스크립트로 작성
 */

pipeline{
    agent any
    stages {
        //Excute Script
        stage('Execute Script') {
            environment {
                GITHUB_ACCESS_TOKEN = credentials("github-access-token")
            }
            steps{
                echo 'Execute Script'
                script {
                    echo "${env.sha1}"
                    echo "${env.ghprbPullId}"
                    echo "${env.ghprbPullLink}"
                    sh """
                        pip3 install PyGithub
                        python3 python_ci.py --access-token ${env.GITHUB_ACCESS_TOKEN} --repo-name austin-lee/pygithub-test --accounts bot1 bot2 --pr-num 6
                       """
                }
            }
        }
    }
}
