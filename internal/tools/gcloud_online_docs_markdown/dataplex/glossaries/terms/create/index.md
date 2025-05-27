# gcloud dataplex glossaries terms create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/create](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/create)*

**NAME**

: **gcloud dataplex glossaries terms create - creates a glossary term**

**SYNOPSIS**

: **`gcloud dataplex glossaries terms create` (`[GLOSSARY_TERM](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/create#GLOSSARY_TERM)` : `[--glossary](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/create#--glossary)`=`GLOSSARY` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/create#--location)`=`LOCATION`) `[--parent](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/create#--parent)`=`PARENT` [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/terms/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: A glossary term holds a rich text description that can be attached to entries or
specific columns to enrich them.

**EXAMPLES**

: To create a glossary term `test-term` in glossary
`test-glossary` in project `test-project` in location
`us-central1`, with description `test description`,
displayName `displayName` and parent
`projects/test-project/locations/us-central1/glossaries/test-glossary/categories/test-category`
, run:

```
gcloud dataplex glossaries terms create test-term --glossary=test-glossary --location=us-central1 --project=test-project --parent='projects/test-project/locations/us-central1/glossaries/test-glossary/categories/test-category' --description='test description' --display-name='displayName'
```

**POSITIONAL ARGUMENTS**

: **Glossary term resource - Arguments and flags that define the Dataplex Glossary
Term you want to create. The arguments in this group can be used to specify the
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
The name of glossary term to use.
To set the `glossary` attribute:

- provide the argument `glossary_term` on the command line with a fully
specified name;
- provide the argument `--glossary` on the command line.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `glossary_term` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**REQUIRED FLAGS**

: **--parent**:
Immediate parent of the created glossary term.

**OPTIONAL FLAGS**

: **--description**:
Description of the glossary term.

**--display-name**:
Display name of the glossary term.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
gcloud alpha dataplex glossaries terms create
```