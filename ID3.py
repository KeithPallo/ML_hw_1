from node import Node
import math


def ID3(examples, default, root = True):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node)
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"

  Itype: List of Dictionaries

  '''

  if root == True:
    examples_c = []

    for i in examples:
        deep = i.copy()
        examples_c.append(deep)
  else:
    examples_c = examples


  if not examples_c:
    return Node(label = default)

  elif same_class(examples_c) or no_non_trivial(examples_c):
    mode = choose_mode(examples_c)
    return Node(label = mode)

  else:
      #print(examples)
      attribute, examples_list = choose_best(examples_c)
      t = Node(label = attribute)
      mode = choose_mode(examples_c)

      for i in examples_list:
        split_attribute = i[0][attribute]

        for j in i:
            del j[attribute]

        subtree = ID3(i,mode,False)
        #subtree.parent_split(attribute)
        t.add_subtree(subtree,split_attribute)

      return t



def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''
  # check to see type of node
  # if leaf, test vs. mode of current

  # split and pass based on attributes

  # pass in examples to current node
  pass

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''
  #print(examples )
  num_tested = 0
  num_correct = 0

  for i in examples:
    #print(i)
    num_tested += 1

    predict = evaluate(node,i)
    correct = i["Class"]

    if predict == correct:
      num_correct += 1

  return (num_correct / num_tested)

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
  x = node.evaluate(example)

  return x



# Custom definitions created
# -----------------------------------------------------------------------------
def test_example(node,example):
    pass

def ID3_build(examples,default):
    pass

def choose_best(examples):


    # Create a list of all possible attributes
    potential_splits = list(examples[0].keys())
    potential_splits.remove("Class")

    # Initialize constants
    split_val = 10000
    attribute = "None"
    examples_list = []

    # For all possible splits, check if min entropy
    for i in potential_splits:

        # Calculate entropy and partitioned examples
        current, values = entropy(examples,i)
        if current < split_val:
            split_val = current
            attribute = i
            examples_list = values

    return attribute, examples_list


def entropy(examples,i):
  # i is the split attribute


  entropy = 0
  list_of_groups = [] # Type list of list of dictionary
  g_num = 0
  dict_of_groups = {}
  num_examples = 0

  # accumulate all possible outputs from split i
  for j in examples:

    num_examples += 1
    current = j[i]

    if current in dict_of_groups.keys():
      position = dict_of_groups[current]
      list_of_groups[position].append(j)

    else:
      dict_of_groups[current] = g_num
      g_num += 1
      list_of_groups.append([j])

  for k in list_of_groups:
      in_list = len(k)
      nested_prob = 0

      # Calculate the number of total classes in this sample
      # m is of type dictionary. Keys are possible classes
      # and values are number of time appeared in this group
      m = class_counter(k)

      # Calculate entropy for each individual output
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

    # return False

    first = list(examples[0].items())
    first = [i for i in first if i[0] != "Class"]

    for i in range(1,len(examples)):
        current = list(examples[i].items())
        current = [j for j in current if current[0] != "Class"]

        if current != first:
            return False


    return True

"""
"""



#print(type(data))
#print(same_class(data))
#print(ID3(data,"fail"))

data = [dict(a=1, b=0, Class=0), dict(a=1, b=1, Class=1)]
tree = ID3(data, 0)
#print(tree.children)
#print(tree.label)
#print(evaluate(tree, dict(a=1, b=0)))
