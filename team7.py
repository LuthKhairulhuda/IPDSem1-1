# -*- coding: utf-8 -*-
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Lucy K#7' # Only 10 chars displayed.
strategy_name = 'lots of code'
strategy_description = '''Main strategy is titfortat or doing the other
person's last move. Combats alternating by betraying. Checks previous rounds
for similar scenario. After 49 rounds, betray.
'''
import random


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    #final strategy
    if len(their_history) == 0:
        return 'c'
    else:
        recent_round_them = their_history[-1]
        recent_round_me = my_history[-1]
        if 'c' not in their_history: #if they always betray
            return 'b'
        elif 'cbc' in their_history[0:2] or 'bcb' in their_history[0:2]: #if they alternate, do this
            return 'b'
        for round in range(len(my_history)-1): #see E4, compares the history to see if there is something similar
            prior_round_them = their_history[round]
            prior_round_me = my_history[round]
            if (prior_round_me == recent_round_me) and \
                    (prior_round_them == recent_round_them):
                return their_history[round]
        if my_history[-1]=='c' and their_history[-1]=='b':
            return 'b' 
        elif len(my_history) >= 49 and 'b' not in my_history:
            return 'b'
        else:
            return their_history[-1] #titfortat strategy
        
    
    #second strategy(fail)
    '''
    betrayed = False
    if len(their_history) == 0:
        return 'c'
    if len(their_history) >= 2:
        if random.random()<0.01:
            return 'b'
        else:
            return 'c'
        if 'b' in their_history[-2:]:
            return 'b'
        elif 'b' in my_history[-1] and 'c' in their_history[-1]:
            return 'c'
        elif 'b' in my_history[-2] and 'b' in their_history[-1]:
            betrayed = True
            return 'b'
        elif betrayed == True:
            return 'b'
    '''
    #first strategy
    '''
    if len(their_history) == 0:
        return 'c'
    if 'b' in their_history[-2:]:
        return 'b'
    else:
        if random.random()<0.01:
            return 'b'
        else:
            return 'c'
    '''
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print('Test passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             