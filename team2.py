import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team Alpha' # Only 10 chars displayed.
strategy_name = 'Shenanaguens, '
strategy_description = 'the strategy will choose wether to collude or betray at random, then the next move will go based off of what they did in the previouse round.then if we havent been betrayed in the last 20 rounds then collude. then if the opponent has betrayed for more than three then we betray, if nothing else it will pick at random. ' 
def move(We, them, my_history, their_history, my_score, their_score, result):

    if not them.history:
        return 'c'

    if len(them.history) > (We.tournament_attributes['length'] - 3):
        return 'b'

    if len(them.history) < 180:
        if len(them.history) > 6:
            if 'b' not in them.history[:7]:
                 return 'c'

    if them.defections > 3:
        return 'd'
    else:
        return random.choice ('b', 'c')
        
        
def strategy_2(self, opponent):

    
    


answer = random.choice(['b', 'c'])
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = answer
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
         print 'Test passed'
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
