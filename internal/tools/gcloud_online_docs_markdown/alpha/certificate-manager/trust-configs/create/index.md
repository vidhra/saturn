# gcloud alpha certificate-manager trust-configs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/trust-configs/create](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/trust-configs/create)*

**NAME**

: **gcloud alpha certificate-manager trust-configs create - create TrustConfig**

**SYNOPSIS**

: **`gcloud alpha certificate-manager trust-configs create` (`[TRUST_CONFIG](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/trust-configs/create#TRUST_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/trust-configs/create#--location)`=`LOCATION`) (`[--allowlisted-certificates](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/trust-configs/create#--allowlisted-certificates)`=[`ALLOWLISTED_CERTIFICATES`,…] `[--trust-store](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/trust-configs/create#--trust-store)`=[`intermediate-cas`=`INTERMEDIATE-CAS`],[`trust-anchors`=`TRUST-ANCHORS`]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/trust-configs/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/trust-configs/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/trust-configs/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/trust-configs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a TrustConfig.

**EXAMPLES**

: To create a TrustConfig from PEM certificate files, run:

```
gcloud alpha certificate-manager trust-configs create my-trust-config --description="my description" --labels=my-key1=my-value1,my-key2=my-value2 --trust-store=trust-anchors=ta.pem,intermediate-cas="ica1.pem;ica2.pem"
```

**POSITIONAL ARGUMENTS**

: **TrustConfig resource - Name of the TrustConfig to create. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `trust_config` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TRUST_CONFIG`**:
ID of the trustConfig or fully qualified identifier for the trustConfig.
To set the `trust_config` attribute:

- provide the argument `trust_config` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Certificate Manager location.
To set the `location` attribute:

- provide the argument `trust_config` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- default value of location is [global].**

**REQUIRED FLAGS**

: **--allowlisted-certificates**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Human-readable description of the resource.

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

**API REFERENCE**

: This command uses the `certificatemanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/certificate-manager](https://cloud.google.com/certificate-manager)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud certificate-manager trust-configs create
```

```
gcloud beta certificate-manager trust-configs create
```