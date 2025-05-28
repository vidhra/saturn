# gcloud secrets versions destroy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/secrets/versions/destroy](https://cloud.google.com/sdk/gcloud/reference/secrets/versions/destroy)*

**NAME**

: **gcloud secrets versions destroy - destroy a secret version's metadata and secret data**

**SYNOPSIS**

: **`gcloud secrets versions destroy` (`[VERSION](https://cloud.google.com/sdk/gcloud/reference/secrets/versions/destroy#VERSION)` : `[--secret](https://cloud.google.com/sdk/gcloud/reference/secrets/versions/destroy#--secret)`=`SECRET`) [`[--etag](https://cloud.google.com/sdk/gcloud/reference/secrets/versions/destroy#--etag)`=`ETAG`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/secrets/versions/destroy#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/secrets/versions/destroy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Destroy a secret version's metadata and secret data. This action is
irreversible.

**EXAMPLES**

: Destroy version `123` of the secret named `my-secret`:

```
gcloud secrets versions destroy 123 --secret=my-secret
```

Destroy version `123` of the secret named `my-secret`
using etag:

```
gcloud secrets versions destroy 123 --secret=my-secret --etag=123
```

**POSITIONAL ARGUMENTS**

: **Version resource - Numeric secret version to destroy. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `VERSION` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`VERSION`**:
ID of the version or fully qualified identifier for the version.
To set the `version` attribute:

- provide the argument `VERSION` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--secret**:
The secret of the version.
To set the `secret` attribute:

- provide the argument `VERSION` on the command line with a fully
specified name;
- provide the argument `--secret` on the command line.**

**FLAGS**

: **--etag**:
Current entity tag (ETag) of the secret version. If specified, the version is
destroyed only if the ETag provided matches the current version's ETag.

**Location resource - The location to destroy . This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line.**

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

: This variant is also available:

```
gcloud beta secrets versions destroy
```