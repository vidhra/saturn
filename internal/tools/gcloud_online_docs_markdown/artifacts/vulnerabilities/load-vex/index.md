# gcloud artifacts vulnerabilities load-vex  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/vulnerabilities/load-vex](https://cloud.google.com/sdk/gcloud/reference/artifacts/vulnerabilities/load-vex)*

**NAME**

: **gcloud artifacts vulnerabilities load-vex - load VEX data from a CSAF file into Artifact Analysis**

**SYNOPSIS**

: **`gcloud artifacts vulnerabilities load-vex` `[--source](https://cloud.google.com/sdk/gcloud/reference/artifacts/vulnerabilities/load-vex#--source)`=`SOURCE` `[--uri](https://cloud.google.com/sdk/gcloud/reference/artifacts/vulnerabilities/load-vex#--uri)`=`URI` [`[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/vulnerabilities/load-vex#--location)`=`LOCATION`] [`[--project](https://cloud.google.com/sdk/gcloud/reference/artifacts/vulnerabilities/load-vex#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/vulnerabilities/load-vex#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Command loads VEX data from a Common Security Advisory Framework (CSAF) file
into Artifact Analysis as VulnerabilityAssessment Notes. VEX data tells Artifact
Analysis whether vulnerabilities are relevant and how.

**EXAMPLES**

: To load a CSAF security advisory file given an artifact in Artifact Registry and
the file on disk, run:

```
gcloud artifacts vulnerabilities load-vex --uri=us-east1-docker.pkg.dev/project123/repository123/someimage@sha256:49765698074d6d7baa82f --source=/path/to/vex/file
```

To load a CSAF security advisory file given an artifact with a tag and a file on
disk, run:

```
gcloud artifacts vulnerabilities load-vex --uri=us-east1-docker.pkg.dev/project123/repository123/someimage:latest --source=/path/to/vex/file
```

**REQUIRED FLAGS**

: **--source**:
The path of the VEX file.

**--uri**:
The path of the artifact in Artifact Registry. A 'gcr.io' image can also be used
if redirection is enabled in Artifact Registry. Make sure
'artifactregistry.projectsettings.get' permission is granted to the current
gcloud user to verify the redirection status.

**OPTIONAL FLAGS**

: **--location**:
If specified, all requests to Artifact Analysis for occurrences will go to
location specified

**--project**:
The parent project to load security advisory into.

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