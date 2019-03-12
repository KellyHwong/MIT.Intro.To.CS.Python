# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return sequence
    elif len(sequence) == 2: 
        return [sequence, sequence[::-1]]
    elif len(sequence) > 2:
        temp = get_permutations(sequence[1:])
        ret = []
        for perm in temp:
            for i in range(len(perm) + 1):
                ret.append(perm[:i] + sequence[0] + perm[i:])
        # return [sequence[0] + perm for perm in temp]
        return ret
    # pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    sequence = "abc"
    # sequence = "abcd"
    print(get_permutations(sequence))
    # pass #delete this line and replace with your code here

