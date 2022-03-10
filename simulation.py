from hashlib import new
import random
# returns an int


def getPopulation():
    populationSize = input("enter a population size: ")
    # ensure the population size is a number
    while populationSize.isnumeric() != True:
        print("\nplease enter a valid size. only whole number integers \n")
        populationSize = input("enter a population size: ")

    return int(populationSize)

# takes in a dictionary and an int value then returns an int


def sickNumber(populationSize):
    sick = input("number of sick: ")

    while sick.isnumeric() != True or int(sick) > populationSize:
        if int(sick) > populationSize:
            print("\nsick number is greater than population :(")
        else:
            print("\nplease enter a whole number below: " + str(populationSize))
        sick = input("\nnumber of sick: ")

    return int(sick)

# return an array counting the victom stats


def infectedCount(victoms):
    # healthy sick dead
    health = [0, 0, 0]
    for patient in victoms:
        if victoms[patient][0] == "healthy":
            health[0] += 1
        elif victoms[patient][0] == "sick":
            health[1] += 1
        elif victoms[patient][0] == "dead":
            health[2] += 1

    return health
# takes in a dictionary, int and int and returns a dictionary


def addSick(victoms, totalPopulation, sickNumber):

    infect = sickNumber
    infectedPopulation = victoms
    # check if any sick can be added
    check = infectedCount(infectedPopulation)
    if check[0] < 1:
        print("\nno sick can be added\n")
        return infectedPopulation
    else:
        for victom in range(totalPopulation):
            # check if that person has already been infected
            if infectedPopulation[victom][0] == "healthy" and infect > 0:
                # infect said person if they are healthy
                infectedPopulation[victom][0] = "sick"
                infect -= 1
    return infectedPopulation


# takes in an int value then returns a dictionary


def citizens(populationSize):
    citizens = {}
    # create a population of people
    for people in range(populationSize):
        # set all people to healthy and the days they are sick is 0
        citizens[people] = ["healthy", 10]

    return citizens

# how long the simulation will last


def simulationDays():
    days = input("enter number of days: ")
    # ensure the population size is a number
    while days.isnumeric() != True:
        print("\nplease enter a valid size. only whole number integers \n")
        days = input("enter number of days: ")
    return int(days)


def death():
    diceOfDeath = random.randint(0, 100)
    return diceOfDeath


def recovery(population):
    recovered = population
    for sick in population:
        grimReaper = death()
        if grimReaper <= 20:
            recovered[sick] = ["dead", 0]
        elif recovered[sick][0] == "sick" and recovered[sick][1] >= 10 and grimReaper > 20:
            recovered[sick] = ["healthy", 0]

    return recovered


def main():
    populationSize = getPopulation()
    days = simulationDays()
    people = citizens(populationSize)
    numSickPeople = sickNumber(populationSize)

    patients = addSick(people, populationSize, numSickPeople)
    print(patients)
    print("H/S/D |check sick: " + str(infectedCount(patients)))
    recover = recovery(patients)
    print(recover)


main()
