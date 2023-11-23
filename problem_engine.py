import random

NUMBER_MAX = 10

PROBLEM_TYPE_ADD_SUBTRACT = 1
PROBLEM_TYPE_MULTIPLICAITON = 2
PROBLEM_TYPE_VARIED = 3

PROBLEM_DOMAIN_POSITIVE=1
PROBLEM_DOMAIN_POSITIVE_NEGATIVE=2



def generate_problem(prob_type, prob_domain):
    term1 = random.randint(0, NUMBER_MAX)
    term2 = random.randint(0, NUMBER_MAX)
    
    # if we allow both positive and negative numbers, possibly flip the terms
    if prob_domain == PROBLEM_DOMAIN_POSITIVE_NEGATIVE:

        # flip term 1 half the time
        if random.random()>0.5:
            term1 = term1 * -1

        # flip term 2 half the time
        if random.random()>0.5:
            term2 = term2 * -1
            
    if prob_type not in [PROBLEM_TYPE_ADD_SUBTRACT, \
                         PROBLEM_TYPE_MULTIPLICAITON, \
                         PROBLEM_TYPE_VARIED]:
        print(f"Not a valid problem type: {prob_type}")

    if prob_type==PROBLEM_TYPE_ADD_SUBTRACT:
        if random.random()>0.5:
            operation="+"
        else:
            operation="-"
    elif prob_type==PROBLEM_TYPE_MULTIPLICAITON:
        operation="*"

    elif prob_type==PROBLEM_TYPE_VARIED:
        if random.random()<0.333:
            operation="+"
        elif random.random()<0.667:
            operation="-"
        else:
            operation="*"

    problem = f"{term1:>2}  {operation}  {term2:>2}"
    answer = eval(problem)
    return problem, answer
