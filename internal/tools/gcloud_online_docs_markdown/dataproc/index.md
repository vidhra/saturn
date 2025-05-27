# gcloud dataproc  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc](https://cloud.google.com/sdk/gcloud/reference/dataproc)*

**NAME**

: **gcloud dataproc - create and manage Google Cloud Dataproc clusters and jobs**

**SYNOPSIS**

: **`gcloud dataproc` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/dataproc#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud dataproc command group lets you create and manage Dataproc clusters
and jobs.
Dataproc is an Apache Hadoop, Apache Spark, Apache Pig, and Apache Hive service.
It easily processes big datasets at low cost, creating managed clusters of any
size that scale down once processing is complete.
More information on Dataproc can be found here: [https://cloud.google.com/dataproc](https://cloud.google.com/dataproc)
and detailed documentation can be found here: [https://cloud.google.com/dataproc/docs/](https://cloud.google.com/dataproc/docs/)

**EXAMPLES**

: To see how to create and manage clusters, run:

```
gcloud dataproc clusters
```

To see how to submit and manage jobs, run:

```
gcloud dataproc jobs
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[autoscaling-policies](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies)`**:
Create and manage Dataproc autoscaling policies.

**`[batches](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches)`**:
Submit Dataproc batch jobs.

**`[clusters](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters)`**:
Create and manage Dataproc clusters.

**`[jobs](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs)`**:
Submit and manage Dataproc jobs.

**`[node-groups](https://cloud.google.com/sdk/gcloud/reference/dataproc/node-groups)`**:
Manage Dataproc node groups.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/dataproc/operations)`**:
View and manage Dataproc operations.

**`[workflow-templates](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates)`**:
Create and manage Dataproc workflow templates.

**NOTES**

: These variants are also available:

```
gcloud alpha dataproc
```

```
gcloud beta dataproc
```