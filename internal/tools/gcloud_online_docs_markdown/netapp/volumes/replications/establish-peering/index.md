# gcloud netapp volumes replications establish-peering  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/establish-peering](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/establish-peering)*

**NAME**

: **gcloud netapp volumes replications establish-peering - establish peering for Hybrid replication**

**SYNOPSIS**

: **`gcloud netapp volumes replications establish-peering` (`[REPLICATION](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/establish-peering#REPLICATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/establish-peering#--location)`=`LOCATION`) `[--peer-cluster-name](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/establish-peering#--peer-cluster-name)`=`PEER_CLUSTER_NAME` `[--peer-svm-name](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/establish-peering#--peer-svm-name)`=`PEER_SVM_NAME` `[--peer-volume-name](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/establish-peering#--peer-volume-name)`=`PEER_VOLUME_NAME` [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/establish-peering#--async)`] [`[--peer-ip-addresses](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/establish-peering#--peer-ip-addresses)`=`PEER_IP_ADDRESS`,[…]] [`[--volume](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/establish-peering#--volume)`=`VOLUME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/establish-peering#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Establish peering for Hybrid replication.

**EXAMPLES**

: The following command establishes peering for Hybrid replication named NAME
using the arguments specified:

```
gcloud netapp volumes replications establish-peering NAME --volume=volume1 --peer-cluster-name=peer-cluster-name1 --peer-svm-name=peer-svm-name1 --peer-volume-name=peer-volume-name1 --peer-ip-addresses=1.1.1.1,2.2.2.2
```

**POSITIONAL ARGUMENTS**

: **Replication resource - The Hybrid replication to establish peering for. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `replication` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `volume` attribute:

- provide the argument `replication` on the command line with a fully
specified name;
- provide the argument `--volume` on the command line.

This must be specified.

**`REPLICATION`**:
ID of the replication or fully qualified identifier for the replication.
To set the `replication` attribute:

- provide the argument `replication` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the replication.
To set the `location` attribute:

- provide the argument `replication` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.**

**REQUIRED FLAGS**

: **--peer-cluster-name**:
Name of the destination cluster to be peered with the source cluster.

**--peer-svm-name**:
Name of the local source vserver svm to be peered with the destination cluster.

**--peer-volume-name**:
Name of the source volume to be peered with the destination volume.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--peer-ip-addresses**:
List of ip addresses to be used for peering.

**Volume resource - The Volume that the Replication is based on This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.

**--volume**:
ID of the volume or fully qualified identifier for the volume.
To set the `volume` attribute:

- provide the argument `--volume` on the command line.**

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
gcloud alpha netapp volumes replications establish-peering
```

```
gcloud beta netapp volumes replications establish-peering
```