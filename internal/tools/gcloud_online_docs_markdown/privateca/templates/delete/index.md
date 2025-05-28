# gcloud privateca templates delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/templates/delete](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/delete)*

**NAME**

: **gcloud privateca templates delete - delete a certificate template**

**SYNOPSIS**

: **`gcloud privateca templates delete` (`[CERTIFICATE_TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/delete#CERTIFICATE_TEMPLATE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/delete#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/delete#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To delete a certificate template:

```
gcloud privateca templates delete my-template --location=us-west1
```

To delete a certificate template while skipping the confirmation input:

```
gcloud privateca templates delete my-template --location=us-west1 --quiet
```

**POSITIONAL ARGUMENTS**

: **CERTIFICATE TEMPLATE resource - The template to delete. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `CERTIFICATE_TEMPLATE` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CERTIFICATE_TEMPLATE`**:
ID of the CERTIFICATE_TEMPLATE or fully qualified identifier for the
CERTIFICATE_TEMPLATE.
To set the `certificate template` attribute:

- provide the argument `CERTIFICATE_TEMPLATE` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the CERTIFICATE_TEMPLATE.
To set the `location` attribute:

- provide the argument `CERTIFICATE_TEMPLATE` on the command line with
a fully specified name;
- provide the argument `--location` on the command line;
- set the property `privateca/location`.**

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