
stagiaires_list=["purentin","boris","donald","daryl","adora","sahid","jores"]

with open("stagiaires.txt","w+") as file:
    for stagiaire in stagiaires_list:
        file.write(stagiaire +"-Etudiant\n")
    file.close()
