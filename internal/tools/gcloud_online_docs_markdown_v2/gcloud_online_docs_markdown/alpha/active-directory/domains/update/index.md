# gcloud alpha active-directory domains update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update)*

**NAME**

: **gcloud alpha active-directory domains update - update a Managed Microsoft AD domain**

**SYNOPSIS**

: **`gcloud alpha active-directory domains update` `[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update#DOMAIN)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update#--async)`] [`[--enable-audit-logs](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update#--enable-audit-logs)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--add-authorized-networks](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update#--add-authorized-networks)`=[`AUTH_NET1`, `[AUTH_NET2](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update#AUTH_NET2)`, …,…]     | `[--remove-authorized-networks](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update#--remove-authorized-networks)`=[`AUTH_NET1`, `[AUTH_NET2](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update#AUTH_NET2)`, …,…]] [`[--add-region](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update#--add-region)`=`ADD_REGION`     | `[--remove-region](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update#--remove-region)`=`REMOVE_REGION`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update the metadata and/or configuration parameters of a
managed Microsoft AD domain.
This command can fail for the following reasons:

- The AD domain specified does not exist.
- The active account does not have permission to update the given AD domain.

**EXAMPLES**

: The following command updates an AD domain with the name
`my-domain.com` to add the two labels, `env` and
`service` and to add a provisioned region `us-west1`:

```
gcloud alpha active-directory domains update my-domain.com --update-labels=env=test,service=foo --add-region=us-west1
```

This peers the domain `my-domain.com` to the network
`my-network`.

```
gcloud alpha active-directory domains update my-domain.com --add-authorized-networks=projects/my-project/global/networks/my-network
```

**POSITIONAL ARGUMENTS**

: **Domain resource - Name of the Managed Microsoft AD domain you want to update.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `domain` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DOMAIN`**:
ID of the domain or fully qualified identifier for the domain.
To set the `domain` attribute:

- provide the argument `domain` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--enable-audit-logs**:
If specified, Active Directory data audit logs are enabled for the domain.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--add-authorized-networks**

**--add-region**

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

: This command uses the `managedidentities/v1alpha1` API. The full
documentation for this API can be found at: [https://cloud.google.com/managed-microsoft-ad/](https://cloud.google.com/managed-microsoft-ad/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud active-directory domains update
```

```
gcloud beta active-directory domains update
```