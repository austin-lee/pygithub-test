"""
해당 파이썬 스크립트를 실행하기 위해 필요한 파라미터는 argparse 를 이용하여 입력하도록 하였습니다.
나머지는 Pygithub 라이브러리를 이용하여 작성을 하였고,
리뷰어가 accounts 목록에 있는 경우에 approval을 해제하기 위해 Dismiss 함수를 호출하여 처리하였습니다.
"""

import argparse
from github import Github

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='pygithub pull request checker')
    parser.add_argument('--access-token', help="User Token Info")
    parser.add_argument('--repo-name', help="Repository Name")
    parser.add_argument('--accounts', nargs='+', help="Account list")
    parser.add_argument('--pr-num', help="Pull Request Number", type=int)

    args = parser.parse_args()

    # using an access token
    g = Github(args.access_token)

    # project name
    project_name = args.repo_name

    # login id
    accounts = args.accounts
    print(accounts)

    # pull request num
    pr_num = args.pr_num

    # get repository
    repo_info = g.get_repo(project_name)
    # get pull request
    pr_info = repo_info.get_pull(pr_num)
    # get reviewers
    reviewers = pr_info.get_reviews()

    # check dismiss user
    dismiss_list = []
    for reviewer in reviewers:
        if reviewer.user.login in accounts:
            dismiss_list.append(reviewer)

    # process dismiss
    if len(dismiss_list) == 0:
        print("Pull Request is APPROVAL")
    else:
        for user in dismiss_list:
            user.dismiss("Dismissing a pull request review")

