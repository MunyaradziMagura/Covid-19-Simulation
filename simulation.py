def getPopulation():
    populationSize = input("enter a population size: ")
    # ensure the population size is a number
    while populationSize.isnumeric() != True:
        print("\nplease enter a valid size. only whole number integers \n")
        populationSize = input("enter a population size: ")

    return populationSize

# takes in a dictionary and an int value


def addSick(victoms, totalPopulation):
    return 1

# takes in an int value


def citizens(populationSize):
    citizens = {}
    # create a population of people
    for people in len(populationSize):
        # set all people to healthy
        citizens[people] = "healthy"

    return citizens


def main():

    populationSize = getPopulation()
    people = citizens(populationSize)
    patients = addSick(people)


main()
