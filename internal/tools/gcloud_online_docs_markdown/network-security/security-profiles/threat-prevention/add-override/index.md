# gcloud network-security security-profiles threat-prevention add-override  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override)*

**NAME**

: **gcloud network-security security-profiles threat-prevention add-override - add overrides to Threat Prevention Profile**

**SYNOPSIS**

: **`gcloud network-security security-profiles threat-prevention add-override` (`[SECURITY_PROFILE](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override#SECURITY_PROFILE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override#--organization)`=`ORGANIZATION`) `[--action](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override#--action)`=`ACTION` (`[--antivirus](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override#--antivirus)`=[`PROTOCOL`,…]     | `[--severities](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override#--severities)`=[`SEVERITY_LEVEL`,…]     | `[--threat-ids](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override#--threat-ids)`=[`THREAT-ID`,…]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override#--async)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add antivirus, severities, or threat-ids to existing threat prevention profile
with intended action on each specified. Check the updates of add-override
command by using `gcloud network-security security-profiles
threat-prevention list-override my-security-profile`.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To add an override, run:

```
gcloud network-security security-profiles threat-prevention add-override my-security-profile --severities=MEDIUM --action=ALLOW
```

`my-security-profile` is the name of the Security Profile in the
format organizations/{organizationID}/locations/{location}/securityProfiles/
{security_profile_id} where organizationID is the organization ID to which the
changes should apply, location - `global` specified and
security_profile_id the Security Profile Identifier

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

: **--action**:
Action associated with antivirus, severity, or threat-id.
`ACTION` must be one of: `DEFAULT_ACTION`,
`ALLOW`, `ALERT`, `DENY`.

**--antivirus**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `False`.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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
gcloud alpha network-security security-profiles threat-prevention add-override
```

```
gcloud beta network-security security-profiles threat-prevention add-override
```