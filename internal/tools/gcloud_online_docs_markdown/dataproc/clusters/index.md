# gcloud dataproc clusters  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters)*

**NAME**

: **gcloud dataproc clusters - create and manage Dataproc clusters**

**SYNOPSIS**

: **`gcloud dataproc clusters` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create and manage Dataproc clusters.

**EXAMPLES**

: To create a cluster, run:

```
gcloud dataproc clusters create my-cluster --region=us-central1
```

To resize a cluster, run:

```
gcloud dataproc clusters update my-cluster --region=us-central1 --num-workers 5
```

To delete a cluster, run:

```
gcloud dataproc clusters delete my-cluster --region=us-central1
```

To view the details of a cluster, run:

```
gcloud dataproc clusters describe my-cluster --region=us-central1
```

To see the list of all clusters, run:

```
gcloud dataproc clusters list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[gke](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/gke)`**:
Create Dataproc GKE-based virtual clusters.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create)`**:
Create a cluster.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/delete)`**:
Delete a cluster.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/describe)`**:
View the details of a cluster.

**`[diagnose](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/diagnose)`**:
Run a detailed diagnostic on a cluster.

**`[export](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/export)`**:
Export a cluster.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/get-iam-policy)`**:
Get IAM policy for a cluster.

**`[import](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/import)`**:
Import a cluster.

**`[list](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/list)`**:
View a list of clusters in a project.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/set-iam-policy)`**:
Set IAM policy for a cluster.

**`[start](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/start)`**:
Start a cluster.

**`[stop](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/stop)`**:
Stop a cluster.

**`[update](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update)`**:
Update labels and/or the number of worker nodes in a cluster.

**NOTES**

: These variants are also available:

```
gcloud alpha dataproc clusters
```

```
gcloud beta dataproc clusters
```