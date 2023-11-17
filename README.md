# redox-patient-push-spark
Reading in a resource defined from  https://developer.redoxengine.com/data-models/ClinicalSummary.html#PatientPush


# Pyspark example

```python
import json
from pyspark.sql.types import StructType

schema = StructType.fromJson(json.load(open("./schemas/clinicalsummary-patientpush.spark.json", "r")))
df = spark.read.format("json").schema(schema).load("sampledata/*json")
df.columns
"""
['Meta', 'Header', 'AdvanceDirectivesText', 'AdvanceDirectives', 'AllergyText', 'Allergies', 'CareTeams', 'EncountersText', 'Encounters', 'FamilyHistoryText', 'FamilyHistory', 'FunctionalStatusText', 'FunctionalStatus', 'GoalsText', 'Goals', 'HealthConcernsText', 'HealthConcerns', 'ImmunizationText', 'Immunizations', 'InsurancesText', 'Insurances', 'MedicalHistoryText', 'MedicalEquipmentText', 'MedicalEquipment', 'MedicationsText', 'Medications', 'NoteSections', 'PlanOfCareText', 'PlanOfCare', 'ProblemsText', 'Problems', 'ProceduresText', 'Procedures', 'ResolvedProblemsText', 'ResolvedProblems', 'ResultText', 'Results', 'SocialHistoryText', 'SocialHistory', 'VitalSignsText', 'VitalSigns']
"""
```
