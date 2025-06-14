# gcloud dataproc clusters set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/set-iam-policy)*

**NAME**

: **gcloud dataproc clusters set-iam-policy - set IAM policy for a cluster**

**SYNOPSIS**

: **`gcloud dataproc clusters set-iam-policy` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/set-iam-policy#CLUSTER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/set-iam-policy#--region)`=`REGION`) `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets the IAM policy for a cluster, given a cluster name and the policy.

**EXAMPLES**

: The following command sets the IAM policy for a cluster with the name
`example-cluster-name-1` using policy.yaml:

```
gcloud dataproc clusters set-iam-policy example-cluster-name-1 policy.yaml
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - The name of the cluster to set the policy on. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLUSTER`**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Dataproc region for the cluster. Each Dataproc region constitutes an independent
resource namespace constrained to deploying instances into Compute Engine zones
inside the region. Overrides the default `dataproc/region` property
value for this command invocation.
To set the `region` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `dataproc/region`.**

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha dataproc clusters set-iam-policy
```

```
gcloud beta dataproc clusters set-iam-policy
```