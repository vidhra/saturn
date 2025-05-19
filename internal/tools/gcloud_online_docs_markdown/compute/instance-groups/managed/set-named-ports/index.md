# gcloud compute instance-groups managed set-named-ports  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-named-ports](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-named-ports)*

**NAME**

: **gcloud compute instance-groups managed set-named-ports - sets the list of named ports for an instance group**

**SYNOPSIS**

: **`gcloud compute instance-groups managed set-named-ports` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-named-ports#NAME)` `[--named-ports](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-named-ports#--named-ports)`=[`NAME`:`[PORT](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-named-ports#PORT)`,…] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-named-ports#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-named-ports#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-named-ports#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Named ports are key:value pairs metadata representing the service name and the
port that it's running on. Named ports can be assigned to an instance group,
which indicates that the service is available on all instances in the group.
This information is used by Application Load Balancers and proxy Network Load
Balancers.
`gcloud compute instance-groups managed set-named-ports` sets the
list of named ports for all instances in an instance group.
Note: Running this command will clear all existing named ports.

**EXAMPLES**

: For example, to apply the named ports to an entire instance group:

```
gcloud compute instance-groups managed set-named-ports example-instance-group --named-ports=example-service:1111 --zone=us-central1-a
```

The above example will assign a name 'example-service' for port 1111 to the
instance group called 'example-instance-group' in the
``us-central1-a`` zone. The command removes any
named ports that are already set for this instance group.
To clear named ports from instance group provide empty named ports list as
parameter:

```
gcloud compute instance-groups managed set-named-ports example-instance-group --named-ports="" --zone=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the instance group to operate on.

**REQUIRED FLAGS**

: **--named-ports**:
The comma-separated list of key:value pairs representing the service name and
the port that it is running on.
To clear the list of named ports pass empty list as flag value. For example:

```
gcloud compute instance-groups managed set-named-ports example-instance-group --named-ports ""
```

**OPTIONAL FLAGS**

: **--region**

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
gcloud alpha compute instance-groups managed set-named-ports
```

```
gcloud beta compute instance-groups managed set-named-ports
```