# gcloud compute instances start  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/start](https://cloud.google.com/sdk/gcloud/reference/compute/instances/start)*

**NAME**

: **gcloud compute instances start - start a stopped virtual machine instance**

**SYNOPSIS**

: **`gcloud compute instances start` `[INSTANCE_NAMES](https://cloud.google.com/sdk/gcloud/reference/compute/instances/start#INSTANCE_NAMES)` [`[INSTANCE_NAMES](https://cloud.google.com/sdk/gcloud/reference/compute/instances/start#INSTANCE_NAMES)` …] [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/instances/start#--async)`] [`[--csek-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/instances/start#--csek-key-file)`=`FILE`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/start#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/start#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instances start` is used to start a stopped Compute
Engine virtual machine. Only a stopped virtual machine can be started.

**EXAMPLES**

: To start a stopped instance named 'example-instance' in zone
``us-central1-a``, run:

```
gcloud compute instances start example-instance --zone=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAMES` [`INSTANCE_NAMES` …]**:
Names of the instances to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--csek-key-file**:
Path to a Customer-Supplied Encryption Key (CSEK) key file that maps Compute
Engine resources to user managed keys to be used when creating, mounting, or
taking snapshots of disks.
If you pass `-` as value of the flag, the CSEK is read from stdin.
See [https://cloud.google.com/compute/docs/disks/customer-supplied-encryption](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
for more details.

**--zone**:
Zone of the instances to operate on. If not specified, you might be prompted to
select a zone (interactive mode only). `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` attempts to identify the
appropriate zone by searching for resources in your currently active project. If
the zone cannot be determined, `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with
all available Google Cloud Platform zones.
To avoid prompting when this flag is omitted, the user can set the
``compute/zone`` property:

```
gcloud config set compute/zone ZONE
```

A list of zones can be fetched by running:

```
gcloud compute zones list
```

To unset the property, run:

```
gcloud config unset compute/zone
```

Alternatively, the zone can be stored in the environment variable
``CLOUDSDK_COMPUTE_ZONE``.

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
gcloud alpha compute instances start
```

```
gcloud beta compute instances start
```