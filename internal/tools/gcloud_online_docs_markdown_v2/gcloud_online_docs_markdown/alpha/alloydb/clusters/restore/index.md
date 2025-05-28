# gcloud alpha alloydb clusters restore  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore)*

**NAME**

: **gcloud alpha alloydb clusters restore - restore an AlloyDB cluster from a given backup or a source cluster and a timestamp**

**SYNOPSIS**

: **`gcloud alpha alloydb clusters restore` `[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#CLUSTER)` `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#--region)`=`REGION` (`[--backup](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#--backup)`=`BACKUP`     | `[--point-in-time](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#--point-in-time)`=`POINT_IN_TIME` `[--source-cluster](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#--source-cluster)`=`SOURCE_CLUSTER`) [`[--allocated-ip-range-name](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#--allocated-ip-range-name)`=`ALLOCATED_IP_RANGE_NAME`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#--async)`] [`[--enable-private-service-connect](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#--enable-private-service-connect)`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#--network)`=`NETWORK`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#--tags)`=[`KEY`=`VALUE`,…]] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#--kms-project)`=`KMS_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Restore an AlloyDB cluster from a given backup or a source
cluster and a timestamp.

**EXAMPLES**

: To restore a cluster from a backup, run:

```
gcloud alpha alloydb clusters restore my-cluster --region=us-central1 --backup=my-backup
```

To restore a cluster from a source cluster and a timestamp, run:

```
gcloud alpha alloydb clusters restore my-cluster --region=us-central1 --source-cluster=old-cluster --point-in-time=2012-11-15T16:19:00.094Z
```

**POSITIONAL ARGUMENTS**

: **`CLUSTER`**:
AlloyDB cluster ID

**REQUIRED FLAGS**

: **--region**:
Regional location (e.g. `asia-east1`, `us-east1`). See the
full list of regions at [https://cloud.google.com/sql/docs/instance-locations](https://cloud.google.com/sql/docs/instance-locations).

**--backup**

**OPTIONAL FLAGS**

: **--allocated-ip-range-name**:
Name of the allocated IP range for the private IP AlloyDB cluster, for example:
"google-managed-services-default". If set, the instance IPs for this cluster
will be created in the allocated range. The range name must comply with RFC
1035. Specifically, the name must be 1-63 characters long and match the regular
expression [a-z]([-a-z0-9]`[a-z0-9])?.`

**--async``**:
Return immediately, without waiting for the operation in progress to complete.

**--enable-private-service-connect``**:
Enable Private Service Connect (PSC) connectivity for the cluster.

**--network`=`NETWORK``**:
Network in the current project that the instance will be part of. To specify
using a network with a shared VPC, use the full URL of the network. For an
example host project, `testproject`, and shared network,
`testsharednetwork`, this would be of the
form:`--network=projects/testproject/global/networks/testsharednetwork`

**--tags`=[`KEY`=`VALUE`,…]`**:
List of tags KEY=VALUE pairs to bind. Each item must be expressed as
`<tag-key-namespaced-name>=<tag-value-short-name>`.
Example: `123/environment=production,123/costCenter=marketing`

**Key resource - The Cloud KMS (Key Management Service) cryptokey that will be
used to protect the cluster. The 'AlloyDB Service Agent' service account must
hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The arguments in this
group can be used to specify the attributes of this resource.

**--kms-key`=`KMS_KEY``**:
ID of the key or fully qualified identifier for the key.
To set the `kms-key` attribute:

- provide the argument `--kms-key` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--kms-keyring`=`KMS_KEYRING``**:
The KMS keyring of the key.
To set the `kms-keyring` attribute:

- provide the argument `--kms-key` on the command line with a fully
specified name;
- provide the argument `--kms-keyring` on the command line.

**--kms-location`=`KMS_LOCATION``**:
The Google Cloud location for the key.
To set the `kms-location` attribute:

- provide the argument `--kms-key` on the command line with a fully
specified name;
- provide the argument `--kms-location` on the command line.

**--kms-project`=`KMS_PROJECT``**:
The Google Cloud project for the key.
To set the `kms-project` attribute:

- provide the argument `--kms-key` on the command line with a fully
specified name;
- provide the argument `--kms-project` on the command line;
- set the property `core/project`.**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud alloydb clusters restore
```

```
gcloud beta alloydb clusters restore
```