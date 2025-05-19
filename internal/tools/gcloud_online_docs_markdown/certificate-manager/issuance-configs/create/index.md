# gcloud certificate-manager issuance-configs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create)*

**NAME**

: **gcloud certificate-manager issuance-configs create - create a Certificate Issuance Config**

**SYNOPSIS**

: **`gcloud certificate-manager issuance-configs create` (`[CERTIFICATE_ISSUANCE_CONFIG](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create#CERTIFICATE_ISSUANCE_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create#--location)`=`LOCATION`) `[--ca-pool](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create#--ca-pool)`=`CA_POOL` [`[--async](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create#--description)`=`DESCRIPTION`] [`[--key-algorithm](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create#--key-algorithm)`=`KEY_ALGORITHM`; default="rsa-2048"] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--lifetime](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create#--lifetime)`=`LIFETIME`; default="P30D"] [`[--rotation-window-percentage](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create#--rotation-window-percentage)`=`ROTATION_WINDOW_PERCENTAGE`; default=66] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/issuance-configs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Certificate Issuance Config.

**EXAMPLES**

: To create a Certificate Issuance Config called `my-cic`, run:

```
gcloud certificate-manager issuance-configs create my-cic --ca-pool=my-ca-pool
```

**POSITIONAL ARGUMENTS**

: **CertificateIssuanceConfig resource - Name of the Certificate Issuance Config to
create. The arguments in this group can be used to specify the attributes of
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

**REQUIRED FLAGS**

: **--ca-pool**:
CA Pool used for issuing certificates. For example:

```
gcloud certificate-manager issuance-configs create --ca-pool=projects/test-project/locations/us-west1/caPools/my-ca-pool
```

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Human-readable description of the resource.

**--key-algorithm**:
Key algorithm to use when generating the private key. Defaults to
`rsa-2048`. `KEY_ALGORITHM` must be one of:
`ecdsa-p256`, `rsa-2048`.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--lifetime**:
Lifetime of issued certificates in ISO 8601 format. Use `[gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)`
for details. Defaults to `P30D`.

**--rotation-window-percentage**:
How long along the lifetime of the ceritificate to renew, expressed as a
percentage. Defaults to `66`.

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

: These variants are also available:

```
gcloud alpha certificate-manager issuance-configs create
```

```
gcloud beta certificate-manager issuance-configs create
```