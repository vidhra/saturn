# gcloud iam workload-identity-pools update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update)*

**NAME**

: **gcloud iam workload-identity-pools update - update a workload identity pool**

**SYNOPSIS**

: **`gcloud iam workload-identity-pools update` (`[WORKLOAD_IDENTITY_POOL](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update#WORKLOAD_IDENTITY_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update#--description)`=`DESCRIPTION`] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update#--disabled)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update#--display-name)`=`DISPLAY_NAME`] [`[--inline-trust-config-file](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update#--inline-trust-config-file)`=`INLINE_TRUST_CONFIG_FILE`] [`[--inline-certificate-issuance-config-file](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update#--inline-certificate-issuance-config-file)`=`INLINE_CERTIFICATE_ISSUANCE_CONFIG_FILE`     | `[--certificate-lifetime](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update#--certificate-lifetime)`=`CERTIFICATE_LIFETIME` `[--key-algorithm](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update#--key-algorithm)`=`KEY_ALGORITHM` `[--rotation-window-percentage](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update#--rotation-window-percentage)`=`ROTATION_WINDOW_PERCENTAGE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a workload identity pool.

**EXAMPLES**

: The following command updates the workload identity pool with the ID
``my-workload-identity-pool``:

```
gcloud iam workload-identity-pools update my-workload-identity-pool --location="global" --display-name="My workload pool" --description="My workload pool description" --disabled
```

**POSITIONAL ARGUMENTS**

: **Workload identity pool resource - The workload identity pool to update. The
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

**--inline-certificate-issuance-config-file**

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
gcloud alpha iam workload-identity-pools update
```

```
gcloud beta iam workload-identity-pools update
```