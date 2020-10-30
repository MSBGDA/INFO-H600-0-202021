import random

# Your code here

if __name__=="__main__":
    l = (["John",    42, ["Bruxelles", "Paris"]],
         ["Ken",     18, ["Namur"]],
         ["Jack",    15, ["Bruxelles"]],
         ["Arthur",  15, ["Liege"]],
         ["Leonard", 15, ["Hasselt"]],
         ["Luke",    15, ["Bruxelles", "Hasselt"]],
         ["Ben",     23, ["Paris"]],
         ["Lee",     44, ["Gent", "Oostende"]],
         ["Alfred",  54, ["Namur", "Liege", "Bruxelles"]],
         ["Leonard", 15, ["Hasselt"]],
         ["Stephen", 23, ["Brugges"]],
         ["Marty",   66, ["Bruxelles", "Gent"]],
         ["Fred",    43, ["Bruxelles", "Hasselt"]],
         ["Paul",    17, ["Paris"]],
         ["Frank",   39, ["Gent", "Oostende"]],
         ["George",  81, ["Namur", "Liege", "Paris"]],
         ["Albert",  27, ["Bruxelles", "Hasselt"]],
         ["Stan",    43, ["Paris"]],
         ["Peter",   74, ["Gent", "Oostende"]],
         ["Guy",     44, ["Namur", "Gent", "Bruxelles"]],
         ["Simon",   13, ["Bruxelles", "Hasselt"]],
         ["Rudolph", 23, ["Paris"]],
         ["Mark",    44, ["Gent", "Oostende"]],
         ["Karl",    54, ["Namur", "Bruxelles"]],
         ["Damien",  32, ["Oostende"]])

    people = [People(*li) for li in l]
    random.seed(0)
    for i in range(20):
        a = people[random.randint(0, len(people)-1)]
        b = people[random.randint(0, len(people)-1)]
        if a == b:
            pass
        if play_rps(a, b):
            print(a.get_name() + " won against " + b.get_name())
        else:
            print(b.get_name() + " won against " + a.get_name())

    """ Should print:
    Damien won against Fred
    Rudolph won against Stephen
    Stephen won against Lee
    Arthur won against Leonard
    Stephen won against Peter
    Frank won against George
    Paul won against Stephen
    Ben won against Luke
    Ken won against Guy
    Rudolph won against Frank
    Karl won against Stephen
    John won against Guy
    Rudolph won against Damien
    George won against Stan
    Guy won against Albert
    Leonard won against Simon
    Stan won against Marty
    George won against Arthur
    Karl won against Stephen
    Jack won against Marty
    """





