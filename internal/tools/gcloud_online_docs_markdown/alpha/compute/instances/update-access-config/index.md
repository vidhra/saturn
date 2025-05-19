# gcloud alpha compute instances update-access-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config)*

**NAME**

: **gcloud alpha compute instances update-access-config - update a Compute Engine virtual machine access configuration**

**SYNOPSIS**

: **`gcloud alpha compute instances update-access-config` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config#INSTANCE_NAME)` [`[--network-interface](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config#--network-interface)`=`NETWORK_INTERFACE`; default="nic0"] [`[--network-tier](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config#--network-tier)`=`NETWORK_TIER`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config#--zone)`=`ZONE`] [`[--no-ipv6-public-ptr](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config#--ipv6-public-ptr)`     | `[--ipv6-public-ptr-domain](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config#--ipv6-public-ptr-domain)`=`IPV6_PUBLIC_PTR_DOMAIN`] [`[--public-dns](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config#--public-dns)`     | `[--no-public-dns](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config#--public-dns)`] [`[--public-ptr](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config#--public-ptr)`     | `[--no-public-ptr](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config#--public-ptr)`] [`[--public-ptr-domain](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config#--public-ptr-domain)`=`PUBLIC_PTR_DOMAIN`     | `[--no-public-ptr-domain](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config#--public-ptr-domain)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-access-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instances
update-access-config` is used to update access configurations for network
interfaces of Compute Engine virtual machines. IPv4 and IPv6 access
configurations cannot be updated together.

**EXAMPLES**

: To update public PTR record in IPv4 access config in network interface 'nic0' of
an instance, run:

```
gcloud alpha compute instances update-access-config example-instance --network-interface=nic0 --zone=us-central1-b --public-ptr --public-ptr-domain=exampledomain.com.
```

To update public PTR record in IPv6 access config in default network interface
'nic0' of an instance, run:

```
gcloud alpha compute instances update-access-config example-instance --zone=us-central1-b --ipv6-public-ptr-domain=exampledomain.com.
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--network-interface**:
Specifies the name of the network interface which contains the access
configuration. If this is not provided, then "nic0" is used as the default.

**--network-tier**:
Update the network tier of the access configuration. It does not allow to change
from `PREMIUM` to `STANDARD` and visa versa.

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

**--no-ipv6-public-ptr**

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
gcloud compute instances update-access-config
```

```
gcloud beta compute instances update-access-config
```