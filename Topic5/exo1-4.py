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
    bx = City.get_city("Bruxelles")
    print(bx.get_population())                      # should print 10






