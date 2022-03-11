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
        citizens[people] = ["healthy", 0]

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


def infected(population):
    infected = population
    for sick in population:
        grimReaper = death()
        if grimReaper <= 2:
            infected[sick] = ["dead", 0]
        elif infected[sick][0] == "sick" and infected[sick][1] >= 10 and grimReaper > 2:
            infected[sick] = ["healthy", 0]
        elif infected[sick][0] == "sick":
            infected[sick][1] += 1

    return infected

# returns array


def peopleMet(maxPopulation, currentPatient):
    # max number of possible infected
    if maxPopulation > 20:
        maxInfected = 20
    else:
        maxInfected = maxPopulation - 1

    # how many people meet
    encounters = random.randint(0, maxInfected)
    # keys of met people
    meetNames = []
    for i in range(0, encounters):
        encounter = random.randint(0, maxInfected)
        if encounter not in meetNames and currentPatient != encounter:
            # will this person get infected? 30% chance of infection
            infectionChance = random.randint(0, 100)
            if infectionChance < 30:
                meetNames.append(encounter)
        else:
            encounter = random.randint(0, maxInfected)
            i -= 1
    return meetNames
# returns new dictionay


def newInfected(people, newInfected):
    updated = people
    for victom in newInfected:
        if updated[victom] == "healthy":
            updated[victom] = "sick"

    return updated


def main():
    # get population size
    populationSize = getPopulation()
    # get days
    days = simulationDays()
    # create citizens
    people = citizens(populationSize)
    # add sick people
    numSickPeople = sickNumber(populationSize)
    # add sick people
    patients = addSick(people, populationSize, numSickPeople)
    print("Healthy/Sick/Dead | initial sick: " + str(infectedCount(patients)))

    dailyInfected = []
    # loop through days
    for day in range(0, days):
        # 1: check if a patient is going to die, 2) update their sick days, 3) update their health status i.e. from sick to healthy
        patients = infected(patients)
        for person in patients:
            if patients[person][0] == "sick":
                # who this patient has met and infected
                dailyInfected += peopleMet(populationSize, person)
                # remove duplicates
                dailyInfected = list(dict.fromkeys(dailyInfected))

                # add new infected to patients

        # add new infected to patients
        patients = newInfected(patients, dailyInfected)

        print("Healthy/Sick/Dead |check sick: " + str(infectedCount(patients)))
        # clear daily infected
        dailyInfected = []


main()
