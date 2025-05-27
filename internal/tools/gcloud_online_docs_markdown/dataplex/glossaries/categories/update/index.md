# gcloud dataplex glossaries categories update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/update](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/update)*

**NAME**

: **gcloud dataplex glossaries categories update - updates a glossary category**

**SYNOPSIS**

: **`gcloud dataplex glossaries categories update` (`[GLOSSARY_CATEGORY](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/update#GLOSSARY_CATEGORY)` : `[--glossary](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/update#--glossary)`=`GLOSSARY` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/update#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/update#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/update#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--parent](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/update#--parent)`=`PARENT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates a glossary category.

**EXAMPLES**

: To update display name, desciption and labels of glossary category
`test-category` in glossary `test-glossary` in project
`test-project` in location `us-central1`, run:

```
gcloud dataplex glossaries categories update test-category --location=us-central1 --project=test-project --glossary=test-glossary --description='updated description' --display-name='updated displayName' --labels=key1=value1,key2=value2
```

To update parent of glossary category `test-category` in glossary
`test-glossary` in project `test-project` in location
`us-central1`, run:

```
gcloud dataplex glossaries categories update test-category --location=us-central1 --project=test-project --glossary=test-glossary --parent='projects/test-project/locations/us-central1/glossaries/updated-glossary'
```

**POSITIONAL ARGUMENTS**

: **Glossary category resource - Arguments and flags that define the Dataplex
Glossary Category you want to update. The arguments in this group can be used to
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

**FLAGS**

: **--description**:
Description of the glossary category.

**--display-name**:
Display Name of the glossary category.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--parent**:
Immediate parent of the created glossary category.

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
gcloud alpha dataplex glossaries categories update
```