# gcloud alpha compute addresses update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/update)*

**NAME**

: **gcloud alpha compute addresses update - update a Compute Engine address**

**SYNOPSIS**

: **`gcloud alpha compute addresses update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/update#NAME)` [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/update#--remove-labels)`=[`KEY`,…]] [`[--global](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/update#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/update#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute addresses update` updates
labels for a Compute Engine address.

**EXAMPLES**

: To add/update labels 'k0' and 'k1' and remove labels with key 'k3' for address
'example-address', run:

```
gcloud alpha compute addresses update example-address --region=us-central1 --update-labels=k0=value1,k1=value2 --remove-labels=k3
```

Labels can be used to identify the address and to filter them as in:

```
gcloud alpha compute addresses list --filter='labels.k1:value2'
```

To list existing labels for address 'example-address', run:

```
gcloud alpha compute addresses describe example-address --format="default(labels)"
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the address to operate on.

**FLAGS**

: **--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

**--global**

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
gcloud beta compute addresses update
```