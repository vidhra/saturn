# gcloud deploy apply  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/apply](https://cloud.google.com/sdk/gcloud/reference/deploy/apply)*

**NAME**

: **gcloud deploy apply - applies a yaml configuration containing Delivery Pipeline(s), Target(s), Custom Target Type(s), Deploy Policy(ies), and Automation(s) declarative definitions**

**SYNOPSIS**

: **`gcloud deploy apply` `[--file](https://cloud.google.com/sdk/gcloud/reference/deploy/apply#--file)`=`FILE` [`[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/apply#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/apply#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Applies a yaml configuration containing Delivery Pipeline(s), Target(s), Custom
Target Type(s), Deploy Policy(ies), and Automation(s) declarative definitions.

**EXAMPLES**

: To apply a Cloud Deploy YAML file `deploy.yaml`:

```
gcloud deploy apply --file=deploy.yaml --region=us-central1
```

**REQUIRED FLAGS**

: **--file**:
Path to yaml file containing Delivery Pipeline(s), Target(s) declarative
definitions.

**OPTIONAL FLAGS**

: **Location resource - The Cloud region of {resource}. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--region` on the command line with a fully
specified name;
- set the property `deploy/region` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--region**:
ID of the location or fully qualified identifier for the location.
To set the `region` attribute:

- provide the argument `--region` on the command line;
- set the property `deploy/region`.**

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
gcloud alpha deploy apply
```

```
gcloud beta deploy apply
```