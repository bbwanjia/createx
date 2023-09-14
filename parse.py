from action import Action
def extract(commands:list[str]) -> Action:
    check = Action.check_eligibility(commands)
    if check:
        raise check
    # passes check
    return Action(commands=commands)


def _quit() -> int:
    print("EXIT\n\n")
    return 0
    
    
def _create() -> int:
    ...
    
    
def _edit() -> int:
    ...
    
    
def _make() -> int:
    ...
    
    
def _help() -> int:
    ...
    
      
def _quit() -> int:
    ...
    
        
def _del() -> int:
    ...
