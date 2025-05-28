# gcloud certificate-manager maps entries delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/delete](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/delete)*

**NAME**

: **gcloud certificate-manager maps entries delete - delete a certificate map entry**

**SYNOPSIS**

: **`gcloud certificate-manager maps entries delete` (`[ENTRY](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/delete#ENTRY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/delete#--location)`=`LOCATION` `[--map](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/delete#--map)`=`MAP`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a certificate map entry resource.

**EXAMPLES**

: To delete the certificate map entry with name simple-entry, run:

```
gcloud certificate-manager maps entries delete simple-entry --map=simple-map
```

**POSITIONAL ARGUMENTS**

: **Certificate map entry resource - The certificate map entry to delete. The
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: These variants are also available:

```
gcloud alpha certificate-manager maps entries delete
```

```
gcloud beta certificate-manager maps entries delete
```