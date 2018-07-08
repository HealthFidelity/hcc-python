from hcc_2018_87 import Diagnosis, Beneficiary, ICDType, score, EntitlementReason
from pyDatalog import pyDatalog


person= Beneficiary(hicno="002267669A", sex= "female",dob= "20180112")

person.add_diagnosis(Diagnosis(person,"M25511",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"I272",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"H6123",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"E785",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"M368",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"J8410",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"N390",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"R0989",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"M358",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"I2720",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"R0602",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"K219",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"J9600",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"I517",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"R809",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"J849",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"J8417",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"E538",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"R8271",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"G609",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"M7541",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"Z87891",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"M19049",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"M170",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"G64",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"G3184",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"G629",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"I10",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"J439",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"Z9981",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"I4891",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"M159",ICDType.TEN))
person.add_diagnosis(Diagnosis(person,"R5381",ICDType.TEN))


pyDatalog.create_terms("X")


score(person, "community", X)
print("community: %s" % X)

score(person, "institutional", X)
print("institutional: %s" % X)

score(person, "new_enrollee", X)
print("new_enrollee: %s" % X)


""" 
output:

community: [2.895]
institutional: [3.006]
new_enrollee: [0.601]

"""