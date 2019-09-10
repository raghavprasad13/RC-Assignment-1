# RC Assignment 1

## Components of Assignment 1:

- [x] Check if formula entered is valid or not
- [x] Check DNF formula satisfiability
- [x] Check CNF formula satisfiability
- [x] Convert any given formula to CNF
- [x] Convert any given formula to DNF

### Formula validity checker
While using the formula validity checker, use the following symbols for the operators:

* **.** corresponds to AND
* **+** corresponds to OR
* **!** corresponds to NOT
* **>** corresponds to IMPLICATION
* **<** corresponds to BI-IMPLICATION

**An example of a correct formula**: `(s<(r>(!(p+q))))`  
**An example of an incorrect formula**: `s+(r.p.q)` [due to missing parantheses]

Additionally, it generates a prefix expression on the valid formula which is the prescribed input format for the **Converter to CNF/DNF**

For example:  
`(s<(r>(!(p+q))))` generates `[['iff', 's', ['if', 'r', ['not', ['or', 'p', 'q']]]]]`

**Warning**: This entire system has been built with the restriction that the letter `X` cannot be used in any formulae.

### DNF and CNF Satisfiability checkers
The inputs to the CNF and DNF SAT checkers are sets of clauses, which in turn are sets of literals.  
Thus, a sample input would look like: `[['s'], ['!r', '!p'], ['!r', '!q']]`

The atomic propositions preceded by a `!` indicate a negated literal.

The output is `True` if the formula is satisfiable and `False` otherwise

### Converter to CNF/DNF
The input to the Converter to CNF/DNF is a prefix expression of the formula. The output is the corresponding CNF/DNF formula in the same prefix notation.

For example:  
`[['or', 's', ['and', 'r', ['or', 'p', 'q']]]]` produces the CNF,  
`['and', ['or', 'r', 's'], ['or', 'p', 'q', 's']]` and the DNF,  
`['or', 's', ['and', 'p', 'r'], ['and', 'q', 'r']]`
