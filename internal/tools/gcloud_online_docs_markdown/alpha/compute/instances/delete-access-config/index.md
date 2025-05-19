# gcloud alpha compute instances delete-access-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete-access-config](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete-access-config)*

**NAME**

: **gcloud alpha compute instances delete-access-config - delete an access configuration from a virtual machine network interface**

**SYNOPSIS**

: **`gcloud alpha compute instances delete-access-config` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete-access-config#INSTANCE_NAME)` [`[--access-config-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete-access-config#--access-config-name)`=`ACCESS_CONFIG_NAME`; default="external-nat"] [`[--network-interface](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete-access-config#--network-interface)`=`NETWORK_INTERFACE`; default="nic0"] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete-access-config#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete-access-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instances
delete-access-config` is used to delete access configurations from network
interfaces of Compute Engine virtual machines. Access configurations let you
assign a public, external IP to a virtual machine. The delete-access-config
operation removes external IP from the instance interface. If there is traffic
routed to the external IP, after deleting the access config operation, traffic
to the external IP will not reach the VM anymore.

**EXAMPLES**

: To remove the externally accessible IP from a virtual machine named
``example-instance`` in zone
``us-central1-a``, run:

```
gcloud alpha compute instances delete-access-config example-instance --zone=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--access-config-name**:
Specifies the name of the access configuration to delete.
``external-nat`` is used as the default if this
flag is not provided.

**--network-interface**:
Specifies the name of the network interface from which to delete the access
configuration. If this is not provided, then
``nic0`` is used as the default.

**--zone**:
Zone of the instance to operate on. If not specified, you might be prompted to
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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instances delete-access-config
```

```
gcloud beta compute instances delete-access-config
```