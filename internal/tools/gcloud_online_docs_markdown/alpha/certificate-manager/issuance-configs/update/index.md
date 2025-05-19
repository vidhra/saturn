# gcloud alpha certificate-manager issuance-configs update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/issuance-configs/update](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/issuance-configs/update)*

**NAME**

: **gcloud alpha certificate-manager issuance-configs update - update a Certificate Issuance Config**

**SYNOPSIS**

: **`gcloud alpha certificate-manager issuance-configs update` (`[CERTIFICATE_ISSUANCE_CONFIG](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/issuance-configs/update#CERTIFICATE_ISSUANCE_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/issuance-configs/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/issuance-configs/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/issuance-configs/update#--description)`=`DESCRIPTION`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/issuance-configs/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/issuance-configs/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/issuance-configs/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/issuance-configs/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a Certificate Issuance Config.

**EXAMPLES**

: To update a Certificate Issuance Config called `my-cic`, run:

```
gcloud alpha certificate-manager issuance-configs update my-cic --description="updated description" --update-labels=my-key1=my-updated-value1 --remove-labels=my-key2
```

**POSITIONAL ARGUMENTS**

: **CertificateIssuanceConfig resource - Name of the Certificate Issuance Config to
update. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `certificate_issuance_config` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CERTIFICATE_ISSUANCE_CONFIG`**:
ID of the certificateIssuanceConfig or fully qualified identifier for the
certificateIssuanceConfig.
To set the `certificate_issuance_config` attribute:

- provide the argument `certificate_issuance_config` on the command
line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Certificate Manager location.
To set the `location` attribute:

- provide the argument `certificate_issuance_config` on the command
line with a fully specified name;
- provide the argument `--location` on the command line;
- default value of location is [global].**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Human-readable description of the resource.

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

: This command uses the `certificatemanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/certificate-manager](https://cloud.google.com/certificate-manager)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud certificate-manager issuance-configs update
```

```
gcloud beta certificate-manager issuance-configs update
```