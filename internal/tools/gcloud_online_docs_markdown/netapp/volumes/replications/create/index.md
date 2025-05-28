# gcloud netapp volumes replications create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/create](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/create)*

**NAME**

: **gcloud netapp volumes replications create - create a Cloud NetApp Volume Replication**

**SYNOPSIS**

: **`gcloud netapp volumes replications create` (`[REPLICATION](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/create#REPLICATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/create#--location)`=`LOCATION`) `[--destination-volume-parameters](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/create#--destination-volume-parameters)`=[`description`=`DESCRIPTION`],[`share_name`=`SHARE_NAME`],[`storage_pool`=`STORAGE_POOL`],[`tiering_policy`=`TIERING_POLICY`],[`volume_id`=`VOLUME_ID`] `[--replication-schedule](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/create#--replication-schedule)`=`REPLICATION_SCHEDULE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/create#--async)`] [`[--cluster-location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/create#--cluster-location)`=`CLUSTER_LOCATION`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--volume](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/create#--volume)`=`VOLUME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud NetApp Volume Replication.

**EXAMPLES**

: The following command creates a Replication named NAME using the required
arguments:

```
gcloud netapp volumes replications create NAME --location=us-central1 --volume=vol1 --replication-schedule=EVERY_10_MINUTES --destination-volume-parameters=storage_pool=sp1,volume_id=vol2,share_name=share2
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

**REQUIRED FLAGS**

: **--destination-volume-parameters**:
Required, sets `destination_volume_parameters` value.

**`description`**:
Sets `description` value.

**`share_name`**:
Sets `share_name` value.

**`storage_pool`**:
Required, sets `storage_pool` value.

**`tiering_policy`**:
Sets `tiering_policy` value.

**`cooling-threshold-days`**:
Sets `cooling-threshold-days` value.

**`tier-action`**:
Sets `tier-action` value.

**`volume_id`**:
Sets `volume_id` value.

`Shorthand Example:`

```
--destination-volume-parameters='description=string,share_name=string,storage_pool=string,tiering_policy={"cooling-threshold-days": int, "tier-action": "string"},volume_id=string'
```

`JSON Example:`

```
--destination-volume-parameters='{"description": "string", "share_name": "string", "storage_pool": "string", "tiering_policy": {"cooling-threshold-days": int, "tier-action": "string"}, "volume_id": "string"}'
```

`File Example:`

```
--destination-volume-parameters=path_to_file.(yaml|json)
```

**--replication-schedule**:
The schedule for the Replication.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cluster-location**:
Location of the user cluster.

**--description**:
A description of the Cloud NetApp Replication

**--labels**:
List of label KEY=VALUE pairs to add.
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
gcloud alpha netapp volumes replications create
```

```
gcloud beta netapp volumes replications create
```