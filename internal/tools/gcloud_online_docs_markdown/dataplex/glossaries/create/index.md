# gcloud dataplex glossaries create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/create](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/create)*

**NAME**

: **gcloud dataplex glossaries create - create a Dataplex Glossary resource**

**SYNOPSIS**

: **`gcloud dataplex glossaries create` (`[GLOSSARY](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/create#GLOSSARY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/create#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/create#--async)`     | `[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: A Glossary represents a collection of Categories and Terms.

**EXAMPLES**

: To create a Glossary `test-glossary` in project
`test-dataplex` at location `us-central1`, with
description `test description` and displayName
`displayName` , run:

```
gcloud dataplex glossaries create test-glossary --location=us-central1 --project=test-dataplex --description='test description' --display-name='displayName'
```

**POSITIONAL ARGUMENTS**

: **Glossary resource - Arguments and flags that define the Dataplex Glossary you
want to create. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `glossary` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`GLOSSARY`**:
ID of the glossary or fully qualified identifier for the glossary.
To set the `glossary` attribute:

- provide the argument `glossary` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `glossary` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**FLAGS**

: **--description**:
Description of the Glossary.

**--display-name**:
Display Name of the Glossary.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--async**

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
gcloud alpha dataplex glossaries create
```