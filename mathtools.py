#!/usr/bin/env python
#title           :mathtools.py
#description     :math function library
#author          :Moises Holguin
#date            :09-22-2013
#python_version  :2.7.3
#==============================================================================

"math function library"

def fact(n):
    '''-> n-factorial computed iteratively in a for loop
       O(n) time, O(1) space'''
    total = 1
    for number in xrange(n):
        total *= number + 1
    return total

def fact2(n):
    '''-> n-factorial computed iteratively in a while loop
       O(n) time, O(1) space'''
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total

def factR(n):
    '''-> n-factorial computed recursively
       O(n) time, O(n) space as python cannot optimize recursion'''
    if n < 2:
        return 1
    return n * factR(n-1)

def fact1(n):
    '''-> n-factorial computed by a single line of code
       O(n) time, O(1) space'''
    return reduce(lambda x, y: x * y, [n+1 for n in xrange(n)], 1)

def fib(n):
    '''-> nth Fibonacci number computed iteratively
       O(n) time, O(1) space'''
    first, second = 0, 1
    if n == 0: return 0
    for i in xrange(n):
        first, second = second, first + second 
    return first

def fibs(n):
    '''Generator function yielding the Fibonacci numbers up to fib(n)
       O(n) time, O(1) space'''
    i, first, second = 0, 0, 1
    while i < n + 1:
        yield first
        first, second = second, first + second
        i += 1

def fibR(n):
    '''-> nth Fibonacci number computed with 2 recursive calls
       what's bad about this algorithm?'''
    if n in [0, 1]: return n
    return fibR(n-1) + fibR(n-2)
    
def rPascal(L):
    '''given nth row of Pascal's triangle as a list L -> (n+1)th row
       O(len(L)) time and space'''
    i = 0
    pascalLine = [1]
    if L == pascalLine: return [1, 1]
    while i < len(L) - 1:
        pascalLine += [L[i] + L[i+1]]
        i += 1
    return pascalLine + [1]

def rPascal1(L):
    '''single line version of rPascal
       O(len(L)) time and space'''
    return [1] + [pair[0] + pair[1] for pair in zip(L[:-1], L[1:])] + [1]

def tPascal(n):
    '''-> first n+1 rows of Pascal's triangle as a list of lists
       the nth row represents the binomial coefficients of (x+y)**n
       O(n**2) time and space'''
    triangle = [[1]]
    if n == 0: return triangle
    triangle.append([1, 1])
    if n == 1: return triangle
    i = 0
    while i < n - 1:
        triangle.append(rPascal(triangle[-1])) # one line version of commented out code
#        j = 0
#        line = [1]
#        while j < len(triangle[-1]) - 1:
#            line += [triangle[-1][j] + triangle[-1][j+1]]
#            j += 1
#        triangle.append(line + [1])
        i += 1
    return triangle

def tPascal1(n):
    '''single line version of tPascal which reuses rPascal1
       O(n**2) time and space'''
   # return [1] + [rPascal1() for x in xrange(n)]
   # return reduce()
    pass

def getCombinationsFunc(maxN):
    '''-> a function c(n, k) where n must be passed a value <= maxN
       c(n, k) -> the number of ways to choose k items from a set of size n
       getCombinationsFunc(maxN) = O(maxN**2) time and space
       c(n, k) = O(1) time and space'''
    def combinations(n, k):
        if n <= maxN: return fact(n) / (fact(k) * fact(n-k))
        else: print 'First parameter n must be less than or equal to', maxN
    return combinations

def permutations(n, k):
    '''-> number of ways to order r items chosen from a set of size n
       O(k) time, O(1) space'''
    return fact(n) / fact(n-k)

# accept_sequence(f) is a decorator for any function f(*args)
# -> a function w(*args) such that:
# w(one_iterable_argument) -> f(argument_unpacked)
# otherwise, w(*args) -> f(*args)
# accept_sequence(f) = O(1) time and space
# w has identical time and space complexity to f'''
def accept_sequence(f):  # EXTRA CREDIT
    pass

def is_iterable(obj):  # EXTRA CREDIT - helps with accept_sequence
    '''-> True or False depending on whether obj is iterable
       O(1) time and space'''
    import collections
    return isinstance(obj, collections.Iterable) or hasattr(obj, '__iter__')

def powerList(*args):
    '''-> a list of tuples representing all possible subsets of args
       O(2**len(args)) time and space'''
    powerset = []
    for n in xrange(2**len(args)):
        subset = []
        for index, value in enumerate(args):
            if n & 2**index: subset.append(value)
        powerset.append(tuple(subset))
    return powerset

def powerList1(*args):
    '''single line version of powerList
       O(2**len(args)) time and space'''
    return [tuple([v for i, v in enumerate(args) if n&2**i]) for n in xrange(2**len(args))]

def permuteSetR(*args):  # EXTRA CREDIT
    '''-> every permutation of args as a list of tuples computed recursively
       O(n(n!))) time and space, where n = len(args)'''
    pass

def permuteSetG(*args):  # EXTRA CREDIT
    '''Generator function yields each permutation of args.
       O(n(n!)) time, O(n) or O(n**2) space, where n = len(args)'''
    pass

def perms1(S):  # EXTRA EXTRA CREDIT, 80 character limit relaxed
    '''-> every permuataion of elements of S. Single line version.
       O(n(n!))) time and space, where n = len(S)'''
    pass


