# gcloud filestore instances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update)*

**NAME**

: **gcloud filestore instances update - update a Filestore instance**

**SYNOPSIS**

: **`gcloud filestore instances update` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#INSTANCE)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#--zone)`=`ZONE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#--description)`=`DESCRIPTION`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#--location)`=`LOCATION`] [`[--performance](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#--performance)`=[`max-iops`=`MAX-IOPS`],[`max-iops-per-tb`=`MAX-IOPS-PER-TB`]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#--region)`=`REGION`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#--remove-labels)`=[`KEY`,…]] [[`[--file-share](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#--file-share)`=[`capacity`=`CAPACITY`],[`name`=`NAME`],[`nfs-export-options`=`NFS-EXPORT-OPTIONS`] : `[--clear-nfs-export-options](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#--clear-nfs-export-options)`]] [`[--[no-]deletion-protection](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#--[no-]deletion-protection)` `[--deletion-protection-reason](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#--deletion-protection-reason)`=`DELETION_PROTECTION_REASON`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Filestore instance.

**EXAMPLES**

: The following command updates the Filestore instance NAME to change the
description to "A new description."

```
gcloud filestore instances update NAME --description="A new description."
```

The following command updates a Filestore instance named NAME to add the label
"key1=value1" and remove any metadata with the label "key2".

```
gcloud filestore instances update NAME --update-labels=key1=value1 --remove-labels=key2
```

```
gcloud filestore instances update NAME --zone=ZONE --flags-file=FILE_PATH
```

Example json configuration file:
```
{
"--file-share":
{
  "capacity": "102400",
  "name": "my_vol",
  "nfs-export-options": [
    {
      "access-mode": "READ_WRITE",
      "ip-ranges": [
        "10.0.0.0/29",
        "10.2.0.0/29"
      ],
      "squash-mode": "ROOT_SQUASH",
      "anon_uid": 1003,
      "anon_gid": 1003
    }
  ]
}
}
```

The following command updates a Filestore instance named NAME to change the
capacity to CAPACITY.

```
gcloud filestore instances update NAME --project=PROJECT_ID --zone=ZONE --file-share=name=VOLUME_NAME,capacity=CAPACITY
```

The following command updates a Filestore instance named NAME to configure the
max-iops-per-tb to MAX-IOPS-PER-TB.

```
gcloud filestore instances update NAME --project=PROJECT_ID --zone=ZONE --performance=max-iops-per-tb=MAX-IOPS-PER-TB
```

**POSITIONAL ARGUMENTS**

: **Instance resource - The instance to update. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
The zone of the instance.
To set the `zone` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line;
- provide the argument `region` on the command line;
- provide the argument `location` on the command line;
- set the property `filestore/zone`;
- set the property `filestore/region`;
- set the property `filestore/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
A description of the Cloud Filestore instance.

**--location**:
Location of the Cloud Filestore instance/operation.

**--performance**:
Performance configuration for the instance. This flag is used to configure the
read IOPS provisioned for the instance. The instance's write IOPS and read/write
throughputs will be derived from the configured read IOPS. For more information
about the derived performance limits and default performance see: [https://cloud.google.com/filestore/docs/performance](https://cloud.google.com/filestore/docs/performance).
Must be one of:

```
max-iops
  The number of IOPS to provision for the instance.
  MAX-IOPS must be in multiple of 1000 and in the supported IOPS
  range for the current capacity of the instance.
  For more details, see: https://cloud.google.com/filestore/docs/performance.
```

```
max-iops-per-tb
  Is used for setting the max IOPS of the instance by
  specifying the IOPS per TB. When this parameter is used, the
  max IOPS are derived from the instance capacity:
  The instance max IOPS will be calculated by multiplying the
  capacity of the instance (TB) by MAX-IOPS-PER-TB, and rounding
  to the nearest 1000. The max IOPS will be changed
  dynamically based on the instance capacity.
  MAX-IOPS-PER-TB must be in the supported range of the instance.
  For more details, see: https://cloud.google.com/filestore/docs/performance.
```

Examples:
Configure an instance with `max-iops` performance:

```
gcloud filestore instances update example-cluster --performance=max-iops=17000
```

Configure an instance with `max-iops-per-tb` performance:

```
gcloud filestore instances update example-cluster --performance=max-iops-per-tb=17000
```

**--region**:
Region of the Cloud Filestore instance.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

**--file-share**

**--[no-]deletion-protection**

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
gcloud alpha filestore instances update
```

```
gcloud beta filestore instances update
```