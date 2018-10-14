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
    return Node(label = mode)

  else:
      attribute, examples_list = choose_best(examples)
      t = Node(label = attribute,examples = examples_list)

      for i in examples_list:
        subtree = ID3(i,choose_mode(i))
        t.add_subtree(subtree,subtree.split_type())

      return t



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




# Custom definitions created
# -----------------------------------------------------------------------------
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
    examples_list = []

    for i in potential_splits:

        current, values = entropy(examples,i)
        if current > split_val:
            split_val = current
            attribute = i
            examples_list = values

    return attribute, examples_list

    # For all potential splits
        # sum ( num of elements in split * E(class))

def entropy(examples,i):


  # Split on the i for each
  entropy = 0
  list_of_groups = [] # Type list of list of dictionary
  g_num = 0
  dict_of_groups = {}
  num_examples = 0


  for j in examples:

    num_examples += 1
    current = j[i]
    #print(current)

    if current in dict_of_groups.keys():
      position = dict_of_groups[current]
      list_of_groups[position].append(j)

    else:
      dict_of_groups[current] = g_num
      g_num += 1
      list_of_groups.append([j])
  #print(i, list_of_groups)
  for k in list_of_groups:
      in_list = len(k)
      nested_prob = 0

      m = class_counter(k)

      for n in m.values():
          lg_val = math.log((n/in_list),2)
          nested_prob += (n/in_list) * (lg_val)

      entropy += (in_list / num_examples) * nested_prob
  return entropy, list_of_groups





def class_counter(examples):
    dict = {}

    for i in examples:
        class_current = i["Class"]

        if class_counter in dict.keys():
            dict[class_counter] += 1
        else:
            dict[class_counter] = 1

    return dict




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
        return False

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




data = [ dict(a=1, b=1, Class=2), dict(a=2, b=1, Class=1),dict(a=3, b=0, Class=1), dict(a=3, b=1, Class=1)]

#print(type(data))
#print(same_class(data))
#print(ID3(data,"fail"))
