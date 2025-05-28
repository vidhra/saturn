# gcloud alpha compute instances add-access-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config)*

**NAME**

: **gcloud alpha compute instances add-access-config - create a Compute Engine virtual machine access configuration**

**SYNOPSIS**

: **`gcloud alpha compute instances add-access-config` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config#INSTANCE_NAME)` [`[--access-config-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config#--access-config-name)`=`ACCESS_CONFIG_NAME`; default="external-nat"] [`[--address](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config#--address)`=`ADDRESS`] [`[--network-interface](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config#--network-interface)`=`NETWORK_INTERFACE`; default="nic0"] [`[--network-tier](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config#--network-tier)`=`NETWORK_TIER`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config#--zone)`=`ZONE`] [`[--public-dns](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config#--public-dns)`     | `[--no-public-dns](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config#--public-dns)`] [`[--public-ptr](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config#--public-ptr)`     | `[--no-public-ptr](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config#--public-ptr)`] [`[--public-ptr-domain](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config#--public-ptr-domain)`=`PUBLIC_PTR_DOMAIN`     | `[--no-public-ptr-domain](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config#--public-ptr-domain)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instances
add-access-config` is used to create access configurations for network
interfaces of Compute Engine virtual machines. This allows you to assign a
public, external IP to a virtual machine.

**EXAMPLES**

: To assign an public, externally accessible IP to a virtual machine named
``example-instance`` in zone
``us-central1-a``, run:

```
gcloud alpha compute instances add-access-config example-instance --zone=us-central1-a
```

To assign the specific, reserved public IP address
``123.456.789.123`` to the virtual machine,
run:

```
gcloud alpha compute instances add-access-config example-instance --zone=us-central1-a --address=123.456.789.123
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--access-config-name**:
Specifies the name of the new access configuration.
``external-nat`` is used as the default if this
flag is not provided. Since ONE_TO_ONE_NAT is currently the only access-config
type, it is not recommended that you change this value.

**--address**:
Specifies the external IP address of the new access configuration. If this is
not specified, then the service will choose an available ephemeral IP address.
If an explicit IP address is given, then that IP address must be reserved by the
project and not be in use by another resource.

**--network-interface**:
Specifies the name of the network interface which contains the access
configuration. If this is not provided, then "nic0" is used as the default.

**--network-tier**:
Specifies the network tier of the access configuration.
``NETWORK_TIER`` must be one of:
`PREMIUM`, `STANDARD`. The default value is
`PREMIUM`.

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

**--public-dns**

**--public-ptr**

**--public-ptr-domain**

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
gcloud compute instances add-access-config
```

```
gcloud beta compute instances add-access-config
```