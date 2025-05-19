# gcloud certificate-manager certificates create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create)*

**NAME**

: **gcloud certificate-manager certificates create - create a certificate**

**SYNOPSIS**

: **`gcloud certificate-manager certificates create` (`[CERTIFICATE](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create#CERTIFICATE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create#--location)`=`LOCATION`) (`[--certificate-file](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create#--certificate-file)`=`PATH_TO_FILE` `[--private-key-file](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create#--private-key-file)`=`PATH_TO_FILE`     | [`[--domains](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create#--domains)`=[`DOMAINS`,…] : `[--dns-authorizations](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create#--dns-authorizations)`=[`DNS_AUTHORIZATIONS`,…] | `[--issuance-config](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create#--issuance-config)`=`ISSUANCE_CONFIG`]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--scope](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create#--scope)`=`SCOPE`; default="DEFAULT"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new certificate.

- Managed certificates can be created by supplying one or more domain names and an
(optional) list of DNS authorizations for those domain names.
- Self-managed certificates can be created by uploading a certificate and its
corresponding private key (both in PEM format).

**EXAMPLES**

: To create (upload) a self-managed certificate called
`www-example-com`, run:

```
gcloud certificate-manager certificates create www-example-com --private-key-file=key.pem --certificate-file=cert.pem
```

To create a certificate managed by Certificate Manager called
`api-example-com`, run:

```
gcloud certificate-manager certificates create api-example-com --domains="api.example.com"
```

To create a certificate managed by Certificate Manager called
`api-example-com`, using an existing DNS authorization, run:

```
gcloud certificate-manager certificates create api-example-com --dns-authorizations=api-example-com --domains="api.example.com"
```

**POSITIONAL ARGUMENTS**

: **Certificate resource - The name of the certificate to create. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `certificate` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CERTIFICATE`**:
ID of the certificate or fully qualified identifier for the certificate.
To set the `certificate` attribute:

- provide the argument `certificate` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Certificate Manager location.
To set the `location` attribute:

- provide the argument `certificate` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- default value of location is [global].**

**REQUIRED FLAGS**

: **--certificate-file**

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

**--scope**:
Scope of the managed certificate. This determines which services the certificate
can be attached to/associated with. Defaults to `DEFAULT`.
`SCOPE` must be one of:

**`all-regions`**:
Certificates with scope ALL_REGIONS are currently used for Cross-region Internal
Application Load Balancer only.

**`client-auth`**:
Certificates with scope CLIENT_AUTH are used for client authentication.

**`default`**:
Certificates with DEFAULT scope are used for Load Balancing and Cloud CDN.
If unsure, choose this option.

**`edge-cache`**:
Certificates with scope EDGE_CACHE are special-purposed certificates, scoped for
use with Media Edge services only.

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
gcloud alpha certificate-manager certificates create
```

```
gcloud beta certificate-manager certificates create
```