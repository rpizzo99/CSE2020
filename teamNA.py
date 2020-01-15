####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E0'
strategy_name = 'Collude'
strategy_description = 'Always collude.'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'd'
    elif their_history[-1]=='d'and their_history[-2]=='d':
        return 'd'
    else:
        return 'c'
        
    
