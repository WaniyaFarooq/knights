from logic import *
# knave jhoota
# knight sacha
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Biconditional(And(AKnight,AKnave),AKnight),
    
    Or(AKnight,AKnave),Not(And(AKnight,AKnave))
    
    )

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight,AKnave),Not(And(AKnight,AKnave))
    ,Biconditional(And(BKnave,AKnave),AKnight),
    
    Or(BKnight,BKnave),Not(And(BKnight,BKnave)),
    
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
   
    Or(AKnight,AKnave),Not(And(AKnight,AKnave)),
    Or(BKnight,BKnave),Not(And(BKnight,BKnave)),
    Biconditional(Or(And(AKnave,BKnight),And(AKnight,BKnave)),BKnight),

       Biconditional(Or(And(AKnave,BKnave),And(AKnight,BKnight)),AKnight),
     
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
A_said_knight = Symbol("A said 'I am a knight'")
A_said_knave  = Symbol("A said 'I am a knave'")

knowledge3 = And(
    # Identity constraints
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # A said exactly one of the two
    Or(A_said_knight, A_said_knave),
    Not(And(A_said_knight, A_said_knave)),

   # If A is a knight, A's statement must be true
    Implication(AKnight, Implication(A_said_knight, AKnight)),
    Implication(AKnight, Implication(A_said_knave, Not(AKnight))),
    
    # If A is a knave, A's statement must be false
    Implication(Not(AKnight), Implication(A_said_knight, Not(AKnight))),
    Implication(Not(AKnight), Implication(A_said_knave, AKnight)),

    # B's statements
    Biconditional(BKnight, And(
        A_said_knave,
        CKnave
    )),
Biconditional(BKnave, And(
        Not(A_said_knave),
        Not(CKnave)
    )),
    # C's statement
    Biconditional(CKnight, AKnight)
  
)


def main():
    
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave, A_said_knave,]
    
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
