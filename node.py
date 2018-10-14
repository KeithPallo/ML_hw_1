class Node:
  def __init__(self, examples = [], label = False):
    self.label = None
    self.children = {}
	# you may want to add additional fields here...
    self.examples = examples
    self.type = type # Leaf or Split

    # If examples are empty, then this is a leaf node and we use label
    # to test
