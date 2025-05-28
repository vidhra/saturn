# gcloud resource-manager tags holds create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/create](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/create)*

**NAME**

: **gcloud resource-manager tags holds create - create a TagHold resource**

**SYNOPSIS**

: **`gcloud resource-manager tags holds create` `[PARENT](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/create#PARENT)` `[--holder](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/create#--holder)`=`HOLDER` [`[--help-link](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/create#--help-link)`=`HELP_LINK`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/create#--location)`=`LOCATION`] [`[--origin](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/create#--origin)`=`ORIGIN`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a TagHold under a TagValue, indicating that the TagValue is being used by
a holder (cloud resource) from an (optional) origin. The TagValue can be
represented with its numeric id or its namespaced name of
{parent_namespace}/{tag_key_short_name}/{tag_value_short_name}.

**EXAMPLES**

: To create a TagHold on tagValues/123, with holder cloud-resource-holder, origin
creator-origin, in region us-central1-a, with help link
www.example.help.link.com, run:

```
gcloud resource-manager tags holds create tagValues/123 --holder=cloud-resource-holder --origin=creator-origin --help-link=www.example.help.link.com --location=us-central1-a
```

To create a TagHold under TagValue test under TagKey env in organization id 789,
with holder cloud-resource-holder, run:

```
gcloud resource-manager tags holds create 789/env/test --holder=cloud-resource-holder
```

**POSITIONAL ARGUMENTS**

: **`PARENT`**:
Tag value name or namespaced name.

**REQUIRED FLAGS**

: **--holder**:
The name of the resource where the TagValue is being used. Must be less than 200
characters.

**OPTIONAL FLAGS**

: **--help-link**:
A URL where an end user can learn more about removing this hold.

**--location**:
Region or zone where the TagHold will be stored. If not provided, the TagHold
will be stored in a "global" region.

**--origin**:
An optional string representing the origin of this request. This field should
include human-understandable information to distinguish origins from each other.
Must be less than 200 characters.

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
gcloud alpha resource-manager tags holds create
```

```
gcloud beta resource-manager tags holds create
```