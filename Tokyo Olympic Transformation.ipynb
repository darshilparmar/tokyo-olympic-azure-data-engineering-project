{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "c76c1683-d905-4ae9-86f8-3729c50f213a",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.sql.functions import col\n",
    "from pyspark.sql.types import IntegerType, DoubleType, BooleanType, DateType"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "78d23d0b-1160-408a-8054-6c8dd40f052f",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Out[5]: True"
     ]
    }
   ],
   "source": [
    "configs = {\"fs.azure.account.auth.type\": \"OAuth\",\n",
    "\"fs.azure.account.oauth.provider.type\": \"org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider\",\n",
    "\"fs.azure.account.oauth2.client.id\": \"\",\n",
    "\"fs.azure.account.oauth2.client.secret\": '',\n",
    "\"fs.azure.account.oauth2.client.endpoint\": \"https://login.microsoftonline.com/tanent_id/oauth2/token\"}\n",
    "\n",
    "\n",
    "dbutils.fs.mount(\n",
    "source = \"abfss://tokyo-olympic-data@tokyoolympicdata.dfs.core.windows.net\", # contrainer@storageacc\n",
    "mount_point = \"/mnt/tokyoolymic\",\n",
    "extra_configs = configs)\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "e4102f61-4816-46d5-abf4-488b29cfa366",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>path</th><th>name</th><th>size</th><th>modificationTime</th></tr></thead><tbody><tr><td>dbfs:/mnt/tokyoolymic/raw-data/</td><td>raw-data/</td><td>0</td><td>1691562179000</td></tr><tr><td>dbfs:/mnt/tokyoolymic/transformed-data/</td><td>transformed-data/</td><td>0</td><td>1691562189000</td></tr></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [
        [
         "dbfs:/mnt/tokyoolymic/raw-data/",
         "raw-data/",
         0,
         1691562179000
        ],
        [
         "dbfs:/mnt/tokyoolymic/transformed-data/",
         "transformed-data/",
         0,
         1691562189000
        ]
       ],
       "datasetInfos": [],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {
        "isDbfsCommandResult": false
       },
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [
        {
         "metadata": "{}",
         "name": "path",
         "type": "\"string\""
        },
        {
         "metadata": "{}",
         "name": "name",
         "type": "\"string\""
        },
        {
         "metadata": "{}",
         "name": "size",
         "type": "\"long\""
        },
        {
         "metadata": "{}",
         "name": "modificationTime",
         "type": "\"long\""
        }
       ],
       "type": "table"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "%fs\n",
    "ls \"/mnt/tokyoolymic\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "5e603a56-c274-4afd-8cbf-1d013b0c5d09",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "            <div>\n",
       "                <p><b>SparkSession - hive</b></p>\n",
       "                \n",
       "        <div>\n",
       "            <p><b>SparkContext</b></p>\n",
       "\n",
       "            <p><a href=\"/?o=2723700013584314#setting/sparkui/0809-071007-ueyejyn5/driver-8670347769851812044\">Spark UI</a></p>\n",
       "\n",
       "            <dl>\n",
       "              <dt>Version</dt>\n",
       "                <dd><code>v3.3.2</code></dd>\n",
       "              <dt>Master</dt>\n",
       "                <dd><code>local[*, 4]</code></dd>\n",
       "              <dt>AppName</dt>\n",
       "                <dd><code>Databricks Shell</code></dd>\n",
       "            </dl>\n",
       "        </div>\n",
       "        \n",
       "            </div>\n",
       "        "
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "arguments": {},
       "data": "\n            <div>\n                <p><b>SparkSession - hive</b></p>\n                \n        <div>\n            <p><b>SparkContext</b></p>\n\n            <p><a href=\"/?o=2723700013584314#setting/sparkui/0809-071007-ueyejyn5/driver-8670347769851812044\">Spark UI</a></p>\n\n            <dl>\n              <dt>Version</dt>\n                <dd><code>v3.3.2</code></dd>\n              <dt>Master</dt>\n                <dd><code>local[*, 4]</code></dd>\n              <dt>AppName</dt>\n                <dd><code>Databricks Shell</code></dd>\n            </dl>\n        </div>\n        \n            </div>\n        ",
       "datasetInfos": [],
       "metadata": {},
       "removedWidgets": [],
       "textData": null,
       "type": "htmlSandbox"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "spark"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "181fa770-c731-4991-946c-d3d5bc32400f",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "athletes = spark.read.format(\"csv\").option(\"header\",\"true\").option(\"inferSchema\",\"true\").load(\"/mnt/tokyoolymic/raw-data/athletes.csv\")\n",
    "coaches = spark.read.format(\"csv\").option(\"header\",\"true\").option(\"inferSchema\",\"true\").load(\"/mnt/tokyoolymic/raw-data/coaches.csv\")\n",
    "entriesgender = spark.read.format(\"csv\").option(\"header\",\"true\").option(\"inferSchema\",\"true\").load(\"/mnt/tokyoolymic/raw-data/entriesgender.csv\")\n",
    "medals = spark.read.format(\"csv\").option(\"header\",\"true\").option(\"inferSchema\",\"true\").load(\"/mnt/tokyoolymic/raw-data/medals.csv\")\n",
    "teams = spark.read.format(\"csv\").option(\"header\",\"true\").option(\"inferSchema\",\"true\").load(\"/mnt/tokyoolymic/raw-data/teams.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "ce0247a7-d206-47ec-994f-80ceedd06721",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+--------------------+-------------------+\n",
      "|          PersonName|             Country|         Discipline|\n",
      "+--------------------+--------------------+-------------------+\n",
      "|     AALERUD Katrine|              Norway|       Cycling Road|\n",
      "|         ABAD Nestor|               Spain|Artistic Gymnastics|\n",
      "|   ABAGNALE Giovanni|               Italy|             Rowing|\n",
      "|      ABALDE Alberto|               Spain|         Basketball|\n",
      "|       ABALDE Tamara|               Spain|         Basketball|\n",
      "|           ABALO Luc|              France|           Handball|\n",
      "|        ABAROA Cesar|               Chile|             Rowing|\n",
      "|       ABASS Abobakr|               Sudan|           Swimming|\n",
      "|    ABBASALI Hamideh|Islamic Republic ...|             Karate|\n",
      "|       ABBASOV Islam|          Azerbaijan|          Wrestling|\n",
      "|        ABBINGH Lois|         Netherlands|           Handball|\n",
      "|         ABBOT Emily|           Australia|Rhythmic Gymnastics|\n",
      "|       ABBOTT Monica|United States of ...|  Baseball/Softball|\n",
      "|ABDALLA Abubaker ...|               Qatar|          Athletics|\n",
      "|      ABDALLA Maryam|               Egypt|  Artistic Swimming|\n",
      "|      ABDALLAH Shahd|               Egypt|  Artistic Swimming|\n",
      "| ABDALRASOOL Mohamed|               Sudan|               Judo|\n",
      "|   ABDEL LATIF Radwa|               Egypt|           Shooting|\n",
      "|    ABDEL RAZEK Samy|               Egypt|           Shooting|\n",
      "|   ABDELAZIZ Abdalla|               Egypt|             Karate|\n",
      "+--------------------+--------------------+-------------------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "athletes.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "d6e90e0a-cbce-4afb-8baf-857b3f47554d",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "root\n",
      " |-- PersonName: string (nullable = true)\n",
      " |-- Country: string (nullable = true)\n",
      " |-- Discipline: string (nullable = true)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "athletes.printSchema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "26fd4755-4eb4-4117-b4f5-33b396184b3c",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+--------------------+-----------------+--------+\n",
      "|                Name|             Country|       Discipline|   Event|\n",
      "+--------------------+--------------------+-----------------+--------+\n",
      "|     ABDELMAGID Wael|               Egypt|         Football|    null|\n",
      "|           ABE Junya|               Japan|       Volleyball|    null|\n",
      "|       ABE Katsuhiko|               Japan|       Basketball|    null|\n",
      "|        ADAMA Cherif|       C�te d'Ivoire|         Football|    null|\n",
      "|          AGEBA Yuya|               Japan|       Volleyball|    null|\n",
      "|AIKMAN Siegfried ...|               Japan|           Hockey|     Men|\n",
      "|       AL SAADI Kais|             Germany|           Hockey|     Men|\n",
      "|       ALAMEDA Lonni|              Canada|Baseball/Softball|Softball|\n",
      "|     ALEKNO Vladimir|Islamic Republic ...|       Volleyball|     Men|\n",
      "|     ALEKSEEV Alexey|                 ROC|         Handball|   Women|\n",
      "|ALLER CARBALLO Ma...|               Spain|       Basketball|    null|\n",
      "|       ALSHEHRI Saad|        Saudi Arabia|         Football|     Men|\n",
      "|           ALY Kamal|               Egypt|         Football|    null|\n",
      "| AMAYA GAITAN Fabian|         Puerto Rico|       Basketball|    null|\n",
      "|    AMO AGUADO Pablo|               Spain|         Football|    null|\n",
      "|   ANDONOVSKI Vlatko|United States of ...|         Football|   Women|\n",
      "|        ANNAN Alyson|         Netherlands|           Hockey|   Women|\n",
      "|  ARNAU CREUS Xavier|               Japan|           Hockey|   Women|\n",
      "|       ARNOLD Graham|           Australia|         Football|     Men|\n",
      "|         AXNER Tomas|              Sweden|         Handball|   Women|\n",
      "+--------------------+--------------------+-----------------+--------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "coaches.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "ab0d4dbf-2ade-43f5-b063-c61ea7098cc2",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "root\n",
      " |-- Name: string (nullable = true)\n",
      " |-- Country: string (nullable = true)\n",
      " |-- Discipline: string (nullable = true)\n",
      " |-- Event: string (nullable = true)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "coaches.printSchema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "2f729fb9-3809-434c-9d4d-88eaefc68adb",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+------+----+-----+\n",
      "|          Discipline|Female|Male|Total|\n",
      "+--------------------+------+----+-----+\n",
      "|      3x3 Basketball|    32|  32|   64|\n",
      "|             Archery|    64|  64|  128|\n",
      "| Artistic Gymnastics|    98|  98|  196|\n",
      "|   Artistic Swimming|   105|   0|  105|\n",
      "|           Athletics|   969|1072| 2041|\n",
      "|           Badminton|    86|  87|  173|\n",
      "|   Baseball/Softball|    90| 144|  234|\n",
      "|          Basketball|   144| 144|  288|\n",
      "|    Beach Volleyball|    48|  48|   96|\n",
      "|              Boxing|   102| 187|  289|\n",
      "|        Canoe Slalom|    41|  41|   82|\n",
      "|        Canoe Sprint|   123| 126|  249|\n",
      "|Cycling BMX Frees...|    10|   9|   19|\n",
      "|  Cycling BMX Racing|    24|  24|   48|\n",
      "|Cycling Mountain ...|    38|  38|   76|\n",
      "|        Cycling Road|    70| 131|  201|\n",
      "|       Cycling Track|    90|  99|  189|\n",
      "|              Diving|    72|  71|  143|\n",
      "|          Equestrian|    73| 125|  198|\n",
      "|             Fencing|   107| 108|  215|\n",
      "+--------------------+------+----+-----+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "entriesgender.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "85eb5e27-ae12-44ad-9a19-a52262f54da2",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "root\n",
      " |-- Discipline: string (nullable = true)\n",
      " |-- Female: string (nullable = true)\n",
      " |-- Male: string (nullable = true)\n",
      " |-- Total: string (nullable = true)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "entriesgender.printSchema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "f86a74cb-1bc3-439b-b7f3-594fb6ee48a7",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "entriesgender = entriesgender.withColumn(\"Female\",col(\"Female\").cast(IntegerType()))\\\n",
    "    .withColumn(\"Male\",col(\"Male\").cast(IntegerType()))\\\n",
    "    .withColumn(\"Total\",col(\"Total\").cast(IntegerType()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "33b83c1b-f99c-46da-ba2e-5971f86c66f1",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "root\n",
      " |-- Discipline: string (nullable = true)\n",
      " |-- Female: integer (nullable = true)\n",
      " |-- Male: integer (nullable = true)\n",
      " |-- Total: integer (nullable = true)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "entriesgender.printSchema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "d2c66e87-314b-4ab2-9e8c-bbe6cf321f2d",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+----+--------------------+----+------+------+-----+-------------+\n",
      "|Rank|        Team_Country|Gold|Silver|Bronze|Total|Rank by Total|\n",
      "+----+--------------------+----+------+------+-----+-------------+\n",
      "|   1|United States of ...|  39|    41|    33|  113|            1|\n",
      "|   2|People's Republic...|  38|    32|    18|   88|            2|\n",
      "|   3|               Japan|  27|    14|    17|   58|            5|\n",
      "|   4|       Great Britain|  22|    21|    22|   65|            4|\n",
      "|   5|                 ROC|  20|    28|    23|   71|            3|\n",
      "|   6|           Australia|  17|     7|    22|   46|            6|\n",
      "|   7|         Netherlands|  10|    12|    14|   36|            9|\n",
      "|   8|              France|  10|    12|    11|   33|           10|\n",
      "|   9|             Germany|  10|    11|    16|   37|            8|\n",
      "|  10|               Italy|  10|    10|    20|   40|            7|\n",
      "|  11|              Canada|   7|     6|    11|   24|           11|\n",
      "|  12|              Brazil|   7|     6|     8|   21|           12|\n",
      "|  13|         New Zealand|   7|     6|     7|   20|           13|\n",
      "|  14|                Cuba|   7|     3|     5|   15|           18|\n",
      "|  15|             Hungary|   6|     7|     7|   20|           13|\n",
      "|  16|   Republic of Korea|   6|     4|    10|   20|           13|\n",
      "|  17|              Poland|   4|     5|     5|   14|           19|\n",
      "|  18|      Czech Republic|   4|     4|     3|   11|           23|\n",
      "|  19|               Kenya|   4|     4|     2|   10|           25|\n",
      "|  20|              Norway|   4|     2|     2|    8|           29|\n",
      "+----+--------------------+----+------+------+-----+-------------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "medals.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "a4fcce57-31ed-4aa8-9499-633d5bb2a4c7",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "root\n",
      " |-- Rank: integer (nullable = true)\n",
      " |-- Team_Country: string (nullable = true)\n",
      " |-- Gold: integer (nullable = true)\n",
      " |-- Silver: integer (nullable = true)\n",
      " |-- Bronze: integer (nullable = true)\n",
      " |-- Total: integer (nullable = true)\n",
      " |-- Rank by Total: integer (nullable = true)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "medals.printSchema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "d05e8089-77c5-424c-aeb9-6c659dc8d20a",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-------------+--------------+--------------------+------------+\n",
      "|     TeamName|    Discipline|             Country|       Event|\n",
      "+-------------+--------------+--------------------+------------+\n",
      "|      Belgium|3x3 Basketball|             Belgium|         Men|\n",
      "|        China|3x3 Basketball|People's Republic...|         Men|\n",
      "|        China|3x3 Basketball|People's Republic...|       Women|\n",
      "|       France|3x3 Basketball|              France|       Women|\n",
      "|        Italy|3x3 Basketball|               Italy|       Women|\n",
      "|        Japan|3x3 Basketball|               Japan|         Men|\n",
      "|        Japan|3x3 Basketball|               Japan|       Women|\n",
      "|       Latvia|3x3 Basketball|              Latvia|         Men|\n",
      "|     Mongolia|3x3 Basketball|            Mongolia|       Women|\n",
      "|  Netherlands|3x3 Basketball|         Netherlands|         Men|\n",
      "|       Poland|3x3 Basketball|              Poland|         Men|\n",
      "|          ROC|3x3 Basketball|                 ROC|         Men|\n",
      "|          ROC|3x3 Basketball|                 ROC|       Women|\n",
      "|      Romania|3x3 Basketball|             Romania|       Women|\n",
      "|       Serbia|3x3 Basketball|              Serbia|         Men|\n",
      "|United States|3x3 Basketball|United States of ...|       Women|\n",
      "|    Australia|       Archery|           Australia|  Men's Team|\n",
      "|    Australia|       Archery|           Australia|  Mixed Team|\n",
      "|   Bangladesh|       Archery|          Bangladesh|  Mixed Team|\n",
      "|      Belarus|       Archery|             Belarus|Women's Team|\n",
      "+-------------+--------------+--------------------+------------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "teams.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "ffe5cb4c-cd58-4b1f-a4c5-66b41931d69a",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "root\n",
      " |-- TeamName: string (nullable = true)\n",
      " |-- Discipline: string (nullable = true)\n",
      " |-- Country: string (nullable = true)\n",
      " |-- Event: string (nullable = true)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "teams.printSchema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "a1dbbc4d-457b-4db2-aa1e-65047ccc9247",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+----+\n",
      "|        Team_Country|Gold|\n",
      "+--------------------+----+\n",
      "|United States of ...|  39|\n",
      "|People's Republic...|  38|\n",
      "|               Japan|  27|\n",
      "|       Great Britain|  22|\n",
      "|                 ROC|  20|\n",
      "|           Australia|  17|\n",
      "|         Netherlands|  10|\n",
      "|              France|  10|\n",
      "|             Germany|  10|\n",
      "|               Italy|  10|\n",
      "|              Canada|   7|\n",
      "|              Brazil|   7|\n",
      "|         New Zealand|   7|\n",
      "|                Cuba|   7|\n",
      "|             Hungary|   6|\n",
      "|   Republic of Korea|   6|\n",
      "|              Poland|   4|\n",
      "|      Czech Republic|   4|\n",
      "|               Kenya|   4|\n",
      "|              Norway|   4|\n",
      "+--------------------+----+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Find the top countries with the highest number of gold medals\n",
    "top_gold_medal_countries = medals.orderBy(\"Gold\", ascending=False).select(\"Team_Country\",\"Gold\").show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "227067b1-3b5b-4a01-a3d1-5bf3f5972cd7",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+------+----+-----+-------------------+-------------------+\n",
      "|          Discipline|Female|Male|Total|         Avg_Female|           Avg_Male|\n",
      "+--------------------+------+----+-----+-------------------+-------------------+\n",
      "|      3x3 Basketball|    32|  32|   64|                0.5|                0.5|\n",
      "|             Archery|    64|  64|  128|                0.5|                0.5|\n",
      "| Artistic Gymnastics|    98|  98|  196|                0.5|                0.5|\n",
      "|   Artistic Swimming|   105|   0|  105|                1.0|                0.0|\n",
      "|           Athletics|   969|1072| 2041| 0.4747672709456149| 0.5252327290543851|\n",
      "|           Badminton|    86|  87|  173|0.49710982658959535| 0.5028901734104047|\n",
      "|   Baseball/Softball|    90| 144|  234|0.38461538461538464| 0.6153846153846154|\n",
      "|          Basketball|   144| 144|  288|                0.5|                0.5|\n",
      "|    Beach Volleyball|    48|  48|   96|                0.5|                0.5|\n",
      "|              Boxing|   102| 187|  289|0.35294117647058826| 0.6470588235294118|\n",
      "|        Canoe Slalom|    41|  41|   82|                0.5|                0.5|\n",
      "|        Canoe Sprint|   123| 126|  249| 0.4939759036144578| 0.5060240963855421|\n",
      "|Cycling BMX Frees...|    10|   9|   19| 0.5263157894736842|0.47368421052631576|\n",
      "|  Cycling BMX Racing|    24|  24|   48|                0.5|                0.5|\n",
      "|Cycling Mountain ...|    38|  38|   76|                0.5|                0.5|\n",
      "|        Cycling Road|    70| 131|  201| 0.3482587064676617| 0.6517412935323383|\n",
      "|       Cycling Track|    90|  99|  189|0.47619047619047616| 0.5238095238095238|\n",
      "|              Diving|    72|  71|  143| 0.5034965034965035| 0.4965034965034965|\n",
      "|          Equestrian|    73| 125|  198| 0.3686868686868687| 0.6313131313131313|\n",
      "|             Fencing|   107| 108|  215|0.49767441860465117| 0.5023255813953489|\n",
      "+--------------------+------+----+-----+-------------------+-------------------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Calculate the average number of entries by gender for each discipline\n",
    "average_entries_by_gender = entriesgender.withColumn(\n",
    "    'Avg_Female', entriesgender['Female'] / entriesgender['Total']\n",
    ").withColumn(\n",
    "    'Avg_Male', entriesgender['Male'] / entriesgender['Total']\n",
    ")\n",
    "average_entries_by_gender.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "b2bda1f9-a0d7-46df-a895-b418522dc40d",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "athletes.repartition(1).write.mode(\"overwrite\").option(\"header\",'true').csv(\"/mnt/tokyoolymic/transformed-data/athletes\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "c489a24b-05e4-47c3-a329-9d5e5e1d85b3",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "coaches.repartition(1).write.mode(\"overwrite\").option(\"header\",\"true\").csv(\"/mnt/tokyoolymic/transformed-data/coaches\")\n",
    "entriesgender.repartition(1).write.mode(\"overwrite\").option(\"header\",\"true\").csv(\"/mnt/tokyoolymic/transformed-data/entriesgender\")\n",
    "medals.repartition(1).write.mode(\"overwrite\").option(\"header\",\"true\").csv(\"/mnt/tokyoolymic/transformed-data/medals\")\n",
    "teams.repartition(1).write.mode(\"overwrite\").option(\"header\",\"true\").csv(\"/mnt/tokyoolymic/transformed-data/teams\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "bb18401a-d221-4421-9a8d-4d8c5cbdee29",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "dashboards": [],
   "language": "python",
   "notebookMetadata": {
    "mostRecentlyExecutedCommandWithImplicitDF": {
     "commandId": 1201695797254400,
     "dataframes": [
      "_sqldf"
     ]
    },
    "pythonIndentUnit": 4
   },
   "notebookName": "Tokyo Olympic Transformation",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
