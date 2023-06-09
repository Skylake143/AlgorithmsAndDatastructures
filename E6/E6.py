global bool_weight
bool_weight = False
global bottomupweights
bottomupweights = [3,9,14,5,16,10,25,2]     


def recursive_weight_adder(weights, elements, w):
    global bool_weight
    if bool_weight == True: return True

    if len(weights)==0: return False

    local_weights = weights.copy()
    for weight in local_weights:
        local_elements = elements.copy()

        local_elements.append(weight)
        local_weights.remove(weight)
        if sum(local_elements)==w: 
            return True
        bool_weight = recursive_weight_adder(local_weights.copy(), local_elements.copy(), w)
    return bool_weight

def bottom_up_balance(n, w):
    global bottomupweights
    if n==1: 
        if w==0 or w==bottomupweights[0]:
            return True
        else: return False
    else: 
        withThisWeight = bottom_up_balance(n-1, w-bottomupweights[n])
        withoutThisWeight = bottom_up_balance(n-1, w)
        if withThisWeight or withoutThisWeight: return True
        else: return False

def closest

if __name__ == "__main__":
    w = 20
    elements = []
    print("Recursive Weight Balance: ", recursive_weight_adder(bottomupweights, elements, w))
    print("Bottom-Up: ", bottom_up_balance(len(bottomupweights)-1,w))

