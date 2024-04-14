class DecisionNode:
    def __init__(self, decision, true_branch=None, false_branch=None):
        self.decision = decision
        self.true_branch = true_branch
        self.false_branch = false_branch

    def evaluate(self, data):
        return self.decision(data)


def create_decision_tree(decision_func):
    def true_branch_factory():
        return create_decision_tree(decision_func)

    def false_branch_factory():
        return create_decision_tree(decision_func)

    return DecisionNode(decision_func, true_branch_factory, false_branch_factory)


# Example usage:
def decision_function(data):
    return data > 5

infinite_tree = create_decision_tree(decision_function)

# Lazy evaluation of the tree
data = 3
current_node = infinite_tree
while True:
    decision = current_node.evaluate(data)
    print("Decision:", decision)
    if decision:
        current_node = current_node.true_branch()
    else:
        current_node = current_node.false_branch()
