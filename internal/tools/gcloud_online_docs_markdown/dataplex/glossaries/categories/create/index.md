# gcloud dataplex glossaries categories create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/create](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/create)*

**NAME**

: **gcloud dataplex glossaries categories create - creates a glossary category**

**SYNOPSIS**

: **`gcloud dataplex glossaries categories create` (`[GLOSSARY_CATEGORY](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/create#GLOSSARY_CATEGORY)` : `[--glossary](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/create#--glossary)`=`GLOSSARY` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/create#--location)`=`LOCATION`) `[--parent](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/create#--parent)`=`PARENT` [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: A glossary category represents a collection of glossary categories and glossary
terms within a glossary that are related to each other.

**EXAMPLES**

: To create a glossary category `test-category` in glossary
`test-glossary` in project `test-project` in location
`us-central1`, with description `test description`,
displayName `displayName` and parent
`projects/test-project/locations/us-central1/glossaries/test-glossary`
, run:

```
gcloud dataplex glossaries categories create test-category --glossary=test-glossary --location=us-central1 --project=test-project --parent='projects/test-project/locations/us-central1/glossaries/test-glossary' --description='test description' --display-name='displayName'
```

**POSITIONAL ARGUMENTS**

: **Glossary category resource - Arguments and flags that define the Dataplex
Glossary Category you want to create. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `glossary_category` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`GLOSSARY_CATEGORY`**:
ID of the glossary category or fully qualified identifier for the glossary
category.
To set the `glossary_category` attribute:

- provide the argument `glossary_category` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--glossary**:
The name of glossary category to use.
To set the `glossary` attribute:

- provide the argument `glossary_category` on the command line with a
fully specified name;
- provide the argument `--glossary` on the command line.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `glossary_category` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**REQUIRED FLAGS**

: **--parent**:
Immediate parent of the created glossary category.

**OPTIONAL FLAGS**

: **--description**:
Description of the glossary category.

**--display-name**:
Display name of the glossary category.

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
gcloud alpha dataplex glossaries categories create
```