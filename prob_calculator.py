import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    '''
    Initializes the hat
    
    Parameters
    ----------
      kwargs 
        number of balls of each color example: black=2
    
    Returns
    -------
    None
    '''
    self.contents = []
    for kwarg, val in kwargs.items():
      for _ in range(val):
        #print(kwarg)
        self.contents.append(kwarg)

  def draw(self, nballs):
    '''
    Function to draw balls from the hat
    
    Parameters
    ----------
      nballs : object
        number of balls to draw
    
    Returns
    -------
    float
      probability that the the expected amount of balls will be drawn at a minimum
    '''
    lballs = []
    nballs = min(nballs, len(self.contents))
    for _ in range(nballs):
      lballs.append(self.contents.pop(random.randrange(len(self.contents))))
    return lballs

    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  '''
  Function to define an experiment to determine probability of drawing expected balls
  
  Parameters
  ----------
    kwargs 
      number of balls of each color example: black=2
  
  Returns
  -------
  None
  '''
  m = 0
  
  for _ in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    drawn_balls = new_hat.draw(num_balls_drawn)
    req_balls = 0
    for kwarg, val in expected_balls.items():
      if drawn_balls.count(kwarg) >= val:
        req_balls += 1 
    if req_balls == len(expected_balls): m += 1 
  return m/num_experiments
  
