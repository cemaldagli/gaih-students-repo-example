def creatDict(name,surname,age,jobTitle,areaofInterest,occupationalSkills,softSkills):

    cvDic={"name":name,"surname":surname,"age":age,"jobTitle":jobTitle,"areaofInterest":areaofInterest,
                    "occupationalSkills":occupationalSkills,"softSkills":softSkills}

    return cvDic



def printCVs(applicantList,numberApplicant):

    listExtentions=["","st","nd","rd","th","th"]

    for i in range(0,numberApplicant):

        print("---------------------------- {0}.{1} Candidate ----------------------------".format(i+1,listExtentions[i+1]))
        print("Name:" +applicantList[i]["name"] + "\n"
        + "Surname: "+ applicantList[i]["surname"] + "\n" + "Age: " +applicantList[i]["age"] + "\n" +
              "jobTitle:"+applicantList[i]["jobTitle"] + "\n" + "Area of Interest: " +  applicantList[i]["areaofInterest"] + "\n"


            + "Occupational Skill: " + applicantList[i]["occupationalSkills"] + "\n"
        + "Soft Skills: " + applicantList[i]["softSkills"] + "\n\n")




if __name__ == '__main__':



    numberApplicant  = int(input("How many candidates will the CV-Pool be containing?"))

    applicantList=[]

    for i in range(0,numberApplicant):

        sampleApplicant=creatDict(input("Name:"),input("Surame:"),input("Age:"),input("jobTitle:"),
                                 input("areaofInterest:"),input("occupationalSkills:"),input("softSkills:"))

        applicantList.append(dict(sampleApplicant))

        sampleApplicant={}

    for i in range(0, numberApplicant):

        printCVs(applicantList , numberApplicant)


















