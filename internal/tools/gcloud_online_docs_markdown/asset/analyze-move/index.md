# gcloud asset analyze-move  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/asset/analyze-move](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-move)*

**NAME**

: **gcloud asset analyze-move - analyzes resource move**

**SYNOPSIS**

: **`gcloud asset analyze-move` `[--project](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-move#--project)`=`PROJECT_ID` (`[--destination-folder](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-move#--destination-folder)`=`FOLDER_ID`     | `[--destination-organization](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-move#--destination-organization)`=`ORGANIZATION_ID`) [`[--blockers-only](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-move#--blockers-only)`=`BLOCKERS_ONLY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-move#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Analyze resource migration from its current resource hierarchy.

**EXAMPLES**

: To analyze the impacts of moving a project to a different organization, run:

```
gcloud asset analyze-move --project=YOUR_PROJECT_ID --destination-organization=ORGANIZATION_ID
```

To analyze the impacts of moving a project to a different folder, run:

```
gcloud asset analyze-move --project=YOUR_PROJECT_ID --destination-folder=FOLDER_ID
```

To analyze only the blockers of moving a project to a different folder, run:

```
gcloud asset analyze-move --project=YOUR_PROJECT_ID --destination-folder=FOLDER_ID --blockers-only=true
```

**REQUIRED FLAGS**

: **--project**:
The project ID or number to perform the analysis.

**--destination-folder**

**OPTIONAL FLAGS**

: **--blockers-only**:
Determines whether to perform analysis against blockers only. Leaving it empty
means the full analysis will be performed including warnings and blockers for
the specified resource move.

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