suspicious_activities = [
    ("Albert", "San Francisco", "deposit"),
    ("Brad", "San Francisco", "withdraw"),
    ("Claire", "New York", "withdraw")
]

new_activities = [
    ("Joe", "Miami", "withdraw"),
    ("John", "San Francisco", "deposit"),
    ("Diana", "London", "withdraw"),
    ("Diana", "San Francisco", "withdraw"),
    ("Albert", "London", "withdraw"),
    ("Joe", "New York", "update_address"),
    ("Claire", "Miami", "deposit"),
    ("Diana", "New York", "deposit"),
    ("Albert", "Chicago", "withdraw"),
    ("Brad", "Paris", "deposit"),
    ("Claire", "Paris", "deposit"),
    ("Diana", "Vancouver", "file_dispute"),
    ("John", "Mumbai", "withdraw")
]

def find_suspicious_activities(new_activities, suspicious_activities):
    confirmed_suspicious = [False]*len(new_activities)
    new_suspicious_activities = []

    suspicious_activities_index = 0
    while suspicious_activities_index < len(suspicious_activities):
        new_activities_index = 0
        while new_activities_index < len(new_activities):
            if not(confirmed_suspicious[new_activities_index]) and is_suspicious_activitie(suspicious_activities[suspicious_activities_index], new_activities[new_activities_index]):
                new_suspicious_activities.append(new_activities[new_activities_index])
                confirmed_suspicious[new_activities_index] = True
                suspicious_activities.append(new_activities[new_activities_index])

            new_activities_index += 1

        suspicious_activities_index += 1

    return new_suspicious_activities

def is_suspicious_activitie(current_suspicious_activitie, new_suspicious_activitie):
    k = 2
    total = 0
    for i in range(3):
        if current_suspicious_activitie[i] == new_suspicious_activitie[i]:
            total = total + 1
        
        if total == k:
            return True
    
    return False

new_suspicious_activities = find_suspicious_activities(new_activities, suspicious_activities)
print(new_suspicious_activities)