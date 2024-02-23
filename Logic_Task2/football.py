from logic import *

milan = Symbol("Milan")
real = Symbol("Real")
metalist = Symbol("Metalist")

teams = [milan, real, metalist]

antonio = Symbol("Antonio")
rodrigo = Symbol("Rodrigo")
mykola = Symbol("Mykola")

coaches = [antonio, rodrigo, mykola]

knowledge = And(Or(milan,real,metalist), Or(antonio,rodrigo,mykola))
knowledge.add(metalist)
knowledge.add(Not(And(milan, antonio)))
knowledge.add(Not(And(real, rodrigo)))
knowledge.add(Not(And(metalist, mykola)))

#First condition
#knowledge.add(Implication(metalist, Not(antonio)))
#Second condition
knowledge.add(Not(And(real, mykola)))
knowledge.add(Implication(real, Not(mykola)))
knowledge.add(And(Not(real), Not(mykola)))
knowledge.add(And(rodrigo))

print(knowledge.formula())
for coach in coaches:
    print(coach, model_check(knowledge, coach))




