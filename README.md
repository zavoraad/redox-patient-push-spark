# redox-patient-push-spark
Reading in a resource defined from  https://developer.redoxengine.com/data-models/ClinicalSummary.html#PatientPush


# Pyspark example

``` python
import json
from pyspark.sql.types import StructType

schema = StructType.fromJson(json.load(open("./schemas/clinicalsummary-patientpush.spark.json", "r")))
df = spark.read.option("multiline", True).format("json").schema(schema).load("test_data/*json") 
df.columns
"""
['Meta', 'Header', 'AdvanceDirectivesText', 'AdvanceDirectives', 'AllergyText', 'Allergies', 'CareTeams', 'EncountersText', 'Encounters', 'FamilyHistoryText', 'FamilyHistory', 'FunctionalStatusText', 'FunctionalStatus', 'GoalsText', 'Goals', 'HealthConcernsText', 'HealthConcerns', 'ImmunizationText', 'Immunizations', 'InsurancesText', 'Insurances', 'MedicalHistoryText', 'MedicalEquipmentText', 'MedicalEquipment', 'MedicationsText', 'Medications', 'NoteSections', 'PlanOfCareText', 'PlanOfCare', 'ProblemsText', 'Problems', 'ProceduresText', 'Procedures', 'ResolvedProblemsText', 'ResolvedProblems', 'ResultText', 'Results', 'SocialHistoryText', 'SocialHistory', 'VitalSignsText', 'VitalSigns']
"""
```

# Json schema produced from "Hotfix" branch

https://github.com/databricks-industry-solutions/json2spark-schema/tree/hotfix

``` scala
import java.io._
import io.circe._
import scala.reflect.runtime.universe._
import org.apache.spark.sql.types._
import io.circe.parser._
import com.databricks.industry.solutions.json2spark._

val file = new FileWriter(new File("./redox-patient-push-spark/clinicalsummary-patientpush.spark.json"))
val y = new Json2Spark(Json2Spark.file2String("./redox-patient-push-spark/clinicalsummary-patientpush.json"))
//y.convert2Spark.prettyJson
file.write(y.convert2Spark.prettyJson)
file.close()

```



