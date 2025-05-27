# gcloud dataproc clusters gke  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke)*

**NAME**

: **gcloud dataproc clusters gke - create Dataproc GKE-based virtual clusters**

**SYNOPSIS**

: **`gcloud dataproc clusters gke` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: All interactions other than creation should be handled by "gcloud dataproc
clusters" commands.

**EXAMPLES**

: To create a cluster, run:

```
gcloud dataproc clusters gke my-cluster --region='us-central1' --gke-cluster='my-gke-cluster' --spark-engine-version='latest' --pools='name=dp,roles=default'
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke/create)`**:
Create a GKE-based virtual cluster.

**NOTES**

: These variants are also available:

```
gcloud alpha dataproc clusters gke
```

```
gcloud beta dataproc clusters gke
```