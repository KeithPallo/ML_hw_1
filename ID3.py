from node import Node
import math

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node)
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"

  Itype: List of Dictionaries

  '''

  if not examples:
    return node(type = default)

  elif same_class(examples) or no_non_trivial(examples):
    mode = choose_mode(examples)
    return node(label = mode)

  else:
      pass

def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''
  pass

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''
  # num correct
  # num tested

  # Predict value
  # correct or not
  # update ratio

  # return accuracy

  pass


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
  pass

# Custom definitions created

def test_example(node,example):
    pass

def ID3_build(examples,default):
    pass

def choose_best(examples):
    # represents

    potential_splits = list(examples[0].keys())

    potential_splits.remove("Class")

    #print(potential_splits)

    split_val = -10000
    attribute = "None"

    for i in potential_splits:
        pass
        current, vals = entropy(examples,i)
        #split_val = max(split_val,current)

    return attribute

    # For all potential splits
        # sum ( num of elements in split * E(class))

def entropy(examples,i):


  # Split on the i for each
  entropy = 0
  list_of_groups = [] # Type list of list of dictionary
  g_num = 0
  dict_of_groups = {}

  for j in examples:

    current = j[i]
    #print(current)

    if current in dict_of_groups.keys():
      position = dict_of_groups[current]
      list_of_groups[position].append(j)

    else:
      dict_of_groups[current] = g_num
      g_num += 1
      list_of_groups.append([j])

  for k in list_of_groups:








def choose_mode(examples):
    #print(examples)
    dict_of_freq = dict()

    for i in examples:
        current = i["Class"]

        if current not in dict_of_freq:
            dict_of_freq[current] = 1
        else:
            dict_of_freq[current] += 1

    return max(dict_of_freq,key=dict_of_freq.get)


def same_class(examples):
    """
    Itype: List of Dictionaries
    Rtype: Boolean. True if all same classifcation or empty.
    """

    if not examples:
        return

    check_list = []

    for i in examples:
        if not check_list:
            check_list.append(i["Class"])
        else:
            current = i["Class"]
            if current not in check_list:
                return False

    return True


def no_non_trivial(examples):
    return False




data = [ dict(a=1, b=1, Class=1), dict(a=2, b=1, Class=1),dict(a=3, b=0, Class=1), dict(a=3, b=1, Class=1)]

#print(type(data))
#print(same_class(data))

print(entropy(data,"a"))
