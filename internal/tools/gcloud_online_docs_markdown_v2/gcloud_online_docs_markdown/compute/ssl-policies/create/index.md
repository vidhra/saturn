# gcloud compute ssl-policies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/create](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/create)*

**NAME**

: **gcloud compute ssl-policies create - create a new Compute Engine SSL policy**

**SYNOPSIS**

: **`gcloud compute ssl-policies create` `[SSL_POLICY](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/create#SSL_POLICY)` [`[--custom-features](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/create#--custom-features)`=[`CUSTOM_FEATURES`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/create#--description)`=`DESCRIPTION`] [`[--min-tls-version](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/create#--min-tls-version)`=`MIN_TLS_VERSION`; default="1.0"] [`[--profile](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/create#--profile)`=`PROFILE`; default="COMPATIBLE"] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/create#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute ssl-policies create` creates a new SSL policy.
An SSL policy specifies the server-side support for SSL features. An SSL policy
can be attached to a TargetHttpsProxy or a TargetSslProxy. This affects
connections between clients and the load balancer. SSL policies do not affect
the connection between the load balancers and the backends. SSL policies are
used by Application Load Balancers and proxy Network Load Balancers.

**POSITIONAL ARGUMENTS**

: **`SSL_POLICY`**:
Name of the SSL policy to create.

**FLAGS**

: **--custom-features**:
A comma-separated list of custom features, required when the profile being used
is CUSTOM.
Using CUSTOM profile allows customization of the features that are part of the
SSL policy. This flag allows specifying those custom features.
The list of all supported custom features can be obtained using:

```
gcloud compute ssl-policies list-available-features
```

**--description**:
An optional, textual description for the SSL policy.

**--min-tls-version**:
Minimum TLS version. `MIN_TLS_VERSION` must be one of:

**`1.0`**:
TLS 1.0.

**`1.1`**:
TLS 1.1.

**`1.2`**:
TLS 1.2.

**--profile**:
SSL policy profile. Changing profile from CUSTOM to COMPATIBLE|MODERN|RESTRICTED
will clear the custom-features field. `PROFILE` must be
one of:

**`COMPATIBLE`**:
Compatible profile. Allows the broadest set of clients, even those which support
only out-of-date SSL features, to negotiate SSL with the load balancer.

**`CUSTOM`**:
Custom profile. Allows customization by selecting only the features which are
required. The list of all available features can be obtained using:

```
gcloud compute ssl-policies list-available-features
```

**`MODERN`**:
Modern profile. Supports a wide set of SSL features, allowing modern clients to
negotiate SSL.

**`RESTRICTED`**:
Restricted profile. Supports a reduced set of SSL features, intended to meet
stricter compliance requirements.

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

: These variants are also available:

```
gcloud alpha compute ssl-policies create
```

```
gcloud beta compute ssl-policies create
```