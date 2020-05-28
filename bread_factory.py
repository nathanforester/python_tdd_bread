ingredient1 = 'water'
ingredient2 = 'flour'
def make_dough(ingredient1, ingredient2):
    if (ingredient1 == 'water' and ingredient2 == 'flour') or (ingredient1 == 'flour' and ingredient2 == 'water'):
        return 'dough'
    else:
        return 'not dough'

def bake_bread(dough):
    if dough =='baked':
        return 'bread baked'
    else:
        return 'bread not baked'



def wholewheat(ingredient1, ingredient2):
    if ingredient1== 'water' and ingredient2=='wholewheat flour':
        return 'factory downtime more effective and new markets'
    else:
        return 'factory downtime not more effective and no new markets'

def wholewheat_sell(dough):
    if dough=='baked':
        return 'sell to niche clients'
    else:
        return 'cannot sell to niche clients'





