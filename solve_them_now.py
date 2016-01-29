# get set and start solving!!!
# RUN this to get a problem on your browser.
# hugs or bugs at sagar.pp6@gmail.com

__author__ = 'sagarpatel26'

from urllib import request
import json
import random
import webbrowser

def fetch_page_as_string(url = None):
    '''
        This function takes in a parameter url and return a string representing
        the Http Response, obtained at the given URL.

        NOTE:- Functions is bottleneck to the script performance, consider cahching
                the response if the update is not too frequent.

        Paramters:-
            url: the url of the page to be fetched.

        Returns:-
            http_response_string: string representing the Http Response obtained
            from the given url.
    '''
    print('fetching the response from ' + url)

    # fetch the response, read them as bytes and convert the read bytes to string
    # using decode() method.
    http_response_string = request.urlopen(url).read().decode()

    print('response from ' + url +' fetched successfully!!')
    return http_response_string



def get_problem_codeforces(tag = 'not_specified'):
    '''
        Currently function returns, an url to a randomly chosen problm from
        codeforces problemset.

        Parameters:-
        tag: based on the input tag the problems are filtered. It might happen-
            there exists no problem, with given tag. In that case the function-
            raises an Exception.

        Returns:-
            to_solve_url: A url to the randomly chosen problem.
    '''

    # TODO:
    # 1. add a feature that if user<parameter> is not returned a problem(url), which he/she has already solved.
    # 2. add a filter based on the difficulty of problems(A-E), index<parameter>
    # done ---- 3. add a feature that provides problems of based on some tag<parameter>

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

    codeforces_request_url = CODEFORCES_URL
    # if the tag is defined and the query string for the tag.
    if tag != 'not_specified':
        codeforces_request_url = codeforces_request_url + '?tags=' + tag

    # TODO: think of caching the response page, for increasing the performance.
    api_response = fetch_page_as_string(codeforces_request_url)
    api_response_json_dict = json.loads(api_response)

    if (api_response_json_dict['status']!='OK'):
        raise Exception('Problem with Codeforces API!!')

    all_problems = api_response_json_dict['result']['problems']
    if (len(all_problems)==0):
        raise Exception('No Such Tag!!')

    to_solve = random.choice(all_problems)
    to_solve_url = CODEFORCES_PROBLEM + str(to_solve['contestId']) + '/' + to_solve['index']
    return to_solve_url


if __name__ == '__main__':
    webbrowser.open(get_problem_codeforces('math'))
