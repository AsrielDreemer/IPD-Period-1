 ####
# Each team's file must define four tokens:
# team_name: a string
# strategy_name: a string
# strategy_description: a string
# move: A function that returns 'c' or 'b'
####

team_name = 'Team4'
strategy_name = 'Payback.'
strategy_description = 'Betray if they have betrayed 3 or more times.'

def move(my_history, their_history, my_score, their_score):
 if len(my_history)==0: # It's the first round; collude.
  return 'c'
 elif len(their_history) < 180: #If its the last or second to last turn; betray.
  if len(their_history) > 6:
   if 'b' not in their_history[:7]:
    return 'c'
 elif their_history[3] <= 'b' : #If they have betrayed 3 or more times; betray.
  return 'b'
 else: #If all else fails; collude.
  return 'c'

      
