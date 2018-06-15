from hcc import Diagnosis, Beneficiary, ICDType, score, EntitlementReason
from pyDatalog import pyDatalog

jane = Beneficiary(hicno='0220F11E0B2EC004', sex='female', dob='19480601')
dx1 = Diagnosis(jane, "E1165", ICDType.TEN)
jane.add_diagnosis(dx1)
dx2 = Diagnosis(jane, "E118", ICDType.TEN)
jane.add_diagnosis(dx2)

pyDatalog.create_terms("X")
score(jane, "community", X)
print("X: %s" % X)

score(jane, "institutional", X)
print("X: %s" % X)

score(jane, "new_enrollee", X)
print("X: %s" % X)


daniel = Beneficiary(1,"male","19740824",EntitlementReason.DIB)
daniel.add_diagnosis(Diagnosis(daniel,"A0223",ICDType.TEN))  # 51
daniel.add_diagnosis(Diagnosis(daniel,"A0224",ICDType.TEN))  # 52
daniel.add_diagnosis(Diagnosis(daniel,"D66",ICDType.TEN))
daniel.add_diagnosis(Diagnosis(daniel,"C163",ICDType.TEN))
daniel.add_diagnosis(Diagnosis(daniel,"C163",ICDType.TEN))
daniel.add_diagnosis(Diagnosis(daniel,"C182",ICDType.TEN))
daniel.add_diagnosis(Diagnosis(daniel,"C800",ICDType.TEN))
daniel.add_diagnosis(Diagnosis(daniel,"A072",ICDType.TEN))
score(daniel, "community", X)
print("Daniel Community Score: %s" % X)