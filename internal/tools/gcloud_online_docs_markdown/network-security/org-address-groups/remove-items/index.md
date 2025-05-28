# gcloud network-security org-address-groups remove-items  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/remove-items](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/remove-items)*

**NAME**

: **gcloud network-security org-address-groups remove-items - remove items from an address group of organization**

**SYNOPSIS**

: **`gcloud network-security org-address-groups remove-items` (`[ADDRESS_GROUP](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/remove-items#ADDRESS_GROUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/remove-items#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/remove-items#--organization)`=`ORGANIZATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/remove-items#--async)`] [`[--items](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/remove-items#--items)`=[`ITEMS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/remove-items#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Remove items from an existing address group of organization.

**EXAMPLES**

: Remove an item from an address group named
``my-address-group`` of organization 1234.

```
gcloud network-security org-address-groups remove-items my-address-group --items=192.168.1.1 --organization=1234
```

**POSITIONAL ARGUMENTS**

: **Address group resource - Name of the address group to be updated. The arguments
in this group can be used to specify the attributes of this resource.
This must be specified.

**`ADDRESS_GROUP`**:
ID of the address group or fully qualified identifier for the address group.
To set the `address_group` attribute:

- provide the argument `address_group` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `address_group` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
Organization number.
To set the `organization` attribute:

- provide the argument `address_group` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--items**:
Items to be removed from the address group.

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

: This command uses the `networksecurity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/networking](https://cloud.google.com/networking)

**NOTES**

: These variants are also available:

```
gcloud alpha network-security org-address-groups remove-items
```

```
gcloud beta network-security org-address-groups remove-items
```