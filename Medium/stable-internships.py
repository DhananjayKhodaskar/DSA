# Question Link - https://www.algoexpert.io/questions/stable-internships

# O(n^2) Time | O(n^2) Space
def stableInternships(interns, teams):
    chosenInterns = {}
    freeInterns = list(range(len(interns)))
    currentInternChoices = [0 for i in range(len(interns))]
    
    teamMap = []
    for team in teams:
        rank = {}
        for idx,internNum in enumerate(team):
            rank[internNum] =  idx
        teamMap.append(rank)
        

    while len(freeInterns) > 0:
        internNum  = freeInterns.pop()
        
        intern = interns[internNum]
        teamPreference = intern[currentInternChoices[internNum]]
        currentInternChoices[internNum] += 1

        if teamPreference not in chosenInterns:
            chosenInterns[teamPreference] = internNum
            continue

        previousIntern = chosenInterns[teamPreference]
        previousInternRank = teamMap[teamPreference][previousIntern]
        currentInternRank = teamMap[teamPreference][internNum]


        if currentInternRank < previousInternRank:
            chosenInterns[teamPreference] = internNum
            freeInterns.append(previousIntern)
        else:
            freeInterns.append(internNum)

    matches = [[internNum,teamNum]for teamNum,internNum in chosenInterns.items()]
    return matches

    
