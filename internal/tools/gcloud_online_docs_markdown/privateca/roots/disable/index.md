# gcloud privateca roots disable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/roots/disable](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/disable)*

**NAME**

: **gcloud privateca roots disable - disable a root certificate authority**

**SYNOPSIS**

: **`gcloud privateca roots disable` (`[CERTIFICATE_AUTHORITY](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/disable#CERTIFICATE_AUTHORITY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/disable#--location)`=`LOCATION` `[--pool](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/disable#--pool)`=`POOL`) [`[--ignore-dependent-resources](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/disable#--ignore-dependent-resources)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/disable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Disables a root certificate authority. The root certificate authority will not
be allowed to issue certificates once disabled. It may still revoke certificates
and/or generate CRLs. The CA certfificate will still be included in the
FetchCaCertificates response for the parent CA Pool.

**EXAMPLES**

: To disable a root CA:

```
gcloud privateca roots disable prod-root --pool=prod-root-pool --location=us-west1
```

**POSITIONAL ARGUMENTS**

: **CERTIFICATE AUTHORITY resource - The certificate authority to disable. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CERTIFICATE_AUTHORITY`**:
ID of the CERTIFICATE_AUTHORITY or fully qualified identifier for the
CERTIFICATE_AUTHORITY.
To set the `certificate_authority` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the CERTIFICATE_AUTHORITY.
To set the `location` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line with
a fully specified name;
- provide the argument `--location` on the command line;
- set the property `privateca/location`.

**--pool**:
The parent CA Pool of the CERTIFICATE_AUTHORITY.
To set the `pool` attribute:

- provide the argument `CERTIFICATE_AUTHORITY` on the command line with
a fully specified name;
- provide the argument `--pool` on the command line.**

**FLAGS**

: **--ignore-dependent-resources**:
This field skips the integrity check that would normally prevent breaking a CA
Pool if it is used by another cloud resource and allows the CA Pool to be in a
state where it is not able to issue certificates. Doing so may result in
unintended and unrecoverable effects on any dependent resource(s) since the CA
Pool would not be able to issue certificates.

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