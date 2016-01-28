# get set and start solving!!!
# RUN this to get a problem on your browser.
# hugs or bugs at sagar.pp6@gmail.com

__author__ = 'sagarpatel26'

from urllib import request
import json
import random
import webbrowser

def get_problem_codeforces():
    '''
        This function returns, an url to a randomly chosen problm from codeforces problemset.

        TODO:
        1. add a feature that if user<parameter> is not returned a problem(url), which he/she has already solved.
        2. add a feature that provides problems of based on some tag<parameter>
        3. add a filter based on the difficulty of problems(A-E)

    '''


    CODEFORCES_PROBLEM = 'http://codeforces.com/problemset/problem/'
    CODEFORCES_URL = 'http://codeforces.com/api/problemset.problems/'

    # json format, of the api response:-
    # {'status':....,
    #   'result':{'problems': [
    #                 {
    #                    contestId:- Integer. Id of the contest, containing the problem.
    #                    index:- String. Usually a letter of a letter, followed by a digit,
    #                           that represent a problem index in a contest.
    #                    name:- String. Localized.
    #                    type:- Enum: PROGRAMMING, QUESTION.
    #                    points:- Floating point number. Can be absent. Maximum ammount of points for the problem.
    #                    tags:- String list. Problem tags.
    #                }, ........
    #           ]
    #       }
    # }

    print('fetching the problems!!')
    # api_response string of the json response
    api_response = request.urlopen(CODEFORCES_URL).read().decode()
    print('problems fetched successfully!!')
    api_response_json_dict = json.loads(api_response)
    if (api_response_json_dict['status']!='OK'):
        raise Exception
    all_problems = api_response_json_dict['result']['problems']
    to_solve = random.choice(all_problems)
    to_solve_url = CODEFORCES_PROBLEM + str(to_solve['contestId']) + '/' + to_solve['index']
    return to_solve_url


if __name__ == '__main__':
    webbrowser.open(get_problem_codeforces())
