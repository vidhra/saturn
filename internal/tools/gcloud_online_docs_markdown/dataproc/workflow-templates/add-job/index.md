# gcloud dataproc workflow-templates add-job  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job)*

**NAME**

: **gcloud dataproc workflow-templates add-job - add Dataproc jobs to workflow template**

**SYNOPSIS**

: **`gcloud dataproc workflow-templates add-job` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To add a Hadoop MapReduce job, run:

```
gcloud dataproc workflow-templates add-job hadoop --workflow-template my_template --jar my_jar.jar -- arg1 arg2
```

To add a Spark Scala or Java job, run:

```
gcloud dataproc workflow-templates add-job spark --workflow-template my_template --jar my_jar.jar -- arg1 arg2
```

To add a PySpark job, run:

```
gcloud dataproc workflow-templates add-job pyspark --workflow-template my_template my_script.py -- arg1 arg2
```

To add a Spark SQL job, run:

```
gcloud dataproc workflow-templates add-job spark-sql --workflow-template my_template --file my_queries.q
```

To add a Pig job, run:

```
gcloud dataproc workflow-templates add-job pig --workflow-template my_template --file my_script.pig
```

To add a Hive job, run:

```
gcloud dataproc workflow-templates add-job hive --workflow-template my_template --file my_queries.q
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[hadoop](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hadoop)`**:
Add a hadoop job to the workflow template.

**`[hive](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/hive)`**:
Add a Hive job to the workflow template.

**`[pig](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/pig)`**:
Add a Pig job to the workflow template.

**`[presto](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/presto)`**:
Add a Presto job to the workflow template.

**`[pyspark](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/pyspark)`**:
Add a PySpark job to the workflow template.

**`[spark](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark)`**:
Add a Spark job to the workflow template.

**`[spark-r](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark-r)`**:
Add a SparkR job to the workflow template.

**`[spark-sql](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/spark-sql)`**:
Add a SparkSql job to the workflow template.

**`[trino](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/trino)`**:
Add a Trino job to the workflow template.

**NOTES**

: These variants are also available:

```
gcloud alpha dataproc workflow-templates add-job
```

```
gcloud beta dataproc workflow-templates add-job
```