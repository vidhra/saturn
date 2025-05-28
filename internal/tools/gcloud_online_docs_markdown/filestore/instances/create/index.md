# gcloud filestore instances create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create)*

**NAME**

: **gcloud filestore instances create - create a Filestore instance**

**SYNOPSIS**

: **`gcloud filestore instances create` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#INSTANCE)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--zone)`=`ZONE`) `[--file-share](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--file-share)`=[`capacity`=`CAPACITY`],[`name`=`NAME`],[`nfs-export-options`=`NFS-EXPORT-OPTIONS`],[`source-backup`=`SOURCE-BACKUP`],[`source-backup-region`=`SOURCE-BACKUP-REGION`] `[--network](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--network)`=[`connect-mode`=`CONNECT-MODE`],[`name`=`NAME`],[`reserved-ip-range`=`RESERVED-IP-RANGE`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--location](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--location)`=`LOCATION`] [`[--performance](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--performance)`=[`max-iops`=`MAX-IOPS`],[`max-iops-per-tb`=`MAX-IOPS-PER-TB`]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--region)`=`REGION`] [`[--source-instance](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--source-instance)`=`SOURCE_INSTANCE`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--tags)`=[`KEY`=`VALUE`,…]] [`[--tier](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--tier)`=`TIER`; default=`"BASIC_HDD"`] [`[--deletion-protection](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--deletion-protection)` : `[--deletion-protection-reason](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--deletion-protection-reason)`=`DELETION_PROTECTION_REASON`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#--kms-project)`=`KMS_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Filestore instance.

**EXAMPLES**

: The following command creates a Filestore instance named NAME with a single
volume.

```
gcloud filestore instances create NAME --description=DESCRIPTION --tier=TIER --file-share=name=VOLUME_NAME,capacity=CAPACITY --network=name=NETWORK_NAME,reserved-ip-range=RESERVED_IP_RANGE,connect-mode=CONNECT_MODE --zone=ZONE --performance=max-iops-per-tb=MAX-IOPS-PER-TB --kms-key=KMS-KEY --kms-keyring=KMS_KEYRING --kms-location=KMS_LOCATION --kms-project=KMS_PROJECT --flags-file=FLAGS_FILE --source-instance=SOURCE_INSTANCE
```

```
Example json configuration file:

 { "--file-share": {"capacity": "61440",
"name": "my_vol",
"nfs-export-options": [
  {
    "access-mode": "READ_WRITE",
    "ip-ranges": [
      "10.0.0.0/8",
    ],
    "squash-mode": "NO_ROOT_SQUASH",
  },
   {
    "access-mode": "READ_ONLY",
    "ip-ranges": [
      "192.168.0.0/24"
    ],
    "squash-mode": "ROOT_SQUASH",
    "anon_uid": 1003,
    "anon_gid": 1003
  }
]
 } }
```

**POSITIONAL ARGUMENTS**

: **Instance resource - The instance to create. The arguments in this group can be
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

**REQUIRED FLAGS**

: **--file-share**:
File share configuration for an instance. Specifying both `name` and
`capacity` is required.

**`capacity`**:
The desired capacity of the volume in GB or TB units. If no capacity unit is
specified, GB is assumed. Acceptable instance capacities for each tier are as
follows:

- BASIC_HDD: 1TB-63.9TB in 1GB increments or its multiples.
- BASIC_SSD: 2.5TB-63.9TB in 1GB increments or its multiples.
- HIGH_SCALE_SSD: 10TB-100TB in 2.5TB increments or its multiples.
- ZONAL: 1TB-100TB:

- 1TB-9.75TB in 256GB increments or its multiples.
- 10TB-100TB in 2.5TB increments or its multiples.
- ENTERPRISE: 1TB-10TB in 256GB increments or its multiples.
- REGIONAL: 1TB-100TB:

- 1TB-9.75TB in 256GB increments or its multiples.
- 10TB-100TB in 2.5TB increments or its multiples.

**`name`**:
The desired logical name of the volume.

**`nfs-export-options`**:
The NfsExportOptions for the Cloud Filestore instance file share. Configuring
NfsExportOptions is optional and can only be set using flags-file. Use the
`--flags-file` flag to specify the path to a JSON or YAML
configuration file that contains the required NfsExportOptions flags.

