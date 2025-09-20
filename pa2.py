M = [{'':{1}, 'a':{2}},     # state 0 
     {'':{2}},              # state 1 
     {'b':{1,3}},           # state 2 
     {'a':{1,3}}]           # state 3

A = {1,3}                   # accepting states 

def nfa_enclosure(M, s): 
    """
    Returns the ε-closure of state s in the NFA M, which is the set of all states reachable from s by zero or 
    # more ε-transitions. Note that the ε-closure of s always includes s itself."
    
    >>> nfa_enclosure(M, 0)
    {0, 1, 2}
    
    """
    pass

    return
    
def nfs_accepts(M, A, x):
    """
    Takes an NFA M, a set A of accepting states, and a string x. 
    Returns True if M accepts x and False otherwise.

    >>> nfa_accepts(M, A, '') 
    True 
    >>> nfa_accepts(M, A, 'babba') 
    True 
    >>> nfa_accepts(M, A, 'aaba') 
    False 

    """
    pass

    return