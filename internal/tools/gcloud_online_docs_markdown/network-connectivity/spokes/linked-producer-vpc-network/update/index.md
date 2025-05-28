# gcloud network-connectivity spokes linked-producer-vpc-network update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update)*

**NAME**

: **gcloud network-connectivity spokes linked-producer-vpc-network update - update a Producer VPC spoke**

**SYNOPSIS**

: **`gcloud network-connectivity spokes linked-producer-vpc-network update` `[SPOKE](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update#SPOKE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update#--description)`=`DESCRIPTION`] [`[--exclude-export-ranges](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update#--exclude-export-ranges)`=[`CIDR_RANGE`,…]] [`[--global](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update#--global)`] [`[--include-export-ranges](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update#--include-export-ranges)`=[`CIDR_RANGE`,…]] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the details of a Producer VPC spoke.

**EXAMPLES**

: To update the description of a Producer VPC spoke named
``my-spoke``, run:

```
gcloud network-connectivity spokes linked-producer-vpc-network update myspoke --global --description="new spoke description"
```

**POSITIONAL ARGUMENTS**

: **Spoke resource - Name of the spoke to update. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `spoke` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `spoke` on the command line with a fully
specified name;
- provide the argument `--global` on the command line.

This must be specified.

**`SPOKE`**:
ID of the spoke or fully qualified identifier for the spoke.
To set the `spoke` attribute:

- provide the argument `spoke` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
New description of the spoke.

**--exclude-export-ranges**:
New exclude export ranges of the spoke.

**--global**:
Indicates that the spoke is global.

**--include-export-ranges**:
New include export ranges of the spoke.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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

: This command uses the networkconnectivity/v1 API. The full documentation for
this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: This variant is also available:

```
gcloud beta network-connectivity spokes linked-producer-vpc-network update
```