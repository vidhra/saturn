# gcloud pam entitlements update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/update](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/update)*

**NAME**

: **gcloud pam entitlements update - update an existing Privileged Access Manager entitlement**

**SYNOPSIS**

: **`gcloud pam entitlements update` (`[ENTITLEMENT](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/update#ENTITLEMENT)` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/update#--folder)`=`FOLDER` `[--location](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/update#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/update#--organization)`=`ORGANIZATION`) `[--entitlement-file](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/update#--entitlement-file)`=`PATH_TO_FILE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/update#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an existing Privileged Access Manager (PAM) entitlement.

**EXAMPLES**

: The following command updates an entitlement with a name of
`sample-entitlement`, in a project named `sample-project`,
in location `global`, and the new entitlement configuration stored in
a file named `sample-entitlement.yaml`:

```
gcloud pam entitlements update sample-entitlement --project=sample-project --location=global --entitlement-file=sample-entitlement.yaml
```

The following command updates an entitlement with a name of
`sample-entitlement`, in a folder with ID
``FOLDER_ID``, in location `global`,
and the new entitlement configuration stored in a file named
`sample-entitlement.yaml`:

```
gcloud pam entitlements update sample-entitlement --folder=FOLDER_ID --location=global --entitlement-file=sample-entitlement.yaml
```

The following command updates an entitlement with a name of
`sample-entitlement`, in an organization with ID
``ORGANIZATION_ID``, in location
`global`, and the new entitlement configuration stored in a file
named `sample-entitlement.yaml`:

```
gcloud pam entitlements update sample-entitlement --organization=ORGANIZATION_ID --location=global --entitlement-file=sample-entitlement.yaml
```

**POSITIONAL ARGUMENTS**

: **Entitlement resource - Name of the entitlement to update. The arguments in this
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

**REQUIRED FLAGS**

: **--entitlement-file**:
YAML file containing the new configuration of the entitlement. Use a full or
relative path to a local file containing the value of entitlement_file.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha pam entitlements update
```

```
gcloud beta pam entitlements update
```