# gcloud network-security address-groups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/address-groups/create](https://cloud.google.com/sdk/gcloud/reference/network-security/address-groups/create)*

**NAME**

: **gcloud network-security address-groups create - create an address group**

**SYNOPSIS**

: **`gcloud network-security address-groups create` (`[ADDRESS_GROUP](https://cloud.google.com/sdk/gcloud/reference/network-security/address-groups/create#ADDRESS_GROUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/address-groups/create#--location)`=`LOCATION`) `[--capacity](https://cloud.google.com/sdk/gcloud/reference/network-security/address-groups/create#--capacity)`=`CAPACITY` `[--type](https://cloud.google.com/sdk/gcloud/reference/network-security/address-groups/create#--type)`=`TYPE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/address-groups/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-security/address-groups/create#--description)`=`DESCRIPTION`] [`[--items](https://cloud.google.com/sdk/gcloud/reference/network-security/address-groups/create#--items)`=[`ITEMS`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-security/address-groups/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--purpose](https://cloud.google.com/sdk/gcloud/reference/network-security/address-groups/create#--purpose)`=[`PURPOSE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/address-groups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new address group with the given name.

**EXAMPLES**

: Create an address group with the name
``my-address-group``, type
``IPV4``, capacity
``100`` and the description
``optional description``.

```
gcloud network-security address-groups create my-address-group --type=IPV4 --capacity=100 --description="optional description"
```

**POSITIONAL ARGUMENTS**

: **Address group resource - Name of the address group to be created. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `address_group` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

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
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--capacity**:
Capacity of the address group.

**--type**:
Type of the address group. `TYPE` must be one of:
`ipv4`, `ipv6`.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the address group.

**--items**:
Items of the address group.

**--labels**:
List of label KEY=VALUE pairs to add.

**--purpose**:
List of Address Group purposes. `PURPOSE` must be one of:
`cloud-armor`, `default`.

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
gcloud alpha network-security address-groups create
```

```
gcloud beta network-security address-groups create
```