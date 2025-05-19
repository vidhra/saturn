# gcloud alpha bms networks update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bms/networks/update](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/networks/update)*

**NAME**

: **gcloud alpha bms networks update - update a Bare Metal Solution network**

**SYNOPSIS**

: **`gcloud alpha bms networks update` (`[NETWORK](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/networks/update#NETWORK)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/networks/update#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/networks/update#--async)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/networks/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--add-ip-range-reservation](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/networks/update#--add-ip-range-reservation)`=[`PROPERTY`=`VALUE`,…]     | `[--clear-ip-range-reservations](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/networks/update#--clear-ip-range-reservations)`     | `[--remove-ip-range-reservation](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/networks/update#--remove-ip-range-reservation)`=[`PROPERTY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/networks/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/networks/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/networks/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a Bare Metal Solution network.
This call returns immediately, but the update operation may take several minutes
to complete. To check if the operation is complete, use the
`describe` command for the network.

**EXAMPLES**

: To update an network called ``my-network`` in
region ``us-central1`` with a new label
``key1=value1``, run:

```
gcloud alpha bms networks update my-network --region=us-central1 --update-labels=key1=value1
```

To clear all labels, run:

```
gcloud alpha bms networks update my-network --region=us-central1 --clear-labels
```

**POSITIONAL ARGUMENTS**

: **Network resource - network. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `network` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NETWORK`**:
ID of the network or fully qualified identifier for the network.
To set the `network` attribute:

- provide the argument `network` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Region of the resource.
To set the `region` attribute:

- provide the argument `network` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--add-ip-range-reservation**

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

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud bms networks update
```