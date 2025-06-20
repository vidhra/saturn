# gcloud functions describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/functions/describe](https://cloud.google.com/sdk/gcloud/reference/functions/describe)*

**NAME**

: **gcloud functions describe - display details of a Google Cloud Function**

**SYNOPSIS**

: **`gcloud functions describe` (`[NAME](https://cloud.google.com/sdk/gcloud/reference/functions/describe#NAME)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/functions/describe#--region)`=`REGION`) [`[--v2](https://cloud.google.com/sdk/gcloud/reference/functions/describe#--v2)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/functions/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display details of a Google Cloud Function.

**POSITIONAL ARGUMENTS**

: **Function resource - The Cloud Function name to describe. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `NAME` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NAME`**:
ID of the function or fully qualified identifier for the function.
To set the `function` attribute:

- provide the argument `NAME` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud region for the function. Overrides the default
`functions/region` property value for this command invocation.
To set the `region` attribute:

- provide the argument `NAME` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `functions/region`.**

**FLAGS**

: **--v2**:
If specified, this command will use Cloud Functions v2 APIs and return the
result in the v2 format (See
https://cloud.google.com/functions/docs/reference/rest/v2/projects.locations.functions#Function).
If not specified, 1st gen and 2nd gen functions will use v1 and v2 APIs
respectively and return the result in the corresponding format (For v1 format,
see
https://cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#resource:-cloudfunction).
This command conflicts with `--no-gen2`. If specified with this
combination, v2 APIs will be used.

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
gcloud alpha functions describe
```

```
gcloud beta functions describe
```