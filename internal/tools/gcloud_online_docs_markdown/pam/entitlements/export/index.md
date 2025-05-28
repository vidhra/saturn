# gcloud pam entitlements export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/export](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/export)*

**NAME**

: **gcloud pam entitlements export - export a Privileged Access Manager entitlement into a local YAML file**

**SYNOPSIS**

: **`gcloud pam entitlements export` (`[ENTITLEMENT](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/export#ENTITLEMENT)` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/export#--folder)`=`FOLDER` `[--location](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/export#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/export#--organization)`=`ORGANIZATION`) [`[--destination](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/export#--destination)`=`DESTINATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export a Privileged Access Manager (PAM) entitlement into a local YAML file.

**EXAMPLES**

: The following command exports an entitlement with a name of
`sample-entitlement`, in a project named `sample-project`,
and in location `global` to a local YAML file named
`sample-entitlement.yaml`:

```
gcloud pam entitlements export sample-entitlement --project=sample-project --location=global --destination=sample-entitlement.yaml
```

The following command exports an entitlement with a name of
`sample-entitlement`, in a folder with ID
``FOLDER_ID``, and in location
`global` to a local YAML file named
`sample-entitlement.yaml`:

```
gcloud pam entitlements export sample-entitlement --folder=FOLDER_ID --location=global --destination=sample-entitlement.yaml
```

The following command exports an entitlement with a name of
`sample-entitlement`, in an organization with ID
``ORGANIZATION_ID``, and in location
`global` to a local YAML file named
`sample-entitlement.yaml`:

```
gcloud pam entitlements export sample-entitlement --organization=ORGANIZATION_ID --location=global --destination=sample-entitlement.yaml
```

**POSITIONAL ARGUMENTS**

: **Entitlement resource - Name of the entitlement to export. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `entitlement` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`. This resource can be one of the
following types: [privilegedaccessmanager.projects.locations.entitlements,
privilegedaccessmanager.folders.locations.entitlements,
privilegedaccessmanager.organizations.locations.entitlements].

This must be specified.

**`ENTITLEMENT`**:
ID of the entitlement or fully qualified identifier for the entitlement.
To set the `entitlement` attribute:

- provide the argument `entitlement` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--folder**:
The name of the folder
To set the `folder` attribute:

- provide the argument `entitlement` on the command line with a fully
specified name;
- provide the argument `--folder` on the command line. Must be
specified for resource of type
[privilegedaccessmanager.folders.locations.entitlements].

**--location**:
The resource location
To set the `location` attribute:

- provide the argument `entitlement` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
The name of the organization
To set the `organization` attribute:

- provide the argument `entitlement` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line. Must be
specified for resource of type
[privilegedaccessmanager.organizations.locations.entitlements].**

**FLAGS**

: **--destination**:
Path to a YAML file where the configuration will be exported. The exported data
will not contain any output-only fields. Alternatively, you may omit this flag
to write to standard output. For a schema describing the export/import format,
see $CLOUDSDKROOT/lib/googlecloudsdk/schemas/…

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

: This command uses the `privilegedaccessmanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/iam/docs/pam-overview](https://cloud.google.com/iam/docs/pam-overview)

**NOTES**

: These variants are also available:

```
gcloud alpha pam entitlements export
```

```
gcloud beta pam entitlements export
```