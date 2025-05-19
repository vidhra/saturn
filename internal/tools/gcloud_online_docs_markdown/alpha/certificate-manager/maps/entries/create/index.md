# gcloud alpha certificate-manager maps entries create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/create](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/create)*

**NAME**

: **gcloud alpha certificate-manager maps entries create - create a certificate map entry**

**SYNOPSIS**

: **`gcloud alpha certificate-manager maps entries create` (`[ENTRY](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/create#ENTRY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/create#--location)`=`LOCATION` `[--map](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/create#--map)`=`MAP`) (`[--hostname](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/create#--hostname)`=`HOSTNAME`     | `[--set-primary](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/create#--set-primary)`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/create#--description)`=`DESCRIPTION`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/create#--async)`] [`[--certificates](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/create#--certificates)`=[`CERTIFICATES`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` This command creates a certificate map entry.

**EXAMPLES**

: To create a certificate map entry with name simple-entry, run:

```
gcloud alpha certificate-manager maps entries create simple-entry --map=simple-map --certificates=simple-cert
```

**POSITIONAL ARGUMENTS**

: **Certificate map entry resource - The certificate map entry to create. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `entry` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENTRY`**:
ID of the certificate map entry or fully qualified identifier for the
certificate map entry.
To set the `entry` attribute:

- provide the argument `entry` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the certificate map entry.
To set the `location` attribute:

- provide the argument `entry` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- default value of location is [global].

**--map**:
The certificate map for the certificate map entry.
To set the `map` attribute:

- provide the argument `entry` on the command line with a fully
specified name;
- provide the argument `--map` on the command line.**

**REQUIRED FLAGS**

: **--hostname**

**COMMONLY USED FLAGS**

: **--description**:
Text description of a certificate map entry.

**OTHER FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**Certificate resource - The certificates to be attached to the entry. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--certificates` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--certificates` on the command line with a
fully specified name;
- default value of location is [global].

**--certificates**:
IDs of the certificates or fully qualified identifiers for the certificates.
To set the `certificate` attribute:

- provide the argument `--certificates` on the command line.**

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
gcloud certificate-manager maps entries create
```

```
gcloud beta certificate-manager maps entries create
```