**`ip-ranges`**:
A list of IPv4 addresses or CIDR ranges that are allowed to mount the file
share. IPv4 addresses format: {octet 1}.{octet 2}.{octet 3}.{octet 4}. CIDR
range format: {octet 1}.{octet 2}.{octet 3}.{octet 4}/{mask size}. Overlapping
IP ranges are allowed for all tiers other than BASIC_HDD and BASIC_SSD. The
limit of IP ranges/addresses for each FileShareConfig among all NfsExportOptions
is 64 per instance.

**`access-mode`**:
The type of access allowed for the specified IP-addresses or CIDR ranges.
READ_ONLY: Allows only read requests on the exported file share. READ_WRITE:
Allows both read and write requests on the exported file share. The default
setting is READ_WRITE.

**`squash-mode`**:
Enables or disables root squash for the specified IP addresses or CIDR ranges.
NO_ROOT_SQUASH: Disables root squash to allow root access on the exported file
share. ROOT_SQUASH. Enables root squash to remove root access on the exported
file share. The default setting is NO_ROOT_SQUASH.

**`anon_uid`**:
An integer that represents the user ID of anonymous users. Anon_uid may only be
set when squash_mode is set to ROOT_SQUASH. If NO_ROOT_SQUASH is specified, an
error will be returned. The default value is 65534.

**`anon_gid`**:
An integer that represents the group ID of anonymous groups. Anon_gid may only
be set when squash_mode is set to ROOT_SQUASH. If NO_ROOT_SQUASH is specified,
an error will be returned. The default value is 65534.

**`source-backup`**:
The name of the backup to restore from.

**`source-backup-region`**:
The region of the source backup.

**--network**:
Network configuration for a Cloud Filestore instance. Specifying
`reserved-ip-range` and `connect-mode` is optional.

**`name`**:
The name of the Google Compute Engine [VPC network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which
the instance is connected.

**`reserved-ip-range`**:
The `reserved-ip-range` can have one of the following two types of
values: a CIDR range value when using DIRECT_PEERING connect mode or an
allocated IP address range
(https://cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address)
when using PRIVATE_SERVICE_ACCESS connect mode. When the name of an allocated IP
address range is specified, it must be one of the ranges associated with the
private service access connection. When specified as a direct CIDR value, it
must be a /29 CIDR block for Basic tier or a /24 CIDR block for High Scale,
Zonal, Enterprise or Regional tier in one of the internal IP address ranges
(https://www.arin.net/knowledge/address_filters.html) that identifies the range
of IP addresses reserved for this instance. For example, 10.0.0.0/29 or
192.168.0.0/24. The range you specify can't overlap with either existing subnets
or assigned IP address ranges for other Cloud Filestore instances in the
selected VPC network.

**`connect-mode`**:
Network connection mode used by instances. CONNECT_MODE must be one of:
DIRECT_PEERING or PRIVATE_SERVICE_ACCESS.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
A description of the Cloud Filestore instance.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
gcloud filestore instances create example-cluster --performance=max-iops=17000
```

Configure an instance with `max-iops-per-tb` performance:

```
gcloud filestore instances create example-cluster --performance=max-iops-per-tb=17000
```

**--region**:
Region of the Cloud Filestore instance.

**--source-instance**:
The replication source instance of the Cloud Filestore instance.

**--tags**:
List of tags KEY=VALUE pairs to bind. Each item must be expressed as
`<tag-key-namespaced-name>=<tag-value-short-name>`.
Example: `123/environment=production,123/costCenter=marketing`

**--tier**:
The service tier for the Cloud Filestore instance. For more details, see: [https://cloud.google.com/filestore/docs/instance-tiers](https://cloud.google.com/filestore/docs/instance-tiers)
`TIER` must be one of:

**`basic-hdd`**:
Performant NFS storage system using HDD.

**`basic-ssd`**:
Performant NFS storage system using SSD.

**`enterprise`**:
Enterprise instance. Use REGIONAL instead whenever possible.

**`high-scale-ssd`**:
High Scale SSD instance, an alias for ZONAL. Use ZONAL instead whenever
possible.

**`premium`**:
Premium Filestore instance, An alias for BASIC_SSD. Use BASIC_SSD instead
whenever possible.

**`regional`**:
Regional instances offer the features and availability needed for
mission-critical workloads.

**`standard`**:
Standard Filestore instance, An alias for BASIC_HDD. Use BASIC_HDD instead
whenever possible.

**`zonal`**:
Zonal instances offer NFS storage system suitable for high performance computing
application requirements. It offers fast performance that scales with capacity
and allows you to grow and shrink capacity.

**--deletion-protection**

**--kms-key**

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
gcloud alpha filestore instances create
```

```
gcloud beta filestore instances create
```