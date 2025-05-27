# gcloud dataproc jobs submit  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit)*

**NAME**

: **gcloud dataproc jobs submit - submit Dataproc jobs to execute on a cluster**

**SYNOPSIS**

: **`gcloud dataproc jobs submit` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit#COMMAND)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit#--async)`] [`[--bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit#--bucket)`=`BUCKET`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Submit Dataproc jobs to execute on a cluster.

**EXAMPLES**

: To submit a Hadoop MapReduce job, run:

```
gcloud dataproc jobs submit hadoop --cluster my-cluster --jar my_jar.jar -- arg1 arg2
```

To submit a Spark Scala or Java job, run:

```
gcloud dataproc jobs submit spark --cluster my-cluster --jar my_jar.jar -- arg1 arg2
```

To submit a PySpark job, run:

```
gcloud dataproc jobs submit pyspark --cluster my-cluster my_script.py -- arg1 arg2
```

To submit a Spark SQL job, run:

```
gcloud dataproc jobs submit spark-sql --cluster my-cluster --file my_queries.q
```

To submit a Pig job, run:

```
gcloud dataproc jobs submit pig --cluster my-cluster --file my_script.pig
```

To submit a Hive job, run:

```
gcloud dataproc jobs submit hive --cluster my-cluster --file my_queries.q
```

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--bucket**:
The Cloud Storage bucket to stage files in. Defaults to the cluster's configured
bucket.

**--region**:
Dataproc region to use. Each Dataproc region constitutes an independent resource
namespace constrained to deploying instances into Compute Engine zones inside
the region. Overrides the default `dataproc/region` property value
for this command invocation.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[flink](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/flink)`**:
Submit a Flink job to a cluster.

**`[hadoop](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop)`**:
Submit a Hadoop job to a cluster.

**`[hive](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hive)`**:
Submit a Hive job to a cluster.

**`[pig](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/pig)`**:
Submit a Pig job to a cluster.

**`[presto](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/presto)`**:
Submit a Presto job to a cluster.

**`[pyspark](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/pyspark)`**:
Submit a PySpark job to a cluster.

**`[spark](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark)`**:
Submit a Spark job to a cluster.

**`[spark-r](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-r)`**:
Submit a SparkR job to a cluster.

**`[spark-sql](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-sql)`**:
Submit a Spark SQL job to a cluster.

**`[trino](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/trino)`**:
Submit a Trino job to a cluster.

**NOTES**

: These variants are also available:

```
gcloud alpha dataproc jobs submit
```

```
gcloud beta dataproc jobs submit
```