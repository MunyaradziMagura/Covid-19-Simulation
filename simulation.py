def getPopulation():
    populationSize = input("enter a population size: ")
    # ensure the population size is a number
    while populationSize.isnumeric() != True:
        print("\nplease enter a valid size. only whole number integers \n")
        populationSize = input("enter a population size: ")

    return populationSize

# takes in a dictionary and an int value


def sickNumber(populationSize):
    sick = input("number of sick: ")
    while sick.isnumeric() != True or sick > populationSize:
        if sick > populationSize:
            print("\nsick number is greater than population :(")
        else:
            print("\nplease enter a whole number below: " + str(populationSize))
        sick = input("\nnumber of sick: ")
    return sick


def addSick(victoms, totalPopulation, sickNumber):
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
    patients = addSick(people, populationSize, )


main()
