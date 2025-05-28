# gcloud netapp volumes replications resume  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/resume](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/resume)*

**NAME**

: **gcloud netapp volumes replications resume - resume a Cloud NetApp Volume Replication**

**SYNOPSIS**

: **`gcloud netapp volumes replications resume` (`[REPLICATION](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/resume#REPLICATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/resume#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/resume#--async)`] [`[--volume](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/resume#--volume)`=`VOLUME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/resume#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Resume a Cloud NetApp Volume Replication.

**EXAMPLES**

: The following command resumes a Replication named NAME using the required
arguments:

```
gcloud netapp volumes replications resume NAME --location=us-central1 --volume=vol1
```

To resume a Replication named NAME asynchronously, run the following command:

```
gcloud netapp volumes replications resume NAME --location=us-central1 --volume=vol1 --async
```

**POSITIONAL ARGUMENTS**

: **Replication resource - The Replication to create. The arguments in this group
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
gcloud alpha netapp volumes replications resume
```

```
gcloud beta netapp volumes replications resume
```