# gcloud privateca templates replicate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/templates/replicate](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/replicate)*

**NAME**

: **gcloud privateca templates replicate - replicate a certificate template to multiple locations**

**SYNOPSIS**

: **`gcloud privateca templates replicate` (`[CERTIFICATE_TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/replicate#CERTIFICATE_TEMPLATE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/replicate#--location)`=`LOCATION`) (`[--all-locations](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/replicate#--all-locations)`     | `[--target-locations](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/replicate#--target-locations)`=[`LOCATION`,…]) [`[--continue-on-error](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/replicate#--continue-on-error)`] [`[--overwrite](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/replicate#--overwrite)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/templates/replicate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Replicate a certificate template to multiple locations.

**EXAMPLES**

: To replicate a certificate templates to all supported locations, run:

```
gcloud privateca templates replicate my-template --location=us-west1 --all-locations
```

To replicate a certificate template to 'us-west2' and 'us-east1', run:

```
gcloud privateca templates replicate my-template --location=us-west1 --target-locations=us-west2,us-east1
```

To overwrite existing templates with the same resource ID in the target
locations, use the --overwrite flag:

```
gcloud privateca templates replicate my-template --location=us-west1 --target-locations=us-west2,us-east1 --overwrite
```

To continue replicating templates in other locations in the event of a failure
in one or more locations, use the --continue-on-error flag:

```
gcloud privateca templates replicate my-template --location=us-west1 --all-locations --continue-on-error
```

**POSITIONAL ARGUMENTS**

: **CERTIFICATE TEMPLATE resource - The template to replicate. The arguments in this
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

**REQUIRED FLAGS**

: **--all-locations**

**OPTIONAL FLAGS**

: **--continue-on-error**:
Continue replicating the template to other locations even if an error is
encountered. If this is set, an error in one location will be logged but will
not prevent replication to other locations.

**--overwrite**:
Overwrite any existing templates with the same name, if they exist.

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