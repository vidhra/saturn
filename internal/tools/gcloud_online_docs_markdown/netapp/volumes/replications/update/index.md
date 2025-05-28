# gcloud netapp volumes replications update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/update](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/update)*

**NAME**

: **gcloud netapp volumes replications update - update a Cloud NetApp Volume Replication**

**SYNOPSIS**

: **`gcloud netapp volumes replications update` (`[REPLICATION](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/update#REPLICATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/update#--async)`] [`[--cluster-location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/update#--cluster-location)`=`CLUSTER_LOCATION`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/update#--description)`=`DESCRIPTION`] [`[--replication-schedule](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/update#--replication-schedule)`=`REPLICATION_SCHEDULE`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--volume](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/update#--volume)`=`VOLUME`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud NetApp Volume Replication and its specified parameters.

**EXAMPLES**

: The following command updates a Replication named NAME and its specified
parameters:

```
gcloud netapp volumes replications update NAME --location=us-central1 --volume=vol1 --replication-schedule=EVERY_5_MINUTES --description="new description" --cluster-location= us-central1
```

**POSITIONAL ARGUMENTS**

: **Replication resource - The Replication to update. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cluster-location**:
Location of the user cluster.

**--description**:
A description of the Cloud NetApp Replication

**--replication-schedule**:
The schedule for the Replication.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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

**--clear-labels**

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
gcloud alpha netapp volumes replications update
```

```
gcloud beta netapp volumes replications update
```