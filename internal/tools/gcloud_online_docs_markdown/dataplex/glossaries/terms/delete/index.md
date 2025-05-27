# gcloud dataplex glossaries terms delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/delete](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/delete)*

**NAME**

: **gcloud dataplex glossaries terms delete - deletes a glossary term**

**SYNOPSIS**

: **`gcloud dataplex glossaries terms delete` (`[GLOSSARY_TERM](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/delete#GLOSSARY_TERM)` : `[--glossary](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/delete#--glossary)`=`GLOSSARY` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/delete#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes a glossary term.

**EXAMPLES**

: To delete the glossary term `test-term` in glossary
`test-glossary` in project `test-project` in location
`us-central1`, run:

```
gcloud dataplex glossaries terms delete test-term --glossary=test-glossary --location=us-central1 --project=test-project
```

**POSITIONAL ARGUMENTS**

: **Glossary term resource - Arguments and flags that define the glossary term you
want to delete. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `glossary_term` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`GLOSSARY_TERM`**:
ID of the glossary term or fully qualified identifier for the glossary term.
To set the `glossary_term` attribute:

- provide the argument `glossary_term` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--glossary**:
Identifier of the Dataplex Glossary resource.
To set the `glossary` attribute:

- provide the argument `glossary_term` on the command line with a fully
specified name;
- provide the argument `--glossary` on the command line.

**--location**:
Location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `glossary_term` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

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

: This command uses the `dataplex/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/dataplex/docs](https://cloud.google.com/dataplex/docs)

**NOTES**

: This variant is also available:

```
gcloud alpha dataplex glossaries terms delete
```