if __name__ == '__main__':
    # PUT YOUR TESTING CODE HERE
    count = [0, 0]
    failures = []
    print "\ntesting mathtools module\n"
    
    def tester(name, variables, answers, function):
        print "Testing", name
        for answer, variable in zip(answers, variables):
            outcome = "PASSED" if function(variable)==answer else "***FAILED***"
            if outcome == "PASSED": count[0] += 1
            else:
                count[1] += 1
                failures.append(name)
            print "\tTest Case:", name, "for", variable, outcome

    # factorial function testing
    names = ['fact(n)', 'fact2(n)', 'factR(n)', 'fact1(n)']
    functions = [fact, fact2, factR, fact1]
    for name, function in zip(names, functions):
        tester(name, [0, 1, 10, 100],[1, 1, 3628800, 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000L], function)

    # fibonocci sequence testing
    names = ['fib(n)']
    functions = [fib]
    for name, function in zip(names, functions):
        tester(name, [0, 1, 2, 20, 100], [0, 1, 1, 6765, 354224848179261915075L], function)
    
    # fibonocci recursive function
    names = ['fibR(n)']
    functions = [fibR]
    for name, function in zip(names, functions):
        tester(name, [0, 1, 2, 5, 20], [0, 1, 1, 5, 6765], function)

    # fibonocci sequence generator function
    model = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    test = []
    print 'Testing fibs(n)'
    for i in fibs(10): test.append(i)
    outcome = 'PASSED' if model==test else 'FAILED'
    if outcome == "PASSED": count[0] += 1
    else:
        count[1] += 1
        failures.append('fibs(n)')
    print '\tTest Case: fibs(n) for 10', outcome

    # rPascal testing
    names = ['rPascal(n)', 'rPascal1(n)']
    functions = [rPascal, rPascal1]
    for name, function in zip(names, functions):
        tester(name, [[1], [1,1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]], [[1, 1], [1, 2, 1], [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]], function)

    # tPascal testing
    names = ['tPascal(n)', 'tPascal1(n)']
    functions = [tPascal, tPascal1]
    for name, function in zip(names, functions):
        tester(name, [1, 2, 10], [[[1], [1, 1]], [[1], [1, 1], [1, 2, 1]], [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1], [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]]], function)

    # combinations testing
    c = getCombinationsFunc(100)
    print 'Testing getCombinationsFunc(nMax)'
    print 'Testing c(n, k) with nMax 100'
    outcome = 'PASSED' if c(0,0)==1 else 'FAILED'
    if outcome == "PASSED": count[0] += 1
    else:
        count[1] += 1
        failures.append('c(n, k)')
    print '\tTest Case: n(c, k) for 0,0', outcome 
    outcome = 'PASSED' if c(60,23)==23385332420868600L else 'FAILED'
    if outcome == "PASSED": count[0] += 1
    else:
        count[1] += 1
        failures.append('c(n, k)')
    print '\tTest Case: n(c, k) for 60,23', outcome
    outcome = 'PASSED' if c(100,50)==100891344545564193334812497256L else 'FAILED'
    if outcome == "PASSED": count[0] += 1
    else:
        count[1] += 1
        failures.append('c(n, k)')
    print '\tTest Case: n(c, k) for 100,50', outcome

    # permutations testing
    print 'Testing permutations(n, k)'
    outcome = 'PASSED' if permutations(7,5)==2520 else 'FAILED'
    if outcome == "PASSED": count[0] += 1
    else:
        count[1] += 1
        failures.append('permutations(n, k)')
    print '\tTest Case: permutations(c, k) for 7,5', outcome
    outcome = 'PASSED' if permutations(7,1)==7 else 'FAILED'
    if outcome == "PASSED": count[0] += 1
    else: 
        count[1] += 1
        failures.append('permutations(n, k)')
    print '\tTest Case: permutations(c, k) for 7,1', outcome

    # powerlist testing
    print 'Testing powerList(*args)'
    outcome = 'PASSED' if powerList(1, 2, 3)==[(), (1,), (2,), (1, 2), (3,), (1, 3), (2, 3), (1, 2, 3)] else 'FAILED'
    if outcome == "PASSED": count[0] += 1
    else:
        count[1] += 1
        failures.append('powerList(*args)')
    print '\tTest Case: powerList(*args) for 1,2,3', outcome
    outcome = 'PASSED' if powerList(1.2,'hello',False)== [(), (1.2,), ('hello',), (1.2, 'hello'), (False,), (1.2, False), ('hello', False), (1.2, 'hello', False)] else 'FAILED'
    if outcome == "PASSED": count[0] += 1
    else:
        count[1] += 1
        failures.append('powerList(*args)')
    print '\tTest Case: powerList(*args) for 1.2,\'hello\',False', outcome
    print 'Testing powerList1(*args)'
    outcome = 'PASSED' if powerList1(1, 2, 3)==[(), (1,), (2,), (1, 2), (3,), (1, 3), (2, 3), (1, 2, 3)] else 'FAILED'
    if outcome == "PASSED": count[0] += 1
    else:
        count[1] += 1
        failures.append('powerList1(*args)')
    print '\tTest Case: powerList1(*args) for 1,2,3', outcome
    outcome = 'PASSED' if powerList1(1.2,'hello',False)== [(), (1.2,), ('hello',), (1.2, 'hello'), (False,), (1.2, False), ('hello', False), (1.2, 'hello', False)] else 'FAILED'
    if outcome == "PASSED": count[0] += 1
    else:
        count[1] += 1
        failures.append('powerList1(*args)')
    print '\tTest Case: powerList1(*args) for 1.2,\'hello\',False', outcome 

    # Display results
    print '\n===================='
    print 'TOTAL TESTS:', count[0] + count[1]
    print 'PASSED:', count[0]
    print 'FAILED:', count[1]
    if count[1] > 0:
        print 'INSPECT THE FOLLOWING'
        for failure in set(failures):
            print '==>', failure
    
    print '===================='
    print 'TESTING COMPLETE'
    print '===================='
