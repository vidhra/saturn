# gcloud network-security security-profiles custom-intercept create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/create](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/create)*

**NAME**

: **gcloud network-security security-profiles custom-intercept create - create a new Custom Intercept Profile**

**SYNOPSIS**

: **`gcloud network-security security-profiles custom-intercept create` (`[SECURITY_PROFILE](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/create#SECURITY_PROFILE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/create#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/create#--organization)`=`ORGANIZATION`) (`[--intercept-endpoint-group](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/create#--intercept-endpoint-group)`=`INTERCEPT_ENDPOINT_GROUP` : `[--intercept-endpoint-group-location](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/create#--intercept-endpoint-group-location)`=`INTERCEPT_ENDPOINT_GROUP_LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Custom Intercept Security Profile.

**EXAMPLES**

: To create a Custom Intercept Security Profile named
`intercept-profile` linked to a Intercept Endpoint Group (q.v.), run:

```
gcloud network-security security-profiles custom-intercept create intercept-profile --description="An Intercept Profile" --intercept-endpoint-group=projects/my-project/locations/global/interceptEndpointGroups/my-mep
```

**POSITIONAL ARGUMENTS**

: **Security profile resource - Security Profile Name. The arguments in this group
can be used to specify the attributes of this resource.
This must be specified.

**`SECURITY_PROFILE`**:
ID of the security_profile or fully qualified identifier for the
security_profile.
To set the `security_profile` attribute:

- provide the argument `security_profile` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
location of the security_profile - Global.
To set the `location` attribute:

- provide the argument `security_profile` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.

**--organization**:
Organization ID to which the changes should apply.
To set the `organization` attribute:

- provide the argument `security_profile` on the command line with a
fully specified name;
- provide the argument `--organization` on the command line.**

**REQUIRED FLAGS**

: **Intercept endpoint group resource - Intercept Endpoint Group. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--intercept-endpoint-group` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--intercept-endpoint-group**:
ID of the intercept endpoint group or fully qualified identifier for the
intercept endpoint group.
To set the `id` attribute:

- provide the argument `--intercept-endpoint-group` on the command
line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--intercept-endpoint-group-location**:
Location of the intercept endpoint group.
To set the `location` attribute:

- provide the argument `--intercept-endpoint-group` on the command line
with a fully specified name;
- provide the argument `--intercept-endpoint-group-location` on the
command line;
- provide the argument `--location` on the command line;
- provide the argument
`networksecurity.projects.locations.interceptEndpointGroupAssociations`
on the command line with a fully specified name.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `False`.

**--description**:
Brief description of the security profile

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

: These variants are also available:

```
gcloud alpha network-security security-profiles custom-intercept create
```

```
gcloud beta network-security security-profiles custom-intercept create
```