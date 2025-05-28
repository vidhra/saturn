# gcloud iam workload-identity-pools create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create)*

**NAME**

: **gcloud iam workload-identity-pools create - create a new workload identity pool**

**SYNOPSIS**

: **`gcloud iam workload-identity-pools create` (`[WORKLOAD_IDENTITY_POOL](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create#WORKLOAD_IDENTITY_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create#--description)`=`DESCRIPTION`] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create#--disabled)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create#--display-name)`=`DISPLAY_NAME`] [`[--inline-certificate-issuance-config-file](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create#--inline-certificate-issuance-config-file)`=`INLINE_CERTIFICATE_ISSUANCE_CONFIG_FILE`] [`[--inline-trust-config-file](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create#--inline-trust-config-file)`=`INLINE_TRUST_CONFIG_FILE`] [`[--mode](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create#--mode)`=`MODE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new workload identity pool.

**EXAMPLES**

: The following command creates a disabled workload identity pool in the default
project with the ID
``my-workload-identity-pool``. Explicit values
for all required and optional parameters are provided.

```
gcloud iam workload-identity-pools create my-workload-identity-pool --location="global" --display-name="My workload pool" --description="My workload pool description" --disabled
```

**POSITIONAL ARGUMENTS**

: **Workload identity pool resource - The workload identity pool to create. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `workload_identity_pool` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`WORKLOAD_IDENTITY_POOL`**:
ID of the workload identity pool or fully qualified identifier for the workload
identity pool.
To set the `workload_identity_pool` attribute:

- provide the argument `workload_identity_pool` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `workload_identity_pool` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--description**:
A description of the pool. Cannot exceed 256 characters.

**--disabled**:
Whether the pool is disabled. You cannot use a disabled pool to exchange tokens,
or use existing tokens to access resources. If the pool is re-enabled, existing
tokens grant access again.

**--display-name**:
A display name for the pool. Cannot exceed 32 characters.

**--inline-certificate-issuance-config-file**:
YAML file with configuration for certificate issuance. Example file format:
```
inlineCertificateIssuanceConfig:
  caPools:
    us-east1: projects/1234/locations/us-east1/caPools/capoolname
    us-west1: projects/1234/locations/us-west1/caPools/capoolname
  keyAlgorithm: ECDSA_P256
  lifetime: 86400s
  rotationWindowPercentage: 50
```

**--inline-trust-config-file**:
YAML file with configuration for providing additional trust bundles. Example
file format:
```
inlineTrustConfig:
  additionalTrustBundles:
    example.com:
      trustAnchors:
      - pemCertificate: "-----BEGIN CERTIFICATE-----
        <certificate>
        -----END CERTIFICATE-----"
      - pemCertificate: "-----BEGIN CERTIFICATE-----
        <certificate>
        -----END CERTIFICATE-----"
    myorg.com:
      trustAnchors:
      - pemCertificate: "-----BEGIN CERTIFICATE-----
        <certificate>
        -----END CERTIFICATE-----"
      - pemCertificate: "-----BEGIN CERTIFICATE-----
        <certificate>
        -----END CERTIFICATE-----"
```

**--mode**:
The mode of the pool. `MODE` must be one of:
`federation-only`, `mode-unspecified`,
`trust-domain`.

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

: This command uses the `iam/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/iam/](https://cloud.google.com/iam/)

**NOTES**

: These variants are also available:

```
gcloud alpha iam workload-identity-pools create
```

```
gcloud beta iam workload-identity-pools create
```