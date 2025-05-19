# gcloud alpha asset get-history  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/asset/get-history](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/get-history)*

**NAME**

: **gcloud alpha asset get-history - get the update history of assets that overlaps a time window**

**SYNOPSIS**

: **`gcloud alpha asset get-history` `[--asset-names](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/get-history#--asset-names)`=[`ASSET_NAMES`,…] `[--content-type](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/get-history#--content-type)`=`CONTENT_TYPE` `[--start-time](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/get-history#--start-time)`=`START_TIME` (`[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/get-history#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/get-history#--project)`=`PROJECT_ID`) [`[--end-time](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/get-history#--end-time)`=`END_TIME`] [`[--relationship-types](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/get-history#--relationship-types)`=[`RELATIONSHIP_TYPES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/get-history#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Get the update history of assets that overlaps a time
window.

**EXAMPLES**

: To get the history of asset metadata for
'//compute.googleapis.com/projects/test-project/zones/us-central1-f/instances/instance1'
between '2018-10-02T15:01:23.045Z' and '2018-12-05T13:01:21.045Z', run:

```
gcloud alpha asset get-history --project='test-project' --asset-names='//compute.googleapis.com/projects/test-project/zones/us-central1-f/instances/instance1' --start-time='2018-10-02T15:01:23.045Z' --end-time='2018-12-05T13:01:21.045Z' --content-type='resource'
```

To get the history of asset iam policy for
'//cloudresourcemanager.googleapis.com/projects/10179387634' between
'2018-10-02T15:01:23.045Z' and '2018-12-05T13:01:21.045Z', and project
'10179387634' is in organization '1060499660910', run:

```
gcloud alpha asset get-history --organization='1060499660910' --asset-names='//cloudresourcemanager.googleapis.com/projects/10179387634' --start-time='2018-10-02T15:01:23.045Z' --end-time='2018-12-05T13:01:21.045Z' --content-type='iam-policy'
```

**REQUIRED FLAGS**

: **--asset-names**:
A list of full names of the assets to get the history for. For more information,
see: [https://cloud.google.com/apis/design/resource_names#full_resource_name](https://cloud.google.com/apis/design/resource_names#full_resource_name)

**--content-type**:
Asset content type. Specifying `resource` will export resource
metadata, specifying `iam-policy` will export the IAM policy for each
child asset, specifying `org-policy` will export the Org Policy set
on child assets, specifying `access-policy` will export the Access
Policy set on child assets, specifying `os-inventory` will export the
OS inventory of VM instances, and specifying `relationship` will
export relationships of the assets. `CONTENT_TYPE` must be
one of: `resource`, `iam-policy`, `org-policy`,
`access-policy`, `os-inventory`,
`relationship`.

**--start-time**:
Start time of the time window (inclusive) for the asset history. Must be after
the current time minus 35 days. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

**--organization**

**OPTIONAL FLAGS**

: **--end-time**:
End time of the time window (exclusive) for the asset history. Defaults to
current time if not specified. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

**--relationship-types**:
A list of relationship types (i.e., "INSTANCE_TO_INSTANCEGROUP") to take a
snapshot. This argument will only be honoured if content_type=RELATIONSHIP. If
specified and non-empty, only relationships matching the specified types will be
returned. See [http://cloud.google.com/asset-inventory/docs/supported-asset-types](http://cloud.google.com/asset-inventory/docs/supported-asset-types)
for supported relationship types.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud asset get-history
```

```
gcloud beta asset get-history
```