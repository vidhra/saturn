# gcloud filestore instances promote-replica  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/instances/promote-replica](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/promote-replica)*

**NAME**

: **gcloud filestore instances promote-replica - promote a Filestore standby replication instance**

**SYNOPSIS**

: **`gcloud filestore instances promote-replica` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/promote-replica#INSTANCE)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/promote-replica#--zone)`=`ZONE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/promote-replica#--async)`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/promote-replica#--location)`=`LOCATION`] [`[--peer-instance](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/promote-replica#--peer-instance)`=`PEER_INSTANCE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/promote-replica#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Promote a Filestore standby replication instance to a regular instance. This
command can be called directly on the standby instance or on the active instance
with the standby peer instance parameter. When used on the standby instance
promotes the standby instance to a regular instance even if the active instance
is unavailable. When used on the active instance detaches the standby instance
from the active instance even if the standby instance is unavailable.
This command can fail for the following reasons:

- The target instance does not exist.
- The instance is not a standby replication member.
- The instance is an active instance and the peer instance parameter is missing or
invalid.

**EXAMPLES**

: To promote a standby instance with the name
``my-replica-instance`` located in
``us-central1``, run:

```
gcloud filestore instances promote-replica my-replica-instance --zone=us-central1
```

To promote a standby instance with the name
``my-replica-instance`` located in
``us-central1``, attached to the active peer
instance ``my-active-instance`` located in
``us-west1``, run:

```
gcloud filestore instances promote-replica my-active-instance --zone=us-west1 --peer-instance=projects/my-project/locations/us-central1/instances/my-replica-instance
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Filestore instance to
promote. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
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
The zone of the Filestore instance.
To set the `zone` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line;
- provide the argument `--location` on the command line;
- set the property `filestore/zone`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--location**:
Location of the Filestore instance to promote.

**--peer-instance**:
The name of the standby peer instance to promote.

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

**API REFERENCE**

: This command uses the `file/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/filestore/](https://cloud.google.com/filestore/)

**NOTES**

: This variant is also available:

```
gcloud beta filestore instances promote-replica
```